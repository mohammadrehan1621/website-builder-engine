import io
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_system_documentation_pdf(output_path: str):
    """Generates an executive, beautifully formatted technical architecture PDF."""
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    # Color Palette
    primary_color = colors.HexColor("#0f172a")     # Deep Slate 900
    accent_color = colors.HexColor("#4f46e5")      # Indigo 600
    secondary_accent = colors.HexColor("#0284c7")  # Cyan 600
    text_color = colors.HexColor("#334155")        # Slate 700
    muted_color = colors.HexColor("#64748b")       # Slate 500
    card_bg = colors.HexColor("#f8fafc")           # Slate 50
    border_color = colors.HexColor("#cbd5e1")      # Slate 300

    # Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=primary_color,
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=muted_color,
        spaceAfter=12
    )

    h1_style = ParagraphStyle(
        'Header1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=accent_color,
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Header2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=primary_color,
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13.5,
        textColor=text_color,
        spaceAfter=5
    )

    bullet_style = ParagraphStyle(
        'BulletCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13.5,
        textColor=text_color,
        leftIndent=14,
        firstLineIndent=-8,
        spaceAfter=3
    )

    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=11,
        textColor=primary_color
    )

    elements = []

    # 1. Top Header Banner
    banner_data = [
        [
            Paragraph("<b>AUTONOMOUS AI WEBSITE BUILDER &amp; CLIENT AGENCY ENGINE</b>", 
                      ParagraphStyle('BannerH', fontName='Helvetica-Bold', fontSize=9.5, textColor=colors.white)),
            Paragraph("Deep Architecture &amp; Engineering Whitepaper", 
                      ParagraphStyle('BannerR', fontName='Helvetica', fontSize=8.5, textColor=colors.HexColor('#e2e8f0'), alignment=2))
        ]
    ]
    banner_table = Table(banner_data, colWidths=[350, 182])
    banner_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), primary_color),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    elements.append(banner_table)
    elements.append(Spacer(1, 12))

    # 2. Main Title
    elements.append(Paragraph("System Architecture &amp; Operational Blueprint", title_style))
    elements.append(Paragraph("Comprehensive guide to the autonomous generation pipeline, fail-safe frontend runtime, and client sales system.", subtitle_style))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#e2e8f0"), spaceAfter=12))

    # 3. Section 1: Core System Overview
    elements.append(Paragraph("1. Core Architectural Pillars", h1_style))
    elements.append(Paragraph(
        "The software operates as a fully autonomous web development agency and sales engine in a single cohesive codebase. It eliminates external build steps, npm dependencies, and server runtime overhead by compiling prompts and business data directly into zero-dependency, deployable single-file artifacts.",
        body_style
    ))

    overview_table_data = [
        [Paragraph("<b>Component</b>", body_style), Paragraph("<b>File / Subsystem</b>", body_style), Paragraph("<b>Function &amp; Responsibilities</b>", body_style)],
        [Paragraph("AI Reasoning Engine", body_style), Paragraph("generator.py", code_style), Paragraph("Coordinates with Gemini 3.8 Flash to synthesize layouts, Tailwind CSS, copywriting, and interactive components.", body_style)],
        [Paragraph("Multi-Format Ingestion", body_style), Paragraph("pypdf + JSON Loader", code_style), Paragraph("Extracts text from multi-page PDFs (resumes, brochures) and structured business records.", body_style)],
        [Paragraph("Interactive Studio", body_style), Paragraph("streamlit_app.py", code_style), Paragraph("Dashboard running on port 8503 with real-time browser preview, AI Co-Pilot, and exports.", body_style)],
        [Paragraph("Executive PDF Engine", body_style), Paragraph("pdf_generator.py", code_style), Paragraph("Compiles sales proposals with INR (₹) packages, client audits, and ROI projections.", body_style)],
        [Paragraph("Direct Cloud Deployer", body_style), Paragraph("hosting_deployer.py", code_style), Paragraph("Direct upload gateway to Cloudflare Pages and Netlify for instant public URLs.", body_style)]
    ]
    t1 = Table(overview_table_data, colWidths=[120, 110, 302])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), card_bg),
        ('GRID', (0, 0), (-1, -1), 0.5, border_color),
        ('PADDING', (0, 0), (-1, -1), 6),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    elements.append(t1)
    elements.append(Spacer(1, 10))

    # 4. Section 2: Pipeline Data Flow
    elements.append(Paragraph("2. Autonomous Generation Pipeline Flow", h1_style))
    elements.append(Paragraph("<b>Step 1: Input Ingestion &amp; Context Merging</b>", h2_style))
    elements.append(Paragraph("The system accepts prompts, theme selections, and optional file attachments. When a PDF is uploaded, pypdf strips binary formatting and extracts page-by-page text. This text is merged into the user prompt as an explicit knowledge block.", bullet_style))
    
    elements.append(Paragraph("<b>Step 2: Resilient AI Fleet (Gemini 3.5 Flash + Auto-Failover Cascade)</b>", h2_style))
    elements.append(Paragraph("The system routes prompts through a high-availability model cascade (Gemini 3.5 Flash, 3.6 Flash, Flash-Lite, and 3.8 Flash). If a model experiences high demand (503) or quota exhaustion (429), it automatically fails over to the next fleet member within milliseconds with exponential retry, guaranteeing uninterrupted generation.", bullet_style))

    elements.append(Paragraph("<b>Step 3: Multi-Page vs Single-Page Routing</b>", h2_style))
    elements.append(Paragraph("In Single-Page mode, an end-to-end responsive landing page is produced. In Multi-Page mode, a generation loop creates four interconnected pages (index.html, about.html, services.html, contact.html) with relative cross-links and synchronized navigation styling.", bullet_style))

    elements.append(Spacer(1, 8))

    # 5. Section 3: Specialized Interactive Features & Mascot
    elements.append(Paragraph("3. Specialized Interactive Features &amp; AI Mascot", h1_style))
    
    elements.append(Paragraph("<b>🔮 Futuristic Holographic Anime Mascot (Aria v2.5 // Neural Interface):</b>", h2_style))
    elements.append(Paragraph("When enabled, the generator embeds an interactive futuristic holographic anime AI guide in the bottom-right corner. Features include a floating neon cyan/purple hologram capsule, cybernetic scan-line pulse effects, glowing particle rings, neural greeting bubbles, sound toggles, quick-action chips, and an instant client-side domain FAQ chatbot engine.", bullet_style))

    elements.append(Paragraph("<b>📱 Dual-Channel Lead Routing (Discord + WhatsApp):</b>", h2_style))
    elements.append(Paragraph("Contact and inquiry forms submit asynchronously via fetch() to a Discord webhook, delivering notifications with contact details directly to your mobile device. Simultaneously, a floating WhatsApp Business widget allows visitors to initiate one-click direct chats.", bullet_style))

    elements.append(Paragraph("<b>🛍️ E-Commerce Architecture:</b>", h2_style))
    elements.append(Paragraph("Includes product showcase grids in ₹ INR, an interactive slide-out cart drawer, dynamic item counter badges, subtotal calculations, and checkout triggers.", bullet_style))

    elements.append(Spacer(1, 8))

    # 6. Section 4: Enterprise Security & Authentication Systems
    elements.append(Paragraph("4. Enterprise Security Layer &amp; User Authentication", h1_style))
    elements.append(Paragraph("<b>🛡️ Enterprise Security Layer (Selectable Yes/No):</b>", h2_style))
    elements.append(Paragraph("• <b>Content Security Policy (CSP):</b> Injects standard HTTP-Equiv CSP meta tags restricting unauthorized script execution and preventing external data leakage.", bullet_style))
    elements.append(Paragraph("• <b>XSS &amp; CSRF Input Sanitization:</b> All form inputs undergo client-side HTML entity escaping, regex pattern validation, and anti-tamper token generation.", bullet_style))
    elements.append(Paragraph("• <b>Cookie Consent &amp; Privacy Banner:</b> GDPR/CCPA-compliant floating privacy banner with Accept and Preferences controls.", bullet_style))
    elements.append(Paragraph("• <b>Trust Badges:</b> Visual 256-bit SSL encryption and SOC-2 security badges rendered directly into the navbar and footer.", bullet_style))

    elements.append(Paragraph("<b>🔐 User Authentication &amp; Account Portal (Selectable Yes/No):</b>", h2_style))
    elements.append(Paragraph("• <b>Interactive Auth Modal:</b> Elegant glassmorphic popup with tabbed Sign-In and Registration forms, password reveal toggle, and social login simulation.", bullet_style))
    elements.append(Paragraph("• <b>Session State Management:</b> Manages persistent client session via localStorage, dynamically swapping navbar login triggers for a personalized 'My Account / Dashboard' menu with logout capabilities.", bullet_style))

    elements.append(Spacer(1, 8))

    # 7. Section 5: Security & Deployment
    elements.append(Paragraph("5. Engine Architecture, Self-Healing &amp; Zero-Bug Deployment", h1_style))
    elements.append(Paragraph("• <b>Self-Healing Watchdog Daemon:</b> Continuous background process (`watchdog_healer.py`) pinging port 8503, managing zombie process termination, and auto-restoring services within 8 seconds of failure.", bullet_style))
    elements.append(Paragraph("• <b>Live Model Health &amp; Quota Probing:</b> The Sentinel layer benchmarks model response latencies, tracks 429/503 states, and dynamically routes prompts to the healthiest model.", bullet_style))
    elements.append(Paragraph("• <b>DOM &amp; Syntax Auto-Repair:</b> Intercepts all synthesized HTML, injecting missing CDNs, fixing unclosed tags, and ensuring Lucide SVG initialization.", bullet_style))
    elements.append(Paragraph("• <b>Backend API Isolation:</b> The Gemini API key is loaded into process memory via Path(__file__).resolve().parent / '.env'. The key is never rendered or exposed in client-side HTML.", bullet_style))
    elements.append(Paragraph("• <b>Zero Local Build Steps:</b> All output files are pure HTML5/CSS/JS. They can be dragged directly onto Netlify, Vercel, or Cloudflare Pages without running npm install or webpack build commands.", bullet_style))
    elements.append(Paragraph("• <b>Safe Lucide SVG Loading:</b> Icons are wrapped in DOMContentLoaded event listeners to eliminate race conditions during page render.", bullet_style))

    # 8. Section 6: Client Sales Suite
    elements.append(Paragraph("6. Client Pitch &amp; Proposal System", h1_style))
    elements.append(Paragraph(
        "The system doubles as an agency sales suite. In Tab 2, enter your prospect's business name, choose their niche, and pick an investment tier in ₹ INR. Gemini crafts a persuasive proposal including an executive summary, site audit, ROI projection, cold email copy, and a 30-second elevator pitch. This is compiled into a client-ready PDF using ReportLab.",
        body_style
    ))

    elements.append(Spacer(1, 15))
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#e2e8f0"), spaceAfter=8))
    elements.append(Paragraph(
        "<i>Autonomous AI Website Builder • Technical Architecture Whitepaper • Generated October 2026</i>",
        ParagraphStyle('Foot', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=8, textColor=muted_color, alignment=1)
    ))

    doc.build(elements)

if __name__ == "__main__":
    out_file = os.path.join(os.path.dirname(__file__), "Autonomous_Website_Builder_Deep_Model_Explanation.pdf")
    generate_system_documentation_pdf(out_file)
    print(f"PDF successfully generated at: {out_file}")
