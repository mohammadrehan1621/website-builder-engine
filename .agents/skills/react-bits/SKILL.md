---
name: react-bits
description: Complete integration and engineering guide for React Bits (DavidHDev/react-bits), the open-source library of 100+ animated, interactive React & Next.js components. Use for incorporating high-impact backgrounds, text effects, spotlight cards, and micro-interactions.
---

# React Bits -- Production Engineering Codex
Developed by David H (`DavidHDev/react-bits` / `reactbits.dev`).
"The largest open-source library of animated, interactive, and customizable React & Next.js components for building standout web products and experiences. Built for humans and AI agents."

---

## 1. Component Categories & Inventory

| Category | High-Impact Components | Typical Use Case |
| :--- | :--- | :--- |
| **Backgrounds** | `Particles`, `Aurora`, `Hyperspeed`, `GridDistortion`, `Waves`, `Noise` | Hero banners, section backdrops, interactive canvas backgrounds. |
| **Text Animations** | `DecryptedText`, `ShinyText`, `SplitText`, `BlurText`, `TrueFocus`, `VariableProximity` | Cyber security headlines, quantitative proof stats, founder titles. |
| **Interactive Cards** | `SpotlightCard`, `PixelCard`, `TiltedCard`, `GlareCard`, `Stack` | Software flagships, feature grids, pricing tiers. |
| **Micro-Interactions** | `ClickSpark`, `SplashCursor`, `Magnet`, `ElasticSlider` | High-tactile button clicks, interactive proof triggers. |

---

## 2. Core Integration Patterns

React Bits components are designed for easy drop-in adoption with **Tailwind CSS**, **Framer Motion**, and **React**.

### Pattern A: `SpotlightCard` (Hairline Mouse Spotlight)
Adds a subtle radial illumination that follows the cursor across dark obsidian cards without any layout wobble:
```tsx
'use client';

import React, { useRef, useState } from 'react';

interface SpotlightCardProps {
  children: React.ReactNode;
  className?: string;
  spotlightColor?: string;
}

export function SpotlightCard({
  children,
  className = '',
  spotlightColor = 'rgba(16, 185, 129, 0.12)'
}: SpotlightCardProps) {
  const divRef = useRef<HTMLDivElement>(null);
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const [opacity, setOpacity] = useState(0);

  const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    if (!divRef.current) return;
    const rect = divRef.current.getBoundingClientRect();
    setPosition({ x: e.clientX - rect.left, y: e.clientY - rect.top });
  };

  return (
    <div
      ref={divRef}
      onMouseMove={handleMouseMove}
      onMouseEnter={() => setOpacity(1)}
      onMouseLeave={() => setOpacity(0)}
      className={`relative overflow-hidden rounded-2xl border border-slate-800 bg-slate-950 p-6 ${className}`}
    >
      <div
        className="pointer-events-none absolute -inset-px transition-opacity duration-300"
        style={{
          opacity,
          background: `radial-gradient(400px circle at ${position.x}px ${position.y}px, ${spotlightColor}, transparent 70%)`
        }}
      />
      <div className="relative z-10">{children}</div>
    </div>
  );
}
```

### Pattern B: `DecryptedText` (Cryptographic Terminal Scramble)
Simulates a high-speed cryptographic character unscramble for security suites:
```tsx
'use client';

import React, { useEffect, useState } from 'react';

const CHARS = 'ABCDEF0123456789!@#$%^&*()';

export function DecryptedText({ text, speed = 40 }: { text: string; speed?: number }) {
  const [displayText, setDisplayText] = useState('');

  useEffect(() => {
    let iteration = 0;
    const interval = setInterval(() => {
      setDisplayText(
        text
          .split('')
          .map((char, index) => {
            if (index < iteration) return text[index];
            return CHARS[Math.floor(Math.random() * CHARS.length)];
          })
          .join('')
      );

      if (iteration >= text.length) {
        clearInterval(interval);
      }
      iteration += 1 / 2;
    }, speed);

    return () => clearInterval(interval);
  }, [text, speed]);

  return <span className="font-mono font-bold tracking-wider">{displayText}</span>;
}
```

---

## 3. Adapting React Bits to RQL Sovereign Standards

To maintain institutional authority and prevent frontend "slop":
1. **Purge Excessive Wiggles**: Disable aggressive tilt angles on `TiltedCard` (keep maximum tilt <= 3 degrees, or stick to pure `SpotlightCard`).
2. **Color Harmony**: Replace generic purple/pink gradients with the unified palette:
   - Base: Obsidian Slate (`#020617`, `#0b111b`)
   - Accent: Sovereign Emerald (`#10b981`)
   - Telemetry: Precision Sky Blue (`#0ea5e9`)
3. **Canvas Lifecycle Discipline**: Wrap particle/WebGL canvas backgrounds in `IntersectionObserver` to pause render loops when scrolled out of view.
4. **100% 7-Bit ASCII Compliance**: Ensure all characters in code strings are strictly 7-bit ASCII (0-127).
