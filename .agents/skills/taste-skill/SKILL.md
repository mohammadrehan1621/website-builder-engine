---
name: taste-skill
description: Anti-slop design framework and art-direction judgment layer for AI coding tools. Enforces a 7-step design workflow (Start with taste, Pick a direction, Set the rules, Make the visuals, Make it move, Critique it, Audit before launch) to eliminate generic AI templates and deliver distinctive, world-class digital craftsmanship.
---

# Taste Skill: Anti-Slop Design & Art Direction Framework

## Core Philosophy
Most AI-generated frontend code defaults to predictable "slop": generic purple gradients, three-line centered hero text, floating white cards with arbitrary dropshadows, and template layouts. 

Taste Skill injects **human art direction, intentional restraint, and high aesthetic judgment** into every interface component.

---

## The 7-Step Design Workflow

### Step 1: Start with Taste
* **Ban Generic Defaults**: Never use arbitrary purple/pink gradients, centered floating cards without visual hierarchy, or uninspired generic stock layouts.
* **Determine the Soul of the Product**: Identify what feeling the interface must evoke. For Rehan Quant Lab, the soul is **Sovereign Quantitative Bastion** — financial-grade precision, zero-telemetry air-gapped security, and native Rust hardware velocity.
* **Curate Extreme Restraint**: Every pixel, border, and color must earn its place. If an element does not provide clarity, trust, or utility, remove it.

### Step 2: Pick a Direction
* Establish a bold, cohesive visual archetype before writing a single line of CSS:
  * **Precision Neo-Brutalist Minimalism**: Deep obsidian canvas, razor-sharp 1px subtle borders (`rgba(255,255,255,0.08)`), high-density data typography, and restrained ambient glows.
  * **Industrial Terminal**: Monospace tabular figures, emerald/cyan telemetry indicators, tactile status badges, and hardware metrics.
  * **Apple Fluidity**: Tactile interactive feedback, spring-based momentum, and translucent elevated surfaces.

### Step 3: Set the Rules
* **Strict Spacing Scale**: Stick strictly to a 4px/8px/12px/16px/24px/32px/48px modular rhythm. Never use arbitrary random margins.
* **Typography Hierarchy**: Pair a clean display sans (e.g. Inter Display) with an industrial monospace font (JetBrains Mono) for all figures, hashes, codes, and metrics.
* **Color Role Discipline**:
  * Canvas Background: `#06090e` / `#0b111b`
  * Surface Layer: `#0e1624` with 1px border `rgba(255,255,255,0.08)`
  * Accent Emerald: `#10b981` (Sovereign offline / verified / action)
  * Cyber Sky: `#0ea5e9` (Cryptographic verification / telemetry)
  * Muted Text: `#64748b` to `#94a3b8` (never unreadable low-contrast grey)
* **Tabular Numbers Invariant**: Always enforce `font-feature-settings: 'tnum' 1` on prices, dates, hashes, and performance counters.

### Step 4: Make the Visuals
* **Bento Grid Composition**: Group related tools, specs, and actions into structured bento cells with clear visual weight and focal points.
* **Interactive Canvas**: Use hardware-accelerated 60fps HTML5 canvas rendering for interactive simulations, live benchmarks, and cryptographic visualizers.
* **Tactile Affordances**: Buttons must look unmistakably clickable, badges must feel physically pressed, and copy/download controls must provide instantaneous visual confirmation.

### Step 5: Make It Move
* **Velocity-Aware Springs**: Animate using natural physical spring curves (`stiffness: 300, damping: 30`).
* **Kill Latency**: Provide visual feedback on `pointerdown` (0ms delay), never waiting for `click`/touch release.
* **Reversibility**: Animations must be interruptible. If a user hovers and unhovers quickly, the UI must fluidly catch and reverse the momentum rather than completing a jarring linear loop.

### Step 6: Critique It (Anti-Slop Audit)
* Put the component through a ruthless critique before presenting it:
  1. *Does this look like every other AI website?* (If yes, strip the clichés).
  2. *Is the hierarchy instantly obvious in under 2 seconds?*
  3. *Is the contrast ratio WCAG AAA compliant?*
  4. *Are there any awkward text wraps or widowed words?*
  5. *Can this be simplified by 20% without losing functionality?*

### Step 7: Audit Before Launch
* **Real Browser Verification**: Test rendering across Chromium, Safari, and Firefox.
* **Mobile Responsiveness**: Verify layouts at 375px (iPhone SE), 390px (iPhone 14/15), 768px (iPad), and 1920px (Desktop).
* **Cumulative Layout Shift (CLS)**: Must be `0.000`. Every image, canvas, and modal must reserve explicit layout dimensions.
* **Security & Invariants**: Ensure 100% 7-bit ASCII compliance, strict CSP rules, and zero external CDN leaks.
