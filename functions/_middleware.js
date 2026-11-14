// ====================================================================
// Cloudflare Pages Security Edge Middleware - Rehan Quant Lab (RQL)
// Defense-in-Depth against Hidden Dotfiles, Exploit Scanners, and Probes
// ====================================================================

export async function onRequest(context) {
    const url = new URL(context.request.url);
    const pathname = url.pathname.toLowerCase();

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

    // 2. Execute downstream handler / static asset serving
    const response = await context.next();

    // 3. Institutional Security Headers on all edge responses
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
