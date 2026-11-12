---
name: anthropic-canvas
description: Anthropic's high-performance interactive HTML5 canvas design framework. Covers 60fps hardware-accelerated rendering, quantitative data visualization, mathematical curves, interactive physics, particle systems, and zero-dependency in-RAM execution.
---

# Anthropic Canvas: High-Performance Visual & Mathematical Computing

## Core Philosophy
Web visualizers should feel **alive, responsive, and hardware-accelerated**. Rather than importing heavy 500KB third-party graphic libraries, Anthropic Canvas builds lightweight, native HTML5 2D and WebGL engines with zero external network overhead.

---

## 1. The Zero-Lag 60fps Pipeline
* **Native `requestAnimationFrame` Loop**: Synchronize all drawing operations with the display refresh rate (60Hz / 120Hz ProMotion).
* **Frame Budget (<16.6ms)**: Keep all compute loops under 16 milliseconds per frame to guarantee zero dropped frames or stuttering.
* **Zero Garbage Collection**: Reuse vector and coordinate objects inside render loops. Never allocate new objects or arrays inside `render()` to prevent GC pauses.

---

## 2. High-DPI & Retina Sharpness
Always account for `window.devicePixelRatio` so lines, curves, and quantitative charts remain vector-sharp on Apple Retina and 4K displays:
```javascript
function resizeCanvas(canvas, ctx) {
  const dpr = window.devicePixelRatio || 1;
  const rect = canvas.getBoundingClientRect();
  canvas.width = rect.width * dpr;
  canvas.height = rect.height * dpr;
  ctx.scale(dpr, dpr);
}
```

---

## 3. Quantitative & Cryptographic Visualizers
* **Lattice Grids & Wave Fields**: Render mathematical coordinate planes with gentle velocity dampening that reacts subtly to mouse or finger trajectory.
* **Sub-Pixel Precision**: Use integer coordinates for crisp 1px borders and floating-point calculations for smooth fluid physics.
* **Battery & Power Awareness**: Pause the animation loop when the canvas scrolls out of view via `IntersectionObserver` to preserve user battery and CPU resources.

---

## 4. Tactile Air-Gap Proving Ground
* **In-Memory Rendering**: Every visual benchmark (such as RQL's WebP image compressor canvas or HashCheck generator) executes 100% in local client RAM.
* **Direct Export**: Use `canvas.toBlob()` or `canvas.toDataURL()` to allow users to export artifacts with zero server uploads.
