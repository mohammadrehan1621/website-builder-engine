---
name: rql-design-system
description: The sovereign, world-class design system and engineering standard for Rehan Quant Lab (rehanquantlab.com). Synthesizes ConardLi Web Design Engineer mindset, Jakub Krehel interface craftsmanship, Google Chrome modern web guidance, Apple fluidity, Linear/Stripe precision, Paul Bakaus discipline, and Anthropic visual restraint into one definitive law. Enforces 100% rock-solid stability (zero wobbles/scale jumps), unified obsidian/emerald/sky palette, high-density Bento grids, 100% 7-bit ASCII compliance, and CLS=0.
---

# Rehan Quant Lab (RQL) Sovereign Design System & Engineering Codex

## Core Philosophy: "The Bar is Stunning, Not Merely Functional"
Inspired by the industry-defining Web Design Engineer framework (ConardLi), Jakub Krehel's interface engineering, and Google Chrome modern web guidance:

> **"Every pixel is intentional. Every interaction is deliberate. The bar is never merely 'functional' -- it must be undeniably stunning, authoritative, and rock-solid."**

For Rehan Quant Lab, the soul is **The Sovereign Quantitative Bastion**:
- Financial-grade precision, zero-telemetry air-gapped security, and native Rust hardware velocity.
- Rejection of all generic AI frontend "slop": no floating purple blobs, no cartoonish rubber-band bounces, no unanchored cards, no rainbow badge clouds.
- Absolute respect for visual hierarchy, Gestalt psychology, and deliberate whitespace.

---

## 1. The Pre-Flight Five-Dial Calibration Matrix (ConardLi Standard)

Before authoring a single line of CSS or HTML for any page, the agent must calibrate the 5 core dials:

| Dial | Calibration Parameter | Mandated RQL Setting |
| :--- | :--- | :--- |
| **Dial 1: Variance** | Restrained vs. Experimental | **100% Institutional Restraint**: Predictable, rock-solid, financial-grade engineering grid. No bizarre layout shifts. |
| **Dial 2: Motion** | Still vs. Fluid vs. Playful | **Physical Stillness**: Zero scale jumps, zero rubber bounces; feedback is 100% 1px border luminance and shadow elevation. |
| **Dial 3: Density** | Airy vs. Compact / High-Density | **Bloomberg / Linear High-Density**: Compact single-row Command Ribbon, tight data cells, zero wasted vertical whitespace. |
| **Dial 4: Asset Fidelity** | Abstract vs. Photographic vs. Technical | **Authentic Technical Telemetry**: Raw PE64 binaries, SHA-256 hashes, verified screenshots, and architecture diagrams. No generic stock art. |
| **Dial 5: Color Saturation** | Monochrome vs. Restrained vs. High-Vibrancy | **Strict 3-Role Palette**: Obsidian Slate Foundation + Sovereign Emerald (#10b981) + Precision Sky Blue (#0ea5e9). |

---

## 2. Pillar of Rock-Solid Stability (Zero Wobble Law)

Elements must feel physically grounded like professional Bloomberg trading terminals and macOS system utilities.

### The Forbidden List (Purged Everywhere)
1. **NO `hover:scale-*` or `group-hover:scale-*`**: Elements must never suddenly zoom, scale, or jitter when the cursor passes over them.
2. **NO `hover:-translate-y-*` or floating lifts**: Cards must not lift upward on hover. Layout geometry stays strictly fixed.
3. **NO 3D Perspective Tilting**: Banned `perspective(1000px) rotateX(...) rotateY(...)`. No gyroscope card tilting or mouse-following glare.
4. **NO Rubber-Band Bounce Easing**: Banned `cubic-bezier(0.34, 1.56, 0.64, 1)` where overshoot causes wobbly bounces.
5. **NO Magnetic Drift**: Buttons must never follow the cursor (`translate3d(deltaX, deltaY, 0)`).
6. **NO Involuntary Auto-Scrolling**: Navigating tabs or hash links must never jerk or involuntarily scroll the user's viewport.

### The Mandated Interaction Standard
- **Hover Feedback**: Strictly **subtle 1px border luminance** (`border-slate-200` to `border-slate-400` in light mode, or `border-slate-800` to `border-emerald-500/50` in dark mode) paired with soft shadow elevation (`shadow-xs` to `shadow-md`). Zero pixel displacement.
- **Mobile Touch Invariant**: All desktop hover rules MUST be wrapped inside `@media (hover: hover) and (pointer: fine)` to prevent "sticky hover" locks on mobile taps.
- **Click Affordance**: Sub-pixel tactile feedback on `pointerdown` (0ms delay, mechanical click feel).
- **Smoothness**: Native high-performance transitions: `transition: border-color 0.15s ease, box-shadow 0.15s ease`.
- **Keyboard Power**: Every interactive element supports full keyboard navigation (Tab cycling, `Enter`/`Space` activation, `Escape` modal dismissal). Raycast Command Palette accessible everywhere via `Ctrl+K` or `/`.

---

## 3. High-Density Bento Grid & Card Architecture

Interfaces are organized like financial and engineering workstations: high information density, razor-sharp scannability, and zero visual clutter.

### Primary Action Singularity (Hick's Law Enforcement)
Every card, bento cell, or modal must have **EXACTLY ONE dominant primary action**:
- **Primary CTA**: High-contrast Sovereign Emerald or Solid Charcoal button (e.g., `Acquire Commercial License - $179`).
- **Secondary Actions**: Low-visual-weight hairline outline or text links (e.g., `Domestic UPI Desk` | `7-Day Specs`).
- **Media Previews**: Play overlays are integrated directly into thumbnail media containers with optical centering, never competing with checkout CTAs.

### Optical Alignment vs. Mathematical Alignment (Jakub Krehel Rule)
- **Optical Play Centering**: Triangular play glyphs must be offset by `+1.5px` to `+2px` on the X-axis (`ml-0.5` or `translate-x-[1.5px]`) because a triangle's geometric center is left of its visual mass center.
- **Concentric Border Radii**: Nested child elements must scale down border-radius relative to the parent card:
  - If Card = `rounded-2xl` (16px) with 16px padding, inner media container = `rounded-xl` (12px).
  - Outer container = `rounded-3xl` (24px) -> inner card = `rounded-2xl` (16px).
- **Badge Baseline Alignment**: Monospace tags (`font-mono`) next to display titles (`font-sans`) must use optical vertical-alignment (`inline-flex items-center`) to prevent 1px baseline droop.

### Modal Scrollbar Layout Shift Prevention (CLS = 0.000)
When opening any modal dialog:
- Never simply inject `overflow: hidden` on `<body>` without compensating for the removed 15px desktop scrollbar.
- Always apply scrollbar gutter compensation (`scrollbar-gutter: stable` or calculate `padding-right` offset) so the background page does not violently jump 15px horizontally.

---

## 4. The 19 Web Designer Competencies (Baked into RQL Engineering)

### Creative & Technical Disciplines
1. **Visual Design & Gestalt Principles**: Proximity, similarity, and figure-ground separation in all Bento cards.
2. **Typography Hierarchy**:
   - Primary Display Sans: Inter Display / Apple System Sans (`font-sans`) with tight tracking (`tracking-tight`).
   - Technical Monospace: JetBrains Mono / SF Mono (`font-mono`) for all filenames, hashes, commands, and metrics.
   - **Tabular Figures Invariant**: Mandatory `font-feature-settings: 'tnum' 1` (`font-mono` / `tabular-nums`) across all prices, counters, dates, and tables.
   - **Widow Prevention**: Apply `text-wrap: balance` to all headers and `text-wrap: pretty` to body copy.
3. **Composition & Visual Gravity**: Line lengths capped at 65-75 characters (`max-w-2xl` to `max-w-3xl`).
4. **Disciplined Color Theory (The Strict 3-Token System)**:
   - **Role 1 (Structural Canvas)**: Slate / Charcoal / Obsidian (`#020617`, `#0b111b`, `#0f172a`, `#1e293b`, `#334155`, `#f8fafc`).
   - **Role 2 (Sovereign Accent)**: Electric Emerald (`#10b981` / `text-emerald-500` / `bg-emerald-500/10` / `border-emerald-500/30`) for verified status, active tabs, and primary CTAs.
   - **Role 3 (Cyber Telemetry)**: Precision Sky Blue (`#0ea5e9` / `text-sky-400` / `bg-sky-500/10` / `border-sky-500/30`) for hardware architecture, AES-256 encryption tags, and memory benchmarks.
   - **Strict Bans**: BANNED pink/rose pills (`bg-rose-50`, `text-rose-700`), coral-red monospace filenames, and arbitrary purple/orange button clouds.
5. **Modern Web Tools & Baseline APIs (Google Chrome Guidance)**: Semantic HTML, modern dialog elements, fetch priority, and native lazy loading (`loading="lazy"`, `decoding="async"`).
6. **Responsive Layouts & Device Ergonomics**:
   - Mobile Portrait (375px & 390px): Thumb-reachable bottom actions, single-column stacked hierarchy.
   - Tablet Portrait (768px): 2-column balanced Bento grids.
   - Desktop & 4K (1280px to 1920px+): High-density multi-column Bento grids with generous breathing room.
   - Touch targets must always be >= 44x44px.
7. **User Experience (UX) & Cognitive Load Reduction**: 1-click direct checkout with auto-applied Pioneer passes.
8. **User Interface (UI) Precision & 5-State Completeness**:
   Every interactive component (buttons, inputs, cards, tabs) must explicitly define all 5 states:
   1. `Default`: Resting hairline border and clean surface.
   2. `Hover`: Subtle 1px border luminance (`border-slate-300` or `border-emerald-500/50`) + soft elevation shadow.
   3. `Active / Pressed`: Mechanical tactile depression (0ms delay).
   4. `Focus-Visible`: Unmistakable 2px Emerald outline ring for keyboard users (`focus-visible:ring-2 focus-visible:ring-emerald-500`).
   5. `Disabled`: Reduced opacity (`opacity-50 pointer-events-none`) with clear tooltip rationale.
9. **Search Engine Optimization (SEO) & Structured Data**: Valid JSON-LD Schema on every page, semantic heading hierarchy (`h1` -> `h2` -> `h3`), OpenGraph metadata.

### Strategic Mindset & Soft Skills
10. **Patience & Methodical Refinement**: Never rush code changes. Every commit must be tested against Strix and Aegis sentinels.
11. **Collaboration & Empathy**: Listen to the underlying intent and elevate it to world-class craftsmanship.
12. **Strategic Business Thinking**: Every design element must serve a commercial purpose -- building institutional trust, proving zero-telemetry security, or driving perpetual license acquisition.
13. **Attention to Detail**: Hairline 1px borders, pixel-perfect alignment, zero widowed text strings, and zero visual friction.
14. **Continuous Learning**: Continually integrate modern web standards, security patches, and performance optimizations.

---

## 5. Universal Multi-Page Ecosystem Sync

The design system is not applied piecemeal. Every page in the repository must feel like part of the exact same sovereign operating system:

1. **`index.html`**: Flagship quantitative engineering hub, sovereign bento grid, zero scale hovers, unified slate/emerald badges.
2. **`store.html`**: 31-suite commercial catalog, single-row Command Ribbon, high-density cards + hardware telemetry table toggle, SaaS savings calculator.
3. **`projects.html`**: System architecture showcases, rock-solid category filters, pure obsidian/emerald indicators.
4. **`experience.html`**: Career milestones, 1px emerald hairline timeline, technical capabilities matrix.
5. **`security.html`**: WebCrypto in-browser verification terminal, 31-suite cryptographic hash registry, RFC 9116 security declarations.
6. **`contact.html`**: Direct executive communication, institutional inquiry forms, zero-wobble inputs.
7. **`aegis.html`**, **`changelog.html`**, **`legal.html`**, **`demo.html`**: Rock-solid subpages matching header, typography, 1px borders, and footer verbatim.

---

## 6. Pre-Launch 10-Point Failure Checklist

Before any change is committed or deployed, every question must be verified with a 100% "YES":

1. [ ] **Widow Check**: Are all headers protected by `text-wrap: balance` with zero widowed orphan words?
2. [ ] **Accessibility Check**: Does every icon-only button (video play, search trigger, close button) possess an explicit `aria-label`?
3. [ ] **Tabular Numerals**: Do all prices, memory counters, hashes, and dates enforce `font-feature-settings: 'tnum' 1`?
4. [ ] **Touch Target Ergonomics**: Are all clickable buttons, tabs, and inputs >= 44x44px?
5. [ ] **Zero Wobble Verification**: Are all `hover:scale-*`, `hover:-translate-y-*`, and rubber-band bounce transitions eliminated?
6. [ ] **Mobile Sticky-Hover Guard**: Are all desktop hover styles scoped within `@media (hover: hover) and (pointer: fine)`?
7. [ ] **Modal Scrollbar Shift Guard**: Do all modal dialogs preserve scrollbar gutter width to prevent 15px layout jerks?
8. [ ] **Color Discipline**: Are all random pink, purple, and orange pills completely purged in favor of the Slate/Emerald/Sky system?
9. [ ] **100% 7-Bit ASCII Compliance**: Does the file contain zero non-ASCII bytes, zero emojis in code, and zero mojibake?
10. [ ] **Aegis Sentinel Pass**: Does `aegis_watchdog.ps1` execute with 13/13 PASSED?
