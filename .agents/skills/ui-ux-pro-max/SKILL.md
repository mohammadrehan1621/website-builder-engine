---
name: ui-ux-pro-max
description: Next Level Builder UI/UX Pro Max design intelligence engine. Provides design system generation, Bento Grid layouts, modern dark-mode palettes, glassmorphism, micro-interactions, responsive ergonomics, and accessibility guardrails for production web interfaces.
---

# UI/UX Pro Max: Design Intelligence & System Engine

## Overview
UI/UX Pro Max provides an institutional design system engine that turns complex technical software into intuitive, visually breathtaking, and ergonomic web applications.

---

## 1. Design Tokens & System Standards

### Spacing & Layout Rhythm
* **Base Unit**: 4px grid.
* **Component Padding**: `px-4 py-2.5` (compact buttons), `p-5` (standard cards), `p-8` (featured bento hero cards).
* **Grid Gaps**: `gap-4` (compact items), `gap-6` (standard bento grids), `gap-8` (major page sections).

### Typography Hierarchy (Inter + JetBrains Mono)
* **Hero Display**: `text-4xl sm:text-5xl lg:text-6xl font-black font-heading tracking-tight leading-[1.1]`
* **Section Header**: `text-2xl sm:text-3xl font-extrabold font-heading text-white`
* **Card Title**: `text-lg sm:text-xl font-bold font-heading text-slate-100`
* **Body / Description**: `text-xs sm:text-sm text-slate-400 leading-relaxed font-sans`
* **Telemetry & Tags**: `text-[10px] sm:text-[11px] font-mono tracking-wide uppercase`

### Dark Palette Tokens
* **Canvas Void**: `#06090e`
* **Obsidian Surface**: `#0b111b`
* **Elevated Card**: `bg-slate-900/80 backdrop-blur-md`
* **Subtle Border**: `border border-slate-800/80 hover:border-slate-700`
* **Active Glow**: `ring-1 ring-emerald-500/30 shadow-lg shadow-emerald-950/20`

---

## 2. Bento Grid Architecture
Bento Grids create structured visual harmony for complex toolkits:
* **The Hero Anchor (Col-span 2 / Row-span 2)**: Highlights the primary flagship or interactive demo.
* **Metric Cards (Col-span 1)**: Display high-impact numbers (<1ms latency, 100% offline, ₹0/mo).
* **Live Sandbox (Full width)**: Houses tactile interactive tests with zero external dependency.
* **Quick-Spec Cards**: Dense, scannable lists of technical attributes with verified green badges.

---

## 3. Human Ergonomics & UX Laws
* **Fitts's Law (Touch Targets)**: Every interactive button, toggle, and link has a minimum clickable area of 44x44px on mobile devices.
* **Hick's Law (Decision Simplicity)**: Every card has exactly ONE primary action ("Buy on Gumroad" or "Direct UPI Desk") and one subtle secondary action ("View Specs & Specs"). Never overwhelm users with competing primary buttons.
* **Jakob's Law (Predictability)**: Essential controls (navbars, currency toggles, modals, close buttons) reside in universally recognized locations.

---

## 4. Tactile Micro-Interactions
* **Interactive Hover Lifts**: Cards subtly lift on hover (`hover:-translate-y-1 hover:shadow-xl transition-all duration-300`).
* **Instant Button Depress**: `active:scale-[0.98]` gives the sensation of a physical mechanical keycap.
* **Status Badges**: Pulsing green dots (`animate-pulse`) signal live air-gap status or verified verification.
* **Clipboard Copy Feedback**: Instant transformation to green checkmark (`Copied!`) with 1500ms auto-revert.
