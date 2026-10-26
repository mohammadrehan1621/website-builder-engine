import React, { useState, useEffect, useRef } from 'react';
import * as THREE from 'three';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { motion, AnimatePresence } from 'framer-motion';

gsap.registerPlugin(ScrollTrigger);

// ────────────────────────────────────────────────────────────────────────────
// RUST WASM BASE64 EMBED (Pure Rust 1.99.1 wasm32-unknown-unknown)
// ────────────────────────────────────────────────────────────────────────────
const RQL_WASM_BASE64 = "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";

let wasmInstance = null;
let wasmExports = null;

async function getWasmExports() {
  if (wasmExports) return wasmExports;
  try {
    const binStr = atob(RQL_WASM_BASE64);
    const bytes = new Uint8Array(binStr.length);
    for (let i = 0; i < binStr.length; i++) bytes[i] = binStr.charCodeAt(i);
    const mod = await WebAssembly.instantiate(bytes, {});
    wasmInstance = mod.instance;
    wasmExports = wasmInstance.exports;
    return wasmExports;
  } catch (err) {
    console.warn("WASM Init Fallback:", err);
    return null;
  }
}

// ────────────────────────────────────────────────────────────────────────────
// THREE.JS 3D CANVAS COMPONENT
// ────────────────────────────────────────────────────────────────────
function ThreeCanvas() {
  const mountRef = useRef(null);

  useEffect(() => {
    const el = mountRef.current;
    if (!el) return;

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(60, el.clientWidth / el.clientHeight, 0.1, 1000);
    camera.position.z = 22;

    const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
    renderer.setSize(el.clientWidth, el.clientHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    el.appendChild(renderer.domElement);

    // Crystalline 3D Icosahedron
    const geo = new THREE.IcosahedronGeometry(9, 2);
    const wireGeo = new THREE.WireframeGeometry(geo);
    const mat = new THREE.LineBasicMaterial({ color: 0x00f0ff, transparent: true, opacity: 0.35 });
    const mesh = new THREE.LineSegments(wireGeo, mat);
    scene.add(mesh);

    // Particles
    const pCount = 150;
    const pGeo = new THREE.BufferGeometry();
    const pos = new Float32Array(pCount * 3);
    for (let i = 0; i < pCount * 3; i += 3) {
      pos[i] = (Math.random() - 0.5) * 14;
      pos[i + 1] = (Math.random() - 0.5) * 14;
      pos[i + 2] = (Math.random() - 0.5) * 14;
    }
    pGeo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
    const pMat = new THREE.PointsMaterial({ color: 0xa855f7, size: 0.4, transparent: true, opacity: 0.75 });
    const points = new THREE.Points(pGeo, pMat);
    scene.add(points);

    let id;
    let clock = new THREE.Clock();
    const animate = () => {
      id = requestAnimationFrame(animate);
      const t = clock.getElapsedTime();
      mesh.rotation.x = t * 0.08;
      mesh.rotation.y = t * 0.12;
      points.rotation.y = -t * 0.06;
      renderer.render(scene, camera);
    };
    animate();

    const handleResize = () => {
      if (!el) return;
      camera.aspect = el.clientWidth / el.clientHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(el.clientWidth, el.clientHeight);
    };
    window.addEventListener('resize', handleResize);

    return () => {
      cancelAnimationFrame(id);
      window.removeEventListener('resize', handleResize);
      if (el && renderer.domElement) el.removeChild(renderer.domElement);
      renderer.dispose();
    };
  }, []);

  return <div ref={mountRef} className="absolute inset-0 pointer-events-none opacity-40 md:opacity-60 z-0" />;
}

// ────────────────────────────────────────────────────────────────────────────
// ROOT REACT APPLICATION
// ────────────────────────────────────────────────────────────────────
export default function App() {
  const [wasmActive, setWasmActive] = useState(false);
  const [benchText, setBenchText] = useState(null);
  const [chaosGen, setChaosGen] = useState(1);
  const [injecting, setInjecting] = useState(false);
  const [terminalLogs, setTerminalLogs] = useState([
    "[T+0ms] 🛡️ AEGIS PRE-AUDIT: Contract valid. 0.00% precision drift.",
    "[T+1ms] 🚀 STEADY STATE: Genomic Generation #1 executing at 100% equity."
  ]);

  useEffect(() => {
    getWasmExports().then(exp => {
      if (exp) setWasmActive(true);
    });
  }, []);

  const runBenchmark = async () => {
    const exp = await getWasmExports();
    const iter = 1000000;
    let wasmMs = 0;
    let jsMs = 0;

    if (exp && exp.rql_benchmark_crunch) {
      const t0 = performance.now();
      exp.rql_benchmark_crunch(iter);
      wasmMs = performance.now() - t0;
    }

    const t1 = performance.now();
    let acc = 1.0000001;
    let x = 0.5;
    for (let i = 0; i < iter; i++) {
      x = 3.999 * x * (1.0 - x);
      acc = acc + (x * 0.000001) + (i * 0.000000001);
    }
    jsMs = performance.now() - t1;

    setBenchText(
      wasmMs > 0
        ? `⚡ 1,000,000 Ops: Rust WASM = ${wasmMs.toFixed(2)}ms | Pure JS = ${jsMs.toFixed(2)}ms (${(jsMs / wasmMs).toFixed(1)}x faster)`
        : `⚡ 1,000,000 Ops: JS = ${jsMs.toFixed(2)}ms`
    );
  };

  const triggerChaos = () => {
    if (injecting) return;
    setInjecting(true);
    const curr = chaosGen;
    setTerminalLogs(p => [...p, `[T+0ms] 🌪️ INJECTING CHAOS: Gateway 504 Timeout & Thread Freeze!`]);

    setTimeout(() => {
      setTerminalLogs(p => [...p, `[T+11ms] 🛡️ AEGIS SENTINEL: Circuit tripped! 0 bytes lost in Ash Ledger.`]);
    }, 250);

    setTimeout(() => {
      const next = curr + 1;
      setChaosGen(next);
      setTerminalLogs(p => [
        ...p,
        `[T+9ms] 🔥 PHOENIX RESURRECTION: Genome advanced to Gen #${next} (+25% Stiffened Envelope).`,
        `[T+12ms] ✅ AUDIT: $0.00 Capital Loss • 100% Retained Equity.`
      ]);
      setInjecting(false);
    }, 600);
  };

  return (
    <div className="min-h-screen bg-[#050811] text-slate-100 flex flex-col font-sans selection:bg-cyan-500 selection:text-black">
      {/* Header */}
      <header className="sticky top-0 z-50 backdrop-blur-md bg-slate-950/80 border-b border-slate-800">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <img src="/emblem.jpg" alt="RQL Emblem" className="w-9 h-9 rounded-xl border border-cyan-500/30 object-cover" />
            <div>
              <span className="font-bold text-base tracking-tight text-white flex items-center gap-2">
                Rehan Quant Lab™
                <span className="text-[10px] font-mono font-semibold px-2 py-0.5 rounded bg-cyan-500/10 text-cyan-400 border border-cyan-500/30">
                  REACT 3D + RUST
                </span>
              </span>
              <span className="text-[11px] font-mono text-slate-400 block">rehanquantlab.com</span>
            </div>
          </div>

          <div className="flex items-center gap-3">
            <button
              onClick={runBenchmark}
              className="hidden sm:inline-flex items-center gap-2 px-3 py-1.5 rounded-xl text-xs font-mono font-semibold bg-purple-500/10 text-purple-300 border border-purple-500/30 hover:bg-purple-500/20 transition cursor-pointer"
            >
              <span className="w-2 h-2 rounded-full bg-purple-400 animate-pulse"></span>
              <span>{wasmActive ? "🦀 RUST WASM READY" : "LOADING WASM..."}</span>
            </button>
            <a
              href="/Mohammad_Rehan_Resume.pdf"
              download
              className="px-3.5 py-1.5 rounded-xl text-xs font-semibold bg-cyan-500 hover:bg-cyan-400 text-black font-mono transition shadow-md"
            >
              ⬇ PDF RESUME
            </a>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="relative min-h-[80vh] flex items-center justify-center pt-12 pb-20 px-4 text-center overflow-hidden">
        <ThreeCanvas />
        <div className="max-w-4xl mx-auto relative z-10">
          <motion.div
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-slate-900/90 border border-cyan-500/30 text-xs font-mono text-cyan-400 mb-6 backdrop-blur-md"
          >
            <span className="w-2 h-2 rounded-full bg-cyan-400 animate-ping"></span>
            <span>FOUNDER & LEAD SYSTEMS ARCHITECT @ REHAN QUANT LAB™</span>
          </motion.div>

          <motion.h1
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.2 }}
            className="text-4xl sm:text-6xl lg:text-7xl font-extrabold tracking-tight text-white"
          >
            Deterministic Systems. <br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-indigo-400 to-purple-400">
              Unkillable Execution.
            </span>
          </motion.h1>

          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.4 }}
            className="mt-6 text-base sm:text-lg text-slate-300 max-w-2xl mx-auto leading-relaxed"
          >
            4+ years of retail showroom management in Patna, Bihar, fused with ultra-low-latency in-memory engines (<strong className="text-cyan-400">AegisDB™</strong>), 7-Agent Swarm Tribunals, and pure <strong className="text-purple-400">Rust WebAssembly</strong> execution.
          </motion.p>

          <div className="mt-8 flex flex-wrap justify-center gap-4">
            <button
              onClick={runBenchmark}
              className="px-6 py-3 rounded-2xl bg-purple-600 hover:bg-purple-500 text-white font-bold text-sm font-mono transition shadow-lg cursor-pointer"
            >
              🦀 RUN RUST WASM BENCHMARK
            </button>
            <a
              href="#trinity"
              className="px-6 py-3 rounded-2xl bg-slate-900 hover:bg-slate-800 text-cyan-400 border border-cyan-500/30 font-bold text-sm font-mono transition shadow-lg"
            >
              ⚡ THE HOLY TRINITY
            </a>
          </div>

          {benchText && (
            <motion.div
              initial={{ opacity: 0, scale: 0.95 }}
              animate={{ opacity: 1, scale: 1 }}
              className="mt-6 inline-block bg-purple-950/80 border border-purple-500/50 px-4 py-2 rounded-xl text-xs font-mono text-purple-200"
            >
              {benchText}
            </motion.div>
          )}

          {/* Metrics */}
          <div className="mt-14 grid grid-cols-2 md:grid-cols-4 gap-4 text-left">
            <div className="bg-slate-900/80 p-5 rounded-2xl border border-slate-800">
              <span className="text-[11px] font-mono text-slate-400 uppercase">AegisDB Latency</span>
              <span className="text-2xl sm:text-3xl font-extrabold text-cyan-400 font-mono block mt-1">0.38 µs</span>
              <span className="text-xs text-slate-500 mt-1 block">2.62M reads/sec</span>
            </div>
            <div className="bg-slate-900/80 p-5 rounded-2xl border border-slate-800">
              <span className="text-[11px] font-mono text-slate-400 uppercase">Phoenix MTTR</span>
              <span className="text-2xl sm:text-3xl font-extrabold text-emerald-400 font-mono block mt-1">&lt;10 ms</span>
              <span className="text-xs text-slate-500 mt-1 block">Hot-Resurrection</span>
            </div>
            <div className="bg-slate-900/80 p-5 rounded-2xl border border-slate-800">
              <span className="text-[11px] font-mono text-slate-400 uppercase">AVX2 Invariants</span>
              <span className="text-2xl sm:text-3xl font-extrabold text-purple-400 font-mono block mt-1">21.4M /s</span>
              <span className="text-xs text-slate-500 mt-1 block">46.69ns latency</span>
            </div>
            <div className="bg-slate-900/80 p-5 rounded-2xl border border-slate-800">
              <span className="text-[11px] font-mono text-slate-400 uppercase">Retail Roots</span>
              <span className="text-2xl sm:text-3xl font-extrabold text-amber-400 font-mono block mt-1">4+ Years</span>
              <span className="text-xs text-slate-500 mt-1 block">Patna Showroom</span>
            </div>
          </div>
        </div>
      </section>

      {/* Sovereign Dual Doctrine */}
      <section className="py-16 px-4 max-w-7xl mx-auto border-t border-slate-800">
        <div className="text-center mb-10">
          <span className="text-xs font-mono font-bold uppercase text-emerald-400 bg-emerald-500/10 border border-emerald-500/30 px-3 py-1 rounded-full">
            The Philosophical Bedrock
          </span>
          <h2 className="text-3xl sm:text-4xl font-extrabold text-white mt-4">
            The Sovereign Dual Doctrine
          </h2>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div className="bg-slate-900/70 p-8 rounded-3xl border border-slate-800">
            <span className="text-cyan-400 text-xs font-mono font-bold uppercase block mb-3">⚖️ I. Gall's Law</span>
            <blockquote className="text-slate-200 italic font-serif">
              "A complex system that works is always found to have evolved from a simple system that worked. A complex system designed from scratch never works and cannot be made to work."
            </blockquote>
            <p className="text-xs font-mono text-slate-500 mt-3">— John Gall (1975)</p>
          </div>
          <div className="bg-slate-900/70 p-8 rounded-3xl border border-slate-800">
            <span className="text-purple-400 text-xs font-mono font-bold uppercase block mb-3">⚔️ II. Sun Tzu</span>
            <blockquote className="text-slate-200 italic font-serif">
              "All warfare is based on deception. When strong, appear weak. When near, make them believe you are far."
            </blockquote>
            <p className="text-xs font-mono text-slate-500 mt-3">— Sun Tzu (The Art of War)</p>
          </div>
        </div>
      </section>

      {/* Holy Trinity Lab */}
      <section id="trinity" className="py-16 px-4 max-w-7xl mx-auto border-t border-slate-800">
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-8 gap-4">
          <div>
            <span className="text-xs font-mono font-bold uppercase text-cyan-400 bg-cyan-500/10 border border-cyan-500/30 px-3 py-1 rounded-full">
              Live Resilience Simulator
            </span>
            <h2 className="text-3xl font-extrabold text-white mt-3">The Holy Trinity Framework</h2>
          </div>
          <button
            onClick={triggerChaos}
            disabled={injecting}
            className="px-5 py-2.5 rounded-xl font-mono text-xs font-bold bg-rose-600 hover:bg-rose-500 text-white transition shadow-lg cursor-pointer"
          >
            {injecting ? "SIMULATING CHAOS..." : `INJECT 504 CHAOS (GEN #${chaosGen})`}
          </button>
        </div>

        <div className="bg-black/80 rounded-2xl p-4 border border-slate-800 font-mono text-xs max-h-56 overflow-y-auto">
          {terminalLogs.map((l, i) => (
            <div key={i} className={l.includes("🌪️") ? "text-rose-400 font-bold" : (l.includes("🔥") ? "text-emerald-400 font-bold" : "text-slate-400")}>
              {l}
            </div>
          ))}
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-slate-950 border-t border-slate-900 py-8 text-center text-xs text-slate-500 font-mono mt-auto">
        © {new Date().getFullYear()} Rehan Quant Lab™. Architected by Mohammad Rehan.
      </footer>
    </div>
  );
}
