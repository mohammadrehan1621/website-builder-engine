---
name: gsap-animation
description: Comprehensive engineering guide for GreenSock Animation Platform (GSAP 3), ScrollTrigger, Flip, Observer, text animations, and Lenis smooth scroll ticker synchronization. Use when building high-performance, GPU-accelerated web animations with zero layout shift (CLS=0) and full accessibility.
---

# GSAP (GreenSock Animation Platform) -- Production Engineering Codex
Developed by GreenSock (`greensock/GSAP` / `gsap.com`).
The industry standard high-performance JavaScript animation platform for modern web applications.

---

## 1. Core Architecture & GPU Acceleration

GSAP bypasses slow layout recalculations by animating hardware-accelerated compositor properties:
- **Accelerated**: `x`, `y`, `z`, `scale`, `rotation`, `opacity`, `autoAlpha` (animates opacity + toggles visibility).
- **Prohibited**: Animating `top`, `left`, `width`, `height`, `margin`, or `padding` directly (triggers CPU reflow).

### The Sovereign GSAP Setup
```javascript
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

// Enforce standard defaults: snappy, predictable, non-wobbly
gsap.defaults({
  duration: 0.6,
  ease: 'power2.out'
});
```

---

## 2. Lenis Smooth Scroll & GSAP Synchronization

When pairing GSAP ScrollTrigger with Lenis, both systems MUST share a single master ticker to prevent micro-stutters and frame misalignment.

```javascript
// 1. Initialize Lenis
const lenis = new Lenis({
  duration: 1.15,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  smoothTouch: false // Preserve native touch on mobile
});

// 2. Synchronize ScrollTrigger with Lenis on scroll
lenis.on('scroll', ScrollTrigger.update);

// 3. Drive Lenis through GSAP ticker
gsap.ticker.add((time) => {
  lenis.raf(time * 1000); // GSAP time is seconds, Lenis expects milliseconds
});

// 4. Disable GSAP lag smoothing to eliminate inertial lag
gsap.ticker.lagSmoothing(0);
```

---

## 3. ScrollTrigger Best Practices

### Scroll-Driven Stat Odometers (Quartic Spring Count-Up)
```javascript
gsap.utils.toArray('.stat-odometer').forEach((el) => {
  const targetVal = parseFloat(el.getAttribute('data-target-val') || '0');
  
  gsap.fromTo(el, 
    { innerText: 0 },
    {
      innerText: targetVal,
      duration: 1.8,
      ease: 'power3.out',
      snap: { innerText: 1 },
      scrollTrigger: {
        trigger: el,
        start: 'top 85%',
        once: true
      }
    }
  );
});
```

### Staggered Entrance Animations (CLS = 0)
Always wrap animated elements in fixed-dimension containers or use `autoAlpha` so content takes up space before animation begins:
```javascript
gsap.from('.bento-card', {
  autoAlpha: 0,
  y: 20,
  stagger: 0.08,
  duration: 0.7,
  ease: 'power2.out',
  scrollTrigger: {
    trigger: '#catalog-section',
    start: 'top 80%',
    once: true
  }
});
```

---

## 4. React / Next.js Integration (`@gsap/react`)

Always use `useGSAP()` or `gsap.context()` in React to ensure clean unmounting and prevent memory leaks:
```tsx
'use client';

import { useRef } from 'react';
import gsap from 'gsap';
import { useGSAP } from '@gsap/react';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(useGSAP, ScrollTrigger);

export function AnimatedBentoSection() {
  const container = useRef<HTMLDivElement>(null);

  useGSAP(() => {
    gsap.from('.bento-item', {
      autoAlpha: 0,
      y: 24,
      stagger: 0.1,
      scrollTrigger: {
        trigger: container.current,
        start: 'top 75%'
      }
    });
  }, { scope: container });

  return (
    <div ref={container} className="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div className="bento-item p-6 rounded-2xl bg-slate-900 border border-slate-800">Item 1</div>
      <div className="bento-item p-6 rounded-2xl bg-slate-900 border border-slate-800">Item 2</div>
      <div className="bento-item p-6 rounded-2xl bg-slate-900 border border-slate-800">Item 3</div>
    </div>
  );
}
```

---

## 5. Anti-Patterns & Hard Laws

1. **NO Layout-Thrashing Properties**: Never animate `width`, `height`, `top`, or `left`. Use `scale` and `x`/`y`.
2. **NO Overshoot Bounces**: Avoid `elastic` or extreme `back.out(3)` easings that cause wobbly cartoon bounces. Enforce `power2.out` or `expo.out`.
3. **Respect Reduced Motion**: Always wrap entrance tweens in `window.matchMedia('(prefers-reduced-motion: reduce)')`.
4. **Memory Hygiene**: In SPAs, never animate without killing old ScrollTriggers (`ScrollTrigger.getAll().forEach(t => t.kill())`).
