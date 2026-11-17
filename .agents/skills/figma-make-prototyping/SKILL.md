---
name: figma-make-prototyping
description: Master guide and workflows for Figma Make (figma.com/make) AI-native web development, Gemini 4 Carbon prompting, Code-to-Canvas layer extraction, React prototype modernization, and bridging Figma Make web apps with production codebases.
---

# Figma Make & AI React Modernization -- Engineering Codex
Comprehensive operating runbook for Figma Make (`figma.com/make`), Figma's next-generation AI full-stack development environment.

---

## 1. What is Figma Make?

Figma Make is not a traditional drawing board; it is an AI-powered, full-stack code and visual design sandbox:
1. **Live Code Container**: Executes real React, TypeScript, Tailwind CSS, and Vite in an isolated cloud runtime.
2. **AI Prompt Engine**: Powered by Gemini 4 Carbon with automatic file tree parsing, dependency resolution, and multi-file code editing.
3. **The "Open in Canvas" Bridge**: Converts live running React DOM trees into native, editable Figma Auto-Layout design frames, vector shapes, and component libraries.
4. **Instant Deployment**: Features a native `Publish` engine for hosting production-grade web prototypes directly from Figma.

---

## 2. The 3 Primary Views in Figma Make

| View | Purpose | Key Features |
| :--- | :--- | :--- |
| **Browser View** | Interactive Web Preview | Live clickable DOM, responsive viewport toggles, mobile drawer tests, tactile clicks. |
| **Files View** | Full Codebase Tree | Real `.jsx`, `.tsx`, `.css`, and package configs. Inspects component hierarchy and styling tokens. |
| **Canvas View** (`Open in canvas`) | Vector Design Board | Editable frames, typography scales, Figma components, and color variables. |

---

## 3. Calibrating AI Prompts (Gemini 4 Carbon Standard)

When prompting Figma Make through the bottom-left chat (`Ask for changes`):

### A. Aesthetic Definitions
- **Clean Editorial Light / Swiss Tech**: Crisp typography, high contrast, pure white and slate backgrounds, hairline borders, zero clutter. Ideal for executive briefs, technical documentation, and SaaS landing pages.
- **Obsidian Bastion / Terminal Dark**: Pure `#020617` slate, emerald `#10b981` signals, glowing borders, monospace metrics. Ideal for quantitative trading, cybersecurity, and air-gapped software hubs.

### B. Scope Definitions
- **Full React App Modernization**: Converts static multi-page HTML/JS into a single modular React component tree with client-side state, Lucide icons, and Tailwind utilities.
- **Targeted Component Sandbox**: Builds an isolated component (e.g. an interactive pricing slider, a 3D tilt card, or a live search palette).

### C. Exemplary Prompt Template
```text
aesthetic: Clean Editorial Light / Swiss Tech
scope: Full React App Modernization
rules:
- Maintain all 31 software suite entries, exact pricing, and Gumroad checkout links.
- Enforce rock-solid stability (zero wobbles or layout shifts on hover).
- Use Tailwind CSS with high-density Bento grids.
- Ensure 100% accessible contrast and mobile responsive navigation.
```

---

## 4. The Code-to-Canvas Workflow (`Open in canvas`)

1. Click **`Open in canvas`** (top right of Figma Make).
2. Figma exports the compiled React app into a standard Figma Design file (`figma.com/design/[fileKey]/...`).
3. The resulting frames use native **Figma Auto-Layout**:
   - Headers, cards, and buttons become reusable Figma Components.
   - Tailwind color classes become Figma Color Variables.
   - Font sizes and line heights map to Figma Text Styles.
4. Copy the resulting design URL and paste it into Antigravity for automated inspection via `get_design_context` and `use_figma`.

---

## 5. Bridging Figma Make Prototypes into Production

When an ideal prototype is generated in Figma Make:
1. Click the **`Files`** tab at the top.
2. Review the generated component code (e.g. `src/components/Hero.tsx`, `src/components/Catalog.tsx`).
3. Extract the high-value layout classes and markup.
4. Sanitize the code to match Rehan Quant Lab Sovereign Standards:
   - Verify 100% 7-bit ASCII compliance (0 non-ASCII bytes).
   - Ensure `CLS = 0.000` (no layout jumps).
   - Wire up local air-gapped scripts and MSME tax invoice calculations.
