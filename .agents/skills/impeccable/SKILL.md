---
name: impeccable
description: Paul Bakaus's design craftsmanship framework. Enforces uncompromising frontend polish, anti-pattern detection, typography perfectionism, and structured steering commands (craft, critique, audit, polish, distill) to ensure interfaces look intentionally built by senior designers.
---

# Impeccable: Design Craftsmanship & Anti-Slop Discipline

## Core Principles
Created by Paul Bakaus (`pbakaus/impeccable`), this skill enforces design perfectionism. It bridges the gap between functional code and award-winning frontend design.

---

## 1. The 5 Steering Commands & Review Loops

### `/craft` — The Deliberate Creation Phase
* Never write CSS by copying generic snippets. Every spacing token, border radius, and color ratio must be calculated with purpose.
* Build components from the foundation upward: Content &rarr; Semantic Markup &rarr; Spatial Hierarchy &rarr; Typography &rarr; Responsive Adapters &rarr; Fluid Motion.

### `/critique` — The Ruthless Peer Review
Before delivering code, actively hunt for 5 common interface sins:
1. **Contrast Failure**: Is secondary text legible without squinting?
2. **Hierarchy Ambiguity**: Can a first-time visitor identify what is most important in 1.5 seconds?
3. **Alignment Drift**: Are icons, text baselines, and badge heights pixel-aligned?
4. **Padding Inconsistency**: Do sibling cards share identical internal padding and borders?
5. **Generic Clichés**: Did we slip in an unnecessary gradient or generic card shadow?

### `/audit` — The Multi-Environment Pre-Flight
* Test in real viewport sizes:
  * 375px & 390px (Mobile portrait: thumb ergonomics, single-column stacked hierarchy)
  * 768px (Tablet portrait: 2-column bento)
  * 1280px & 1920px (Desktop: full multi-column bento with generous breathing room)
* Test touch ergonomics: All interactive targets >= 44x44px.
* Test keyboard navigation: Tab cycling, Enter/Space activation, Esc modal dismissal.

### `/polish` — The Micro-Interaction Refinement
* **Subtle Border Radii**: Consistent `rounded-2xl` (16px) for cards, `rounded-xl` (12px) for buttons, `rounded-full` for status badges.
* **Border Light Bleed**: Use subtle inner borders (`ring-1 ring-white/10`) to create tactile physical depth without heavy muddy shadows.
* **Hover Micro-Lifts**: Smooth `transform: translateY(-2px)` with soft shadow diffusion.

### `/distill` — The 20% Reduction Rule
* Review the interface and ask: *"What 20% of text, badges, or lines can we delete while making the message stronger?"*
* Delete redundant decorative icons.
* Shorten paragraphs into punchy, scannable, high-conviction sentences.
