---
name: remotion-motion
description: Remotion's programmatic animation and motion physics framework adapted for web UI. Covers frame-accurate interpolation, cubic Bezier springs, spring physics (mass, tension, friction), timeline sequencing, and cinematic fluid transitions.
---

# Remotion Motion Physics & Timeline Choreography

## Core Philosophy
Remotion treats animation as a **deterministic mathematical function of time and physics**, rather than arbitrary CSS transition delays. Every movement on screen has mass, velocity, momentum, and friction.

---

## 1. Mathematical Spring Physics
* **Physical Spring Parameters**:
  * **Mass (`m`)**: Defines inertia (e.g. `mass = 1` for lightweight buttons, `mass = 1.8` for heavy bento cards).
  * **Stiffness (`k`)**: Defines snap and tension (e.g. `stiffness = 240` to `320`).
  * **Damping (`c`)**: Prevents perpetual oscillation (e.g. `damping = 28` for smooth settling without bouncy jiggle).
* **The Spring Formula**:
  $$\ddot{x} + \frac{c}{m}\dot{x} + \frac{k}{m}x = 0$$
  This yields an exponential decay envelope that feels natural to the human eye because it matches real-world physical objects.

---

## 2. Staggered Timeline Choreography
* When revealing grids (such as the 26 commercial suites or feature metrics), never reveal all items at the exact same instant.
* **Deterministic Stagger**: Apply a subtle index-based delay:
  ```css
  animation-delay: calc(var(--index, 0) * 35ms);
  ```
  This creates an organic, cascading wave that leads the user's eyes naturally from top to bottom.

---

## 3. Hardware Compositing (60fps Invariant)
* **Animate ONLY Composite Properties**:
  * `transform: translate3d(x, y, 0) scale(s)`
  * `opacity: o`
* **Strictly Prohibited in Animations**:
  * Never animate `width`, `height`, `margin`, `padding`, `top`, or `left`. These trigger heavy layout recalculations (Reflow) that drop framerates.
* **GPU Layer Promotion**: Use `will-change: transform` sparingly on active elements to promote them to dedicated GPU layers.

---

## 4. Reversible Micro-Transitions
* Hover states must never get stuck in mid-animation if the user sweeps their cursor away.
* All transitions must be bi-directional and interruptible, preserving current momentum and smoothly snapping back to resting position.
