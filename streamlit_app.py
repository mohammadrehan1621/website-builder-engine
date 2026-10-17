import os
import re
import json
import io
import zipfile
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components
from dotenv import load_dotenv

import importlib
import generator
import pdf_generator
import hosting_deployer
import self_healing
import link_extractor
import seo_analyzer
import lead_crm

importlib.reload(generator)
importlib.reload(pdf_generator)
importlib.reload(hosting_deployer)
importlib.reload(self_healing)
importlib.reload(link_extractor)
importlib.reload(seo_analyzer)
importlib.reload(lead_crm)

from generator import WebsiteGenerator, get_api_key
from pdf_generator import create_styled_pitch_pdf, create_styled_resume_pdf
from hosting_deployer import (
    deploy_to_cloudflare_pages, deploy_to_netlify_drop, resolve_cloudflare_credentials,
    save_cloudflare_credentials, add_custom_domain_to_cloudflare, list_cloudflare_custom_domains,
    get_deployed_sites_registry
)
from self_healing import SelfHealingSentinel
from link_extractor import extract_source_data
from seo_analyzer import analyze_website_seo, auto_optimize_seo, generate_sitemap_xml, generate_robots_txt
from lead_crm import get_all_leads, log_new_lead, export_leads_to_csv, clear_all_leads

try:
    from phoenix_engine import PhoenixTelemetry, ImmunityVault, CircuitBreaker, AshLedger, ChaosLedger
    HAS_PHOENIX = True
except ImportError:
    HAS_PHOENIX = False

env_file = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_file)
load_dotenv()

st.set_page_config(
    page_title="Autonomous AI Website Builder",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #2563eb, #7c3aed, #db2777);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .sub-text {
        color: #475569;
        font-size: 1.05rem;
        margin-bottom: 1.5rem;
    }
    .badge-card {
        padding: 0.6rem 1rem;
        border-radius: 8px;
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        color: #1e293b;
        font-size: 0.85rem;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar: Settings
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=64)
    st.title("Studio Settings")
    
    # Secure background key loading (never exposed to UI)
    api_key_input = get_api_key()

    if HAS_PHOENIX:
        p_telem = PhoenixTelemetry.load()
        p_health = p_telem.get("health_index", 100.0)
        p_res = p_telem.get("total_resurrections", 0)
        p_mttr = p_telem.get("avg_mttr_ms", 0.0)
        p_color = "#10b981" if p_health >= 85 else "#f59e0b"
        streak = ChaosLedger.get_consecutive_passes()
        st.markdown(f"""
        <div style="padding: 10px 12px; border-radius: 9px; background: rgba(249, 115, 22, 0.08); border: 1px solid rgba(249, 115, 22, 0.3); margin-top: 8px; margin-bottom: 8px;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 5px;">
                <span style="font-weight: 700; font-size: 11.5px; color: #ea580c; display: flex; align-items: center; gap: 5px;">
                    🔥 Phoenix Engine Active
                </span>
                <span style="font-size: 10px; font-weight: 800; color: {p_color}; background: rgba(16, 185, 129, 0.12); padding: 1px 5px; border-radius: 4px;">
                    {p_health}% HEALTH
                </span>
            </div>
            <div style="font-size: 10.5px; color: #64748b; display: flex; justify-content: space-between; margin-bottom: 4px;">
                <span>Resurrections: <b>{p_res}</b></span>
                <span>MTTR: <b>{p_mttr}ms</b></span>
            </div>
            <div style="font-size: 10px; color: #10b981; font-weight: 700; display: flex; align-items: center; justify-content: space-between; border-top: 1px dashed rgba(249,115,22,0.25); padding-top: 4px;">
                <span>🛡️ Sentinel: <b>ARMED 24/7</b></span>
                <span>Streak: <b>{streak}x 100%</b></span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="padding: 6px 12px; border-radius: 8px; background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.35); color: #34d399; font-size: 11.5px; font-weight: 600; display: flex; align-items: center; gap: 6px; margin-top: 8px; margin-bottom: 8px;">
            <span style="display: inline-block; width: 7px; height: 7px; border-radius: 50%; background: #10b981;"></span>
            Self-Healing Watchdog: Active
        </div>
        """, unsafe_allow_html=True)

    with st.expander("💥 Chaos Engineering Lab", expanded=False):
        st.caption("Permanent Adversarial Gauntlet: Continuous audits auto-fire on boot & every hour.")
        
        # Display latest audit status
        latest_drill = ChaosLedger.get_latest() if HAS_PHOENIX else None
        if latest_drill:
            l_score = latest_drill.get("score", 0.0)
            l_mode = latest_drill.get("mode", "UNKNOWN")
            l_time = latest_drill.get("timestamp", "Never")
            l_dur = latest_drill.get("duration_ms", 0.0)
            l_defended = latest_drill.get("defended", 0)
            l_total = latest_drill.get("total", 0)
            status_badge = "🟢 TITANIUM GRADE" if l_score >= 100 else "⚠️ HARDENING NEEDED"
            st.markdown(f"""
            <div style="background: rgba(15, 23, 42, 0.6); padding: 8px 10px; border-radius: 6px; border: 1px solid rgba(100, 116, 139, 0.3); font-size: 11px; margin-bottom: 8px;">
                <div style="display: flex; justify-content: space-between; font-weight: 700; color: #38bdf8;">
                    <span>Latest Audit: {l_score:.1f}%</span>
                    <span>{status_badge}</span>
                </div>
                <div style="color: #94a3b8; font-size: 10px; margin-top: 2px;">
                    Defended: {l_defended}/{l_total} Missiles | {l_dur:.1f}ms<br>
                    Mode: <code>{l_mode}</code><br>
                    Time: {l_time}
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        if st.button("🔥 Run Live 5-Missile Gauntlet", use_container_width=True):
            try:
                import chaos_lab
                with st.spinner("Firing 5 Chaos Missiles at Phoenix Engine..."):
                    audit = chaos_lab.run_chaos_gauntlet(mode="STUDIO_UI_LIVE")
                    st.success(f"Gauntlet Complete! Score: {audit['score']:.1f}% in {audit['duration_ms']:.1f}ms")
                    for name, ok in audit.get("results", {}).items():
                        st.write(f"• {name}: {'🟢 Defended' if ok else '🔴 Failed'}")
                    st.rerun()
            except Exception as ce:
                st.error(f"Chaos drill error: {ce}")

        # Historical Audit Ledger
        if HAS_PHOENIX:
            history = ChaosLedger.get_history(limit=5)
            if history:
                with st.expander("📜 Audit History Ledger", expanded=False):
                    for h in reversed(history):
                        s_color = "green" if h.get("score", 0) >= 100 else "orange"
                        st.markdown(f"- **{h.get('timestamp')}** (`{h.get('mode')}`): :{s_color}[{h.get('score')}% ({h.get('defended')}/{h.get('total')})] in {h.get('duration_ms', 0):.0f}ms")

    with st.expander("🌐 Cloudflare Live Hosting", expanded=False):
        curr_acc, curr_tok = resolve_cloudflare_credentials()
        st.caption("Active Cloudflare Pages credentials:")
        cf_acc_val = st.text_input("Account ID", value=curr_acc, key="cf_account_input")
        cf_tok_val = st.text_input("API Token", value=curr_tok, type="password", key="cf_token_input")
        if st.button("💾 Save Credentials to .env", use_container_width=True):
            saved = save_cloudflare_credentials(cf_acc_val, cf_tok_val)
            if saved:
                st.toast("Saved Cloudflare credentials to .env!", icon="✅")
            else:
                st.warning("Could not write to .env file.")

    with st.expander("🚀 Saved Live Deployed Sites", expanded=True):
        deployed_reg = get_deployed_sites_registry()
        if deployed_reg:
            st.caption(f"**{len(deployed_reg)} Active Sites Online:**")
            for dom, info in deployed_reg.items():
                p_name = info.get("project_name", dom)
                l_url = info.get("live_url", f"https://{dom}")
                l_path = info.get("local_path", "")
                pages = info.get("pages", [])
                st.markdown(f"""
                <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.28); border-radius: 8px; padding: 10px; margin-bottom: 8px;">
                    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 4px;">
                        <span style="font-weight: 700; font-size: 12.5px; color: #047857;">🌐 {p_name}</span>
                        <span style="font-size: 10px; background: #10b981; color: white; padding: 2px 6px; border-radius: 4px; font-weight: 700;">LIVE</span>
                    </div>
                    <div style="font-size: 11px; margin-bottom: 4px; font-family: monospace;">
                        <a href="{l_url}" target="_blank" style="color: #2563eb; text-decoration: none; font-weight: 600;">🔗 {dom}</a>
                    </div>
                    <div style="font-size: 10px; color: #6b7280; margin-bottom: 6px;">
                        📄 Pages: {', '.join(pages) if pages else 'index.html'}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                col_live_a, col_live_b = st.columns([1, 1])
                with col_live_a:
                    st.link_button("🌐 Visit Live", l_url, use_container_width=True)
                with col_live_b:
                    if st.button("📂 Open Folder", key=f"open_live_{dom}", use_container_width=True, help=f"Open backup folder for {dom}"):
                        target_dir = Path(l_path) if l_path and Path(l_path).exists() else (Path(__file__).resolve().parent / "Deployed_Websites" / dom)
                        if target_dir.exists():
                            os.system(f'explorer "{target_dir}"')
                            st.toast(f"Opened folder for {dom}!", icon="📂")
                        else:
                            st.warning(f"Backup folder not found: {target_dir}")
            
            if st.button("📂 Open Deployed Sites Directory", use_container_width=True, help="Opens Deployed_Websites folder inside website_builder"):
                all_sites_dir = Path(__file__).resolve().parent / "Deployed_Websites"
                if not all_sites_dir.exists():
                    all_sites_dir = Path("C:/Users/rehan/Desktop/Deployed_Websites")
                all_sites_dir.mkdir(parents=True, exist_ok=True)
                os.system(f'explorer "{all_sites_dir}"')
        else:
            st.info("No deployed sites recorded yet. Deploy a website to see it cataloged here!")

    st.markdown("---")
    theme_preset = st.selectbox(
        "Design Theme & Aesthetic",
        [
            "⚪ Minimal Pure & Modern Clean (Crisp White, Slate Hairlines, High-Readability Minimalist UI)",
            "🍙 Minimalist Dark Monochrome (Deep Matte Charcoal, Zero Clutter, Stark Clean Typography)",
            "⚡ Modern Dark Slate & Electric Purple (SaaS / AI / Tech)",
            "🍏 Clean Minimalist White & Titanium (Apple / High-End Fintech)",
            "🌌 Cyberpunk Neon Glow & Deep AMOLED Black (Web3 / Crypto / Gaming)",
            "🏛️ Ultra Luxury & Gold Accents (High-End Real Estate / Jewelry / Private Equity)",
            "🌿 Organic Earthy & Warm Botanical (Wellness / Eco / Coffee / Organic Brands)",
            "💼 Executive Navy & Crisp Slate (Corporate Law / Consulting / Healthcare)",
            "🎨 Brutalist Retro & Bold Typography (Creative Studio / Fashion / Design Agency)",
            "☀️ Sunset Coral & Modern Pastel (B2C Mobile Apps / Social Platforms / Creator Economy)",
            "🖤 Monochromatic High-Contrast Editorial (Photography / Portfolio / Architecture)",
            "🏥 Clean Trust Medical Blue & Mint (Dental / Clinics / Telehealth / MedTech)",
            "🔥 High-Impact Energetic Orange & Obsidian (Fitness / Crossfit / High-Ticket Coaching)",
            "✨ Custom Aesthetic (Specify Your Own Below)"
        ]
    )

    custom_theme = ""
    if "Custom Aesthetic" in theme_preset:
        custom_theme = st.text_input(
            "Describe your custom aesthetic / colors:",
            placeholder="e.g. Deep emerald green with champagne gold accents and serif typography"
        )
    
    effective_theme = custom_theme if custom_theme else theme_preset
    
    model_choice = st.selectbox(
        "Gemini Reasoning Engine",
        [
            "⚡ Gemini 3.5 Flash (Recommended - High Quota & Fast)",
            "🛡️ Auto-Resilient Fleet (Auto Failover)",
            "gemini-3.6-flash",
            "gemini-3.5-flash-lite",
            "gemini-3.8-flash"
        ],
        index=0,
        help="Gemini 3.5 Flash provides ultra-fast generation with high free-tier quotas and automated resilience."
    )
    model_map = {
        "⚡ Gemini 3.5 Flash (Recommended - High Quota & Fast)": "gemini-3.5-flash",
        "🛡️ Auto-Resilient Fleet (Auto Failover)": "gemini-3.5-flash",
        "gemini-3.6-flash": "gemini-3.6-flash",
        "gemini-3.5-flash-lite": "gemini-3.5-flash-lite",
        "gemini-3.8-flash": "gemini-3.8-flash"
    }
    effective_model = model_map.get(model_choice, "gemini-3.5-flash")
    
    st.markdown("---")
    st.markdown("### 🛠️ Builder Features")
    st.markdown("- **Option 1:** Interactive UI with live IFrame preview")
    st.markdown("- **Option 2:** Structured JSON Data ingestion")
    st.markdown("- **Option 3:** Pure AI Autonomous Prompt-to-Site")
    st.markdown("- **Export:** One-click ZIP download")

# Main Content Area
st.markdown('<div class="main-header">⚡ Autonomous Website & Client Pitch Suite</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Combine pure AI prompts + structured data to autonomously generate production-grade websites and high-converting client pitches.</div>', unsafe_allow_html=True)

tabs = st.tabs(["🚀 Generator Studio", "📇 Client Leads & CRM", "🔍 SEO & Quality Inspector", "💼 Client Pitch & Proposal", "📄 Personal Resume & Portfolio PDF", "📋 Structured Data (JSON)", "ℹ️ How it Works & CLI"])

with tabs[0]:
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.subheader("1. What do you want to build?")
        
        st.markdown("**🌐 Website Architecture & Category:**")
        generator_site_type = st.selectbox(
            "Select Purpose / Website Type:",
            [
                "🚀 High-Converting SaaS / AI Tech Landing Page (Pricing, FAQs, Hero, Waitlist)",
                "🛍️ E-Commerce & DTC Online Store (Product catalog, Cart drawer, ₹ INR pricing, Buy buttons)",
                "🏋️‍♂️ Elite Fitness Club, Gym & Crossfit Center (Membership plans in ₹ INR, Class schedules, Free trial pass booking, Trainers)",
                "✨ Luxury Beauty Salon, Spa & Wellness Atelier (Service menu in ₹ INR, Stylist portfolios, Appointment booking, Bridal packages)",
                "🏢 Static Business & Corporate Agency (About, Services, Portfolio, Case studies, Booking)",
                "💼 Local Service Business (Doctors, Dentists, Real Estate, Contractors with quote inquiry)",
                "👤 Personal Portfolio & Professional Resume (Projects, Tech stack badges, Contact modal)",
                "⚡ Event, Conference & Webinar Launch Page (Live countdown timer, Agenda, Speakers, Tickets)",
                "🛠️ Custom Architecture (Specify your exact custom requirements in prompt)"
            ]
        )

        prompt_preset = st.selectbox(
            "Quick Inspiration Presets (or write custom below):",
            [
                "Custom Prompt",
                "Gym & Fitness: Elite Performance Athletic Club (Membership, Schedule, ₹ INR)",
                "Luxury Salon & Spa: Haute Beauty & Bridal Atelier (Services Menu, Appointment, ₹ INR)",
                "E-Commerce: Artisan Leather Goods & Watch Brand (Cart Drawer, ₹ INR)",
                "AI Trading Bot & Algo Execution Platform (Dark SaaS)",
                "Luxury Real Estate Advisory & Villa Showcase",
                "Personal Portfolio & Tech Lead Resume with Projects",
                "Artisan Coffee Roastery & Subscription Service",
                "B2B Cybersecurity & Cloud Compliance Firm"
            ]
        )
        
        default_prompts = {
            "Gym & Fitness: Elite Performance Athletic Club (Membership, Schedule, ₹ INR)": "A powerhouse, high-energy modern fitness club & gym website called 'IronPulse Athletic Club'. Include an impactful hero with dynamic fitness visuals and 'Claim 1-Day Free Guest Pass' CTA, membership tiers (Monthly, Quarterly, Annual with ₹ INR pricing), interactive class schedule grid (HIIT, Strength, CrossFit, Yoga), certified personal trainers showcase with specialties, gym amenities and equipment gallery, instant free workout trial pass booking form, client transformation testimonials, and direct WhatsApp enquiry.",
            "Luxury Salon & Spa: Haute Beauty & Bridal Atelier (Services Menu, Appointment, ₹ INR)": "An ultra-luxurious, editorial beauty salon, spa and bridal makeover atelier called 'Maison Glow Luxury Salon & Spa'. Include a refined hero with silk and gold aesthetics, service menu with ₹ INR prices (Hair styling, Keratin, Luxury Facials, Nail Couture, Bridal packages), master stylists & makeup artists portfolio, client transformations before/after gallery, online VIP appointment / consultation booking form, and direct WhatsApp concierge.",
            "E-Commerce: Artisan Leather Goods & Watch Brand (Cart Drawer, ₹ INR)": "An ultra-premium modern e-commerce storefront for 'Chronos & Hide' luxury handcrafted watches and leather goods. Include product showcase grid with ₹ INR prices, star ratings, working slide-out cart drawer, free shipping trust badges, customer reviews, and a discount newsletter popup.",
            "AI Trading Bot & Algo Execution Platform (Dark SaaS)": "A high-conversion dark-mode SaaS landing page for an institutional algo trading bot platform called ApexFlow. Include hero with glowing stats counters, interactive strategy features, pricing table with starter and pro tiers in ₹ INR, customer testimonials from fund managers, and a lead capture form.",
            "Luxury Real Estate Advisory & Villa Showcase": "A minimalist, ultra-luxurious real estate landing page for 'Aura Estates' featuring coastal villas, private viewings booking form, testimonials, and high-end aesthetics.",
            "Personal Portfolio & Tech Lead Resume with Projects": "Create an elite personal portfolio & interactive resume for Mohammad Rehan, Senior Full-Stack & AI Systems Architect. Include an animated sleek dark hero with a live '🟢 Available for High-Impact Roles' availability pill, dynamic tech stack mastery bars (Python, TypeScript, React, Next.js, FastAPI, Cloudflare, Gemini AI), an interactive career timeline with quantified impact achievements, a project showcase gallery with live demo and GitHub buttons, LinkedIn peer endorsements, 1-click 'Download Resume (PDF)' trigger, and a contact modal with instant 1-click clipboard email copy and direct WhatsApp messaging.",
            "Artisan Coffee Roastery & Subscription Service": "A warm, earth-toned landing page for 'Velvet Bean' artisan coffee roastery. Include a monthly coffee bean subscription pricing in ₹ INR, bean flavor guide, and an order form.",
            "B2B Cybersecurity & Cloud Compliance Firm": "Enterprise cybersecurity consulting firm landing page emphasizing SOC-2 compliance, zero-day threat intelligence, client logos, and an audit request form."
        }
        
        prompt_text = st.text_area(
            "Natural Language Prompt / Instructions:",
            value=default_prompts.get(prompt_preset, ""),
            height=150,
            placeholder="e.g. A sleek modern landing page for a boutique design agency called PixelCraft. Include our services (branding, web development, 3D animations), pricing in ₹ INR, team section, and contact form."
        )
        
        # Social / Source Link Ingestion (YouTube, Instagram, Website)
        st.markdown("**🔗 Ingest from Source Link (YouTube, Instagram, or Website):**")
        lcol1, lcol2 = st.columns([3, 1])
        with lcol1:
            source_url_input = st.text_input(
                "Source Link:",
                value="",
                placeholder="Paste YouTube, Instagram, or Website URL...",
                label_visibility="collapsed",
                key="source_url_input_field"
            )
        with lcol2:
            ingest_btn = st.button("⚡ Ingest Link", use_container_width=True, key="ingest_link_action_btn")

        if ingest_btn and source_url_input:
            with st.spinner("🔍 Fetching live data, media assets, and embed codes from source..."):
                source_data = extract_source_data(source_url_input)
                if source_data.get("success"):
                    st.session_state["ingested_source_data"] = source_data
                    st.toast(f"Ingested {source_data.get('platform')}: {source_data.get('title')}", icon="✅")
                else:
                    st.error(f"Failed to ingest link: {source_data.get('message', 'Unknown error')}")

        if st.session_state.get("ingested_source_data"):
            src = st.session_state["ingested_source_data"]
            with st.container(border=True):
                p_c1, p_c2 = st.columns([1, 3])
                with p_c1:
                    if src.get("thumbnail"):
                        st.image(src["thumbnail"], use_container_width=True)
                with p_c2:
                    st.markdown(f"**[{src.get('platform')}] {src.get('title')}**")
                    if src.get("author"):
                        st.caption(f"Author / Channel: **{src.get('author')}**")
                    if src.get("description"):
                        st.caption(src.get("description")[:140] + "...")
                    if st.button("🗑️ Remove Ingested Link", key="clear_ingested_link_btn"):
                        del st.session_state["ingested_source_data"]
                        st.rerun()

        # Multi-Format Context & File Upload (PDF, JSON, TXT, Markdown)
        st.markdown("**📎 Upload Business Data or Reference Files (PDF / JSON / TXT / MD):**")
        uploaded_doc = st.file_uploader(
            "Upload brochure, company profile, pricing document, or JSON:",
            type=["pdf", "json", "txt", "md"],
            help="Upload a PDF brochure, business proposal, or JSON file. The AI will extract its text and autonomously construct the website from it!"
        )

        extracted_file_context = ""
        uploaded_json_data = None

        if uploaded_doc is not None:
            fname = uploaded_doc.name.lower()
            try:
                if fname.endswith(".pdf"):
                    import pypdf
                    reader = pypdf.PdfReader(uploaded_doc)
                    pdf_text_parts = []
                    for i, page in enumerate(reader.pages):
                        page_text = page.extract_text()
                        if page_text:
                            pdf_text_parts.append(f"--- Page {i+1} ---\n{page_text}")
                    extracted_file_context = "\n".join(pdf_text_parts)
                    st.success(f"✅ Successfully extracted text from '{uploaded_doc.name}' ({len(reader.pages)} pages)!")
                    with st.expander("🔍 View Extracted PDF Text"):
                        st.text_area("Extracted Content Preview", value=extracted_file_context[:1000] + ("..." if len(extracted_file_context) > 1000 else ""), height=150)
                elif fname.endswith(".json"):
                    uploaded_json_data = json.load(uploaded_doc)
                    st.success(f"✅ Loaded structured JSON data from '{uploaded_doc.name}'!")
                else:
                    # TXT or MD
                    extracted_file_context = uploaded_doc.read().decode("utf-8", errors="ignore")
                    st.success(f"✅ Loaded text document '{uploaded_doc.name}'!")
            except Exception as e:
                st.error(f"Error reading file '{uploaded_doc.name}': {e}")

        # Autonomous Enhancements: Mode, Webhook & WhatsApp
        st.markdown("---")
        site_mode = st.radio("Site Structure Mode:", ["Single-Page Full App", "Multi-Page Portfolio (Home, Projects, Experience, Contact)", "Multi-Page Business (Home, About, Services, Contact)"], horizontal=True)

        wcol1, wcol2 = st.columns([1, 1])
        with wcol1:
            default_webhook = os.getenv("DISCORD_WEBHOOK_URL", "")
            webhook_input = st.text_input(
                "Lead Webhook URL (Discord / Formspree):",
                value=default_webhook if default_webhook else "",
                placeholder="https://discord.com/api/webhooks/...",
                help="Form submissions will push notifications directly to this Discord or Formspree endpoint."
            )
        with wcol2:
            default_whatsapp = os.getenv("BUSINESS_WHATSAPP", os.getenv("KOTAK_MOBILE", "7091518548"))
            whatsapp_input = st.text_input(
                "Business WhatsApp Number (with country code):",
                value=f"+91{default_whatsapp}" if default_whatsapp and not default_whatsapp.startswith("+") else default_whatsapp,
                placeholder="+919876543210",
                help="Embeds a floating WhatsApp chat widget and 1-click 'Chat on WhatsApp' direct buttons on the website!"
            )

        # Security & Authentication Toggles (Yes / No)
        st.markdown("**🛡️ Security & Authentication Features:**")
        col_sec1, col_sec2 = st.columns(2)
        with col_sec1:
            enable_security = st.checkbox(
                "🛡️ Enterprise Security Layer",
                value=False,
                help="Embeds Content Security Policy (CSP), anti-tamper form sanitization, SSL 256-bit trust badges, and GDPR/Cookie consent banner."
            )
        with col_sec2:
            enable_auth = st.checkbox(
                "🔐 User Authentication & Portal",
                value=False,
                help="Embeds client-side user authentication modal (Sign In / Register), password visibility toggle, and dynamic user session portal in the navbar."
            )

        # Interactive AI Mascot / Anime Character Toggle
        include_character = st.checkbox(
            "✨ Add Futuristic Holographic Anime Mascot / AI Neural Guide?",
            value=False,
            help="Embeds a futuristic holographic anime AI companion (Aria v2.5) with cybernetic pulsing scan-lines, floating hologram capsule, particle glow, and instant neural domain FAQ responder!"
        )

        generate_btn = st.button("✨ Autonomously Build Website", type="primary", use_container_width=True)

    with col2:
        st.subheader("2. Live Preview, 1-Click Deploy & Export")
        
        if generate_btn:
            with st.spinner("🤖 AI Architect is reading inputs, designing layout, copywriting, and crafting responsive HTML/CSS/JS..."):
                gen = WebsiteGenerator(api_key=api_key_input, model=effective_model)
                
                # Combine prompt with ingested link metadata and extracted PDF / document content
                combined_prompt = prompt_text
                if st.session_state.get("ingested_source_data"):
                    src_summary = st.session_state["ingested_source_data"].get("context_summary", "")
                    combined_prompt = f"{combined_prompt}\n\n=== INGESTED SOURCE ASSETS & DATA FROM URL ===\n{src_summary}"
                if extracted_file_context:
                    combined_prompt = f"{combined_prompt}\n\n=== ATTACHED REFERENCE DOCUMENT / PDF CONTENT ===\n{extracted_file_context}"

                if "Multi-Page" in site_mode:
                    is_portfolio_mode = "portfolio" in site_mode.lower() or "portfolio" in generator_site_type.lower()
                    pages_result = gen.generate_multipage_site(
                        prompt=combined_prompt,
                        data=uploaded_json_data,
                        theme_hint=effective_theme,
                        webhook_url=webhook_input,
                        whatsapp_number=whatsapp_input or "+917091518548",
                        include_interactive_character=include_character,
                        enable_auth=enable_auth,
                        enable_security=enable_security,
                        is_portfolio=is_portfolio_mode
                    )
                    st.session_state["multipage_dict"] = pages_result
                    st.session_state["generated_html"] = pages_result.get("index.html", "")
                    st.session_state["last_model_used"] = getattr(gen, "last_used_model", effective_model)
                    
                    # Auto-export all 4 pages to a dedicated folder on Desktop
                    try:
                        desktop_website_dir = Path("C:/Users/rehan/Desktop/Generated_Website")
                        desktop_website_dir.mkdir(parents=True, exist_ok=True)
                        for fname, content in pages_result.items():
                            (desktop_website_dir / fname).write_text(content, encoding="utf-8")
                        st.session_state["exported_desktop_dir"] = str(desktop_website_dir)
                    except Exception as err:
                        print(f"Desktop auto-export error: {err}")

                    st.toast(f"Multi-page website (4 pages) generated & saved to Desktop/Generated_Website via {st.session_state['last_model_used']}!", icon="🎉")
                else:
                    if "multipage_dict" in st.session_state:
                        del st.session_state["multipage_dict"]
                    html_result = gen.generate_site(
                        prompt=combined_prompt,
                        data=uploaded_json_data,
                        theme_hint=effective_theme,
                        site_type=generator_site_type,
                        webhook_url=webhook_input,
                        whatsapp_number=whatsapp_input,
                        include_interactive_character=include_character,
                        enable_auth=enable_auth,
                        enable_security=enable_security
                    )
                    st.session_state["generated_html"] = html_result
                    st.session_state["last_model_used"] = getattr(gen, "last_used_model", effective_model)
                    
                    # Also auto-export single page to Desktop/Generated_Website
                    try:
                        desktop_website_dir = Path("C:/Users/rehan/Desktop/Generated_Website")
                        desktop_website_dir.mkdir(parents=True, exist_ok=True)
                        (desktop_website_dir / "index.html").write_text(html_result, encoding="utf-8")
                        st.session_state["exported_desktop_dir"] = str(desktop_website_dir)
                    except Exception as err:
                        print(f"Desktop auto-export error: {err}")

                    st.toast(f"Website generated & saved to Desktop/Generated_Website via {st.session_state['last_model_used']}!", icon="🎉")

        if "generated_html" in st.session_state:
            is_multipage = "multipage_dict" in st.session_state and bool(st.session_state["multipage_dict"])
            curr_page_name = "index.html"
            
            if is_multipage:
                st.markdown("**📑 Multi-Tab Page Switcher (Click to switch preview):**")
                page_keys = list(st.session_state["multipage_dict"].keys())
                icon_map = {
                    "index.html": "🏠 Home (index.html)",
                    "about.html": "ℹ️ About (about.html)",
                    "services.html": "⚙️ Services (services.html)",
                    "contact.html": "📞 Contact (contact.html)"
                }
                if "active_page_tab" not in st.session_state or st.session_state["active_page_tab"] not in page_keys:
                    st.session_state["active_page_tab"] = "index.html"

                tab_cols = st.columns(len(page_keys))
                for idx, pname in enumerate(page_keys):
                    with tab_cols[idx]:
                        is_active = (st.session_state["active_page_tab"] == pname)
                        btn_label = f"✨ {icon_map.get(pname, pname)}" if is_active else icon_map.get(pname, pname)
                        if st.button(btn_label, key=f"page_tab_btn_{pname}", type="primary" if is_active else "secondary", use_container_width=True):
                            st.session_state["active_page_tab"] = pname
                            st.rerun()

                curr_page_name = st.session_state["active_page_tab"]
                curr_html = st.session_state["multipage_dict"][curr_page_name]
                st.caption(f"Active Preview: **{curr_page_name}** • All 4 pages saved to `Desktop/Generated_Website/`. You can also click navbar links directly inside the preview below to switch tabs live!")
            else:
                curr_page_name = "index.html"
                curr_html = st.session_state["generated_html"]
            
            # Prepare ZIP in memory
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
                if is_multipage:
                    for fname, content in st.session_state["multipage_dict"].items():
                        zip_file.writestr(fname, content)
                    zip_file.writestr("README.md", "# Multi-Page Website\nBuilt autonomously with Autonomous Website Builder.\n\nOpen `index.html` or upload folder to Cloudflare / Netlify / Vercel.")
                else:
                    zip_file.writestr("index.html", curr_html)
                    zip_file.writestr("README.md", "# Generated Website\nBuilt autonomously with Autonomous Website Builder.\n\nSimply open `index.html` in any browser or deploy directly to Cloudflare/Netlify/Vercel.")
            zip_buffer.seek(0)
            zip_bytes = zip_buffer.getvalue()

            # Action bar: Downloads, Desktop Folder Opener & 1-Click Hosting Deploy
            bcol1, bcol2, bcol3, bcol4 = st.columns([1, 1, 1, 1.2])
            with bcol1:
                st.download_button(
                    label=f"📥 Download {curr_page_name}",
                    data=curr_html,
                    file_name=curr_page_name,
                    mime="text/html",
                    use_container_width=True
                )
            with bcol2:
                st.download_button(
                    label="📦 Download 4-Page ZIP" if is_multipage else "📦 Download ZIP Bundle",
                    data=zip_bytes,
                    file_name="website_bundle.zip",
                    mime="application/zip",
                    use_container_width=True
                )
            with bcol3:
                if st.button("📂 Open on Desktop", use_container_width=True, help="Opens Desktop/Generated_Website folder in Windows Explorer"):
                    target_dir = Path("C:/Users/rehan/Desktop/Generated_Website")
                    target_dir.mkdir(parents=True, exist_ok=True)
                    os.system(f'explorer "{target_dir}"')
                    st.toast("Opened Desktop/Generated_Website in Explorer!", icon="📂")
            with bcol4:
                deploy_btn = st.button("🚀 1-Click Live Deploy", use_container_width=True)

            if deploy_btn:
                with st.spinner("🌐 Deploying site live to Cloudflare Pages..."):
                    cf_account, cf_token = resolve_cloudflare_credentials(
                        account_id=st.session_state.get("cf_account_input"),
                        api_token=st.session_state.get("cf_token_input")
                    )
                    d_res = deploy_to_cloudflare_pages(zip_bytes, project_name="autonomous-site", account_id=cf_account, api_token=cf_token)

                    if d_res.get("success"):
                        st.success(f"{d_res.get('message')}")
                        st.markdown(f"👉 **Live Production URL**: [{d_res.get('url')}]({d_res.get('url')})")
                        if d_res.get("preview_url") and d_res.get("preview_url") != d_res.get("url"):
                            st.markdown(f"🔍 **Deployment Version**: [{d_res.get('preview_url')}]({d_res.get('preview_url')})")
                    else:
                        st.warning(f"{d_res.get('message')}")
                        st.info("💡 To configure Cloudflare Pages: Ensure `CLOUDFLARE_ACCOUNT_ID` and `CLOUDFLARE_API_TOKEN` are in your `.env` file, or drag-and-drop the downloaded ZIP onto [Netlify Drop](https://app.netlify.com/drop)!")

            # Custom Domain Binding (Cloudflare Pages)
            with st.expander("🌐 Custom Domain Binding (.com / .dev / .in)", expanded=False):
                st.markdown("Attach your own custom domain directly to your Cloudflare Pages live website:")
                cd_col1, cd_col2 = st.columns([2, 1])
                with cd_col1:
                    custom_domain_val = st.text_input(
                        "Domain Name (e.g. rehan.dev, portfolio.rehan.com):",
                        key="custom_domain_text",
                        placeholder="rehan.dev"
                    )
                with cd_col2:
                    attach_dom_btn = st.button("🔗 Attach Domain", use_container_width=True, key="attach_domain_btn")
                
                if attach_dom_btn and custom_domain_val:
                    with st.spinner(f"Attaching '{custom_domain_val}' on Cloudflare..."):
                        cf_account, cf_token = resolve_cloudflare_credentials(
                            account_id=st.session_state.get("cf_account_input"),
                            api_token=st.session_state.get("cf_token_input")
                        )
                        cd_res = add_custom_domain_to_cloudflare(
                            domain_name=custom_domain_val,
                            project_name="rehan-ai-portfolio-demo",
                            account_id=cf_account,
                            api_token=cf_token
                        )
                        if cd_res.get("success"):
                            st.success(cd_res.get("message"))
                        else:
                            st.warning(cd_res.get("message"))
                            if cd_res.get("cname_target"):
                                st.info(f"👉 Point a CNAME record for `{custom_domain_val}` to `{cd_res.get('cname_target')}` in your DNS registrar.")

            # Live preview iframe with interactive Multi-Tab Live Router
            if is_multipage:
                import base64
                b64_pages = base64.b64encode(json.dumps(st.session_state["multipage_dict"]).encode("utf-8")).decode("ascii")
                router_script = f"""
                <script id="__INLINE_PREVIEW_ROUTER__">
                (function() {{
                    try {{
                        const rawPages = decodeURIComponent(escape(atob("{b64_pages}")));
                        const pages = JSON.parse(rawPages);
                        document.addEventListener('click', function(e) {{
                            const a = e.target.closest('a');
                            if (!a) return;
                            const href = a.getAttribute('href');
                            if (!href || href.startsWith('http') || href.startsWith('//') || href.startsWith('mailto:') || href.startsWith('tel:') || href.startsWith('javascript:') || href.startsWith('#')) return;
                            let clean = href.split('#')[0].replace('./', '').replace(/^[\\/\\\\]+/, '').trim();
                            if (!clean || clean === 'index' || clean === '/') clean = 'index.html';
                            if (!clean.endsWith('.html') && pages[clean + '.html']) clean = clean + '.html';
                            if (pages[clean]) {{
                                e.preventDefault();
                                const nextContent = pages[clean];
                                const scriptTag = document.getElementById('__INLINE_PREVIEW_ROUTER__');
                                const scriptHtml = scriptTag ? scriptTag.outerHTML : '';
                                const updated = nextContent.includes('</body>') 
                                    ? nextContent.replace('</body>', scriptHtml + '\\n</body>')
                                    : nextContent + scriptHtml;
                                document.open();
                                document.write(updated);
                                document.close();
                            }}
                        }});
                    }} catch(err) {{
                        console.error('Preview router notice:', err);
                    }}
                }})();
                </script>
                """
                if "</body>" in curr_html:
                    preview_to_show = curr_html.replace("</body>", f"{router_script}\n</body>")
                else:
                    preview_to_show = curr_html + router_script
            else:
                preview_to_show = curr_html

            # Device Viewport Switcher Bar
            st.markdown("<div style='margin-top: 14px; margin-bottom: 4px;'></div>", unsafe_allow_html=True)
            vp_c1, vp_c2 = st.columns([2.2, 1])
            with vp_c1:
                viewport_mode = st.radio(
                    "Device Viewport Simulation:",
                    ["💻 Desktop (100% Full)", "📱 Tablet (768px iPad)", "📲 Mobile (385px iPhone)"],
                    horizontal=True,
                    index=0,
                    key="device_viewport_selector"
                )
            with vp_c2:
                st.caption("Inspect responsive layout, mascot sizing, and mobile menus live.")

            if "Mobile" in viewport_mode:
                _, mob_col, _ = st.columns([1, 1.4, 1])
                with mob_col:
                    st.markdown('''
                    <div style="text-align: center; margin-bottom: 6px;">
                        <span style="display: inline-block; padding: 3px 12px; border-radius: 12px; background: #0f172a; color: #38bdf8; font-size: 11px; font-weight: 700; border: 1px solid rgba(56, 189, 248, 0.3);">
                            📲 iPhone 15 Pro (385px Fluid)
                        </span>
                    </div>
                    ''', unsafe_allow_html=True)
                    with st.container(border=True):
                        components.html(preview_to_show, height=680, scrolling=True)
            elif "Tablet" in viewport_mode:
                _, tab_col, _ = st.columns([0.15, 2.2, 0.15])
                with tab_col:
                    st.markdown('''
                    <div style="text-align: center; margin-bottom: 6px;">
                        <span style="display: inline-block; padding: 3px 12px; border-radius: 12px; background: #0f172a; color: #a855f7; font-size: 11px; font-weight: 700; border: 1px solid rgba(168, 85, 247, 0.3);">
                            📱 iPad Air (768px Fluid)
                        </span>
                    </div>
                    ''', unsafe_allow_html=True)
                    with st.container(border=True):
                        components.html(preview_to_show, height=660, scrolling=True)
            else:
                components.html(preview_to_show, height=650, scrolling=True)

            # SEO Quality Score & 1-Click Auto-Fix
            with st.expander("⚡ SEO, Performance & Core Web Vitals Auditor (1-Click Auto-Fix)", expanded=False):
                audit = analyze_website_seo(curr_html)
                ac1, ac2, ac3 = st.columns([1, 1, 1.8])
                with ac1:
                    st.metric("SEO Health Score", f"{audit['score']}/100", f"Grade: {audit['grade']}")
                with ac2:
                    st.metric("Checks Passed", f"{len(audit['passed'])}/{len(audit['passed']) + len(audit['warnings'])}")
                with ac3:
                    if st.button("🚀 1-Click Auto-Optimize SEO & Social Cards", use_container_width=True, key="btn_auto_opt_seo"):
                        optimized = auto_optimize_seo(curr_html)
                        if is_multipage:
                            st.session_state["multipage_dict"][curr_page_name] = optimized
                            if curr_page_name == "index.html":
                                st.session_state["generated_html"] = optimized
                            try:
                                desk_dir = Path("C:/Users/rehan/Desktop/Generated_Website")
                                if desk_dir.exists():
                                    (desk_dir / curr_page_name).write_text(optimized, encoding="utf-8")
                            except Exception:
                                pass
                        else:
                            st.session_state["generated_html"] = optimized
                        st.toast("Auto-injected OpenGraph cards, Twitter cards, DNS preconnects, and lazy loading!", icon="🎉")
                        st.rerun()

                p_t, w_t, r_t = st.tabs([f"✅ Passed ({len(audit['passed'])})", f"⚠️ Warnings ({len(audit['warnings'])})", f"💡 Recommendations ({len(audit['recommendations'])})"])
                with p_t:
                    for p in audit["passed"]:
                        st.caption(f"• {p}")
                with w_t:
                    for w in audit["warnings"]:
                        st.caption(f"• {w}")
                with r_t:
                    for r in audit["recommendations"]:
                        st.caption(f"• {r}")
            
            # Autonomous AI Refinement / Co-Pilot with 1-Click Action Presets
            with st.expander("🤖 AI Co-Pilot: Iterate & Polish This Website with Prompts", expanded=False):
                st.markdown("Want to modify something? Tell Gemini what to change, or click an instant preset below:")

                # 1-Click Action Presets
                st.markdown("**⚡ Quick Polish Presets:**")
                pr_col1, pr_col2, pr_col3 = st.columns(3)
                preset_clicked = None
                with pr_col1:
                    if st.button("🌙 Dark Cyber Theme", use_container_width=True, key="preset_dark"):
                        preset_clicked = "Convert the aesthetic to a futuristic dark cyberpunk theme with glowing neon cyan/indigo gradients, dark slate interior, and glowing hover states."
                    if st.button("⭐ Add Customer Reviews", use_container_width=True, key="preset_reviews"):
                        preset_clicked = "Add an interactive 5-star customer testimonials and social proof carousel section with realistic avatar badges, star ratings, and verified client endorsements."
                with pr_col2:
                    if st.button("⚪ Minimal Monochrome", use_container_width=True, key="preset_minimal"):
                        preset_clicked = "Switch to pure clean modern monochrome light theme with generous whitespace, subtle slate borders, and crisp high-contrast typography."
                    if st.button("💰 Add ₹ INR Pricing Cards", use_container_width=True, key="preset_pricing"):
                        preset_clicked = "Add a modern 3-tier pricing table formatted in Indian Rupees (₹ INR) with monthly and yearly discount toggle and a highlighted popular package."
                with pr_col3:
                    if st.button("📲 Add WhatsApp Pill", use_container_width=True, key="preset_wa"):
                        preset_clicked = "Add a floating glowing WhatsApp chat button linking directly to +91 70915 18548 with instant pre-filled text."
                    if st.button("⚡ Add FAQ Accordion", use_container_width=True, key="preset_faq"):
                        preset_clicked = "Add an interactive FAQ accordion section with smooth pure JS expanding answers and clean chevron icons."

                refine_instruction = st.text_input("Enter custom refinement instruction:", value=preset_clicked or "", placeholder="e.g. Change the background to pure black and add glowing borders to features")
                if st.button("⚡ Apply AI Refinement", use_container_width=True):
                    if refine_instruction:
                        with st.spinner("🤖 AI Co-Pilot is refining your website..."):
                            gen = WebsiteGenerator(api_key=api_key_input, model=effective_model)
                            refined_html = gen.refine_site(curr_html, refine_instruction)
                            if is_multipage:
                                st.session_state["multipage_dict"][curr_page_name] = refined_html
                                if curr_page_name == "index.html":
                                    st.session_state["generated_html"] = refined_html
                                try:
                                    desk_dir = Path("C:/Users/rehan/Desktop/Generated_Website")
                                    if desk_dir.exists():
                                        (desk_dir / curr_page_name).write_text(refined_html, encoding="utf-8")
                                except Exception:
                                    pass
                            else:
                                st.session_state["generated_html"] = refined_html
                            st.toast(f"Refinements applied to {curr_page_name}!", icon="✨")
                            st.rerun()

            with st.expander("🔍 View & Edit Raw HTML Source"):
                edited_html = st.text_area("HTML Code", value=curr_html, height=300)
                if st.button("Apply Manual HTML Edits"):
                    if is_multipage:
                        st.session_state["multipage_dict"][curr_page_name] = edited_html
                        if curr_page_name == "index.html":
                            st.session_state["generated_html"] = edited_html
                        try:
                            desk_dir = Path("C:/Users/rehan/Desktop/Generated_Website")
                            if desk_dir.exists():
                                (desk_dir / curr_page_name).write_text(edited_html, encoding="utf-8")
                        except Exception:
                            pass
                    else:
                        st.session_state["generated_html"] = edited_html
                    st.toast(f"Saved manual edits to {curr_page_name}!", icon="💾")
                    st.rerun()
        else:
            st.info("👈 Enter your prompt or upload data and click **'Autonomously Build Website'** to see your live preview here.")

with tabs[1]:
    st.subheader("📇 Real-Time Inbound Leads & Client CRM")
    st.markdown("Track, manage, and export client inquiries captured from your generated website forms, WhatsApp leads, and live consultations.")

    all_leads = get_all_leads()

    # Informative Banner Clarifying Real vs Demo Data
    st.info("💡 **Note on Leads:** The entries below are **initial demonstration sample leads** to show how your CRM organizes inquiries, budgets, and direct WhatsApp links. Real leads will appear here automatically when visitors submit the contact form on your live website. You can click **'🗑️ Clear All Leads'** below anytime to start completely fresh.")
    
    # Summary Metrics Cards
    lm_col1, lm_col2, lm_col3, lm_col4 = st.columns(4)
    with lm_col1:
        st.metric("Total Inquiries", len(all_leads))
    with lm_col2:
        new_count = sum(1 for l in all_leads if l.get("status") == "New")
        st.metric("New Leads", new_count, "+ Active")
    with lm_col3:
        qualified_count = sum(1 for l in all_leads if l.get("status") == "Qualified")
        st.metric("Qualified Pipeline", qualified_count)
    with lm_col4:
        st.metric("Target Response SLA", "< 2 Hours", "WhatsApp Fast-Track")

    st.markdown("---")

    crm_col1, crm_col2 = st.columns([2, 1], gap="large")

    with crm_col1:
        st.markdown("**📥 Inquiries & Opportunities:**")
        if all_leads:
            import urllib.parse
            for idx, lead in enumerate(all_leads):
                with st.container(border=True):
                    head_c1, head_c2 = st.columns([2.6, 1.4])
                    with head_c1:
                        st.markdown(f"**👤 {lead.get('name')}** • `{lead.get('email')}` • 📞 `{lead.get('phone')}`")
                        st.caption(f"Budget: **{lead.get('budget')}** | Source: **{lead.get('source_page')}** | Captured: *{lead.get('timestamp')}*")
                    with head_c2:
                        status_color = "#10b981" if lead.get("status") == "Qualified" else "#3b82f6"
                        status_bg = "rgba(16,185,129,0.12)" if lead.get("status") == "Qualified" else "rgba(59,130,246,0.12)"
                        st.markdown(f"<div style='text-align: right;'><span style='display:inline-block; padding: 2px 10px; border-radius: 12px; background: {status_bg}; color: {status_color}; font-size: 11px; font-weight: 700;'>{lead.get('status')}</span></div>", unsafe_allow_html=True)
                        wa_num_clean = re.sub(r'[^0-9]', '', lead.get('phone', ''))
                        if wa_num_clean:
                            wa_encoded_msg = urllib.parse.quote(f"Hi {lead.get('name')}! I received your inquiry on my website regarding {lead.get('budget', 'your project')}.")
                            wa_url = f"https://wa.me/{wa_num_clean}?text={wa_encoded_msg}"
                            st.markdown(f"<div style='text-align: right; margin-top: 6px;'><a href='{wa_url}' target='_blank' style='display:inline-flex; align-items:center; gap:4px; padding: 4px 10px; border-radius: 8px; background: #25D366; color: white; text-decoration: none; font-size: 11px; font-weight: 700;'>💬 Open WhatsApp</a></div>", unsafe_allow_html=True)
                    lead_msg = lead.get('message', '')
                    st.markdown(f"> *\"{lead_msg}\"*")
        else:
            st.info("No client leads currently in queue. Submit a test lead using the simulator on the right or wait for live website submissions!")

        # Export & Management Actions
        act_c1, act_c2 = st.columns(2)
        with act_c1:
            csv_data = export_leads_to_csv()
            st.download_button(
                "📥 Export All Leads (CSV)",
                data=csv_data,
                file_name="website_leads_export.csv",
                mime="text/csv",
                use_container_width=True
            )
        with act_c2:
            if st.button("🗑️ Clear All Leads", use_container_width=True):
                clear_all_leads()
                st.toast("Cleared leads archive.", icon="🧹")
                st.rerun()

    with crm_col2:
        st.markdown("**⚡ Live Lead Capture Simulator:**")
        st.caption("Test how client inquiries are ingested into your CRM:")
        with st.form("test_lead_sim_form"):
            sim_name = st.text_input("Lead Name", value="Rahul Sharma")
            sim_email = st.text_input("Email Address", value="rahul.sharma@patnaretail.in")
            sim_phone = st.text_input("WhatsApp / Phone", value="+91 98350 12345")
            sim_budget = st.selectbox("Estimated Budget", ["₹5,000 - ₹10,000 (Landing Page)", "₹15,000 - ₹25,000 (Multi-Page Site)", "₹50,000+ (Custom Software / Store Billing)"])
            sim_msg = st.text_area("Inquiry Details", value="Need an automated inventory billing software and digital storefront with WhatsApp notifications for our retail chain.")
            sim_source = st.selectbox("Source Page", ["contact.html", "index.html", "projects.html", "experience.html"])
            sim_submit = st.form_submit_button("🚀 Simulate Inbound Client Inquiry", use_container_width=True)

            if sim_submit:
                new_l = log_new_lead(
                    name=sim_name,
                    email=sim_email,
                    phone=sim_phone,
                    message=sim_msg,
                    source_page=sim_source,
                    budget=sim_budget
                )
                st.toast(f"New Lead Captured: {new_l['name']}!", icon="🎉")
                st.rerun()

with tabs[2]:
    st.subheader("🔍 Enterprise SEO, Social Cards & Security Inspector")
    st.markdown("Audit your generated website for search engine visibility, OpenGraph social card rendering, Content Security Policies, and Schema.org rich snippets.")

    if "generated_html" in st.session_state or ("multipage_dict" in st.session_state and st.session_state["multipage_dict"]):
        target_html = st.session_state.get("generated_html", "")
        if "multipage_dict" in st.session_state and st.session_state["multipage_dict"]:
            active_p = st.session_state.get("active_page_tab", "index.html")
            target_html = st.session_state["multipage_dict"].get(active_p, target_html)

        audit_data = analyze_website_seo(target_html)

        i_col1, i_col2 = st.columns([1.1, 1], gap="large")

        with i_col1:
            st.markdown("### 📱 Social Media Share Preview (OpenGraph & Twitter Card)")
            st.caption("How your website appears when shared on WhatsApp, LinkedIn, Twitter/X, and Slack:")
            
            # Custom Social Share Image selector
            img_preset = st.selectbox(
                "Social Share Card Image Preset:",
                [
                    "💻 Tech & AI Architecture (Dark Futuristic Code / Systems)",
                    "👗 Luxury Fashion & Retail Boutique (Indian Ethnic / Sarees)",
                    "🏢 Enterprise Corporate & FinTech Tower",
                    "🌿 Modern Lifestyle & Artisan Coffee",
                    "✨ Custom Image URL"
                ],
                key="seo_og_img_preset"
            )
            img_preset_map = {
                "💻 Tech & AI Architecture (Dark Futuristic Code / Systems)": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=1200&q=80",
                "👗 Luxury Fashion & Retail Boutique (Indian Ethnic / Sarees)": "https://images.unsplash.com/photo-1610030469983-98e550d6193c?auto=format&fit=crop&w=1200&q=80",
                "🏢 Enterprise Corporate & FinTech Tower": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1200&q=80",
                "🌿 Modern Lifestyle & Artisan Coffee": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=1200&q=80"
            }
            if "Custom" in img_preset:
                custom_og_url = st.text_input("Paste Direct Image URL:", value="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=1200&q=80", key="seo_custom_og_url")
            else:
                custom_og_url = img_preset_map.get(img_preset, "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=1200&q=80")

            title_disp = audit_data["metrics"].get("title") or "Mohammad Rehan | AI Systems Architect & Tech Lead"
            desc_disp = audit_data["metrics"].get("description") or "Senior AI Systems Architect specializing in autonomous agent architectures, low-latency microservices, and modern web platforms."

            st.markdown(f'''
            <div style="border-radius: 16px; border: 1px solid #334155; overflow: hidden; background: #0f172a; max-width: 480px; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.3); margin-top: 10px; margin-bottom: 12px;">
                <div style="height: 220px; background-image: url('{custom_og_url}'); background-size: cover; background-position: center;"></div>
                <div style="padding: 18px; color: #f8fafc;">
                    <div style="text-transform: uppercase; font-size: 10px; font-weight: 700; color: #38bdf8; letter-spacing: 0.05em; margin-bottom: 4px;">PRODUCTION CLOUDFLARE LINK</div>
                    <div style="font-size: 15.5px; font-weight: 700; color: #ffffff; line-height: 1.3; margin-bottom: 6px;">{title_disp}</div>
                    <div style="font-size: 12px; color: #94a3b8; line-height: 1.4;">{desc_disp[:140]}...</div>
                </div>
            </div>
            ''', unsafe_allow_html=True)

            opt_c1, opt_c2 = st.columns(2)
            with opt_c1:
                if st.button("⚡ Auto-Optimize Active Page (100%)", use_container_width=True, key="inspector_opt_btn"):
                    opt_html = auto_optimize_seo(target_html, og_image_url=custom_og_url)
                    if "multipage_dict" in st.session_state and st.session_state["multipage_dict"]:
                        st.session_state["multipage_dict"][active_p] = opt_html
                        if active_p == "index.html":
                            st.session_state["generated_html"] = opt_html
                        try:
                            desk_dir = Path("C:/Users/rehan/Desktop/Generated_Website")
                            if desk_dir.exists():
                                (desk_dir / active_p).write_text(opt_html, encoding="utf-8")
                        except Exception:
                            pass
                    else:
                        st.session_state["generated_html"] = opt_html
                    st.toast(f"SEO, Social Cards & Security Injected into {active_p}!", icon="🚀")
                    st.rerun()

            with opt_c2:
                is_multi = bool("multipage_dict" in st.session_state and st.session_state["multipage_dict"])
                if is_multi:
                    if st.button("🚀 Batch Optimize All Pages", use_container_width=True, key="batch_opt_all_btn"):
                        for p_k, p_h in st.session_state["multipage_dict"].items():
                            p_title_sub = f"Mohammad Rehan | {p_k.replace('.html', '').capitalize()}" if p_k != "index.html" else ""
                            st.session_state["multipage_dict"][p_k] = auto_optimize_seo(p_h, site_title=p_title_sub, og_image_url=custom_og_url)
                        st.session_state["generated_html"] = st.session_state["multipage_dict"].get("index.html", target_html)
                        try:
                            desk_dir = Path("C:/Users/rehan/Desktop/Generated_Website")
                            if desk_dir.exists():
                                for p_k, p_h in st.session_state["multipage_dict"].items():
                                    (desk_dir / p_k).write_text(p_h, encoding="utf-8")
                        except Exception:
                            pass
                        st.toast("Batch optimized all pages to 100% Grade A+!", icon="🎉")
                        st.rerun()
                else:
                    st.caption("Active in single-page mode. Switch to Multi-Page to batch-optimize.")

        with i_col2:
            st.markdown("### 📊 Enterprise SEO Audit Breakdown")
            st.metric("Total Compliance Score", f"{audit_data['score']}/100", f"Grade: {audit_data['grade']}")
            
            with st.container(border=True):
                st.markdown("**🛡️ Security & Performance Standards:**")
                st.markdown(f"- **Content Security Policy (CSP):** {'✅ Active' if audit_data['metrics'].get('has_csp') else '⚠️ Missing'}")
                st.markdown(f"- **CDN Preconnect Endpoints:** {audit_data['metrics'].get('preconnect_count', 0)} active")
                st.markdown(f"- **Images Analyzed:** {audit_data['metrics'].get('image_count', 0)} total")
                st.markdown(f"- **Primary <h1> Heading:** {audit_data['metrics'].get('h1_count', 0)} tag detected")
                st.markdown(f"- **External Outbound Links:** {audit_data['metrics'].get('external_links', 0)} verified with `noopener`")

            # Sitemap.xml & Robots.txt generators
            active_domain = "mohammadrehan.pages.dev"
            cur_pages = list(st.session_state.get("multipage_dict", {}).keys()) if st.session_state.get("multipage_dict") else ["index.html"]
            gen_sitemap = generate_sitemap_xml(active_domain, cur_pages)
            gen_robots = generate_robots_txt(active_domain)

            with st.expander("🗺️ Google Sitemap (sitemap.xml)", expanded=False):
                st.caption("Auto-generated XML sitemap informing Googlebot & Bing of all routes:")
                st.code(gen_sitemap, language="xml")
                st.download_button("📥 Download sitemap.xml", data=gen_sitemap, file_name="sitemap.xml", mime="application/xml", use_container_width=True)

            with st.expander("🤖 Search Engine Directives (robots.txt)", expanded=False):
                st.caption("Permits search crawlers and links directly to your sitemap:")
                st.code(gen_robots, language="text")
                st.download_button("📥 Download robots.txt", data=gen_robots, file_name="robots.txt", mime="text/plain", use_container_width=True)

            with st.expander("🔍 View Injected Schema.org JSON-LD"):
                st.caption("Structured data for Google Knowledge Graph and Rich SERP Cards:")
                st.code('''{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Mohammad Rehan",
  "jobTitle": "Senior AI & Full-Stack Systems Architect",
  "url": "https://mohammadrehan.pages.dev",
  "sameAs": [
    "https://wa.me/917091518548",
    "https://github.com",
    "https://linkedin.com"
  ]
}''', language="json")
    else:
        st.info("No website generated yet. Generate a site in the **Generator Studio** to inspect its live SEO audit.")

with tabs[3]:
    st.subheader("💼 Autonomous Client Proposal & Pitch Generator")
    st.markdown("Generate executive-ready client proposals, audit reports, cold outreach scripts, and closing pitches in seconds.")
    
    pcol1, pcol2 = st.columns([1, 1], gap="large")
    
    with pcol1:
        client_name = st.text_input("Prospect / Business Name", value="Apex Wealth Partners", placeholder="e.g. Acme Dental Clinic")
        client_niche_select = st.selectbox(
            "Client Industry / Niche",
            [
                "Fintech & Quantitative Trading",
                "Healthcare, Doctors & Clinics",
                "Fitness Centers, Gyms & CrossFit Studios",
                "Luxury Beauty Salons, Spas & Makeover Studios",
                "E-Commerce & DTC Brands",
                "Real Estate & Luxury Property",
                "B2B SaaS & Tech Startups",
                "Law Firms & Legal Services",
                "Local Services (HVAC, Solar, Roofing)",
                "Restaurants & Hospitality",
                "Coaching & Personal Brand / Course Creators",
                "✨ Custom Industry / Niche (Specify Below)"
            ]
        )
        
        custom_niche_text = ""
        if "Custom Industry" in client_niche_select:
            custom_niche_text = st.text_input("Describe custom industry / niche:", placeholder="e.g. AI-powered Drone Delivery Logistics")
        
        effective_niche = custom_niche_text if custom_niche_text else client_niche_select

        st.markdown("---")
        st.markdown("**🌐 What Type of Website to Pitch?**")
        website_type_select = st.selectbox(
            "Select Website Architecture (All fully buildable with this software):",
            [
                "🚀 High-Converting SaaS / Product Landing Page (Pricing, FAQs, Hero, Waitlist)",
                "🏋️‍♂️ Fitness Club & Gym Website (Membership tiers, Class schedule, Free pass lead-gen)",
                "✨ Luxury Beauty Salon & Spa Website (Service menu, VIP booking, Stylist showcase)",
                "💼 Professional Local Business & Lead Generation Page (Google Reviews, Click-to-Call, Quote Request)",
                "🛍️ E-Commerce / Direct-to-Consumer Showcase (Product grid, Feature highlights, Buy buttons)",
                "🏢 Corporate Agency / Firm Website (Case studies, Service tiers, Consultation booking)",
                "💎 Ultra-Luxury Portfolio / Real Estate Showcase (Full-screen imagery, Virtual tour CTA, VIP contact)",
                "👤 Personal Portfolio & Authority Brand (Resume, Project showcase, Speaking/Consulting booking)",
                "⚡ Event / Webinar Launch Page (Countdown timer, Agenda timeline, Registration modal)",
                "🛠️ Custom Architecture (Describe Your Own Below)"
            ]
        )

        custom_arch_text = ""
        if "Custom Architecture" in website_type_select:
            custom_arch_text = st.text_input("Describe custom website architecture:", placeholder="e.g. Gamified Web3 onboarding portal with wallet connect simulation")

        effective_website_type = custom_arch_text if custom_arch_text else website_type_select

        with st.expander("ℹ️ What websites can this software build for clients?"):
            st.markdown("""
            **Supported Website Capabilities (Autonomous & Custom):**
            - **Single-page & Multi-section landing pages** with sticky responsive navigation
            - **Interactive components**: Accordion FAQs, monthly/yearly pricing toggles, modals, mobile hamburger menus
            - **Conversion forms**: Lead capture, quotation inquiries, event registrations with client-side thank-you toasts
            - **Modern Design**: Powered by Tailwind CSS, Lucide icons, glassmorphism, gradient accents, and dark/light modes
            - **Export & Delivery**: Ready-to-deploy static HTML/CSS/JS (deployable to Vercel, Netlify, or GitHub Pages in 1 click)
            """)

        client_problems = st.text_area(
            "Current Problems / Bottlenecks (Leave default or describe custom):",
            height=85,
            value="Outdated slow website, no mobile responsiveness, losing high-value inbound leads to competitors, and zero automated booking/forms.",
            placeholder="What is wrong with their current online presence?"
        )
        
        proposed_solution = st.text_area(
            "Our Proposed Deliverables (Leave default or describe custom):",
            height=85,
            value="Ultra-fast custom landing page, persuasive copywriting, interactive pricing calculator, instant lead notifications via Discord/Email, and SEO optimization.",
            placeholder="What will you build for them?"
        )
        
        st.markdown("---")
        st.markdown("**💰 Investment / Package Quote (₹ INR)**")
        pricing_preset = st.selectbox(
            "Quick Pricing Presets (or type custom below):",
            [
                "₹25,000 one-time + ₹1,999/mo hosting & support (Starter)",
                "₹45,000 one-time + ₹3,499/mo maintenance & SEO (Growth / Business)",
                "₹85,000 one-time + ₹7,999/mo full management (High-Ticket / Enterprise)",
                "Custom Quote (Enter below)"
            ]
        )

        custom_pricing_input = ""
        if "Custom Quote" in pricing_preset:
            custom_pricing_input = st.text_input(
                "Custom Quote Amount (₹ INR):",
                value="₹35,000 setup + ₹2,500/mo maintenance",
                placeholder="e.g. ₹50,000 complete project"
            )

        pricing_quote = custom_pricing_input if custom_pricing_input else pricing_preset
        
        pitch_btn = st.button("🚀 Generate Pitch & Cold Outreach", type="primary", use_container_width=True)

    with pcol2:
        st.subheader("📄 Generated Pitch & Strategy")
        
        if pitch_btn:
            with st.spinner("🤖 Crafting high-converting proposal & pitch scripts..."):
                gen = WebsiteGenerator(api_key=api_key_input, model=effective_model)
                pitch_result = gen.generate_pitch(
                    client_name=client_name,
                    niche=effective_niche,
                    website_type=effective_website_type,
                    client_problems=client_problems,
                    proposed_solution=proposed_solution,
                    pricing_quote=pricing_quote
                )
                st.session_state["generated_pitch"] = pitch_result
                st.session_state["pitch_client_name"] = client_name
                st.session_state["pitch_niche"] = effective_niche
                st.toast("Client pitch ready!", icon="🔥")

        if "generated_pitch" in st.session_state:
            curr_pitch = st.session_state["generated_pitch"]
            p_client = st.session_state.get("pitch_client_name", "Client")
            p_niche = st.session_state.get("pitch_niche", "Business")

            # Generate attractive PDF
            try:
                pdf_buffer = create_styled_pitch_pdf(curr_pitch, p_client, p_niche)
                pdf_bytes = pdf_buffer.getvalue()
            except Exception as e:
                pdf_bytes = None
                st.error(f"Error styling PDF: {e}")

            dcol1, dcol2 = st.columns([1, 1])
            with dcol1:
                if pdf_bytes:
                    st.download_button(
                        label="📄 Download Executive Proposal (PDF)",
                        data=pdf_bytes,
                        file_name=f"{p_client.replace(' ', '_')}_Executive_Proposal.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )
            with dcol2:
                st.download_button(
                    label="📝 Download Text / Markdown",
                    data=curr_pitch,
                    file_name=f"{p_client.replace(' ', '_')}_pitch_proposal.md",
                    mime="text/markdown",
                    use_container_width=True
                )

            st.markdown(curr_pitch)
        else:
            st.info("Fill in the prospect details on the left and click **'Generate Pitch & Cold Outreach'** to see your customized proposal.")

with tabs[4]:
    st.subheader("📄 Executive Personal Resume & Portfolio PDF Maker")
    st.markdown("Craft high-impact, ATS-optimized executive PDF resumes and portfolio dossiers with tailored typography, quantifiable impact metrics, and 1-click live web deployment.")
    
    rcol1, rcol2 = st.columns([1, 1], gap="large")
    
    with rcol1:
        cand_name = st.text_input("Candidate Full Name", value="Mohammad Rehan", key="resume_cand_name")
        cand_title = st.text_input("Target Role / Professional Title", value="Senior Full-Stack & AI Systems Architect", key="resume_cand_title")
        
        with st.expander("📍 Contact, Social & Portfolio Links", expanded=False):
            c_email = st.text_input("Email", value="contact@rehan.dev", key="res_email")
            c_phone = st.text_input("Phone / WhatsApp", value="+91 70915 18548", key="res_phone")
            c_loc = st.text_input("Location", value="India / Remote Worldwide", key="res_loc")
            c_li = st.text_input("LinkedIn URL", value="linkedin.com/in/rehan", key="res_li")
            c_gh = st.text_input("GitHub Profile", value="github.com/rehan", key="res_gh")
            c_port = st.text_input("Live Portfolio URL", value="rehan-ai-portfolio-demo.pages.dev", key="res_port")
        
        contact_dict = {
            "email": c_email,
            "phone": c_phone,
            "location": c_loc,
            "linkedin": c_li,
            "github": c_gh,
            "portfolio": c_port
        }
        
        cand_bio = st.text_area(
            "Professional Summary / Executive Bio:",
            value="High-impact Software Engineer & Systems Architect with 5+ years of experience designing autonomous agent architectures, multi-tenant SaaS platforms, and low-latency algorithmic trading systems. Proven track record of scaling production microservices to 100k+ active users with 99.99% uptime.",
            height=100,
            key="resume_bio"
        )
        
        cand_skills = st.text_area(
            "Core Technical Skills & Stack:",
            value="Python, TypeScript, React, Next.js, Node.js, FastAPI, Google Gemini API, Cloudflare Pages, Docker, Redis, PostgreSQL, WebSockets, Microservices, CI/CD",
            height=80,
            key="resume_skills"
        )
        
        cand_exp = st.text_area(
            "Work Experience & Achievements:",
            value="Lead AI & Full-Stack Systems Engineer at NextGen Tech Innovations (2024–Present):\n- Architected autonomous website studio with multi-model self-healing failover, reducing edge latency by 68%.\n- Deployed 24/7 background sentinel daemons achieving 99.99% availability.\n\nSenior Backend & Systems Engineer at Apex FinTech (2022–2024):\n- Built high-frequency algorithmic order routing engine processing 10,000+ msgs/sec with sub-50ms latency.",
            height=120,
            key="resume_exp"
        )
        
        cand_proj = st.text_area(
            "Key Projects & Systems Built:",
            value="Autonomous AI Website Builder: Full-stack agency suite with holographic AI mascot, CSP security, and 1-click Cloudflare Pages deployment.\nAlgorithmic Trading Bot Platform: Real-time options execution terminal with live tick charts and automated risk controls.",
            height=100,
            key="resume_proj"
        )
        
        bcol1, bcol2 = st.columns([1, 1])
        with bcol1:
            gen_ai_res_btn = st.button("🤖 Polish with AI (Gemini)", type="primary", use_container_width=True)
        with bcol2:
            compile_res_pdf_btn = st.button("📄 Refresh / Compile PDF", use_container_width=True)

    with rcol2:
        st.subheader("📑 Document & PDF Preview")
        
        # If AI Polish button is clicked
        if gen_ai_res_btn:
            with st.spinner("✨ AI is crafting an executive-grade resume dossier..."):
                gen = WebsiteGenerator(api_key=api_key_input, model=effective_model)
                generated_resume_md = gen.generate_resume_portfolio_content(
                    candidate_name=cand_name,
                    role_title=cand_title,
                    bio_background=cand_bio,
                    key_skills=cand_skills,
                    projects=cand_proj,
                    experience=cand_exp,
                    contact_info=contact_dict
                )
                st.session_state["resume_markdown_content"] = generated_resume_md
                st.toast("Resume polished with AI!", icon="🚀")

        # If user hasn't generated via AI yet, build default markdown structure
        if "resume_markdown_content" not in st.session_state:
            st.session_state["resume_markdown_content"] = f"""# {cand_name} - {cand_title}

> {cand_bio}

## Core Technical Competencies
- **Core Stack:** {cand_skills}

## Professional Experience
{cand_exp}

## Featured Projects & Portfolio
{cand_proj}

## Education & Certifications
- **Bachelor of Technology in Computer Science & Engineering** — First Class with Distinction
- **Cloud & AI Certified Specialist**
"""

        current_resume_md = st.session_state["resume_markdown_content"]

        # Render PDF
        try:
            res_pdf_buf = create_styled_resume_pdf(
                current_resume_md,
                candidate_name=cand_name,
                role_title=cand_title,
                contact_details=contact_dict
            )
            res_pdf_bytes = res_pdf_buf.getvalue()
        except Exception as e:
            res_pdf_bytes = None
            st.error(f"Error compiling Resume PDF: {e}")

        dl_col1, dl_col2 = st.columns([1, 1])
        with dl_col1:
            if res_pdf_bytes:
                st.download_button(
                    label="📥 Download Executive Resume (PDF)",
                    data=res_pdf_bytes,
                    file_name=f"{cand_name.replace(' ', '_')}_Resume_Portfolio.pdf",
                    mime="application/pdf",
                    type="primary",
                    use_container_width=True
                )
        with dl_col2:
            st.download_button(
                label="📝 Download Markdown Source",
                data=current_resume_md,
                file_name=f"{cand_name.replace(' ', '_')}_Resume.md",
                mime="text/markdown",
                use_container_width=True
            )

        st.markdown("---")
        st.markdown(current_resume_md)

with tabs[5]:
    st.subheader("📋 Autonomous Structured Data Ingestion")
    st.markdown("""
    You can feed structured business data directly. If you have an existing `business_info.json` file, the builder will autonomously map all fields into appropriate UI components (Hero, Services, Pricing, FAQs, Contacts).
    """)
    sample_file_path = Path(__file__).parent / "sample_business.json"
    if sample_file_path.exists():
        with open(sample_file_path, "r", encoding="utf-8") as f:
            sample_content = f.read()
        st.code(sample_content, language="json")

with tabs[6]:
    st.subheader("📚 System Whitepaper & CLI Reference")
    st.markdown("Download the full technical architecture whitepaper or explore headless CLI commands below:")

    pdf_doc_path = Path(__file__).resolve().parent / "Autonomous_Website_Builder_Deep_Model_Explanation.pdf"
    if pdf_doc_path.exists():
        with open(pdf_doc_path, "rb") as f:
            pdf_bytes = f.read()
        st.download_button(
            label="📄 Download Deep Model Explanation & Architecture Whitepaper (PDF)",
            data=pdf_bytes,
            file_name="Autonomous_Website_Builder_Deep_Model_Explanation.pdf",
            mime="application/pdf",
            type="primary",
            use_container_width=True
        )

    st.markdown("---")
    st.subheader("⚡ CLI Quick Reference")
    st.markdown("""
    You can run this entire generator in headless/automated environments from the command line:
    
    ```bash
    # 1. Generate from natural language prompt:
    python website_builder/generate_site.py --prompt "AI video generation platform landing page" --serve

    # 2. Generate from structured JSON business data:
    python website_builder/generate_site.py --data website_builder/sample_business.json --serve

    # 3. Hybrid: Combine data + prompt + custom theme:
    python website_builder/generate_site.py --data website_builder/sample_business.json --prompt "Focus on high-speed execution" --theme "Cyberpunk Neon" --output my_new_site --serve
    ```
    """)
