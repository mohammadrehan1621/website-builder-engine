---
name: lenis-smooth-scroll
description: Complete engineering guide, best practices, and production integration patterns for Lenis Smooth Scroll by Darkroom Engineering (darkroomengineering/lenis). Use when adding, configuring, or debugging high-performance momentum scrolling, GSAP ScrollTrigger sync, React/Vue Lenis providers, modal scroll locks (lenis.stop/start), anchor link navigation, or data-lenis-prevent nested containers.
---

# Lenis Smooth Scroll -- Production Engineering Codex
Developed by Darkroom Engineering (`darkroomengineering/lenis` / `lenis.dev`).
"Smooth scroll as it should be" -- lightweight, robust, unopinionated, hardware-accelerated momentum scrolling for modern web applications.

---

## 1. Core Architectural Principles

Lenis normalizes scroll momentum across mechanical mouse wheels, Apple Magic Mouse, precision trackpads, and mobile viewports with zero layout thrashing.

### The 4 Sovereign Invariants
1. **Never Hijack Native Mobile Touch (`smoothTouch: false`)**:
   Touch screens already have hardware-accelerated inertia built into iOS and Android. Setting `smoothTouch: true` introduces unnatural rubber-banding and touch latency. Keep native mobile touch intact.
2. **Single Unified RAF Loop**:
   Never run multiple independent `requestAnimationFrame` loops for scrolling. Tie Lenis directly into your primary animation frame or GSAP ticker.
3. **Modal & Drawer Lockout (`lenis.stop()` / `lenis.start()`)**:
   When a dialog, mobile drawer, or command palette (Ctrl+K) opens, call `lenis.stop()` immediately. When the overlay closes, call `lenis.start()`.
4. **Nested Scroll Containers (`data-lenis-prevent`)**:
   Any scrollable dropdown, modal body, code block, or table must carry `data-lenis-prevent` so inner scrolling does not bleed into the outer page.

---

## 2. Vanilla JS / CDN Implementation (Zero-Build Standard)

### Quick CDN Setup
```html
<!-- Lenis Latest Production Bundle -->
<script src="https://unpkg.com/lenis@1.3.27/dist/lenis.min.js"></script>
```

### Production Initialization Script
```javascript
(function initLenisEngine() {
  // 1. Accessibility Check: Respect reduced motion
  var isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (isReducedMotion || typeof window.Lenis === 'undefined') return;

  // 2. Hardware Calibration
  var lenis = new window.Lenis({
    duration: 1.15,
    easing: function(t) {
      // Quartic exponential ease-out curve
      return Math.min(1, 1.001 - Math.pow(2, -10 * t));
    },
    direction: 'vertical',
    gestureDirection: 'vertical',
    smooth: true,
    mouseMultiplier: 1.0,
    smoothTouch: false, // Critical: keep native touch on mobile
    touchMultiplier: 2.0
  });

  // Expose singleton for global access (modals, drawers)
  window.rqlLenis = lenis;

  // 3. RAF Animation Loop
  function raf(time) {
    lenis.raf(time);
    requestAnimationFrame(raf);
  }
  requestAnimationFrame(raf);

  // 4. Smooth Anchor Link Handler (e.g. #pricing, #store)
  document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
    anchor.addEventListener('click', function(e) {
      var targetId = this.getAttribute('href');
      if (targetId && targetId !== '#' && targetId.length > 1) {
        var targetEl = document.querySelector(targetId);
        if (targetEl) {
          e.preventDefault();
          lenis.scrollTo(targetEl, {
            offset: -80, // Header clearance offset in pixels
            duration: 1.2,
            immediate: false
          });
        }
      }
    });
  });

  // 5. Dynamic Content Resize Observer (auto-update scroll dimensions)
  if (window.ResizeObserver) {
    var resizeObserver = new ResizeObserver(function() {
      lenis.resize();
    });
    resizeObserver.observe(document.body);
  }
})();
```

---

## 3. React / Next.js Implementation

### Installation
```bash
npm install lenis
# or
npm install @studio-freight/react-lenis
```

### Global Provider in React / Next.js (App Router)
```tsx
'use client';

import { ReactLenis, useLenis } from 'lenis/react';
import { useEffect } from 'react';

export function SmoothScrollProvider({ children }: { children: React.ReactNode }) {
  const lenis = useLenis(({ scroll }) => {
    // Optional: hook into scroll events
  });

  return (
    <ReactLenis
      root
      options={{
        lerp: 0.1,
        duration: 1.2,
        smoothWheel: true,
        syncTouch: false // Keeps native touch on mobile devices
      }}
    >
      {children}
    </ReactLenis>
  );
}
```

---

## 4. GSAP & ScrollTrigger Synchronization

When pairing Lenis with GSAP `ScrollTrigger`, the two engines must share the exact same animation ticker to prevent jitter or desynchronization.

```javascript
// Register plugins
gsap.registerPlugin(ScrollTrigger);

// Initialize Lenis
const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  smoothTouch: false
});

// 1. Notify ScrollTrigger on every Lenis scroll
lenis.on('scroll', ScrollTrigger.update);

// 2. Drive Lenis through GSAP's high-precision internal ticker
gsap.ticker.add((time) => {
  lenis.raf(time * 1000); // GSAP provides time in seconds, Lenis expects ms
});

// 3. Disable GSAP internal lag smoothing to eliminate micro-stutter
gsap.ticker.lagSmoothing(0);
```

---

## 5. Modal Overlays, Drawers & Command Palettes

### The Problem
When a user opens a modal (such as a command palette `Ctrl+K`, dialog, or side drawer), scrolling the mouse wheel inside the modal might unintentionally scroll the underlying background page.

### The Two-Pronged Solution

#### Prong A: JavaScript Lockout
```javascript
// When opening any modal / drawer / command palette:
function openModal() {
  document.getElementById('my-modal').classList.add('open');
  if (window.rqlLenis) {
    window.rqlLenis.stop(); // Stops Lenis momentum loop
  }
}

// When closing:
function closeModal() {
  document.getElementById('my-modal').classList.remove('open');
  if (window.rqlLenis) {
    window.rqlLenis.start(); // Resumes smooth momentum
  }
}
```

#### Prong B: HTML Isolation Attribute
Add `data-lenis-prevent` to any scrollable element inside the modal:
```html
<div id="modal-container">
  <!-- The inner scrollable results list -->
  <div id="modal-scrollable-body" data-lenis-prevent class="overflow-y-auto max-h-[400px]">
    <!-- Items scroll freely inside without moving the window -->
  </div>
</div>
```

---

## 6. API Reference & Methods

| Method | Parameters | Description |
| :--- | :--- | :--- |
| `lenis.raf(time)` | `time: DOMHighResTimeStamp` | Advances the scroll engine. Must be called on every animation frame. |
| `lenis.scrollTo(target, options)` | `target: string \| HTMLElement \| number`<br>`options: { offset, duration, immediate, lock }` | Smoothly animates to a target selector, element, or pixel offset. |
| `lenis.stop()` | None | Pauses momentum calculations (use for modals and menus). |
| `lenis.start()` | None | Resumes momentum calculations. |
| `lenis.resize()` | None | Recalculates viewport height and document boundaries after dynamic DOM updates. |
| `lenis.destroy()` | None | Unbinds all listeners and cleans up the instance. |

---

## 7. Recommended Options Configuration

```javascript
{
  duration: 1.15,               // Duration in seconds (1.0 to 1.3 is optimal)
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), // Exponential ease out
  orientation: 'vertical',      // 'vertical' or 'horizontal'
  gestureOrientation: 'vertical',
  smoothWheel: true,            // Enable smooth mouse wheel scrolling
  smoothTouch: false,           // NEVER set true: preserve native mobile touch responsiveness
  wheelMultiplier: 1.0,         // Mouse wheel sensitivity
  touchMultiplier: 2.0,         // Mobile multiplier if touch enabled
  infinite: false,              // Infinite wrapping scroll
  autoResize: true              // Automatically call resize() on window resize
}
```

---

## 8. Anti-Patterns & Common Footguns

1. **Anti-Pattern 1: Setting `smoothTouch: true`**:
   Degrades mobile UX, causes touch lag and input delay on mobile Safari / Chrome. **Rule**: Always keep `smoothTouch: false`.
2. **Anti-Pattern 2: Missing `lenis.resize()` after async fetches**:
   When dynamic data or accordions expand, document height changes. Without `lenis.resize()`, scrolling may stop before reaching the new bottom. Use `ResizeObserver` on `document.body`.
3. **Anti-Pattern 3: Unhandled Anchor Jumps**:
   Default `<a href="#section">` browser jumps can cause visual snapping. Intercept anchor clicks with `e.preventDefault()` and call `lenis.scrollTo(target, { offset: -80 })`.
4. **Anti-Pattern 4: Scrollbar Flashing / Double Scrollbars**:
   Do not apply `overflow: scroll` to both `html` and `body`. In CSS, use:
   ```css
   html.lenis, html.lenis body {
     height: auto;
   }
   .lenis.lenis-smooth {
     scroll-behavior: auto !important;
   }
   .lenis.lenis-smooth [data-lenis-prevent] {
     overscroll-behavior: contain;
   }
   ```
