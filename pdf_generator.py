import io
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

EMOJI_REPLACEMENTS = {
    "🎯": "[Focus]",
    "🚀": "[Strategy]",
    "💡": "[Insight]",
    "💰": "[Pricing & ROI]",
    "✉️": "[Outreach Script]",
    "✉": "[Outreach Script]",
    "🎙️": "[Elevator Pitch]",
    "🎙": "[Elevator Pitch]",
    "🔍": "[Audit]",
    "🌐": "[Architecture]",
    "⚡": "[Speed]",
    "✨": "[Highlight]",
    "📊": "[Metrics]",
    "📈": "[Growth]",
    "🔒": "[Security]",
    "🛡️": "[Protection]",
    "🛡": "[Protection]",
    "🔥": "[Priority]",
    "✅": "[Yes]",
    "❌": "[Bottleneck]",
    "🤝": "[Partnership]",
    "📱": "[Mobile]",
    "💻": "[Platform]",
    "🏆": "[Excellence]",
    "⭐": "[Rating]",
    "📌": "[Note]",
    "🔗": "[Link]",
    "💼": "[Business]",
    "📧": "Email:",
    "₹": "Rs. ",
    "→": "->",
    "←": "<-",
    "—": "--",
    "–": "-",
    "“": '"',
    "”": '"',
    "‘": "'",
    "’": "'",
    "…": "...",
}

def clean_emojis_for_pdf(text: str) -> str:
    """Replaces emojis with clean textual tags and removes characters outside Latin-1 to prevent ReportLab black box (■) glyphs."""
    if not text:
        return ""
    for k, v in EMOJI_REPLACEMENTS.items():
        text = text.replace(k, v)
    sanitized = []
    for ch in text:
        # Keep valid Latin-1 characters (code points 0-255)
        if ord(ch) <= 255:
            sanitized.append(ch)
    return "".join(sanitized)

def sanitize_for_reportlab(text: str) -> str:
    """Bulletproof ReportLab paragraph sanitizer:
    - Strips full HTML documents or cleans raw HTML tags (scripts, styles, metas, divs).
    - Removes emojis and non-Latin1 glyphs that cause black square '■' rendering in Helvetica.
    - Escapes unescaped ampersands.
    - Converts valid markdown bold/italics into <b> and <i> tags.
    - Strips unbalanced tags so ReportLab's paraparser NEVER throws unclosed tag syntax errors.
    - Escapes all stray < and > characters.
    """
    if not text:
        return ""
    
    # Clean emojis first to avoid ReportLab black boxes
    cleaned = clean_emojis_for_pdf(text.strip())
    
    # If text contains raw HTML document or markup, clean it safely into readable text
    if any(k in cleaned.lower() for k in ["<!doctype", "<html", "<head", "<body", "<script", "tailwindcss"]):
        cleaned = re.sub(r'<script.*?</script>', '', cleaned, flags=re.DOTALL | re.IGNORECASE)
        cleaned = re.sub(r'<style.*?</style>', '', cleaned, flags=re.DOTALL | re.IGNORECASE)
        cleaned = re.sub(r'<!--.*?-->', '', cleaned, flags=re.DOTALL)
        cleaned = re.sub(r'<h[1-6][^>]*>(.*?)</h[1-6]>', r'\n## \1\n', cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\1\n', cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r'<li[^>]*>(.*?)</li>', r'\n- \1', cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r'<br\s*/?>', '\n', cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r'<[^>]+>', ' ', cleaned)
        cleaned = re.sub(r'\s+', ' ', cleaned).strip()

    # Escape raw ampersands
    cleaned = re.sub(r'&(?!amp;|lt;|gt;|quot;|apos;|#\d+;)', '&amp;', cleaned)

    # Markdown bold/italics conversion
    cleaned = re.sub(r'\*\*([^\*\n]+?)\*\*', r'<b>\1</b>', cleaned)
    cleaned = re.sub(r'\*([^\*\n]+?)\*', r'<i>\1</i>', cleaned)
    cleaned = cleaned.replace('**', '').replace('*', '')

    # Verify balance of tags (b, i, u)
    for tag in ['b', 'i', 'u']:
        open_c = len(re.findall(f'<{tag}>', cleaned, flags=re.IGNORECASE))
        close_c = len(re.findall(f'</{tag}>', cleaned, flags=re.IGNORECASE))
        if open_c != close_c:
            cleaned = re.sub(f'</?{tag}>', '', cleaned, flags=re.IGNORECASE)

    # Escape any other < and > characters that are not valid tags
    allowed = r'(</?(?:b|i|u|font)(?:\s+[^>]*)?>|<br\s*/>)'
    parts = re.split(allowed, cleaned, flags=re.IGNORECASE)
    res = []
    for p in parts:
        if re.match(allowed, p, flags=re.IGNORECASE):
            res.append(p)
        else:
            res.append(p.replace('<', '&lt;').replace('>', '&gt;'))
    return "".join(res)


def create_styled_pitch_pdf(pitch_markdown: str, client_name: str, niche: str) -> io.BytesIO:
    """Creates a beautifully styled, executive agency proposal PDF from Markdown pitch text."""
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    # Custom Color Palette
    primary_color = colors.HexColor("#0f172a")     # Deep slate 900
    accent_color = colors.HexColor("#4f46e5")      # Indigo 600
    secondary_accent = colors.HexColor("#0284c7")  # Cyan 600
    text_color = colors.HexColor("#334155")        # Slate 700
    muted_color = colors.HexColor("#64748b")       # Slate 500
    card_bg = colors.HexColor("#f8fafc")           # Slate 50

    # Custom Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=primary_color,
        spaceAfter=6
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=muted_color,
        spaceAfter=15
    )

    h1_style = ParagraphStyle(
        'Header1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=accent_color,
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Header2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=primary_color,
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=text_color,
        spaceAfter=5
    )

    bullet_style = ParagraphStyle(
        'BulletCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=text_color,
        leftIndent=15,
        firstLineIndent=-8,
        spaceAfter=3
    )

    callout_style = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9.5,
        leading=14,
        textColor=primary_color,
    )

    elements = []

    # 1. Header Banner Box
    banner_data = [
        [
            Paragraph("<b>STRATEGIC CLIENT PROPOSAL &amp; TRANSFORMATION BLUEPRINT</b>", 
                      ParagraphStyle('BannerH', fontName='Helvetica-Bold', fontSize=10, textColor=colors.white)),
            Paragraph(f"Client: <b>{client_name}</b>", 
                      ParagraphStyle('BannerR', fontName='Helvetica', fontSize=9, textColor=colors.HexColor('#e2e8f0'), alignment=2))
        ]
    ]
    banner_table = Table(banner_data, colWidths=[360, 172])
    banner_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), primary_color),
        ('PADDING', (0, 0), (-1, -1), 10),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
    ]))
    elements.append(banner_table)
    elements.append(Spacer(1, 15))

    # 2. Document Title
    elements.append(Paragraph(f"Digital Presence &amp; Conversion Strategy", title_style))
    elements.append(Paragraph(f"Prepared specifically for <b>{client_name}</b> • Industry: <b>{niche}</b>", subtitle_style))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#e2e8f0"), spaceAfter=15))

    # 3. Process Markdown lines
    lines = pitch_markdown.split('\n')
    in_code_block = False
    callout_buffer = []

    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            if callout_buffer:
                # Flush callout only if non-empty
                valid_callouts = [c for c in callout_buffer if c.strip()]
                if valid_callouts:
                    callout_text = "<br/>".join(valid_callouts)
                    t = Table([[Paragraph(callout_text, callout_style)]], colWidths=[532])
                    t.setStyle(TableStyle([
                        ('BACKGROUND', (0, 0), (-1, -1), card_bg),
                        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#cbd5e1")),
                        ('LINELEFT', (0, 0), (-1, -1), 3, accent_color),
                        ('PADDING', (0, 0), (-1, -1), 10),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
                    ]))
                    elements.append(t)
                    elements.append(Spacer(1, 8))
                callout_buffer = []
            else:
                elements.append(Spacer(1, 4))
            continue

        if line.startswith("```"):
            in_code_block = not in_code_block
            continue

        # Format with bulletproof reportlab sanitizer
        clean_line = sanitize_for_reportlab(line)
        if not clean_line:
            continue

        # Check for Horizontal Rules (---, ***, ___)
        if re.match(r'^(\-{3,}|\*{3,}|_{3,}|\s*(\-\s*){3,})$', line.strip()):
            elements.append(Spacer(1, 4))
            elements.append(HRFlowable(width="100%", thickness=0.75, color=colors.HexColor("#e2e8f0"), spaceBefore=4, spaceAfter=6))
            continue

        # Check for any markdown heading (# to ######)
        heading_match = re.match(r'^(#{1,6})\s*(.*)$', line)
        if heading_match:
            heading_level = len(heading_match.group(1))
            raw_text = heading_match.group(2).strip()
            heading_text = sanitize_for_reportlab(raw_text).lstrip("#").strip()

            # Skip duplicate title at top of markdown
            if heading_level <= 2 and any(k in heading_text.lower() for k in ["client proposal", "proposal & pitch", client_name.lower()]):
                continue

            if heading_level <= 2:
                elements.append(Paragraph(heading_text, h1_style))
                elements.append(Spacer(1, 3))
            elif heading_level == 3:
                elements.append(Paragraph(heading_text, h2_style))
                elements.append(Spacer(1, 2))
            else:
                elements.append(Paragraph(f"<b>{heading_text}</b>", h2_style))
                elements.append(Spacer(1, 2))
            continue

        if line.startswith("- ") or line.startswith("* "):
            bullet_text = "• " + clean_line.lstrip("-* ").strip()
            elements.append(Paragraph(bullet_text, bullet_style))
        elif re.match(r'^\d+\.\s', line):
            # Numbered list
            elements.append(Paragraph(clean_line, bullet_style))
        elif line.startswith(">"):
            c_val = clean_line.lstrip("> ").strip()
            if c_val:
                callout_buffer.append(c_val)
        else:
            clean_body = clean_line.lstrip("#").strip()
            if clean_body:
                elements.append(Paragraph(clean_body, body_style))

    # Flush any remaining callout items
    if callout_buffer:
        valid_callouts = [c for c in callout_buffer if c.strip()]
        if valid_callouts:
            callout_text = "<br/>".join(valid_callouts)
            t = Table([[Paragraph(callout_text, callout_style)]], colWidths=[532])
            t.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), card_bg),
                ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#cbd5e1")),
                ('LINELEFT', (0, 0), (-1, -1), 3, accent_color),
                ('PADDING', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ]))
            elements.append(t)
            elements.append(Spacer(1, 8))

    # 4. Final Footer Note
    elements.append(Spacer(1, 15))
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#e2e8f0"), spaceAfter=10))
    footer_text = Paragraph(
        "<i>CONFIDENTIAL &amp; PROPRIETARY • Prepared with Autonomous AI Studio • Ready for implementation upon client signature.</i>",
        ParagraphStyle('Footer', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=8, textColor=muted_color, alignment=1)
    )
    elements.append(footer_text)

    try:
        doc.build(elements)
    except Exception as build_err:
        # Zero-crash fallback: Build clean plain paragraphs
        buffer = io.BytesIO()
        fallback_doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
        fallback_elements = [
            Paragraph(f"<b>{client_name.upper()} — STRATEGIC PROPOSAL</b>", h1_style),
            Spacer(1, 10)
        ]
        for raw_l in pitch_markdown.splitlines():
            txt = re.sub(r'<[^>]+>', ' ', raw_l).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').strip()
            if txt:
                fallback_elements.append(Paragraph(txt, body_style))
                fallback_elements.append(Spacer(1, 4))
        fallback_doc.build(fallback_elements)

    buffer.seek(0)
    return buffer


def create_styled_resume_pdf(resume_markdown: str, candidate_name: str = "Mohammad Rehan", role_title: str = "Senior Full-Stack & AI Systems Engineer", contact_details: dict = None) -> io.BytesIO:
    """Creates a beautifully styled, ATS-optimized executive personal resume / portfolio PDF."""
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=30,
        leftMargin=30,
        topMargin=22,
        bottomMargin=22
    )

    styles = getSampleStyleSheet()

    # Premium Executive Color Palette
    primary_color = colors.HexColor("#0f172a")     # Deep Slate 900
    accent_color = colors.HexColor("#4f46e5")      # Indigo 600
    secondary_accent = colors.HexColor("#0284c7")  # Cyan 600
    text_color = colors.HexColor("#334155")        # Slate 700
    muted_color = colors.HexColor("#64748b")       # Slate 500
    card_bg = colors.HexColor("#f8fafc")           # Slate 50
    border_color = colors.HexColor("#e2e8f0")      # Slate 200

    # Custom Typography Styles
    name_style = ParagraphStyle(
        'ResumeName',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=19,
        leading=22,
        textColor=primary_color,
        spaceAfter=2
    )

    title_style = ParagraphStyle(
        'ResumeTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13.5,
        textColor=accent_color,
        spaceAfter=3
    )

    contact_style = ParagraphStyle(
        'ResumeContact',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.0,
        leading=11.0,
        textColor=muted_color,
        spaceAfter=5
    )

    section_heading = ParagraphStyle(
        'ResumeSectionHeading',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=10.0,
        leading=13.0,
        textColor=primary_color,
        spaceBefore=6,
        spaceAfter=2,
        keepWithNext=True
    )

    subheading_style = ParagraphStyle(
        'ResumeSubHeading',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=8.8,
        leading=11.5,
        textColor=colors.HexColor("#1e293b"),
        spaceBefore=3.5,
        spaceAfter=1.5,
        keepWithNext=True
    )

    item_title_style = ParagraphStyle(
        'ResumeItemTitle',
        parent=styles['Heading4'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.0,
        textColor=colors.HexColor("#0f172a"),
        spaceBefore=3,
        spaceAfter=1.5,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'ResumeBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.1,
        leading=11.0,
        textColor=text_color,
        spaceAfter=1.5
    )

    bullet_style = ParagraphStyle(
        'ResumeBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.1,
        leading=10.8,
        textColor=text_color,
        leftIndent=11,
        firstLineIndent=-7,
        spaceAfter=1.2
    )

    callout_style = ParagraphStyle(
        'ResumeSummary',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.1,
        leading=11.2,
        textColor=colors.HexColor("#1e293b")
    )

    elements = []

    # 1. Executive Top Header (Name + Title + Contact details)
    c_email = (contact_details or {}).get("email", "rehankhan20871621@gmail.com")
    c_phone = (contact_details or {}).get("phone", "+91 70915 18548")
    c_loc = (contact_details or {}).get("location", "Patna, Bihar, India")
    c_linkedin = (contact_details or {}).get("linkedin", "linkedin.com/in/mohammad-rehan-tech")
    c_github = (contact_details or {}).get("github", "github.com/mohammadrehan1621")
    c_portfolio = (contact_details or {}).get("portfolio", "mohammadrehan.pages.dev")

    header_text = [
        Paragraph(f"<b>{candidate_name.upper()}</b>", name_style),
        Paragraph(role_title, title_style),
        Paragraph(f"<b>Email:</b> {c_email} &nbsp;•&nbsp; <b>Phone:</b> {c_phone} &nbsp;•&nbsp; <b>Location:</b> {c_loc}<br/><b>LinkedIn:</b> {c_linkedin} &nbsp;•&nbsp; <b>GitHub:</b> {c_github} &nbsp;•&nbsp; <b>Portfolio:</b> {c_portfolio}", contact_style)
    ]
    elements.extend(header_text)
    elements.append(HRFlowable(width="100%", thickness=1.5, color=accent_color, spaceAfter=5))

    # 2. Parse and render resume markdown content
    lines = resume_markdown.split('\n')
    summary_buffer = []

    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            if summary_buffer:
                valid_summary = [s for s in summary_buffer if s.strip()]
                if valid_summary:
                    summary_text = "<br/>".join(valid_summary)
                    t = Table([[Paragraph(summary_text, callout_style)]], colWidths=[552])
                    t.setStyle(TableStyle([
                        ('BACKGROUND', (0, 0), (-1, -1), card_bg),
                        ('BOX', (0, 0), (-1, -1), 0.75, border_color),
                        ('LINELEFT', (0, 0), (-1, -1), 3.5, accent_color),
                        ('PADDING', (0, 0), (-1, -1), 5),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
                    ]))
                    elements.append(t)
                    elements.append(Spacer(1, 2))
                summary_buffer = []
            continue

        # Check for explicit PageBreak tokens
        if any(token in line.lower() for token in ["[pagebreak]", "<!-- pagebreak -->", "\\pagebreak"]):
            elements.append(PageBreak())
            continue

        if line.startswith("```"):
            continue

        clean_line = sanitize_for_reportlab(line)
        if not clean_line:
            continue

        # Check for Horizontal Rules (---, ***, ___)
        if re.match(r'^(\-{3,}|\*{3,}|_{3,}|\s*(\-\s*){3,})$', line.strip()):
            elements.append(Spacer(1, 2))
            elements.append(HRFlowable(width="100%", thickness=0.75, color=border_color, spaceBefore=2, spaceAfter=4))
            continue

        # Check for any markdown heading (# to ######)
        heading_match = re.match(r'^(#{1,6})\s*(.*)$', line)
        if heading_match:
            heading_level = len(heading_match.group(1))
            raw_text = heading_match.group(2).strip()
            heading_text = sanitize_for_reportlab(raw_text).lstrip("#").strip()

            # Skip duplicate title/name lines at the top of markdown
            if heading_level <= 2 and any(k in heading_text.lower() for k in [candidate_name.lower(), "resume", "curriculum vitae"]):
                continue

            # Check if this heading should be treated as a major section header
            major_sections = [
                "EXECUTIVE SUMMARY", "CORE COMPETENCIES", "ARCHITECTURE STACK",
                "KEY PRODUCTION SYSTEMS", "PRODUCTION SYSTEMS", "PROJECTS",
                "PROFESSIONAL EXPERIENCE", "WORK EXPERIENCE", "EXPERIENCE",
                "EDUCATION", "TECHNICAL SKILLS", "SKILLS", "CERTIFICATIONS", "TECHNICAL ENVIRONMENT"
            ]
            is_major = (heading_level <= 2) or any(sec in heading_text.upper() for sec in major_sections)

            if is_major:
                elements.append(Paragraph(f"<b>{heading_text.upper()}</b>", section_heading))
                elements.append(HRFlowable(width="100%", thickness=0.75, color=border_color, spaceAfter=2.5))
            elif heading_level == 3:
                elements.append(Paragraph(f"<b>{heading_text}</b>", subheading_style))
            else:
                elements.append(Paragraph(f"<b>{heading_text}</b>", item_title_style))
            continue

        if line.startswith("- ") or line.startswith("* "):
            bullet_text = "• " + clean_line.lstrip("-* ").strip()
            elements.append(Paragraph(bullet_text, bullet_style))
        elif re.match(r'^\d+\.\s', line):
            elements.append(Paragraph(clean_line, bullet_style))
        elif line.startswith(">"):
            c_val = clean_line.lstrip("> ").strip()
            if c_val:
                summary_buffer.append(c_val)
        else:
            clean_body = clean_line.lstrip("#").strip()
            if clean_body:
                elements.append(Paragraph(clean_body, body_style))

    if summary_buffer:
        valid_summary = [s for s in summary_buffer if s.strip()]
        if valid_summary:
            summary_text = "<br/>".join(valid_summary)
            t = Table([[Paragraph(summary_text, callout_style)]], colWidths=[552])
            t.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), card_bg),
                ('BOX', (0, 0), (-1, -1), 0.75, border_color),
                ('LINELEFT', (0, 0), (-1, -1), 3.5, accent_color),
                ('PADDING', (0, 0), (-1, -1), 5),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ]))
            elements.append(t)

    # 3. Footer Note
    elements.append(Spacer(1, 4))
    elements.append(HRFlowable(width="100%", thickness=0.75, color=border_color, spaceAfter=3))
    footer_text = Paragraph(
        f"<i>{candidate_name} • Professional Resume &amp; Architecture Dossier • ATS-Optimized High-Impact Executive Dossier</i>",
        ParagraphStyle('ResumeFooter', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=7.0, textColor=muted_color, alignment=1)
    )
    elements.append(footer_text)

    try:
        doc.build(elements)
    except Exception as build_err:
        buffer = io.BytesIO()
        fallback_doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
        fallback_elements = [
            Paragraph(f"<b>{candidate_name.upper()} — RESUME</b>", name_style),
            Spacer(1, 10)
        ]
        for raw_l in resume_markdown.splitlines():
            txt = re.sub(r'<[^>]+>', ' ', raw_l).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').strip()
            if txt:
                fallback_elements.append(Paragraph(txt, body_style))
                fallback_elements.append(Spacer(1, 3))
        fallback_doc.build(fallback_elements)

    buffer.seek(0)
    return buffer

