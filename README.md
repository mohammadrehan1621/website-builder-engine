# Autonomous Website Builder & Agency Studio (AI + CLI + UI)

A full-stack, autonomous website builder and client acquisition suite that transforms natural language prompts, structured business data (JSON), PDF brochures, or a hybrid of all three into complete, production-grade, zero-error websites with multi-page support, security hardening, user authentication, and sales proposals.

---

## 🌟 Key Capabilities

1. **🌐 Multi-Page & Single-Page Architecture**:
   - **Single-Page Full App**: Smooth internal anchor scrolling (`#about`, `#services`, `#projects`, `#contact`).
   - **Multi-Page Connected Architecture**: Generates 4 interconnected pages (`index.html`, `about.html`, `services.html`, `contact.html`) with shared styling and working relative cross-links.
   - **Universal Self-Healing Navigation Guard**: Automatically prevents local `file:///` 404s when previewing offline.
   - **1-Click Auto-Export**: Saves all pages to `C:\Users\rehan\Desktop\Generated_Website` and offers a 1-click **"📂 Open on Desktop"** button.

2. **🛡️ Enterprise Security & 🔐 Authentication Layers**:
   - **Security**: Content Security Policy (CSP) meta tags, XSS/anti-tamper form sanitization, 256-Bit SSL trust badges, and GDPR/CCPA cookie consent banners.
   - **Authentication**: Modern client-side Auth Modal (Sign In / Register), password visibility toggles, and dynamic user session portal in the navbar.

3. **✨ Futuristic Holographic AI Mascot (Aria v2.5 // Neural Interface)**:
   - Interactive cyberpunk anime mascot with glowing scan-lines, floating hologram capsule, particle glow, and instant neural FAQ responder.

4. **🔄 Self-Healing Sentinel & 24/7 Watchdog Daemon**:
   - **Resilient Model Cascade**: Seamlessly routes across Gemini models (`gemini-3.5-flash` → `gemini-3.6-flash` → `gemini-3.5-flash-lite` → `gemini-3.8-flash`) if quota limits (429) or transient spikes (503) occur.
   - **Watchdog Daemon (`watchdog_healer.py`)**: Continuously monitors port **8503**, clears zombie process locks, benchmarks model health, and auto-restores Streamlit in < 10 seconds.

5. **💼 Agency Sales & Client Proposal Engine (Tab 2)**:
   - Generates bespoke client pitches, site audits, ROI projections in **₹ INR**, cold outreach emails, and 30-second elevator closing scripts.
   - 1-click export to an executive, beautifully styled **PDF Proposal**.

---

## 🚀 Quick Start

### 1. Launch Web UI Studio (Port 8503)
```bash
streamlit run streamlit_app.py --server.port 8503
```
Open **[http://localhost:8503](http://localhost:8503)** in your browser.

### 2. Launch Self-Healing Watchdog (Background Daemon)
```bash
python watchdog_healer.py
```

### 3. Headless CLI Script (`generate_site.py`)
```bash
# Single-page landing page:
python generate_site.py --prompt "Modern AI SaaS landing page" --serve

# Multi-page website with security and authentication:
python generate_site.py --prompt "Fintech Wealth Management Advisory" --multipage --security --auth --output ./my_site --serve

# Ingest business JSON data:
python generate_site.py --data sample_business.json --multipage --serve
```

---

## 💰 Monetization & Agency Playbook

1. **24-Hour Website Turnaround Service**:
   - Charge local businesses (clinics, real estate, consultants, gyms, restaurants) ₹5,000 - ₹25,000 per website with instant turnaround.
2. **Cold Outreach with Instant Mockups**:
   - Use Tab 2 to generate audit & pitch, build a sample preview in 30 seconds, and send the owner a screenshot with a 1-click WhatsApp message.
3. **Monthly Maintenance Retainers (MRR)**:
   - Charge ₹999 - ₹2,999 / month per client for hosting on Cloudflare Pages, WhatsApp lead routing, and content updates.
