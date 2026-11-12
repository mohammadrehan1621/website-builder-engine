---
name: anthropic-frontend
description: Anthropic's official frontend design patterns and artifact engineering guidelines. Enforces intentional whitespace, semantic typography, refusal of AI clichés (floating purple blobs, low-contrast text), purpose-driven UI hierarchies, and crisp component modularity.
---

# Anthropic Frontend Design Patterns

## Core Philosophy
Anthropic's design standards emphasize **extreme clarity, high conviction, and the total rejection of AI design tropes**. Software should look like it was designed by a world-class human engineer who respects the user's intelligence and time.

---

## 1. The Anti-Trope Mandates (Zero AI Clichés)
* **No Cliché Purple Gradients**: Never default to purple/violet/pink neon glows. Colors must have functional meaning (emerald = verified/active, amber = performance, sky = cryptographic, slate = neutral structure).
* **No Floating Unanchored Cards**: Every card must belong to an intentional spatial grid with structural borders, not arbitrary dropshadows floating in white space.
* **No Centered Wall-of-Text**: Left-align technical copy, descriptions, and lists. Center only high-impact single-concept hero titles.
* **No Marketing Fluff**: Replace vague buzzwords ("Next-Gen", "Revolutionary", "Seamless") with concrete engineering claims ("Sub-1ms pure Rust kernel", "100% offline air-gapped memory", "Zero cloud telemetry").

---

## 2. Typography & Reading Gravity
* **Optimal Line Length**: Restrict body paragraphs to 60–75 characters per line (`max-w-2xl` to `max-w-3xl`) for effortless scanning.
* **Typographic Hierarchy**:
  * Hero Title: High-density sans display with tight tracking (`tracking-tight`).
  * Section Headers: Clear uppercase mono category tags above bold titles.
  * Technical Specs: Monospace tabular numerals for all metrics, hashes, and dates.
* **True Contrast**: Body copy must always meet WCAG AAA contrast ratios. Never use washed-out grey text on dark backgrounds.

---

## 3. Component Modularity & Ergonomics
* **Purpose-Driven Layouts**: Every screen element must serve one of three purposes: *Informing*, *Demonstrating*, or *Converting*. If an element does none of these, delete it.
* **Instant Visual Affirmation**: Every interactive action (copying a hash, switching a tab, downloading a manifest) must provide immediate, unmistakable tactile feedback (e.g., checkmark swap, color pulse).
* **Progressive Disclosure**: Show essential specifications upfront; tuck deep architectural whitepapers and 26-suite specifications behind seamless modals or tabs.
