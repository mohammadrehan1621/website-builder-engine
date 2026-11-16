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
- **Hard-Law Reduced Motion (`prefers-reduced-motion: reduce`)**:
  ```css
  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
      animation-duration: 0.01ms !important;
      animation-iteration-count: 1 !important;
      transition-duration: 0.01ms !important;
      scroll-behavior: auto !important;
    }
  }
  ```
  Canvas particle loops freeze on a single static frame, and view transitions become instant 0ms cuts.
- **Keyboard Tab Beacon vs. Mouse Focus**:
  - Mouse/touch clicks get `:focus:not(:focus-visible) { outline: none; box-shadow: none; }` (clean clicks, zero ugly rectangles).
  - Keyboard users get `:focus-visible { outline: 2px solid #10b981 !important; outline-offset: 2px !important; }` (unmistakable Sovereign Emerald beacon).
- **Apple-Grade Subpixel Font Smoothing**:
  `body { -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; }`
- **Speculative Link Pre-Fetching on Hover Intent**:
  On internal navigation links, inject `<link rel="prefetch" href="...">` on `pointerenter` to download target HTML in the 250ms gap before the physical click occurs.
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
- **Sub-Pixel Hairlines on High-DPI Displays**: Use Tailwind inset rings (`ring-1 ring-inset ring-slate-800` or `ring-white/10`) to ensure razor-sharp borders on Apple Retina and 4K screens without box-model width distortion.

### Mobile Sticky Table Column Freezing
On data tables (`#commercial-catalog-table`), the primary identifier column stays permanently frozen during horizontal scrolling:
```css
#commercial-catalog-table th:first-child,
#commercial-catalog-table td:first-child {
  position: sticky;
  left: 0;
  background: #020617;
  z-index: 20;
  box-shadow: 1px 0 0 rgba(255, 255, 255, 0.08);
}
```

### Zero-CLS Skeleton Shimmer & Defensive Loading States
- Every media container MUST have an explicit `aspect-video` ratio and a dark placeholder:
  `<div class="aspect-video w-full rounded-xl bg-slate-900 border border-slate-800 relative overflow-hidden">`
- Prevents image load pops and guarantees Cumulative Layout Shift is mathematically 0.000 under any network condition.

### Modal Scrollbar Layout Shift Prevention (CLS = 0.000)
When opening any modal dialog:
- Never simply inject `overflow: hidden` on `<body>` without compensating for the removed 15px desktop scrollbar.
- Always apply scrollbar gutter compensation (`scrollbar-gutter: stable` or calculate `padding-right` offset) so the background page does not violently jump 15px horizontally.

---

## 4. Advanced Performance, Cryptography & Hardware Standards

### 1. Service Worker Cache Invalidation & Zero-Stale Deployment
To ensure users receive fresh production code immediately upon Cloudflare Pages deployments:
- Stamp cache buckets with version tags: `const CACHE_NAME = 'rql-v' + DEPLOY_VERSION;`
- In the Service Worker `activate` listener, automatically purge all outdated cache buckets:
  `caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))))`

### 2. Autoplay Audio Policy Compliance
All Web Audio API operations must check and resume context on the first user interaction:
```javascript
if (audioCtx && audioCtx.state === 'suspended') {
  audioCtx.resume();
}
```
Eliminates console warning errors while providing instantaneous 10ms micro-click feedback.

### 3. Empty-State Architecture & 1-Click Recovery
Every searchable catalog or data table MUST define a dedicated empty state:
- Centralized telemetry icon (`lucide="search-x"`).
- Reassuring copy: *"No commercial engineering suites matched your query."*
- 1-click instant recovery button: `[Reset Filter & View All 31 Suites]` that clears the query and restores all cards instantly.

### 4. Debounced Search & Input Event Batching (120ms RAF Batch)
On live search inputs:
- Wrap search filtering in a 120ms debounce or `requestAnimationFrame` scheduler.
- Prevents dropped keystrokes and maintains silky 60fps typing velocity across 31 cards and tables.

### 5. Multi-Stop Gradient Smoothing (Color Banding Prevention)
On deep obsidian backgrounds (`#020617` / `#0b111b`), replace harsh 2-stop linear gradients with smooth 4-stop mathematical curves:
`linear-gradient(180deg, #020617 0%, #050a14 35%, #09111f 70%, #0e1626 100%)`
Eliminates visible stair-stepping color bands on 8-bit desktop monitors.

### 6. Adaptive SVG Favicon (Dark/Light OS Vector Morphing)
Vector SVG favicons embed a media query so they stand out in all browser themes:
- Light OS mode: Solid dark charcoal shield.
- Dark OS mode: Automatically morphs to vibrant Electric Emerald (`#10b981`).

### 7. LCP Fetch Priority & Asynchronous Image Decoding (`fetchpriority="high"`)
For catalog and gallery grids:
- The first visible flagship card thumbnail MUST declare: `fetchpriority="high" loading="eager" decoding="async"`.
- All remaining below-the-fold cards MUST declare: `loading="lazy" decoding="async"`.
- Cuts Largest Contentful Paint (LCP) load time by up to 60%.

### 8. Accessible Modal Focus Trapping via the HTML `inert` Attribute
When modal dialogs are toggled:
- Set `document.querySelector('main').inert = true;` to freeze background DOM for keyboard users and screen readers.
- Automatically focus the primary interactive element inside the modal.
- On modal dismissal, restore `main.inert = false;` and return focus cleanly to the exact button that launched the modal.

### 9. Safe Web Storage Versioning & Incognito Quota Hygiene
All browser storage access must be protected:
- Wrap `localStorage` calls in try/catch accessors to prevent uncaught `QuotaExceededError` or `SecurityError` crashes in private/incognito browsing windows.
- Prefix all keys with version tags (`rql_store_v1`) to prevent stale legacy keys from corrupting modern interface states.

### 10. Horizontal Table Gesture Containment (`overscroll-behavior-x: contain`)
Data tables (`#commercial-catalog-table`) must prevent accidental full-page navigation:
```css
#commercial-catalog-table {
  overflow-x: auto;
  overscroll-behavior-x: contain;
}
```
Traps horizontal trackpad and touch gestures inside the table container, eliminating accidental Back/Forward swipe navigation on iOS Safari and Android Chrome.

### 11. Custom Sovereign Text Selection Styling (`::selection`)
Replace default Windows/Mac blue selection with theme-coherent accents:
```css
::selection {
  background: #065f46; /* Deep Emerald tint */
  color: #ffffff;
}
code::selection {
  background: #0369a1; /* Cyber Sky tint for cryptographic hashes */
  color: #ffffff;
}
```

### 12. Hardware Safe Area Insets for Notched Displays (`env(safe-area-inset-*)`)
Fixed bottom bars and floating dialogs must never be covered by device gesture bars or camera notches:
```css
.sticky-bottom-bar {
  padding-bottom: max(16px, env(safe-area-inset-bottom));
  padding-left: max(16px, env(safe-area-inset-left));
  padding-right: max(16px, env(safe-area-inset-right));
}
```

### 13. Native View Transitions API (`document.startViewTransition`)
When switching between Cards View and Technical Table View, or between category tabs on `store.html`:
```javascript
if (document.startViewTransition) {
  document.startViewTransition(() => {
    applyActiveCatalogView();
  });
} else {
  applyActiveCatalogView(); // Graceful fallback
}
```
Cross-fades active layouts over a 120ms compositor curve with zero layout jump and zero external animation libraries.

### 14. Cryptographic Subresource Integrity (SRI) & Hash Pinning
Local vendor scripts (`lucide.min.js`, `qrcode.min.js`) must declare cryptographic integrity hashes:
`<script src="assets/lucide.min.js" integrity="sha256-..." crossorigin="anonymous"></script>`
Guarantees browser-level execution refusal if any local vendor script is modified or tampered with.

### 15. Pure-CSS Compositor Scroll Progress (`animation-timeline: scroll()`)
The top reading indicator (`#rql-scroll-progress`) runs entirely on the browser GPU compositor thread without running JavaScript during scroll:
```css
@keyframes rql-progress-grow {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}
#rql-scroll-progress {
  transform-origin: 0% 50%;
  animation: rql-progress-grow auto linear;
  animation-timeline: scroll(root block);
}
```

### 16. Native Numeral Localization (`Intl.NumberFormat`)
Never concatenate currency strings manually:
- Global USD: `new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 }).format(amount)`
- Domestic INR: `new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR', maximumFractionDigits: 0 }).format(amount)`
Enforces correct Indian Lakh/Crore digit grouping (`1,49,999`) vs Western thousands (`149,999`).

### 17. Form Error Geometry Reservation (Zero CLS)
On all inquiry and contact forms:
- Error message containers must declare a fixed reserved height: `min-h-[20px] transition-opacity duration-150`.
- Validation errors transition between `opacity-0` and `opacity-100`, guaranteeing that form submit buttons never shift vertically by even 1 pixel.

### 18. Document Title Status Badging & Tab Awareness
Provide ambient situational awareness in the browser tab bar:
- In-progress verification: `document.title = "[84%] Verifying DocumentShield | Rehan Quant Lab"`
- Completed state: `document.title = "[VERIFIED] DocumentShield | Rehan Quant Lab"`

### 19. Offline PWA & Air-Gap Service Worker Architecture (`sw.js`)
To prove Rehan Quant Lab's 100% offline air-gap promise:
- Implement a zero-dependency Service Worker cache strategy (`sw.js`).
- Cache-first strategy for local static assets (`fonts/*.woff2`, `lucide.min.js`, `store.html`, `security.html`).
- Enables users to load the site, disconnect from Wi-Fi entirely, and run the **WebCrypto Hash Verifier, SaaS Savings Calculator, and Catalog Table 100% offline in browser memory**.

### 20. URL State Machine & History Traversal (`history.pushState` & `popstate`)
On catalog routes (`store.html`):
- Deep-link synchronization: URL updates dynamically without page reloads (`store.html#cat=retail` or `store.html?view=table&q=ssn`).
- Listen to `window.addEventListener('popstate')` so browser Back and Forward navigation cleanly switches tabs without triggering page refreshes or involuntary viewport jumps.

### 21. Battery Preservation & GPU Throttling Safeguards for `<canvas>`
Every background HTML5 canvas particle visualizer must safeguard laptop battery and mobile thermal limits:
- Pause rendering when scrolled out of view using `IntersectionObserver`.
- Pause rendering when the browser tab is hidden or minimized using `document.addEventListener('visibilitychange')`.

### 22. APCA High-Contrast Standards for Monospace Telemetry
In dark obsidian terminals (`#020617` / `#0b111b`):
- 10px-11px monospace numbers (`SHA-256`, RAM figures, PE64 specs) require higher lightness contrast (APCA Lc 75+, e.g. `#e2e8f0` or `#38bdf8`) to eliminate eye fatigue during long code audits.
- Secondary muted labels must never drop below `#94a3b8` (45% lightness).

### 23. OS Browser Theme-Color Synchronization
Seamless edge-to-edge mobile status bar integration on iOS Safari and Android Chrome:
```html
<meta name="theme-color" content="#020617" media="(prefers-color-scheme: dark)">
<meta name="theme-color" content="#fafafa" media="(prefers-color-scheme: light)">
```

### 24. Zero-Byte Web Audio Tactile Micro-Acoustics
For high-importance micro-actions (copying a hash, completing in-browser verification):
- Synthesize an optional 10ms micro-click directly in memory using native Web Audio API (`AudioContext` oscillator at 800Hz, volume 0.02).
- Zero network requests, 0ms latency, automatically muted if `prefers-reduced-motion` is active.

### 25. Streaming Memory-Safe File Hashing (OOM Crash Prevention)
On cryptographic verification routes (`security.html`):
- Multi-hundred megabyte `.exe` binaries must NEVER be read into a single in-memory ArrayBuffer.
- Use incremental stream slicing (`file.slice(offset, offset + chunkSize)` in 2MB to 4MB chunks) updating an incremental cryptographic digest or web worker.
- Guarantees max RAM usage under 10MB during multi-gigabyte file verification, eliminating browser tab crashes.

### 26. Absolute Self-Hosting & Zero-Telemetry CSP Invariant
Rehan Quant Lab is 100% offline and zero-telemetry:
- **Zero External Dependencies**: Every font (`fonts/*.woff2`), script (`lucide.min.js`, `qrcode.min.js`), and asset MUST be self-hosted locally in `/assets/`.
- **Strict Content Security Policy**: Prohibit external telemetry leaks:
  `default-src 'self'; script-src 'self' 'unsafe-inline'; font-src 'self'; connect-src 'self';`

### 27. Dynamic Mobile Viewport Units (`dvh` vs `vh`)
- Never use legacy `100vh` on mobile dialogs, heroes, or floating action bars.
- Use `100dvh` (Dynamic Viewport Height) or `min-h-[100dvh]` so that content is never clipped under the auto-collapsing Safari or Chrome address bar.

### 28. DOM Virtualization via `content-visibility: auto` (Google Chrome Baseline)
For high-density product grids (e.g., the 31 commercial suites on `store.html`):
```css
[data-product-card="true"] {
  content-visibility: auto;
  contain-intrinsic-size: 0 480px;
}
```
Skips rendering off-screen DOM nodes until the user scrolls near them, reducing layout calculation time by up to 80% and maintaining silky 60fps scrolling on mobile devices and lower-spec hardware.

### 29. Dual-Currency Synchronization Architecture (USD vs. Domestic INR)
Rehan Quant Lab serves both global enterprises and Indian domestic founders:
- **Global USD**: Stated first (`$179`), linked directly to international checkout desks (Stripe / Gumroad).
- **Domestic INR & UPI**: Synchronized domestic pricing (`Rs 14,999`), linked to Indian domestic checkout with instant QR and GST invoicing.
- **Discount Synchronization**: Auto-applied discount passes (`PIONEER70` = 70% off, `PIONEER20` = 20% off) must calculate and display synchronously in both currencies without rounding errors.
- **Tabular Alignment**: All prices must enforce `font-feature-settings: 'tnum' 1` (`font-mono`) for clean tabular comparison.

### 30. Tactile Clipboard Copying & Screen Reader Announcements
When users copy discount codes (`PIONEER70`), UPI VPAs, or SHA-256 hashes:
- **Visual State**: Icon swaps to emerald checkmark with `"Copied!"` label for 1800ms.
- **Legacy Fallback**: Automatic fallback to an offscreen `document.execCommand('copy')` if Clipboard API is restricted.
- **Assistive Technology**: Updates an invisible `aria-live="polite"` element announcing the copy action for visually impaired users.

### 31. Fluid Typographic Clamping (`clamp()`)
Main hero titles and section headers must scale continuously between mobile and desktop:
`font-size: clamp(1.85rem, 1.2rem + 2.5vw, 3.25rem);`
Prevents abrupt breakpoint snaps and eliminates awkward 1-word line wraps on tablet viewports.

### 32. Font Loading & Metric Matching (Zero FOUT / FOIT)
Custom local WOFF2 webfonts (Inter & JetBrains Mono) must enforce:
- `font-display: swap` in all `@font-face` definitions to prevent Flash of Invisible Text (FOIT).
- System font fallback stacks must match character widths to prevent layout shifts upon font arrival:
  `font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;`

### 33. Enterprise Print Stylesheet (`@media print`)
Enterprise procurement, legal teams, and auditors require clean PDF exports of license specifications, receipts, and verification declarations:
```css
@media print {
  nav, footer, #catalog-controls-container, #rql-scroll-progress, #rql-palette-backdrop, button, .video-overlay {
    display: none !important;
  }
  body {
    background: #ffffff !important;
    color: #000000 !important;
  }
  [data-product-card="true"] {
    break-inside: avoid;
    border: 1px solid #cbd5e1 !important;
    box-shadow: none !important;
  }
}
```

### 34. High-Contrast & Reduced-Transparency Accessibility
- **High Contrast**: Support `@media (forced-colors: active)` so all hairline borders and active indicators automatically inherit system tokens (`CanvasText`, `Highlight`).
- **Transparency Fallback**: Support `@media (prefers-reduced-transparency: reduce)` by replacing translucent acrylics (`backdrop-blur-md`) with solid 100% opaque slate backgrounds.

### 35. Mobile Virtual Keyboard & Typing Ergonomics
Eliminate typing friction on mobile devices across all search, contact, and dialog fields:
- Search inputs: `type="search" enterkeyhint="search"`
- Numeric / seat inputs: `type="number" inputmode="numeric"`
- Telephone / WhatsApp inputs: `type="tel" inputmode="tel"`
- Discount code fields: `autocapitalize="characters" autocomplete="off" spellcheck="false"`

---

## 5. The 19 Web Designer Competencies (Baked into RQL Engineering)

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

## 6. Universal Multi-Page Ecosystem Sync

The design system is not applied piecemeal. Every page in the repository must feel like part of the exact same sovereign operating system:

1. **`index.html`**: Flagship quantitative engineering hub, sovereign bento grid, zero scale hovers, unified slate/emerald badges.
2. **`store.html`**: 31-suite commercial catalog, single-row Command Ribbon, high-density cards + hardware telemetry table toggle, SaaS savings calculator.
3. **`projects.html`**: System architecture showcases, rock-solid category filters, pure obsidian/emerald indicators.
4. **`experience.html`**: Career milestones, 1px emerald hairline timeline, technical capabilities matrix.
5. **`security.html`**: WebCrypto in-browser verification terminal, 31-suite cryptographic hash registry, RFC 9116 security declarations.
6. **`contact.html`**: Direct executive communication, institutional inquiry forms, zero-wobble inputs.
7. **`aegis.html`**, **`changelog.html`**, **`legal.html`**, **`demo.html`**: Rock-solid subpages matching header, typography, 1px borders, and footer verbatim.

---

## 7. Pre-Launch 22-Point Failure Checklist

Before any change is committed or deployed, every question must be verified with a 100% "YES":

1. [ ] **Widow Check**: Are all headers protected by `text-wrap: balance` with zero widowed orphan words?
2. [ ] **Accessibility Check**: Does every icon-only button (video play, search trigger, close button) possess an explicit `aria-label`?
3. [ ] **Tabular Numerals**: Do all prices, memory counters, hashes, and dates enforce `font-feature-settings: 'tnum' 1`?
4. [ ] **Touch Target Ergonomics**: Are all clickable buttons, tabs, and inputs >= 44x44px?
5. [ ] **Zero Wobble Verification**: Are all `hover:scale-*`, `hover:-translate-y-*`, and rubber-band bounce transitions eliminated?
6. [ ] **Mobile Sticky-Hover Guard**: Are all desktop hover styles scoped within `@media (hover: hover) and (pointer: fine)`?
7. [ ] **Dynamic Viewport (`100dvh`)**: Are all mobile full-height containers protected against bottom bar clipping?
8. [ ] **Modal Scrollbar Shift Guard**: Do all modal dialogs preserve scrollbar gutter width to prevent 15px layout jerks?
9. [ ] **Color Discipline**: Are all random pink, purple, and orange pills completely purged in favor of the Slate/Emerald/Sky system?
10. [ ] **Self-Hosting CSP**: Are all fonts, scripts, and media strictly hosted locally with zero external CDN calls?
11. [ ] **Canvas Lifecycle Guard**: Do all animated canvases pause when scrolled out of view or tab is hidden?
12. [ ] **History Deep-Link Navigation**: Does tab switching sync with the URL and handle browser Back/Forward without reload?
13. [ ] **View Transitions**: Are view and tab swaps wrapped in `document.startViewTransition` with instant fallback?
14. [ ] **Form Error Geometry**: Do all error message blocks have reserved heights to guarantee CLS = 0?
15. [ ] **LCP Priority**: Does the primary suite thumbnail declare `fetchpriority="high"` and `loading="eager"`?
16. [ ] **Modal Focus Trapping**: Is the background `<main>` marked `inert` during active modal presentations?
17. [ ] **Zero-CLS Skeleton**: Do media frames define dark skeleton placeholders to lock layout before download?
18. [ ] **Empty State Recovery**: Does search have a dedicated empty state with a 1-click reset button?
19. [ ] **Reduced Motion Guard**: Does `prefers-reduced-motion: reduce` freeze canvases and make transitions 0ms?
20. [ ] **Sticky Table Column**: Is the suite name frozen on mobile during horizontal table scrolling?
21. [ ] **100% 7-Bit ASCII Compliance**: Does the file contain zero non-ASCII bytes, zero emojis in code, and zero mojibake?
22. [ ] **Aegis Sentinel Pass**: Does `aegis_watchdog.ps1` execute with 13/13 PASSED?
