export async function onRequestPost(context) {
  try {
    const body = await context.request.json();
    const url = body.url;
    const client_name = body.client_name || "Sir";
    const company_name = body.company_name || "your firm";

    if (!url) {
      return new Response(JSON.stringify({ error: "Missing URL to audit" }), { 
        status: 400,
        headers: { "Content-Type": "application/json" }
      });
    }

    let targetUrl = url.trim();
    if (!targetUrl.startsWith("http://") && !targetUrl.startsWith("https://")) {
      targetUrl = "https://" + targetUrl;
    }

    const t0 = Date.now();
    let resp;
    try {
      resp = await fetch(targetUrl, {
        headers: {
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        },
        redirect: "follow"
      });
    } catch (netErr) {
      return new Response(JSON.stringify({ 
        error: `Could not resolve host or establish network connection to ${targetUrl}: ${netErr.message}` 
      }), {
        status: 502,
        headers: { "Content-Type": "application/json" }
      });
    }

    // Verify HTTP Success - Reject dead/unresolved domains
    if (!resp.ok || resp.status >= 400) {
      return new Response(JSON.stringify({ 
        error: `Target server returned error status HTTP ${resp.status} (Domain offline or DNS failed)` 
      }), {
        status: 400,
        headers: { "Content-Type": "application/json" }
      });
    }

    const latency_ms = Date.now() - t0;
    const html = await resp.text();
    const html_lower = html.toLowerCase();

    // Real technical detection from actual HTML source
    const platforms = [];
    if (html_lower.includes("wp-content") || html_lower.includes("wp-includes")) {
      platforms.push("WordPress (PHP)");
    }
    if (html_lower.includes("elementor")) {
      platforms.push("Elementor Page Builder");
    }
    if (html_lower.includes("woocommerce")) {
      platforms.push("WooCommerce");
    }
    if (html_lower.includes("wix.com") || html_lower.includes("_wix")) {
      platforms.push("Wix.com");
    }
    if (html_lower.includes("shopify")) {
      platforms.push("Shopify");
    }
    if (platforms.length === 0) {
      const serverHdr = resp.headers.get("server") || "Custom / Legacy Server";
      platforms.push(serverHdr);
    }

    const detected_platform = platforms.join(", ");
    const page_size_kb = parseFloat((html.length / 1024).toFixed(1));
    const rql_baseline_ms = 208.0;
    const slowdown_factor = parseFloat((latency_ms / rql_baseline_ms).toFixed(1));

    const cleanDomain = targetUrl.replace(/^https?:\/\//i, "").replace(/\/.*$/, "");
    const slowSec = (latency_ms / 1000).toFixed(2);

    const pitch = `Hi ${client_name}, hope business at ${company_name} is going great.

I was doing an engineering performance audit on local business websites today and ran a test on ${cleanDomain}:

• Current site load time: ${slowSec} seconds (${detected_platform})
• Modern high-speed standard: 0.20 seconds (100/100 Google Lighthouse score)

Google recently began penalizing local business websites that take over 2.5 seconds on mobile search.

Since we are both alumni from our BNI chapter, I can rebuild your site on our zero-cloud pure-native engine. It will load in under 250 milliseconds with 100/100 Google SEO, and eliminate your annual hosting bills completely.

Would you be open to seeing a 60-second live speed demo on my phone this week over a cup of tea?`;

    return new Response(JSON.stringify({
      url: targetUrl,
      status_code: resp.status,
      latency_ms,
      detected_platform,
      page_size_kb,
      slowdown_factor,
      whatsapp_pitch: pitch
    }), {
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
      }
    });
  } catch (err) {
    return new Response(JSON.stringify({ error: err.message || "Failed to reach target website across the network" }), {
      status: 500,
      headers: { "Content-Type": "application/json" }
    });
  }
}
