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

    // Phase 1: Physical TCP/TLS Request & Timing
    const t0 = Date.now();
    let resp;
    try {
      resp = await fetch(targetUrl, {
        headers: {
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
          "Accept-Language": "en-US,en;q=0.9"
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
        error: `Target server returned error status HTTP ${resp.status} (Domain offline, DNS failed, or blocked)` 
      }), {
        status: 400,
        headers: { "Content-Type": "application/json" }
      });
    }

    // Phase 2: Measure TTFB and stream payload
    const ttfb_ms = Date.now() - t0;
    const html = await resp.text();
    const latency_ms = Date.now() - t0;

    // Phase 3: Raw Server HTTP Headers Forensic Extraction
    const serverHeader = resp.headers.get("server") || "Hidden / Protected Server";
    const poweredBy = resp.headers.get("x-powered-by") || "Not Exposed (PHP/Framework)";
    const contentEncoding = resp.headers.get("content-encoding") || "None (Uncompressed)";

    // Phase 4: Forensic HTML Inspection & Scientific Evidence Mapping
    const html_lower = html.toLowerCase();
    const platforms = [];
    const evidenceList = [];

    // Extract real page title
    let pageTitle = "Web Application";
    const titleMatch = html.match(/<title[^>]*>([^<]+)<\/title>/i);
    if (titleMatch && titleMatch[1]) {
      pageTitle = titleMatch[1].trim();
    }

    // Count blocking scripts and stylesheets
    const scriptMatches = html.match(/<script\b[^>]*>/gi) || [];
    const scriptCount = scriptMatches.length;

    const cssMatches = html.match(/<link\b[^>]*rel=["']stylesheet["'][^>]*>/gi) || [];
    const cssCount = cssMatches.length;

    if (html_lower.includes("wp-content") || html_lower.includes("wp-includes")) {
      platforms.push("WordPress (PHP)");
      evidenceList.push("Detected /wp-content/ asset paths");
    }
    if (html_lower.includes("elementor")) {
      platforms.push("Elementor Builder");
      evidenceList.push("Detected Elementor DOM layout engine");
    }
    if (html_lower.includes("woocommerce")) {
      platforms.push("WooCommerce");
      evidenceList.push("Detected WooCommerce cart & checkout scripts");
    }
    if (html_lower.includes("wix.com") || html_lower.includes("_wix")) {
      platforms.push("Wix.com");
      evidenceList.push("Detected Wix cloud server infrastructure");
    }
    if (html_lower.includes("shopify")) {
      platforms.push("Shopify");
      evidenceList.push("Detected Shopify liquid storefront CDN");
    }
    if (platforms.length === 0) {
      platforms.push(serverHeader);
      evidenceList.push(`Raw HTTP Server Signature: ${serverHeader}`);
    }

    const detected_platform = platforms.join(", ");
    const page_size_kb = parseFloat((html.length / 1024).toFixed(1));
    const rql_baseline_ms = 208.0;
    const slowdown_factor = parseFloat((latency_ms / rql_baseline_ms).toFixed(1));

    const cleanDomain = targetUrl.replace(/^https?:\/\//i, "").replace(/\/.*$/, "");
    const slowSec = (latency_ms / 1000).toFixed(2);
    const ttfbSec = (ttfb_ms / 1000).toFixed(2);

    const pitch = `Hi ${client_name}, hope business at ${company_name} is going great.

I was doing an engineering performance audit on local business websites today and ran an in-depth wire benchmark on ${cleanDomain}:

• Initial Time-to-First-Byte (TTFB): ${ttfb_ms} ms (${detected_platform})
• Total roundtrip page weight: ${page_size_kb} KB (${scriptCount} external scripts)
• Modern high-speed standard: 0.20 seconds (100/100 Google Lighthouse score)

Google recently began penalizing local business websites that take over 2.5 seconds on mobile search.

Since we are both alumni from our BNI chapter, I can rebuild your site on our zero-cloud pure-native engine. It will load in under 250 milliseconds with 100/100 Google SEO, and eliminate your annual hosting bills completely.

Would you be open to seeing a 60-second live speed demo on my phone this week over a cup of tea?`;

    return new Response(JSON.stringify({
      url: targetUrl,
      clean_domain: cleanDomain,
      status_code: resp.status,
      page_title: pageTitle,
      latency_ms,
      ttfb_ms,
      server_header: serverHeader,
      powered_by: poweredBy,
      content_encoding: contentEncoding,
      script_count: scriptCount,
      css_count: cssCount,
      detected_platform,
      evidence: evidenceList,
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
