// ============================================================================
// REHAN QUANT LAB™ — SOVEREIGN TEMPLATE VAULT
// "High-Contrast • Clean Semantic • Zero External Font/CSS Bloat"
// Founder & Principal Systems Architect: Mohammad Rehan
// ============================================================================

#[allow(dead_code)]
pub struct TemplateVault;

#[allow(dead_code)]
impl TemplateVault {
    pub const PHOENIX_SENTINEL_MINIFIED: &'static str = r#"
(function(){'use strict';const K='rql_wal_v3',H='rql_sha_v3';function h(s){let x=0;for(let i=0;i<s.length;i++){x=((x<<5)-x)+s.charCodeAt(i);x|=0;}return x.toString(16);}window.addEventListener('DOMContentLoaded',()=>{try{const d=localStorage.getItem(K),s=localStorage.getItem(H);if(d&&s&&h(d)===s){const o=JSON.parse(d);for(const[k,v]of Object.entries(o)){const el=document.getElementById(k);if(el&&!el.value){el.value=v;}}}}catch(e){}const f=document.querySelector('form');if(f){f.addEventListener('input',()=>{const inputs=f.querySelectorAll('input,textarea,select'),s={};inputs.forEach(i=>{if(i.id&&i.value)s[i.id]=i.value;});const p=JSON.stringify(s);try{localStorage.setItem(K,p);localStorage.setItem(H,h(p));}catch(e){}});f.addEventListener('submit',()=>{setTimeout(()=>{try{localStorage.removeItem(K);localStorage.removeItem(H);}catch(e){}},1000);});}});})();
"#;

    pub fn render_client_storefront(
        business_name: &str,
        category: &str,
        tagline: &str,
        phone: &str,
        city: &str,
    ) -> String {
        format!(
            r#"<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{business_name} | {category} in {city}</title>
  <meta name="description" content="{business_name} — Premier {category} in {city}. {tagline}" />
  <link rel="canonical" href="https://{business_slug}.pages.dev/" />
  <script src="https://cdn.tailwindcss.com"></script>
  <script>{sentinel}</script>
</head>
<body class="bg-slate-900 text-slate-100 min-h-screen flex flex-col font-sans">
  <header class="border-b border-slate-800 bg-slate-950/80 backdrop-blur sticky top-0 z-50">
    <div class="max-w-6xl mx-auto px-4 py-4 flex justify-between items-center">
      <div class="flex items-center gap-2">
        <span class="w-2.5 h-2.5 rounded-full bg-cyan-400"></span>
        <span class="font-bold text-lg text-white tracking-tight">{business_name}</span>
      </div>
      <a href="tel:{phone}" class="bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold px-4 py-2 rounded-xl text-xs font-mono transition">Call Now</a>
    </div>
  </header>
  <main class="flex-grow max-w-6xl mx-auto px-4 py-16 text-center">
    <div class="inline-block bg-slate-800 border border-slate-700 px-3.5 py-1 rounded-full text-xs font-mono text-cyan-300 mb-6">{category} • {city}</div>
    <h1 class="text-4xl sm:text-6xl font-extrabold text-white tracking-tight max-w-3xl mx-auto leading-tight">{business_name}</h1>
    <p class="mt-6 text-slate-400 text-lg max-w-xl mx-auto leading-relaxed">{tagline}</p>
    <div class="mt-10 flex justify-center gap-4">
      <a href="https://wa.me/{clean_phone}?text=Hello%20{business_name},%20I%20want%20to%20inquire." target="_blank" class="bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold px-6 py-3 rounded-xl transition font-mono text-sm">WhatsApp Concierge</a>
      <a href="tel:{phone}" class="bg-slate-800 hover:bg-slate-700 text-white border border-slate-700 font-bold px-6 py-3 rounded-xl transition font-mono text-sm">Direct Phone</a>
    </div>
  </main>
  <footer class="border-t border-slate-800 py-6 text-center text-xs text-slate-500 font-mono">
    © 2026 {business_name} • Powered by Rehan Quant Lab Sovereign Pure-Rust Engine
  </footer>
</body>
</html>"#,
            business_name = business_name,
            category = category,
            city = city,
            tagline = tagline,
            phone = phone,
            clean_phone = phone.replace('+', "").replace(' ', ""),
            business_slug = business_name.to_lowercase().replace(' ', "-"),
            sentinel = Self::PHOENIX_SENTINEL_MINIFIED
        )
    }
}
