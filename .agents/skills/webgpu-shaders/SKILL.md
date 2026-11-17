---
name: webgpu-shaders
description: Comprehensive engineering codex for declarative WebGPU shaders, components, and effects from shaders.com (shader-effects-inc/shaders). Covers WebGPU canvas architecture, layered shader composition, React/Vue/Svelte/Vanilla JS integration, CLI workflows (npx shaders add), and graceful WebGPU hardware fallbacks.
---

# WebGPU Shaders & Effects -- Production Engineering Codex
Developed by Shader Effects Inc (`shader-effects-inc/shaders` / `shaders.com`).
High-performance, declarative WebGPU shader components for modern web applications.

---

## 1. What is WebGPU Shaders?

WebGPU is the modern successor to WebGL, offering lower overhead, direct GPU hardware compute access, and predictable 60-120fps graphics performance.
`shader-effects-inc/shaders` makes raw WGSL (WebGPU Shading Language) accessible through clean, declarative components:
1. **Declarative Layering**: The parent `<Shader>` component initializes the GPU device and render pipeline. Child components (`<Satin>`, `<MeshGradient>`, `<Noise>`, `<Waves>`) act as composited render passes.
2. **Zero Boilerplate**: No manual buffer allocation, uniform binding, or pipeline layout authoring required.
3. **Multi-Framework**: Native packages for React, Vue, Svelte, Solid, Vanilla JS, and Framer.
4. **Agent & CLI First**: Built with an official agent skill, MCP integration, and CLI commands (`npx shaders add`).

---

## 2. CLI Installation & Component Scaffolding

### CLI Guided Flow
```bash
# Interactive guided CLI
npx shaders add

# Install specific shader layer
npx shaders add satin
npx shaders add mesh-gradient
npx shaders add noise
npx shaders add liquid
```

### Package Installation
```bash
npm install @shaders/react
# or
npm install @shaders/core
```

---

## 3. Core React Integration Pattern

```tsx
'use client';

import { Shader, MeshGradient, Noise, Vignette } from '@shaders/react';
import { useState, useEffect } from 'react';

export function SovereignHeroBackdrop() {
  const [hasWebGPU, setHasWebGPU] = useState(true);

  useEffect(() => {
    // Graceful feature detection
    if (!navigator.gpu) {
      setHasWebGPU(false);
    }
  }, []);

  // Graceful CSS Fallback for older devices without WebGPU
  if (!hasWebGPU) {
    return (
      <div className="absolute inset-0 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 pointer-events-none" />
    );
  }

  return (
    <div className="absolute inset-0 overflow-hidden pointer-events-none z-0">
      <Shader
        className="w-full h-full"
        devicePixelRatio={Math.min(window.devicePixelRatio || 1, 2)}
      >
        {/* Layer 1: Base Sovereign Obsidian & Emerald Gradient */}
        <MeshGradient
          colors={['#020617', '#064e3b', '#020617', '#0f172a']}
          speed={0.4}
          distortion={0.3}
        />

        {/* Layer 2: Subtle Micro-Noise Texture */}
        <Noise
          opacity={0.06}
          scale={1.5}
        />

        {/* Layer 3: Edge Vignette */}
        <Vignette
          darkness={0.8}
          offset={0.4}
        />
      </Shader>
    </div>
  );
}
```

---

## 4. Vanilla JavaScript / Zero-Build WebGPU Integration

For static production websites (like `rehanquantlab.com`):
```html
<canvas id="webgpu-canvas" class="w-full h-full absolute inset-0 pointer-events-none"></canvas>

<script type="module">
  async function initWebGPUShader() {
    if (!navigator.gpu) {
      console.info('[WebGPU] Hardware WebGPU not supported on this browser; using static CSS background.');
      return;
    }

    const adapter = await navigator.gpu.requestAdapter();
    if (!adapter) return;

    const device = await adapter.requestDevice();
    const canvas = document.getElementById('webgpu-canvas');
    const context = canvas.getContext('webgpu');
    const presentationFormat = navigator.gpu.getPreferredCanvasFormat();

    context.configure({
      device: device,
      format: presentationFormat,
      alphaMode: 'premultiplied'
    });

    // Lifecycle: Pause rendering when scrolled out of view
    let isRendering = true;
    const observer = new IntersectionObserver(([entry]) => {
      isRendering = entry.isIntersecting;
    });
    observer.observe(canvas);

    // Render loop driven by requestAnimationFrame
    function frame() {
      if (isRendering) {
        const commandEncoder = device.createCommandEncoder();
        const textureView = context.getCurrentTexture().createView();

        const renderPassDescriptor = {
          colorAttachments: [{
            view: textureView,
            clearValue: { r: 0.008, g: 0.024, b: 0.09, a: 1.0 },
            loadOp: 'clear',
            storeOp: 'store'
          }]
        };

        const passEncoder = commandEncoder.beginRenderPass(renderPassDescriptor);
        passEncoder.end();
        device.queue.submit([commandEncoder.finish()]);
      }
      requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initWebGPUShader);
  } else {
    initWebGPUShader();
  }
</script>
```

---

## 5. Performance Invariants & Sovereign Guidelines

1. **Hardware Detection Invariant**: Always check `if (!navigator.gpu)` before requesting an adapter. Fall back immediately to a static CSS linear-gradient to ensure zero console errors.
2. **IntersectionObserver Pause**: Always freeze the GPU render loop when the canvas is scrolled out of view or the tab is hidden (`visibilitychange`).
3. **Device Pixel Ratio Clamping**: Never set `devicePixelRatio > 2.0`. On 3x/4x high-density Retina screens, rendering full resolution on the GPU wastes battery and drops frames with zero perceptible visual gain.
4. **Color Discipline**: Enforce Rehan Quant Lab's Obsidian (`#020617`) and Sovereign Emerald (`#10b981`) color codes. Avoid hyper-saturated rainbow spectrums.
5. **100% 7-Bit ASCII Compliance**: All component strings, WGSL shaders, and script tags must contain 0 non-ASCII bytes.
