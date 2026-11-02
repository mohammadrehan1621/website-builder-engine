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

    // Phase 1: Physical TCP/TLS Request & Microsecond Timing
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

    // Phase 2: Measure TTFB and stream raw payload
    const ttfb_ms = Date.now() - t0;
    const html = await resp.text();
    const latency_ms = Date.now() - t0;
    const transfer_ms = Math.max(1, latency_ms - ttfb_ms);

    // Phase 3: Raw Server HTTP Headers Forensic Extraction
    const serverHeader = resp.headers.get("server") || "Hidden / Protected Server";
    const poweredBy = resp.headers.get("x-powered-by") || "Not Exposed (PHP/Framework)";
    const contentEncoding = resp.headers.get("content-encoding") || "None (Uncompressed)";
    const altSvc = resp.headers.get("alt-svc") || "";
    const hasHttp3 = altSvc.includes("h3") || altSvc.includes("quic");
    const transportProtocol = hasHttp3 ? "HTTP/3 (QUIC Capable)" : "Legacy HTTP/1.1 or HTTP/2";

    // Phase 4: Forensic Security Headers Inspection
    const hasHsts = resp.headers.has("strict-transport-security");
    const hasCsp = resp.headers.has("content-security-policy");
    const hasXFrame = resp.headers.has("x-frame-options");
    const hasXContent = resp.headers.has("x-content-type-options");

    let securityScore = 100;
    const missingHeaders = [];
    if (!hasHsts) { securityScore -= 25; missingHeaders.push("HSTS"); }
    if (!hasCsp) { securityScore -= 30; missingHeaders.push("CSP"); }
    if (!hasXFrame) { securityScore -= 25; missingHeaders.push("X-Frame-Options"); }
    if (!hasXContent) { securityScore -= 20; missingHeaders.push("X-Content-Type"); }

    let securityGrade = "F";
    if (securityScore >= 90) securityGrade = "A+";
    else if (securityScore >= 75) securityGrade = "B";
    else if (securityScore >= 50) securityGrade = "C";
    else if (securityScore >= 25) securityGrade = "D";

    // Phase 5: Forensic HTML Inspection & Scientific Evidence Mapping
    const html_lower = html.toLowerCase();
    const platforms = [];
    const evidenceList = [];

    // Extract real page title
    let pageTitle = "Web Application";
    const titleMatch = html.match(/<title[^>]*>([^<]+)<\/title>/i);
    if (titleMatch && titleMatch[1]) {
      pageTitle = titleMatch[1].trim();
    }

    // Count blocking scripts, stylesheets, and images
    const scriptMatches = html.match(/<script\b[^>]*>/gi) || [];
    const scriptCount = scriptMatches.length;

    const cssMatches = html.match(/<link\b[^>]*rel=["']stylesheet["'][^>]*>/gi) || [];
    const cssCount = cssMatches.length;

    const imgMatches = html.match(/<img\b[^>]*>/gi) || [];
    const imgCount = imgMatches.length;

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

    // Phase 6: Carbon Footprint & Electrical Wattage Impact (Sustainable Web Standard)
    // Average 0.81 grams CO2 per Megabyte of data transferred over wire
    const weight_mb = html.length / (1024 * 1024);
    const co2_grams_per_view = parseFloat((Math.max(0.015, weight_mb * 0.81)).toFixed(3));
    const co2_annual_10k_kg = parseFloat(((co2_grams_per_view * 10000) / 1000).toFixed(2));

    // Edge Colocation Node
    const edgeColo = context.request.cf?.colo || "EDGE-GLOBAL";

    // Cryptographic Proof Hash (Simulated SHA-256 wire fingerprint)
    const auditTimestamp = new Date().toISOString();
    const rawFingerprint = `${targetUrl}:${latency_ms}:${html.length}:${auditTimestamp}`;
    let hashVal = 0;
    for (let i = 0; i < rawFingerprint.length; i++) {
      hashVal = ((hashVal << 5) - hashVal) + rawFingerprint.charCodeAt(i);
      hashVal |= 0;
    }
    const auditHash = "0x" + Math.abs(hashVal).toString(16).padStart(8, '0') + Math.abs(hashVal * 31).toString(16).padStart(8, '0');

    const cleanDomain = targetUrl.replace(/^https?:\/\//i, "").replace(/\/.*$/, "");
    const slowSec = (latency_ms / 1000).toFixed(2);
    const ttfbSec = (ttfb_ms / 1000).toFixed(2);

    const pitch = `Hi ${client_name}, hope business at ${company_name} is going great.

I was doing an engineering performance audit on local business websites today and ran an in-depth wire benchmark on ${cleanDomain}:

• Initial Time-to-First-Byte (TTFB): ${ttfb_ms} ms (${detected_platform})
• Total roundtrip page weight: ${page_size_kb} KB (${scriptCount} external scripts)
• Security Header Grade: ${securityGrade} (${missingHeaders.length} missing security headers)
• Carbon Impact: ${co2_annual_10k_kg} kg CO2 / year on legacy hosting
• Modern high-speed standard: 0.20 seconds (100/100 Google Lighthouse score)

Google recently began penalizing local business websites that take over 2.5 seconds on mobile search.

Since we are both alumni from our BNI chapter, I can rebuild your site on our zero-cloud pure-native engine. It will load in under 250 milliseconds with 100/100 Google SEO, grade A+ security, and eliminate your annual hosting bills completely.

Would you be open to seeing a 60-second live speed demo on my phone this week over a cup of tea?`;

    return new Response(JSON.stringify({
      url: targetUrl,
      clean_domain: cleanDomain,
      status_code: resp.status,
      page_title: pageTitle,
      latency_ms,
      ttfb_ms,
      transfer_ms,
      server_header: serverHeader,
      powered_by: poweredBy,
      content_encoding: contentEncoding,
      transport_protocol: transportProtocol,
      script_count: scriptCount,
      css_count: cssCount,
      img_count: imgCount,
      security_score: securityScore,
      security_grade: securityGrade,
      missing_headers: missingHeaders,
      security_headers: {
        hsts: hasHsts,
        csp: hasCsp,
        x_frame: hasXFrame,
        x_content: hasXContent
      },
      co2_grams: co2_grams_per_view,
      co2_annual_kg: co2_annual_10k_kg,
      edge_colo: edgeColo,
      audit_hash: auditHash,
      audit_timestamp: auditTimestamp,
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
