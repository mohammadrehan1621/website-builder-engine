---
name: rql-design-system
description: The sovereign, world-class design system and engineering standard for Rehan Quant Lab (rehanquantlab.com). Synthesizes Apple fluidity, Linear/Stripe precision, Paul Bakaus craftsmanship, Anthropic visual restraint, and Vercel technical performance into one definitive law. Enforces 100% rock-solid stability (zero wobbles/scale jumps), unified obsidian/emerald/sky palette, high-density Bento grids, 100% 7-bit ASCII compliance, and CLS=0.
---

# Rehan Quant Lab (RQL) Sovereign Design System & Engineering Codex

## Core Philosophy: The Sovereign Quantitative Bastion
Rehan Quant Lab interfaces must reflect **financial-grade precision, zero-telemetry air-gapped security, and native Rust hardware velocity**.

We categorically reject generic AI frontend "slop":
- **NO** arbitrary purple/pink gradients or floating neon blobs.
- **NO** cartoonish bouncy spring curves, rubber-band overshoots, or wobbly tilts.
- **NO** unanchored floating white cards with muddy shadows.
- **NO** random rainbow badge scatter (pink, purple, orange, coral red).
- **NO** centered walls of generic marketing text.

Every pixel, 1px hairline border, and color token must earn its place. If an element does not provide clarity, trust, or utility, it is purged.

---

## Pillar 1: Rock-Solid Interaction & Motion Law (Zero Wobble)

Interface elements must feel physically grounded, rock-solid, and instantaneous like professional trading terminals, macOS system utilities, and Linear.

### The Forbidden List (Purged Everywhere)
1. **NO `hover:scale-*` or `group-hover:scale-*`**: Elements must never suddenly expand or zoom when the cursor passes over them.
2. **NO `hover:-translate-y-*` or floating lifts**: Cards must not lift upward on hover. Layout geometry stays strictly fixed.
3. **NO 3D Perspective Tilting**: Banned `perspective(1000px) rotateX(...) rotateY(...)`. No gyroscope card tilting or mouse-following glare.
4. **NO Rubber-Band Bounce Easing**: Banned `cubic-bezier(0.34, 1.56, 0.64, 1)` where overshoot causes wobbly bounces.
5. **NO Magnetic Drift**: Buttons must never follow the cursor (`translate3d(deltaX, deltaY, 0)`).
6. **NO Involuntary Auto-Scrolling**: Navigating tabs or hash links must never jerk or involuntarily scroll the user's viewport.

### The Mandated Interaction Standard
- **Hover Feedback**: Strictly **subtle 1px border luminance** (`border-slate-200` to `border-slate-400` in light mode, or `border-slate-800` to `border-emerald-500/50` in dark mode) paired with soft shadow elevation (`shadow-xs` to `shadow-md`). Zero pixel displacement.
- **Click Affordance**: Sub-pixel tactile feedback on `pointerdown` (0ms delay, mechanical click feel).
- **Smoothness**: Use native high-performance transitions: `transition: border-color 0.15s ease, box-shadow 0.15s ease`.
- **Keyboard Power**: Every interactive element supports full keyboard navigation (Tab cycling, `Enter`/`Space` activation, `Escape` modal dismissal). Raycast Command Palette accessible everywhere via `Ctrl+K` or `/`.

---

## Pillar 2: The Sovereign Palette (Strict 3-Color Discipline)

Arbitrary color choices erode trust. RQL strictly enforces a disciplined 3-role semantic color system across all pages:

| Role | Color / Hex Tokens | Purpose & Usage |
| :--- | :--- | :--- |
| **1. Structural Foundation** | **Slate / Charcoal / Obsidian**<br>`#020617` / `#0b111b` / `#0f172a`<br>`#1e293b` / `#334155` / `#f8fafc` | Canvas backgrounds, elevated card surfaces, hair-thin 1px borders, and readable body typography. |
| **2. Sovereign Accent** | **Electric Emerald**<br>`#10b981` / `text-emerald-500`<br>`bg-emerald-500/10` / `border-emerald-500/30` | Official verified releases, 100% air-gapped indicators, active tab selection, and primary high-conversion CTA buttons. |
| **3. Cyber Telemetry** | **Precision Sky Blue**<br>`#0ea5e9` / `text-sky-400`<br>`bg-sky-500/10` / `border-sky-500/30` | Technical architecture specs, cryptography tags (AES-256-GCM, SHA-256), memory telemetry, and code references. |

### Strict Bans
- **BANNED**: Pink and rose pills (`bg-rose-50`, `text-rose-700`, `bg-rose-500`).
- **BANNED**: Coral-red monospace file labels (`text-rose-700`).
- **BANNED**: Arbitrary purple, violet, or yellow badge clouds.
- **BANNED**: Jarring "Checkerboard Sandwiches" (e.g. dropping pure black boxes on pure white backgrounds without proper transitional elevation).

---

## Pillar 3: High-Density Bento Grid & Typography

Interfaces are organized like financial and engineering dashboards: high information density, razor-sharp scannability, and zero visual clutter.

### Typography Hierarchy
- **Primary Display Sans**: Inter Display / Apple System Sans (`font-sans`), tight letter-spacing (`tracking-tight`), crisp font weights (`font-semibold`, `font-bold`, `font-black`).
- **Technical Monospace**: JetBrains Mono / SF Mono (`font-mono`) for all filenames, execution commands, memory metrics, cryptographic hashes, and telemetry counters.
- **Tabular Figures Invariant**: Always enforce `font-feature-settings: 'tnum' 1` (`font-mono` or `tabular-nums`) on prices, dates, hashes, and performance counters.
- **Reading Gravity**: Maximum line width of 65-75 characters (`max-w-2xl` to `max-w-3xl`) for technical descriptions. Left-align all technical copy; center only high-impact single-concept hero titles.
- **WCAG AAA Contrast**: Secondary text must always maintain minimum 7:1 contrast ratio (`text-slate-400` on dark, `text-slate-600` on light). Never use washed-out low-contrast grey.

### Component & Card Architecture
- **Cards**: Single rounded corner scale (`rounded-2xl` for standard cards, `rounded-3xl` for flagship containers). 1px hairline border (`border-slate-200/90` or `border-white/10`).
- **Command Ribbon**: Single-row compact bar (52px max height) consolidating category tabs, real-time live search, and view switcher (Cards vs. Technical Table). No double-box stacking that wastes vertical viewport space.
- **Action Hierarchy**:
  - **Dominant Primary CTA**: Full-width high-contrast button with discount auto-applied (e.g. `Acquire Commercial License - $179`).
  - **Secondary Actions**: Clean, low-friction secondary links (e.g. `Domestic UPI & GST` | `7-Day Specs`).
- **Aspect Ratios**: Every preview, image, and canvas MUST define explicit layout dimensions (`aspect-video`, `w-full h-full`) to guarantee zero Cumulative Layout Shift (`CLS = 0`).

---

## Pillar 4: Universal Multi-Page Ecosystem Sync

The design system is not applied piecemeal. Every page in the repository must feel like part of the exact same sovereign operating system:

1. **`index.html`**: Flagship quantitative engineering hub, sovereign bento grid, zero scale hovers, unified slate/emerald badges.
2. **`store.html`**: 31-suite commercial catalog, single-row Command Ribbon, high-density cards + hardware telemetry table toggle, SaaS savings calculator.
3. **`projects.html`**: System architecture showcases, rock-solid category filters, pure obsidian/emerald indicators.
4. **`experience.html`**: Career milestones, 1px emerald hairline timeline, technical capabilities matrix.
5. **`security.html`**: WebCrypto in-browser verification terminal, 31-suite cryptographic hash registry, RFC 9116 security declarations.
6. **`contact.html`**: Direct executive communication, institutional inquiry forms, zero-wobble inputs.
7. **`aegis.html`**, **`changelog.html`**, **`legal.html`**, **`demo.html`**: Rock-solid subpages matching header, typography, 1px borders, and footer verbatim.

---

## Pillar 5: Production Invariants & Security Sentinel

Before any file is merged or deployed, it must satisfy all 4 invariant rules:

1. **100% 7-Bit ASCII Compliance**: Zero non-ASCII characters, zero unicode emojis in code, zero mojibake. Verified by Strix scanner in `aegis_watchdog.ps1`.
2. **Cumulative Layout Shift (CLS = 0.000)**: All dynamic blocks, images, and embeds must reserve explicit geometric dimensions.
3. **Zero JavaScript / JSON-LD Errors**: All scripts must be syntactically valid and pass automated Node.js AST parsing.
4. **Autonomous Sentinel Pass**: `aegis_watchdog.ps1` must pass 13/13 tests (Strix integrity, PentAGI edge probes, directory checks).

---

## The 5 Continuous Steering Loops (Craft & Audit)

Whenever building or refining any page, run through the 5 loops:

- **`/craft`**: Build deliberately from content -> semantics -> spatial hierarchy -> typography -> rock-solid hover.
- **`/critique`**: Hunt for contrast failures, hierarchy ambiguity, alignment drift, and AI slop cliches.
- **`/audit`**: Test on real viewports: Mobile (375px/390px), Tablet (768px), and Desktop (1440px+). Check touch targets (>= 44x44px).
- **`/polish`**: Refine 1px hairline borders, active rings, and instant feedback affirmations.
- **`/distill`**: Apply the 20% Reduction Rule: *What 20% of redundant badges, borders, or lines can we remove to make the interface 2x clearer and more authoritative?*
