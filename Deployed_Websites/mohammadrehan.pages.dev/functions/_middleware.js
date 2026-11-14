// ====================================================================
// Cloudflare Pages Security Edge Middleware - Rehan Quant Lab (RQL)
// Defense-in-Depth: Exploit Scanner Dropper + API Edge Rate Limiting
// ====================================================================

// In-memory sliding window rate limiter for dynamic edge endpoints (/api/* and /go)
const rateLimitMap = new Map();
const RATE_WINDOW_MS = 60000; // 1 minute window
const MAX_REQUESTS_PER_WINDOW = 60; // Max 60 requests per minute per IP

function isRateLimited(clientIp, pathname) {
    // Only rate limit dynamic API endpoints and redirect forwarders
    if (!pathname.startsWith('/api/') && pathname !== '/go' && !pathname.startsWith('/go?')) {
        return false;
    }

    const now = Date.now();
    const clientData = rateLimitMap.get(clientIp) || { count: 0, resetTime: now + RATE_WINDOW_MS };

    if (now > clientData.resetTime) {
        clientData.count = 1;
        clientData.resetTime = now + RATE_WINDOW_MS;
    } else {
        clientData.count++;
    }

    rateLimitMap.set(clientIp, clientData);

    // Prune stale entries if map exceeds memory bounds
    if (rateLimitMap.size > 1000) {
        for (const [ip, data] of rateLimitMap.entries()) {
            if (now > data.resetTime) rateLimitMap.delete(ip);
        }
    }

    return clientData.count > MAX_REQUESTS_PER_WINDOW;
}

export async function onRequest(context) {
    const url = new URL(context.request.url);
    const pathname = url.pathname.toLowerCase();
    const clientIp = context.request.headers.get("CF-Connecting-IP") || "0.0.0.0";

    // 1. Strict Blocklist: Immediately drop any probe for .git, .env, or sensitive paths
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

    // 2. Edge Rate Limiting: Throttle scrapers & flood bots on dynamic APIs
    if (isRateLimited(clientIp, pathname)) {
        return new Response(JSON.stringify({ error: "429 Too Many Requests: Rate limit exceeded on dynamic endpoint. Try again in 60 seconds." }), {
            status: 429,
            statusText: "Too Many Requests",
            headers: {
                "Content-Type": "application/json",
                "Retry-After": "60",
                "X-RateLimit-Limit": "60",
                "X-RateLimit-Remaining": "0"
            }
        });
    }

    // 3. Execute downstream handler / static asset serving
    const response = await context.next();

    // 4. Institutional Security Headers on all edge responses
    const newHeaders = new Headers(response.headers);
    newHeaders.set("X-Content-Type-Options", "nosniff");
    newHeaders.set("X-Frame-Options", "DENY");
    newHeaders.set("Referrer-Policy", "strict-origin-when-cross-origin");
    newHeaders.set("Permissions-Policy", "geolocation=(), microphone=(), camera=()");

    return new Response(response.body, {
        status: response.status,
        statusText: response.statusText,
        headers: newHeaders
    });
}
