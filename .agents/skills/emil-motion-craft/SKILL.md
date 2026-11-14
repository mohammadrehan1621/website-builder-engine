---
name: emil-motion-craft
description: Emil Kowalski motion physics, Lenis smooth scrolling, GSAP ScrollTrigger, React Bits micro-interactions, WebGL shaders, Spline 3D, and Awwwards-tier visual craftsmanship strictly applied to frontend presentation while preserving backend invariants.
---

# Creative Motion Engineering & Emil Kowalski Interface Craft

## Overview
This skill elevates web interfaces from standard web pages into **Awwwards-tier, Apple-grade, high-performance digital experiences**. It harmonizes:
1. **Emil Kowalski's motion physics & interaction polish** (spatial continuity, tactile spring dampening, micro-interactions).
2. **Lenis smooth momentum scrolling** (cinematic inertia without breaking touch or native scroll semantics).
3. **GSAP & ScrollTrigger** (frame-synchronized timeline choreography, velocity-driven parallax, section pinning).
4. **React Bits & Bento dynamics** (magnetic buttons, cursor spotlight follow, iridescent border beams, 3D tilt cards).
5. **Shaders & WebGL Canvas FX** (film grain, chromatic aberration, aurora gradients, fluid caustics).
6. **Spline 3D & WebGL interaction** (interactive models, camera tracking, glass materials).
7. **Strict Separation of Concerns**: Transforms the **front look** with world-class polish while keeping **100% of the backend, edge functions, API contracts, and cryptographic invariants intact**.

---

## 1. Emil Kowalski's Laws of Motion & Polish

### 1.1 Spatial Continuity (No Teleportation)
- Elements must have a origin. When a modal, drawer, or dropdown opens, it should expand or emerge from its trigger element's spatial position rather than popping out of the void.
- When an item is dismissed, it collapses back to where it came from or follows its exit velocity vector.

### 1.2 Natural Spring Physics (No Cartoon Bouncing)
- Web animations should never feel like rubber cartoons. Use physical spring parameters tuned for professional, industrial-grade software:
  - **Mass (`m`)**: `0.8 &ndash; 1.0` (lightweight, responsive)
  - **Stiffness (`k`)**: `280 &ndash; 340` (crisp, immediate response)
  - **Damping (`c`)**: `28 &ndash; 32` (settles gracefully with zero residual ringing)
- Standard CSS Bezier equivalent: `cubic-bezier(0.16, 1, 0.3, 1)` (snappy ease-out) or `cubic-bezier(0.25, 0.1, 0.25, 1)` (smooth flow).

### 1.3 Micro-Tactile State Choreography
- **Hover**: Subtle lift (`translate3d(0, -2px, 0)`), scale `1.015`, subtle glow shift.
- **Active / Press**: Tactile compression (`scale(0.97)`), instant transition (`duration: 50ms`), mimic physical mechanical switches.
- **Magnetic Buttons**: Elements track the cursor within a 40px radius with an inverse square falloff:
  $$\Delta x = (x_{\text{mouse}} - x_{\text{center}}) \times 0.25$$
  $$\Delta y = (y_{\text{mouse}} - y_{\text{center}}) \times 0.25$$

---

## 2. Lenis Smooth Momentum Scrolling

### 2.1 Clean Initialization
Always configure Lenis with frame-budgeted RAF and zero conflict with fixed overlays:
```javascript
const lenis = new Lenis({
  duration: 1.15,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  direction: 'vertical',
  gestureDirection: 'vertical',
  smooth: true,
  mouseMultiplier: 1.0,
  smoothTouch: false, // Maintain native high-speed mobile touch
  touchMultiplier: 2,
});

function raf(time) {
  lenis.raf(time);
  requestAnimationFrame(raf);
}
requestAnimationFrame(raf);
```

### 2.2 GSAP ScrollTrigger Synchronization
When combining Lenis with GSAP ScrollTrigger, synchronize the update cycle:
```javascript
lenis.on('scroll', ScrollTrigger.update);

gsap.ticker.add((time) => {
  lenis.raf(time * 1000);
});
gsap.ticker.lagSmoothing(0);
```

---

## 3. GSAP Timeline & Scroll-Linked Choreography

### 3.1 Velocity-Aware Batch Reveals
Never reveal entire grids simultaneously. Stagger reveals based on scroll entrance velocity:
```javascript
gsap.from(".bento-card", {
  scrollTrigger: {
    trigger: "#catalog-grid",
    start: "top 80%",
    toggleActions: "play none none none"
  },
  y: 40,
  opacity: 0,
  duration: 0.75,
  ease: "power3.out",
  stagger: {
    amount: 0.25,
    grid: [3, 9],
    from: "start"
  }
});
```

### 3.2 Smooth Text Splitting & Kinetic Typography
- Split headline lines or words into individual masking spans (`overflow: hidden`).
- Slide up from `y: 100%` with ease-out cubic spring curves for high-impact hero typography.

---

## 4. React Bits & Bento Dynamics

### 4.1 Radial Cursor Spotlight Follow
Add cursor-following ambient highlights to cards without expensive DOM query loops:
```javascript
document.querySelectorAll('.spotlight-card').forEach(card => {
  card.addEventListener('mousemove', e => {
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    card.style.setProperty('--mouse-x', `${x}px`);
    card.style.setProperty('--mouse-y', `${y}px`);
  });
});
```
```css
.spotlight-card::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: radial-gradient(400px circle at var(--mouse-x, 0) var(--mouse-y, 0), rgba(99, 102, 241, 0.12), transparent 40%);
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.3s ease;
}
.spotlight-card:hover::before {
  opacity: 1;
}
```

### 4.2 Animated Border Beam
An energetic glowing photon racing along the border perimeter of hero cards:
```css
@keyframes border-beam {
  0% { offset-distance: 0%; }
  100% { offset-distance: 100%; }
}
.border-beam {
  position: absolute;
  aspect-ratio: 1;
  width: 100px;
  background: linear-gradient(to left, #6366f1, #10b981, transparent);
  offset-path: rect(0 auto auto 0 round 1.5rem);
  animation: border-beam 4s infinite linear;
}
```

---

## 5. WebGL Shaders & Canvas FX

### 5.1 Ambient GPU Grain & Film Texture
Procedural hardware-accelerated SVG noise / WebGL fragment shader:
- Never use heavy PNG grain tiles that increase page weight.
- Use zero-cost SVG `<feTurbulence>` filter or a 16x16 WebGL procedurally computed noise texture with `mix(color, noise, 0.035)` for subtle, cinematic tactile warmth.

### 5.2 Raymarched Aurora Gradients
- Use multi-layer radial gradient orbs with `filter: blur(80px)` and GPU compositing (`transform: translate3d(0,0,0)`), drifting on 15s to 25s sinusoidal paths.

---

## 6. Spline 3D & Interactive Models

### 6.1 Non-Blocking Embed Architecture
- Always lazy-load Spline scenes below the fold or after the initial DOM interactive event:
  ```html
  <script type="module" src="https://unpkg.com/@splinetool/viewer@latest/build/spline-viewer.js" defer></script>
  ```
- Wrap with a high-contrast poster placeholder to maintain zero Cumulative Layout Shift (`CLS = 0`).

---

## 7. The Invariant Preservation Protocol (Frontend Only)

When executing redesigns or visual upgrades using this skill:
1. **Zero Backend Modifications**: Keep all Cloudflare Workers edge routes (`/go`, `/api/*`), routing maps, and serverless logic 100% identical.
2. **Zero Form / Checkout Disruption**: Preserve all Gumroad URLs, coupon query parameters (`PIONEER70`, `PIONEER20`), and UPI India Desk modals.
3. **100% 7-Bit ASCII Compliance**: Never inject raw UTF-8 Unicode characters into HTML or JavaScript files. Always use standard HTML entities (`&trade;`, `&#8377;`, `&bull;`, `&rarr;`).
4. **Performance & SEO First**:
   - Lighthouse score target: **100/100 SEO**, **100/100 Best Practices**, **95+ Performance**.
   - Respect `prefers-reduced-motion`: When active, disable smooth scroll lerp and substitute fade transitions for transforms.
   - Maintain full keyboard accessibility (`tabindex`, focus rings, `aria-*` attributes).
