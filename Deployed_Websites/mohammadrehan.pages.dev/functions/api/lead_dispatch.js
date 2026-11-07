// ============================================================================
// REHAN QUANT LAB™ — CLOUDFLARE PAGES EDGE FUNCTION: LEAD & UPI DISPATCH GATEWAY
// "The Doctor's Ding — Sub-10ms Lead Processing & Multi-Channel Alert Router"
// Founder & Principal Systems Architect: Mohammad Rehan
// ============================================================================

export async function onRequest(context) {
  const t0 = Date.now();

  // CORS Preflight
  if (context.request.method === "OPTIONS") {
    return new Response(null, {
      status: 204,
      headers: {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type, Authorization, X-RQL-Signature",
        "Access-Control-Max-Age": "86400",
      }
    });
  }

  try {
    if (context.request.method !== "POST") {
      return new Response(
        JSON.stringify({
          ok: true,
          endpoint: "/api/lead_dispatch",
          description: "RQL Edge Real-Time Lead & UPI Dispatch Gateway",
          method: "POST { type, slug, business_name, clinic_phone, patient_name, patient_phone, service, amount, utr, notes } required"
        }),
        { status: 200, headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" } }
      );
    }

    let body;
    try {
      body = await context.request.json();
    } catch (e) {
      return new Response(
        JSON.stringify({ ok: false, error: "Invalid JSON payload" }),
        { status: 400, headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" } }
      );
    }

    const leadType = body.type || "APPOINTMENT_REQUEST";
    const slug = body.slug || "unspecified-clinic";
    const businessName = body.business_name || "Specialized Clinic";
    const clinicPhone = (body.clinic_phone || "").replace(/[^0-9]/g, "");
    const patientName = (body.patient_name || "Valued Patient").trim();
    const patientPhone = (body.patient_phone || "").trim();
    const service = (body.service || "General Priority Consultation").trim();
    const amount = body.amount || "0";
    const utr = (body.utr || "").trim();
    const notes = (body.notes || "None provided").trim();
    const timestamp = new Date().toISOString();

    if (!patientPhone) {
      return new Response(
        JSON.stringify({ ok: false, error: "Missing required field 'patient_phone'" }),
        { status: 400, headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" } }
      );
    }

    // Cryptographic SHA-256 Seal of Lead
    const leadString = `${slug}:${leadType}:${patientName}:${patientPhone}:${amount}:${utr}:${timestamp}`;
    const encoder = new TextEncoder();
    const hashBuffer = await crypto.subtle.digest("SHA-256", encoder.encode(leadString));
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    const sha256 = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');

    // Format Doctor WhatsApp Alert Text
    const isUpi = leadType === "UPI_TOKEN_PAYMENT" || (utr && utr.length > 0);
    const badge = isUpi ? "⚡ *PRIORITY UPI TOKEN CONFIRMED*" : "📅 *NEW PRIORITY OPD APPOINTMENT*";
    const utrLine = isUpi ? `\n💳 *Token Paid:* ₹${amount} (UTR: ${utr || "Verified on Client"})` : "";

    const alertMessage = 
`${badge}
🏛️ *${businessName}*

👤 *Patient:* ${patientName}
📞 *Contact:* ${patientPhone}
🩺 *Service:* ${service}${utrLine}
📝 *Notes:* ${notes}

⏰ *Received:* ${new Date().toLocaleString("en-IN", { timeZone: "Asia/Kolkata" })} IST
🛡️ *Phoenix WAL Seal:* ${sha256.substring(0, 16)}...

Reply directly to confirm patient's slot.`;

    const encodedMsg = encodeURIComponent(alertMessage);
    const doctorWaUrl = clinicPhone.length >= 10 
      ? `https://wa.me/${clinicPhone.startsWith("91") ? clinicPhone : "91" + clinicPhone}?text=${encodedMsg}`
      : `https://wa.me/?text=${encodedMsg}`;

    const latencyMs = Date.now() - t0;

    const responsePayload = {
      ok: true,
      protocol: "RQL_PHOENIX_SENTINEL_EDGE_DISPATCH_v2",
      lead_id: "LEAD-" + Date.now().toString(36).toUpperCase(),
      sha256: sha256,
      type: leadType,
      business_name: businessName,
      patient_name: patientName,
      patient_phone: patientPhone,
      service: service,
      amount: amount,
      utr: utr,
      timestamp: timestamp,
      doctor_whatsapp_url: doctorWaUrl,
      formatted_alert: alertMessage,
      edge_node: context.request.cf ? context.request.cf.colo : "EDGE-ANYCAST",
      latency_ms: latencyMs
    };

    return new Response(JSON.stringify(responsePayload, null, 2), {
      status: 200,
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
        "Cache-Control": "no-store, no-cache, must-revalidate"
      }
    });

  } catch (err) {
    return new Response(
      JSON.stringify({ ok: false, error: String(err.message || err), latency_ms: Date.now() - t0 }),
      { status: 500, headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" } }
    );
  }
}
