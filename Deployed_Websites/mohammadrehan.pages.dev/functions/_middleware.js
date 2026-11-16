// ====================================================================
// Cloudflare Pages Security Edge Middleware - Rehan Quant Lab (RQL)
// Defense-in-Depth: Exploit Scanner Dropper + Tiered API Rate Limiting
// ====================================================================

// Sliding-window rate limiter maps
// Map structure: ip -> { count: number, resetTime: number }
const rateLimitMaps = {
    apiMutation: new Map(), // /api/* POST/PUT/DELETE (Strict: 10 req/min)
    apiQuery: new Map(),    // /api/* GET/HEAD (30 req/min)
    redirect: new Map()     // /go (60 req/min)
};

const RATE_WINDOW_MS = 60000; // 60-second window

function checkRateLimit(map, clientIp, maxRequests) {
    const now = Date.now();
    const data = map.get(clientIp) || { count: 0, resetTime: now + RATE_WINDOW_MS };

    if (now > data.resetTime) {
        data.count = 1;
        data.resetTime = now + RATE_WINDOW_MS;
    } else {
        data.count++;
    }

    map.set(clientIp, data);

    // Prune stale entries to keep memory bounded in edge runtime
    if (map.size > 2000) {
        for (const [ip, item] of map.entries()) {
            if (now > item.resetTime) map.delete(ip);
        }
    }

    const remaining = Math.max(0, maxRequests - data.count);
    const retryAfter = Math.ceil((data.resetTime - now) / 1000);
    const isLimited = data.count > maxRequests;

    return { isLimited, remaining, resetTime: data.resetTime, retryAfter, limit: maxRequests };
}

export async function onRequest(context) {
    const request = context.request;
    const url = new URL(request.url);
    const pathname = url.pathname.toLowerCase();
    const method = request.method.toUpperCase();
    const clientIp = request.headers.get("CF-Connecting-IP") || "0.0.0.0";

    // 1. HTTP Method Filtering: Reject uncommon or dangerous verbs
    const allowedMethods = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'OPTIONS'];
    if (!allowedMethods.includes(method)) {
        return new Response("405 Method Not Allowed", {
            status: 405,
            statusText: "Method Not Allowed",
            headers: {
                "Allow": "GET, HEAD, POST, PUT, DELETE, OPTIONS",
                "Content-Type": "text/plain; charset=utf-8"
            }
        });
    }

    // 2. Exploit Scanner & Secret Path Dropper: Block known scan paths
    const blockedPatterns = [
        '/.git',
        '/.env',
        '/.svn',
        '/.hg',
        '/.bzr',
        '/.ds_store',
        '/thumbs.db',
        '/web.config',
        '/.aws',
        '/.ssh',
        '/.docker',
        '/.kube',
        '/.vscode',
        '/.idea',
        '/id_rsa',
        '/id_ed25519',
        '/wp-login.php',
        '/wp-admin',
        '/xmlrpc.php',
        '/phpmyadmin',
        '/pma',
        '/cgi-bin',
        '/actuator',
        '/.well-known/../'
    ];

    for (const pattern of blockedPatterns) {
        if (pathname === pattern || pathname.startsWith(pattern + '/') || pathname.includes(pattern)) {
            return new Response("403 Forbidden: Access to sensitive path is strictly prohibited.", {
                status: 403,
                statusText: "Forbidden",
                headers: {
                    "Content-Type": "text/plain; charset=utf-8",
                    "X-Content-Type-Options": "nosniff",
                    "X-Frame-Options": "DENY",
                    "X-Robots-Tag": "noindex, nofollow",
                    "Cache-Control": "no-store, no-cache, must-revalidate"
                }
            });
        }
    }

    // 3. Payload Size Guard on API endpoints (Max 100KB)
    if (pathname.startsWith('/api/')) {
        const contentLength = parseInt(request.headers.get("content-length") || "0", 10);
        if (contentLength > 102400) {
            return new Response(JSON.stringify({ error: "413 Payload Too Large: API request body exceeds 100KB limit." }), {
                status: 413,
                statusText: "Payload Too Large",
                headers: {
                    "Content-Type": "application/json",
                    "Connection": "close"
                }
            });
        }
    }

    // 4. Tiered Edge Rate Limiting
    let rateCheck = null;

    if (pathname.startsWith('/api/')) {
        if (method === 'POST' || method === 'PUT' || method === 'DELETE') {
            // Strict 10 req/min for form / lead / audit mutations
            rateCheck = checkRateLimit(rateLimitMaps.apiMutation, clientIp, 10);
        } else {
            // 30 req/min for API queries
            rateCheck = checkRateLimit(rateLimitMaps.apiQuery, clientIp, 30);
        }
    } else if (pathname === '/go' || pathname.startsWith('/go?')) {
        // 60 req/min for link redirects
        rateCheck = checkRateLimit(rateLimitMaps.redirect, clientIp, 60);
    }

    if (rateCheck && rateCheck.isLimited) {
        return new Response(JSON.stringify({
            error: "429 Too Many Requests: Rate limit exceeded. Try again in " + rateCheck.retryAfter + " seconds.",
            retryAfter: rateCheck.retryAfter
        }), {
            status: 429,
            statusText: "Too Many Requests",
            headers: {
                "Content-Type": "application/json",
                "Retry-After": String(rateCheck.retryAfter),
                "X-RateLimit-Limit": String(rateCheck.limit),
                "X-RateLimit-Remaining": "0",
                "X-RateLimit-Reset": String(rateCheck.resetTime)
            }
        });
    }

    // 5. Downstream Execution
    const response = await context.next();

    // 6. Institutional Security Headers on all edge responses
    const newHeaders = new Headers(response.headers);
    newHeaders.set("X-Content-Type-Options", "nosniff");
    newHeaders.set("X-Frame-Options", "DENY");
    newHeaders.set("Referrer-Policy", "strict-origin-when-cross-origin");
    newHeaders.set("Permissions-Policy", "geolocation=(), microphone=(), camera=(), payment=()");
    newHeaders.set("Cross-Origin-Opener-Policy", "same-origin");

    if (rateCheck) {
        newHeaders.set("X-RateLimit-Limit", String(rateCheck.limit));
        newHeaders.set("X-RateLimit-Remaining", String(rateCheck.remaining));
    }

    return new Response(response.body, {
        status: response.status,
        statusText: response.statusText,
        headers: newHeaders
    });
}
