---
name: vercel-web-design
description: Vercel Web Interface & Design Guidelines. Enforces tabular figures, zero layout shift (CLS = 0), inline contextual help, explicit 4-state component handling, accessible focus states, and precision typography inspired by Geist and Vercel Labs engineering.
---

# Vercel Web Design Guidelines & Interface Engineering

## Overview
Standards distilled from Vercel Labs' official Web Interface Guidelines (`vercel-labs/web-interface-guidelines`), engineered for high-performance, accessible, and mathematically precise web applications.

---

## 1. Typography & Numerics
* **Tabular Numbers Mandatory (`tnum`)**:
  * Any text containing changing numbers, prices, timestamps, SHA-256 hashes, or file sizes MUST use:
    ```css
    font-feature-settings: 'tnum' 1;
    font-variant-numeric: tabular-nums;
    ```
  * *Why*: Monospaced digits prevent numbers from jumping left and right when values change, creating a calm, rock-solid interface.
* **Widow & Orphan Prevention**: Use non-breaking spaces (`&nbsp;`) before the last word of hero headlines and button labels to prevent awkward single-word lines.
* **Typographic Quotes**: Use real apostrophes (`&rsquo;` / `’`) and quotation marks (`&ldquo;` / `&rdquo;`), never plain ASCII dumb quotes (`"` or `'`) in body copy.

---

## 2. Layout Stability & Zero Layout Shift (CLS = 0.000)
* **Never cause layout jumps**:
  * Every image and video element must specify explicit width/height attributes or an aspect-ratio class (`aspect-video`, `aspect-square`).
  * Async content (modals, dropdowns, dynamic pricing) must have reserved layout containers with pre-allocated min-heights.
  * Use skeleton placeholders during any state transitions.

---

## 3. The 4 States of Every Component
Never build a component that only handles the "happy path". Every dynamic card and interactive tool must cleanly handle all 4 states:
1. **Loading / Processing**: Clear spinner or pulse animation with active hardware status indicator.
2. **Empty / Default**: Inviting dropzone or clean benchmark payload with 1-click sample loader.
3. **Error / Rejection**: Clear, friendly explanation of why the action failed, with an immediate 1-click retry path.
4. **Success**: High-contrast, unmistakable verification banner with cryptographic proof.

---

## 4. Accessibility & Keyboard Navigation (WCAG AAA)
* **Visible Focus Rings**: Every button, link, and input must feature a crisp, high-contrast focus ring:
  ```css
  focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-emerald-500 focus-visible:ring-offset-2 focus-visible:ring-offset-slate-950
  ```
* **Color Contrast**: Body copy must achieve at least 7:1 contrast ratio against the background (WCAG AAA standard).
* **Respect Motion Preferences**:
  ```css
  @media (prefers-reduced-motion: reduce) {
    *, ::before, ::after {
      animation-duration: 0.01ms !important;
      transition-duration: 0.01ms !important;
    }
  }
  ```

---

## 5. Interaction Hierarchy
* **Action Anchoring**: Place primary conversion actions (e.g., "Buy License") in the bottom-right corner of cards, where reading flow naturally concludes.
* **Destructive Separation**: Separate irreversible or sensitive actions from routine navigation.
* **Inline Help over Tooltips**: Place essential guidance directly inline as micro-copy, rather than hiding it behind hovering tooltips that fail on mobile touchscreens.
