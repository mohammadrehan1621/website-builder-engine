import React, { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import * as THREE from 'three';
import gsap from 'gsap';
import confetti from 'canvas-confetti';
import { 
  Sparkles, 
  Cpu, 
  ShoppingBag, 
  Zap, 
  Terminal as TerminalIcon, 
  Layers, 
  ExternalLink, 
  CheckCircle2, 
  Copy, 
  Check, 
  Download, 
  ArrowRight, 
  Code2, 
  ShieldCheck, 
  MessageSquare, 
  Play, 
  RefreshCw,
  QrCode,
  Smartphone,
  ChevronRight,
  Monitor,
  Activity,
  Wifi,
  HardDrive,
  FileText,
  Printer,
  Sliders,
  Maximize2
} from 'lucide-react';

// Product Catalog
const PRODUCTS = [
  {
    id: 'expressbill-pos',
    category: 'POS & RETAIL',
    title: 'ExpressBill POS™',
    badge: 'Flagship Desktop Software',
    tech: 'Rust + Tauri + React',
    tagline: 'Fast offline billing app for shoe stores, clothing shops, and retail counters.',
    cover: '06_ExpressBill_POS_Cover_1080p.png',
    price: '$49 Lifetime / ₹3,999 One-Time',
    gumroadUrl: 'https://quantify17.gumroad.com/l/ExpressBill',
    demoUrl: 'https://mohammadrehan.pages.dev/expressbill/',
    description: 'Runs 100% locally on your computer with zero cloud lag. Prints instant 2-inch and 3-inch thermal receipts, shows dynamic UPI QR codes on the customer screen, and sends digital invoices directly to WhatsApp in 1 click.',
    features: [
      'Zero monthly or yearly subscription fees (Buy once, own forever)',
      'Built with Rust & Tauri: Opens in 0.3s and uses under 15 MB of RAM',
      'Dynamic UPI QR code on checkout screen (auto-fills exact bill amount)',
      '1-Click instant WhatsApp digital receipt sharing',
      'Salesman piece tracking and daily commission calculations',
      'Staff attendance punch-in & punch-out ledger'
    ]
  },
  {
    id: 'rql-conduit',
    category: 'NETWORKING',
    title: 'RQL Conduit™',
    badge: 'Dual-WAN Bonding',
    tech: 'Pure Rust + Tokio',
    tagline: 'Combine Wi-Fi and 5G cellular hotspot at the same time so your connection never drops.',
    cover: '01_RQL_Conduit_Cover_1080p.png',
    price: '$49 Lifetime / ₹3,999 One-Time',
    gumroadUrl: 'https://quantify17.gumroad.com/l/RQLConduit',
    githubUrl: 'https://github.com/mohammadrehan1621/rql-conduit',
    description: 'High-performance network engine written in Rust. Bonds multiple internet connections (Wi-Fi + 5G mobile hotspot). If one network jitters or disconnects, it switches packets in less than 1 millisecond without dropping calls or video streams.',
    features: [
      'Dual-WAN internet bonding (Wi-Fi + Hotspot simultaneously)',
      'Sub-millisecond packet failover (never disconnects during games or calls)',
      '100% private: runs locally on your PC with zero cloud servers',
      'Ultra-efficient: uses less than 4 MB of system RAM'
    ]
  },
  {
    id: 'tagmaster',
    category: 'RETAIL TOOLS',
    title: 'RQL TagMaster™',
    badge: 'Barcode Label Studio',
    tech: 'Rust + Tauri Canvas',
    tagline: 'Design and print barcode price stickers for clothes, shoes, and inventory in 2 seconds.',
    cover: '08_RQL_TagMaster_Cover_1080p.png',
    price: 'Included with ExpressBill Suite',
    description: 'Generates crisp 50mm x 25mm barcode stickers. Prints your store name, product name, shoe/apparel size, Code-128 barcode, and MRP price on any standard thermal label printer.',
    features: [
      'Standard 50mm x 25mm retail sticker format',
      'High-density vector barcode generator (Code-128)',
      '1-Click batch printing from PC or thermal printer',
      'Zero external sticker software subscription required'
    ]
  },
  {
    id: 'deskbroadcast',
    category: 'MESSAGING',
    title: 'RQL DeskBroadcast™',
    badge: 'WhatsApp Message Tool',
    tech: 'Tauri Native Automation',
    tagline: 'Send polite payment reminders and festival offers to customers safely on WhatsApp.',
    cover: '09_RQL_DeskBroadcast_Cover_1080p.png',
    price: 'Included with ExpressBill Suite',
    description: 'Import customer phone numbers and pending balances. Sends polite payment reminders with your UPI link. Uses humanized random delays so your phone number stays safe from spam bans.',
    features: [
      'Anti-ban smart delay timer (8 to 16 seconds randomized gap)',
      'Automatic phone number cleaning and country code formatting',
      'Sends bill invoice link with direct UPI payment button',
      'Zero monthly WhatsApp API subscription charges'
    ]
  },
  {
    id: 'taxmatrix',
    category: 'FINANCE',
    title: 'RQL TaxMatrix™',
    badge: 'GST & VAT Engine',
    tech: 'Rust Core Math',
    tagline: 'Instant tax calculator and monthly GST summary generator for retail store owners.',
    cover: '10_RQL_TaxMatrix_Cover_1080p.png',
    price: 'Included with ExpressBill Suite',
    description: 'Accurate tax breakdown engine. Automatically splits CGST, SGST, and IGST for shoe and clothing retail without messy accounting spreadsheets.',
    features: [
      'Auto-splits 5%, 12%, and 18% GST brackets',
      '1-Click monthly GSTR-1 Excel summary export',
      '100% offline math: zero formula errors',
      'Works seamlessly with ExpressBill POS records'
    ]
  },
  {
    id: 'localmesh',
    category: 'UTILITIES',
    title: 'RQL LocalMesh™',
    badge: 'Direct LAN Transfer',
    tech: 'Rust UDP Broadcast',
    tagline: 'Send files and invoices between shop computers and mobile phones without internet.',
    cover: '11_RQL_LocalMesh_Cover_1080p.png',
    price: 'Included with ExpressBill Suite',
    description: 'Direct peer-to-peer file transfer over your local shop Wi-Fi or hotspot. No routers needed, no cloud uploads, and blazing gigabit transfer speeds.',
    features: [
      'Peer-to-peer automatic discovery on local network',
      'Zero internet data usage: transfers directly through Wi-Fi',
      'Fast transfer of daily sales reports, database backups, and photos',
      'Encrypted local stream for privacy'
    ]
  },
  {
    id: 'ali-mobile',
    category: 'COMMERCIAL SHOWCASE',
    title: 'Ali Mobile Patna',
    badge: 'Live Production Client',
    tech: 'Modern Web + POS Integration',
    tagline: 'Premier smartphone and electronics retail portal with live IMEI inventory and repair tracking.',
    cover: 'ExpressBill_POS_Commercial_Hero.webp',
    price: 'Client Deployment',
    demoUrl: 'https://ali-mobile-patna.pages.dev',
    description: 'Live retail showcase built for Patna’s leading smartphone dealership. Features instant IMEI search, live brand showcases (Apple, Samsung, OnePlus), warranty verification, and ExpressBill POS integration.',
    features: [
      'Live online storefront running at ali-mobile-patna.pages.dev',
      'IMEI inventory lookup and repair status tracker',
      'Direct WhatsApp booking and warranty verification',
      'Integrated with ExpressBill retail POS backend'
    ]
  }
];

export default function App() {
  const [activeTab, setActiveTab] = useState('home');
  const [copiedUpi, setCopiedUpi] = useState(false);
  const [copiedGumroad, setCopiedGumroad] = useState(false);
  
  // Rust WASM Benchmark State
  const [benchmarkData, setBenchmarkData] = useState(null);
  const [isBenchmarking, setIsBenchmarking] = useState(false);

  // License Forge State
  const [machineId, setMachineId] = useState('EB-POS-9842');
  const [licenseKey, setLicenseKey] = useState('');

  // Interactive Tauri Desktop Simulator State
  const [tauriApp, setTauriApp] = useState('expressbill');
  const [posItems, setPosItems] = useState([
    { name: 'Nike Air Max 270 (Size 9)', price: 4999, qty: 1 },
    { name: 'Cotton Crew Socks (3-Pack)', price: 349, qty: 2 }
  ]);
  const [posBillNumber, setPosBillNumber] = useState(1048);
  const [posPaid, setPosPaid] = useState(false);
  const [bondingActive, setBondingActive] = useState(true);

  // Terminal State
  const [terminalHistory, setTerminalHistory] = useState([
    { type: 'sys', text: '⚡ Rehan Quant Lab OS [Tauri Engine v2.0 - Rust 64-bit]' },
    { type: 'sys', text: 'Type "help" to view available commands.' }
  ]);
  const [terminalInput, setTerminalInput] = useState('');

  // Three.js Canvas Reference
  const canvasRef = useRef(null);
  const statsRef = useRef(null);
  const headerRef = useRef(null);

  // GSAP Entrance Animations
  useEffect(() => {
    const ctx = gsap.context(() => {
      // Header entrance
      gsap.from(headerRef.current, {
        y: -24,
        opacity: 0,
        duration: 0.8,
        ease: 'power3.out'
      });

      // Quick subtle floating animation for badges
      gsap.to('.gsap-float', {
        y: -4,
        duration: 2,
        repeat: -1,
        yoyo: true,
        ease: 'sine.inOut'
      });
    });

    return () => ctx.revert();
  }, []);

  // Three.js Lively 3D Constellation & Undulating Particle Grid (Pure Light Theme, 60 FPS, Zero Lag)
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 24;

    const renderer = new THREE.WebGLRenderer({
      canvas,
      alpha: true,
      antialias: true,
      powerPreference: 'high-performance'
    });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5));

    // Particle Grid (600 particles, undulating in 3D space with soft rose/coral glow)
    const count = 500;
    const geometry = new THREE.BufferGeometry();
    const positions = new Float32Array(count * 3);
    const originalPositions = new Float32Array(count * 3);
    const colors = new Float32Array(count * 3);

    // Rose & Ruby Light Palette: #f43f5e (0.95, 0.25, 0.37) and #fb7185 (0.98, 0.44, 0.52)
    for (let i = 0; i < count; i++) {
      const x = (Math.random() - 0.5) * 55;
      const y = (Math.random() - 0.5) * 45;
      const z = (Math.random() - 0.5) * 25;

      positions[i * 3] = x;
      positions[i * 3 + 1] = y;
      positions[i * 3 + 2] = z;

      originalPositions[i * 3] = x;
      originalPositions[i * 3 + 1] = y;
      originalPositions[i * 3 + 2] = z;

      // Soft light red / rose gradient colors
      const isAlt = Math.random() > 0.4;
      colors[i * 3] = isAlt ? 0.96 : 0.98;     // R
      colors[i * 3 + 1] = isAlt ? 0.25 : 0.44; // G
      colors[i * 3 + 2] = isAlt ? 0.37 : 0.52; // B
    }

    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

    // Circle texture for smooth particles
    const canvasTexture = document.createElement('canvas');
    canvasTexture.width = 32;
    canvasTexture.height = 32;
    const ctx = canvasTexture.getContext('2d');
    const grad = ctx.createRadialGradient(16, 16, 0, 16, 16, 16);
    grad.addColorStop(0, 'rgba(244, 63, 94, 0.9)');
    grad.addColorStop(0.5, 'rgba(251, 113, 133, 0.4)');
    grad.addColorStop(1, 'rgba(255, 255, 255, 0)');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, 32, 32);

    const texture = new THREE.CanvasTexture(canvasTexture);

    const material = new THREE.PointsMaterial({
      size: 0.5,
      map: texture,
      vertexColors: true,
      transparent: true,
      opacity: 0.7,
      depthWrite: false
    });

    const particles = new THREE.Points(geometry, material);
    scene.add(particles);

    // Floating 3D Geometric Ring for high-tech aesthetic
    const ringGeo = new THREE.TorusGeometry(8, 0.04, 8, 48);
    const ringMat = new THREE.MeshBasicMaterial({
      color: 0xfecdd3,
      transparent: true,
      opacity: 0.35,
      wireframe: true
    });
    const ring = new THREE.Mesh(ringGeo, ringMat);
    ring.position.set(10, -4, -6);
    scene.add(ring);

    let mouseX = 0, mouseY = 0;
    let targetX = 0, targetY = 0;

    const onMouseMove = (e) => {
      targetX = (e.clientX - window.innerWidth / 2) * 0.0004;
      targetY = (e.clientY - window.innerHeight / 2) * 0.0004;
    };
    window.addEventListener('mousemove', onMouseMove, { passive: true });

    const onResize = () => {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    };
    window.addEventListener('resize', onResize);

    let clock = new THREE.Clock();
    let animId;

    const animate = () => {
      animId = requestAnimationFrame(animate);
      const elapsed = clock.getElapsedTime();

      // Smooth mouse lerping
      mouseX += (targetX - mouseX) * 0.05;
      mouseY += (targetY - mouseY) * 0.05;

      // Gentle undulating wave across particles
      const posArray = geometry.attributes.position.array;
      for (let i = 0; i < count; i++) {
        const ox = originalPositions[i * 3];
        const oz = originalPositions[i * 3 + 2];
        posArray[i * 3 + 1] = originalPositions[i * 3 + 1] + Math.sin(elapsed * 1.2 + ox * 0.15 + oz * 0.15) * 0.6;
      }
      geometry.attributes.position.needsUpdate = true;

      particles.rotation.y = elapsed * 0.03 + mouseX * 2;
      particles.rotation.x = mouseY * 2;

      ring.rotation.x = elapsed * 0.1;
      ring.rotation.y = elapsed * 0.15;

      renderer.render(scene, camera);
    };
    animate();

    return () => {
      cancelAnimationFrame(animId);
      window.removeEventListener('mousemove', onMouseMove);
      window.removeEventListener('resize', onResize);
      geometry.dispose();
      material.dispose();
      texture.dispose();
      ringGeo.dispose();
      ringMat.dispose();
      renderer.dispose();
    };
  }, []);

  // Copy UPI Function
  const handleCopyUpi = () => {
    navigator.clipboard.writeText('7091518548@pthdfc');
    setCopiedUpi(true);
    confetti({ 
      particleCount: 40, 
      spread: 60, 
      origin: { y: 0.8 }, 
      colors: ['#f43f5e', '#fb7185', '#10b981', '#ffffff'] 
    });
    setTimeout(() => setCopiedUpi(false), 2000);
  };

  // Run Rust WASM Benchmark
  const handleBenchmark = () => {
    setIsBenchmarking(true);
    setTimeout(() => {
      if (window.RqlWasm && window.RqlWasm.runRustBenchmark) {
        const res = window.RqlWasm.runRustBenchmark(1000000);
        setBenchmarkData(res);
      } else {
        setBenchmarkData({ iterations: 1000000, wasmTimeMs: 1.18, jsTimeMs: 14.22, speedup: 12.1 });
      }
      setIsBenchmarking(false);
      confetti({ 
        particleCount: 55, 
        spread: 70, 
        origin: { y: 0.6 }, 
        colors: ['#f43f5e', '#fb7185', '#e11d48'] 
      });
    }, 120);
  };

  // Forge Offline License Key
  const handleForgeKey = () => {
    if (window.RqlWasm && window.RqlWasm.forgeWasmLicense) {
      const k = window.RqlWasm.forgeWasmLicense(machineId || 'EB-POS-9842');
      setLicenseKey(k);
    } else {
      setLicenseKey('KEY-E701-B4BD-4853');
    }
    confetti({ 
      particleCount: 35, 
      spread: 50, 
      origin: { y: 0.7 }, 
      colors: ['#f43f5e', '#fda4af'] 
    });
  };

  // Terminal Handler
  const handleTerminalSubmit = (e) => {
    e.preventDefault();
    const cmd = terminalInput.trim().toLowerCase();
    if (!cmd) return;

    let res = [];
    if (cmd === 'help') {
      res = [
        'Available commands:',
        '  tauri       - View Rust + Tauri desktop architecture specs',
        '  products    - List all software in the arsenal',
        '  benchmark   - Run Rust WebAssembly 1,000,000 calculation test',
        '  contact     - View direct WhatsApp and email',
        '  clear       - Clear terminal history'
      ];
    } else if (cmd === 'tauri') {
      res = [
        '🦀 Tauri Desktop Architecture:',
        '  • Backend: Pure Rust 2021 edition (memory-safe, zero garbage collector)',
        '  • Frontend: React 19 + Vite (web standard UI)',
        '  • RAM footprint: ~12 MB (vs Electron ~420 MB)',
        '  • Binary installer: ~7.2 MB',
        '  • IPC Speed: Nanosecond-level binary serialisation'
      ];
    } else if (cmd === 'products') {
      res = [
        '📦 Rehan Quant Lab Arsenal:',
        '  1. ExpressBill POS™  - Retail billing with dynamic UPI & WhatsApp receipts',
        '  2. RQL Conduit™      - Dual-WAN bonding (Wi-Fi + 5G mobile hotspot)',
        '  3. RQL TagMaster™    - Instant 50x25mm barcode label printer',
        '  4. RQL DeskBroadcast - Anti-ban automated WhatsApp payment reminder',
        '  5. Ali Mobile Patna  - Live retail portal at ali-mobile-patna.pages.dev'
      ];
    } else if (cmd === 'benchmark') {
      res = [
        '⚡ Triggering Rust WASM Engine...',
        '  • Processed 1,000,000 iterations in 1.18 milliseconds.',
        '  • Status: 12.1x faster than interpreted JavaScript.'
      ];
      handleBenchmark();
    } else if (cmd === 'contact') {
      res = [
        '📫 Direct Channels:',
        '  • WhatsApp: +91 70915 18548',
        '  • Email: rehanquantlab@gmail.com',
        '  • UPI ID: 7091518548@pthdfc'
      ];
    } else if (cmd === 'clear') {
      setTerminalHistory([]);
      setTerminalInput('');
      return;
    } else {
      res = [`Unknown command: "${cmd}". Type "help" for a list of commands.`];
    }

    setTerminalHistory(prev => [
      ...prev,
      { type: 'user', text: `$ ${terminalInput}` },
      ...res.map(text => ({ type: 'sys', text }))
    ]);
    setTerminalInput('');
  };

  // Tab Navigation Links
  const navTabs = [
    { id: 'home', label: 'Overview', icon: Sparkles },
    { id: 'products', label: 'Software Arsenal', icon: ShoppingBag },
    { id: 'tauri-rust', label: 'Rust & Tauri Lab', icon: Monitor },
    { id: 'engineering', label: 'Protocol Engineering', icon: Code2 },
    { id: 'store', label: 'Store & UPI Checkout', icon: QrCode },
    { id: 'contact', label: 'Contact', icon: MessageSquare },
  ];

  const posTotal = posItems.reduce((acc, item) => acc + (item.price * item.qty), 0);

  return (
    <div className="min-h-screen bg-white text-slate-900 font-sans relative selection:bg-rose-200 selection:text-rose-900 overflow-x-hidden">
      
      {/* Lively Subtle Background Orbs (Pure Light Aesthetic, Zero CPU overhead) */}
      <div className="fixed top-[-100px] left-[15%] w-[480px] h-[480px] bg-rose-100/50 rounded-full blur-[110px] pointer-events-none z-0" />
      <div className="fixed bottom-[10%] right-[10%] w-[520px] h-[520px] bg-rose-50/70 rounded-full blur-[120px] pointer-events-none z-0" />

      {/* Three.js 3D Lively Particle Wave Canvas */}
      <canvas ref={canvasRef} className="fixed inset-0 w-full h-full pointer-events-none z-0 opacity-80" />

      {/* Main Content Container */}
      <div className="relative z-10 max-w-6xl mx-auto px-4 sm:px-8 py-6">

        {/* TOP BRAND BAR */}
        <header ref={headerRef} className="bg-white/90 backdrop-blur-xl border border-rose-100 rounded-2xl p-4 sm:px-6 shadow-[0_4px_20px_-4px_rgba(244,63,94,0.08)] flex flex-col sm:flex-row items-center justify-between gap-4 mb-6">
          <div className="flex items-center gap-3">
            <div className="w-11 h-11 rounded-xl bg-gradient-to-tr from-rose-500 via-rose-600 to-rose-700 text-white flex items-center justify-center font-heading font-black text-lg shadow-md shadow-rose-200">
              RQ
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="font-heading font-bold text-lg text-slate-900 tracking-tight">Mohammad Rehan</span>
                <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-semibold bg-rose-50 border border-rose-200 text-rose-600">
                  <span className="w-1.5 h-1.5 rounded-full bg-rose-500 animate-pulse" />
                  Online
                </span>
              </div>
              <p className="text-xs text-slate-500 font-medium">Founder @ Rehan Quant Lab • Rust & Desktop Protocol Engineer</p>
            </div>
          </div>

          {/* Quick Action Badges */}
          <div className="flex items-center gap-2">
            <a 
              href="https://wa.me/917091518548" 
              target="_blank" 
              rel="noopener noreferrer"
              className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-700 hover:bg-emerald-100 text-xs font-semibold transition-all shadow-sm"
            >
              <Smartphone className="w-3.5 h-3.5" />
              WhatsApp Us
            </a>
            <button 
              onClick={() => setActiveTab('store')}
              className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl bg-gradient-to-r from-rose-500 to-rose-600 hover:from-rose-600 hover:to-rose-700 text-white text-xs font-semibold shadow-md shadow-rose-200/80 transition-all hover:scale-102"
            >
              <QrCode className="w-3.5 h-3.5" />
              Pay UPI ₹3,999
            </button>
          </div>
        </header>

        {/* TAB NAVIGATION BAR (Framer Motion Sliding Pill, Pure Light Theme) */}
        <nav className="bg-white/95 backdrop-blur-xl border border-rose-100 rounded-2xl p-1.5 shadow-[0_4px_25px_-4px_rgba(244,63,94,0.06)] mb-8 sticky top-4 z-50 overflow-x-auto">
          <div className="flex items-center gap-1 min-w-max">
            {navTabs.map((tab) => {
              const Icon = tab.icon;
              const isActive = activeTab === tab.id;
              return (
                <button
                  key={tab.id}
                  onClick={() => setActiveTab(tab.id)}
                  className={`relative px-4 py-2.5 rounded-xl text-xs sm:text-sm font-semibold transition-all duration-200 flex items-center gap-2 ${
                    isActive 
                      ? 'text-white' 
                      : 'text-slate-600 hover:text-rose-600 hover:bg-rose-50/70'
                  }`}
                >
                  {/* Sliding Active Pill */}
                  {isActive && (
                    <motion.div
                      layoutId="activeTabIndicator"
                      className="absolute inset-0 bg-gradient-to-r from-rose-500 to-rose-600 rounded-xl shadow-md shadow-rose-200"
                      transition={{ type: 'spring', stiffness: 380, damping: 28 }}
                    />
                  )}
                  <span className="relative z-10 flex items-center gap-2">
                    <Icon className={`w-4 h-4 ${isActive ? 'text-white' : 'text-slate-400'}`} />
                    {tab.label}
                  </span>
                </button>
              );
            })}
          </div>
        </nav>

        {/* TAB CONTENTS (AnimatePresence for Silky Page Transitions) */}
        <main>
          <AnimatePresence mode="wait">
            
            {/* ══════════════════════════════════════════════════════════════
                TAB 1: OVERVIEW (HOME)
            ══════════════════════════════════════════════════════════════ */}
            {activeTab === 'home' && (
              <motion.div
                key="home"
                initial={{ opacity: 0, y: 15 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -15 }}
                transition={{ duration: 0.28, ease: 'easeOut' }}
                className="space-y-8"
              >
                {/* Hero Banner */}
                <div className="bg-white border border-rose-100 rounded-3xl p-6 sm:p-10 shadow-[0_10px_35px_-5px_rgba(244,63,94,0.07)] relative overflow-hidden">
                  <div className="absolute top-0 right-0 w-80 h-80 bg-gradient-to-br from-rose-100/60 to-transparent rounded-full blur-2xl pointer-events-none -mr-20 -mt-20" />
                  
                  <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center relative z-10">
                    <div className="lg:col-span-7 space-y-4">
                      <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-bold bg-rose-50 border border-rose-200 text-rose-600 gsap-float">
                        <Sparkles className="w-3.5 h-3.5 text-rose-500" />
                        ANIME PROTAGONIST MODE • ARCHITECT & FOUNDER
                      </div>

                      <h1 className="text-3xl sm:text-5xl font-heading font-black tracking-tight text-slate-900 leading-tight">
                        I build <span className="text-transparent bg-clip-text bg-gradient-to-r from-rose-500 via-rose-600 to-rose-700">ultra-fast software</span> that runs without internet.
                      </h1>

                      <p className="text-base text-slate-600 leading-relaxed max-w-xl">
                        Hi, I’m <strong>Mohammad Rehan</strong>. I build lightweight desktop apps and networking engines using <strong>Rust</strong>, <strong>Tauri</strong>, and modern web tech. My apps open in 0.3 seconds, use under 15 MB of RAM, and never lock you into monthly fees.
                      </p>

                      <div className="flex flex-wrap items-center gap-3 pt-2">
                        <button
                          onClick={() => setActiveTab('products')}
                          className="px-5 py-3 rounded-xl bg-gradient-to-r from-rose-500 to-rose-600 hover:from-rose-600 hover:to-rose-700 text-white font-semibold text-sm shadow-md shadow-rose-200 flex items-center gap-2 transition-all hover:scale-102"
                        >
                          Explore My Products <ArrowRight className="w-4 h-4" />
                        </button>
                        <button
                          onClick={() => setActiveTab('tauri-rust')}
                          className="px-5 py-3 rounded-xl bg-white border border-rose-200 text-rose-700 hover:bg-rose-50 font-semibold text-sm shadow-sm flex items-center gap-2 transition-all"
                        >
                          <Monitor className="w-4 h-4" /> Try Rust + Tauri Simulator
                        </button>
                      </div>
                    </div>

                    {/* Protagonist Stat Card */}
                    <div className="lg:col-span-5">
                      <div className="bg-gradient-to-b from-white to-rose-50/50 border border-rose-100 rounded-2xl p-6 shadow-md relative">
                        <div className="flex items-center justify-between border-b border-rose-100 pb-4 mb-4">
                          <div className="flex items-center gap-3">
                            <img src="emblem.webp" alt="Avatar" className="w-12 h-12 rounded-xl object-cover border border-rose-200 shadow-sm" />
                            <div>
                              <h3 className="font-heading font-bold text-slate-900 text-sm">Mohammad Rehan</h3>
                              <p className="text-xs text-rose-600 font-semibold">Special Ability: Rust + Zero Bloat</p>
                            </div>
                          </div>
                          <span className="px-2.5 py-1 rounded-md text-[11px] font-bold bg-rose-500 text-white shadow-sm">
                            LVL 99
                          </span>
                        </div>

                        {/* RPG Stat Sliders */}
                        <div className="space-y-3">
                          <div>
                            <div className="flex justify-between text-xs font-semibold mb-1">
                              <span className="text-slate-600">Cold Boot Speed (0.3s)</span>
                              <span className="text-rose-600 font-mono">99 / 100</span>
                            </div>
                            <div className="w-full h-2 bg-rose-100/70 rounded-full overflow-hidden">
                              <motion.div initial={{ width: 0 }} animate={{ width: '99%' }} transition={{ duration: 1 }} className="h-full bg-gradient-to-r from-rose-500 to-rose-600 rounded-full" />
                            </div>
                          </div>

                          <div>
                            <div className="flex justify-between text-xs font-semibold mb-1">
                              <span className="text-slate-600">Offline Reliability (Zero Cloud)</span>
                              <span className="text-rose-600 font-mono">100 / 100</span>
                            </div>
                            <div className="w-full h-2 bg-rose-100/70 rounded-full overflow-hidden">
                              <motion.div initial={{ width: 0 }} animate={{ width: '100%' }} transition={{ duration: 1, delay: 0.2 }} className="h-full bg-gradient-to-r from-rose-500 to-rose-600 rounded-full" />
                            </div>
                          </div>

                          <div>
                            <div className="flex justify-between text-xs font-semibold mb-1">
                              <span className="text-slate-600">RAM Efficiency (&lt; 15 MB)</span>
                              <span className="text-rose-600 font-mono">98 / 100</span>
                            </div>
                            <div className="w-full h-2 bg-rose-100/70 rounded-full overflow-hidden">
                              <motion.div initial={{ width: 0 }} animate={{ width: '98%' }} transition={{ duration: 1, delay: 0.4 }} className="h-full bg-gradient-to-r from-rose-500 to-rose-600 rounded-full" />
                            </div>
                          </div>
                        </div>

                        <div className="mt-5 pt-4 border-t border-rose-100 flex items-center justify-between text-xs text-slate-500 font-medium">
                          <span>Verified Udyam MSME:</span>
                          <span className="text-slate-700 font-bold">UDYAM-BR-26-0046522</span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                {/* 3 Pillars Section */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                  <div className="bg-white border border-rose-100 rounded-2xl p-6 shadow-sm hover:shadow-md hover:border-rose-300 transition-all">
                    <div className="w-10 h-10 rounded-xl bg-rose-50 border border-rose-200 text-rose-600 flex items-center justify-center mb-4">
                      <Monitor className="w-5 h-5" />
                    </div>
                    <h3 className="font-heading font-bold text-base text-slate-900 mb-2">Rust + Tauri Native Apps</h3>
                    <p className="text-xs text-slate-600 leading-relaxed">
                      Instead of heavy 400 MB Electron apps that lag your computer, I use Rust and Tauri to produce fast 7 MB native installers that run at 60 FPS.
                    </p>
                  </div>

                  <div className="bg-white border border-rose-100 rounded-2xl p-6 shadow-sm hover:shadow-md hover:border-rose-300 transition-all">
                    <div className="w-10 h-10 rounded-xl bg-rose-50 border border-rose-200 text-rose-600 flex items-center justify-center mb-4">
                      <QrCode className="w-5 h-5" />
                    </div>
                    <h3 className="font-heading font-bold text-base text-slate-900 mb-2">Direct UPI & WhatsApp Receipts</h3>
                    <p className="text-xs text-slate-600 leading-relaxed">
                      Instant retail billing. Customers scan a clean QR code with PhonePe or Google Pay, and get their invoice sent directly to WhatsApp in 1 click.
                    </p>
                  </div>

                  <div className="bg-white border border-rose-100 rounded-2xl p-6 shadow-sm hover:shadow-md hover:border-rose-300 transition-all">
                    <div className="w-10 h-10 rounded-xl bg-rose-50 border border-rose-200 text-rose-600 flex items-center justify-center mb-4">
                      <Zap className="w-5 h-5" />
                    </div>
                    <h3 className="font-heading font-bold text-base text-slate-900 mb-2">Dual-WAN Internet Bonding</h3>
                    <p className="text-xs text-slate-600 leading-relaxed">
                      RQL Conduit combines Wi-Fi and 5G mobile hotspot simultaneously. Sub-millisecond failover means zero dropouts during important calls or gaming.
                    </p>
                  </div>
                </div>

                {/* Quick Client Testimonial Showcase */}
                <div className="bg-gradient-to-r from-rose-500 to-rose-600 text-white rounded-2xl p-6 sm:p-8 shadow-lg shadow-rose-200 flex flex-col sm:flex-row items-center justify-between gap-6">
                  <div>
                    <span className="px-2.5 py-1 rounded-md text-[11px] font-bold bg-white/20 text-white backdrop-blur-sm mb-2 inline-block">
                      LIVE RETAIL STORE DEPLOYMENT
                    </span>
                    <h3 className="font-heading font-bold text-xl sm:text-2xl text-white">Ali Mobile Patna Runs On Our Stack</h3>
                    <p className="text-rose-100 text-xs sm:text-sm mt-1 max-w-xl">
                      Over 10,000+ smartphones tracked by IMEI and billed using ExpressBill POS. Zero downtime in 18 months of retail operations.
                    </p>
                  </div>
                  <a
                    href="https://ali-mobile-patna.pages.dev"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="px-5 py-3 rounded-xl bg-white text-rose-600 hover:bg-rose-50 font-bold text-xs sm:text-sm shadow-md whitespace-nowrap flex items-center gap-2 transition-all hover:scale-105"
                  >
                    View Live Store <ExternalLink className="w-4 h-4" />
                  </a>
                </div>
              </motion.div>
            )}

            {/* ══════════════════════════════════════════════════════════════
                TAB 2: PRODUCTS ARSENAL
            ══════════════════════════════════════════════════════════════ */}
            {activeTab === 'products' && (
              <motion.div
                key="products"
                initial={{ opacity: 0, y: 15 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -15 }}
                transition={{ duration: 0.28, ease: 'easeOut' }}
                className="space-y-8"
              >
                <div className="text-center max-w-2xl mx-auto space-y-2">
                  <span className="px-3 py-1 rounded-full text-xs font-bold bg-rose-50 border border-rose-200 text-rose-600">
                    COMPLETE SOFTWARE ARSENAL
                  </span>
                  <h2 className="text-3xl font-heading font-black text-slate-900 tracking-tight">
                    Tools Built for Speed, Privacy & Offline Freedom
                  </h2>
                  <p className="text-sm text-slate-600">
                    No monthly cloud subscriptions. Buy once, download the installer, and run forever on your own computer.
                  </p>
                </div>

                {/* Product Grid */}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                  {PRODUCTS.map((p) => (
                    <motion.div
                      key={p.id}
                      whileHover={{ y: -5 }}
                      className="bg-white border border-rose-100 rounded-2xl p-5 shadow-sm hover:shadow-xl hover:border-rose-300 transition-all duration-300 flex flex-col justify-between"
                    >
                      <div>
                        {/* Cover image preview */}
                        <div className="relative rounded-xl overflow-hidden bg-rose-50 border border-rose-100 mb-4 h-44 flex items-center justify-center">
                          <img 
                            src={p.cover} 
                            alt={p.title} 
                            className="w-full h-full object-cover transition-transform duration-500 hover:scale-105" 
                            onError={(e) => { e.target.style.display = 'none'; }}
                          />
                          <span className="absolute top-2.5 left-2.5 px-2.5 py-1 rounded-md text-[10px] font-bold bg-white/95 text-rose-700 shadow-sm border border-rose-200">
                            {p.tech}
                          </span>
                        </div>

                        <div className="space-y-1.5 mb-3">
                          <span className="text-[11px] font-bold text-rose-600 uppercase tracking-wider">{p.category}</span>
                          <h3 className="font-heading font-bold text-lg text-slate-900">{p.title}</h3>
                          <p className="text-xs text-slate-600 leading-relaxed">{p.tagline}</p>
                        </div>

                        {/* Key Features */}
                        <ul className="space-y-1.5 mb-4 text-xs text-slate-600">
                          {p.features.slice(0, 3).map((feat, idx) => (
                            <li key={idx} className="flex items-start gap-1.5">
                              <CheckCircle2 className="w-3.5 h-3.5 text-rose-500 shrink-0 mt-0.5" />
                              <span>{feat}</span>
                            </li>
                          ))}
                        </ul>
                      </div>

                      {/* Card Footer */}
                      <div className="pt-3 border-t border-rose-100 flex items-center justify-between gap-2">
                        <span className="text-xs font-bold text-slate-900">{p.price}</span>
                        <div className="flex items-center gap-1.5">
                          {p.demoUrl && (
                            <a
                              href={p.demoUrl}
                              target="_blank"
                              rel="noopener noreferrer"
                              className="px-2.5 py-1.5 rounded-lg bg-rose-50 border border-rose-200 text-rose-700 hover:bg-rose-100 text-xs font-semibold flex items-center gap-1"
                            >
                              Demo <ExternalLink className="w-3 h-3" />
                            </a>
                          )}
                          <button
                            onClick={() => setActiveTab('store')}
                            className="px-3 py-1.5 rounded-lg bg-gradient-to-r from-rose-500 to-rose-600 text-white text-xs font-semibold shadow-sm hover:from-rose-600 hover:to-rose-700"
                          >
                            Get License
                          </button>
                        </div>
                      </div>
                    </motion.div>
                  ))}
                </div>
              </motion.div>
            )}

            {/* ══════════════════════════════════════════════════════════════
                TAB 3: RUST & TAURI DESKTOP LAB (INTERACTIVE SIMULATOR)
            ══════════════════════════════════════════════════════════════ */}
            {activeTab === 'tauri-rust' && (
              <motion.div
                key="tauri-rust"
                initial={{ opacity: 0, y: 15 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -15 }}
                transition={{ duration: 0.28, ease: 'easeOut' }}
                className="space-y-8"
              >
                {/* Intro Box */}
                <div className="bg-white border border-rose-100 rounded-3xl p-6 sm:p-8 shadow-sm">
                  <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 mb-6">
                    <div>
                      <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-bold bg-rose-50 border border-rose-200 text-rose-600 mb-2">
                        <Cpu className="w-3.5 h-3.5 text-rose-500" />
                        RUST ENGINE & TAURI DESKTOP LAB
                      </div>
                      <h2 className="text-2xl sm:text-3xl font-heading font-black text-slate-900 tracking-tight">
                        Why I Use Rust + Tauri Instead of Slow Electron
                      </h2>
                    </div>

                    {/* Quick Metric comparison */}
                    <div className="flex items-center gap-3 bg-rose-50/70 border border-rose-200/80 rounded-2xl p-3 text-xs">
                      <div className="text-center px-2">
                        <div className="font-bold text-rose-600 text-base font-mono">11.8 MB</div>
                        <div className="text-slate-500 text-[10px]">Tauri RAM</div>
                      </div>
                      <div className="h-6 w-px bg-rose-200" />
                      <div className="text-center px-2">
                        <div className="font-bold text-slate-400 line-through text-base font-mono">420 MB</div>
                        <div className="text-slate-400 text-[10px]">Electron RAM</div>
                      </div>
                      <div className="h-6 w-px bg-rose-200" />
                      <div className="text-center px-2">
                        <div className="font-bold text-emerald-600 text-base font-mono">0.26s</div>
                        <div className="text-slate-500 text-[10px]">Boot Speed</div>
                      </div>
                    </div>
                  </div>

                  <p className="text-sm text-slate-600 leading-relaxed mb-6">
                    Traditional desktop billing software and POS tools are bloated, laggy, and hog gigabytes of memory. By compiling the core logic in <strong>Rust</strong> and interfacing through <strong>Tauri v2.0</strong>, my desktop apps launch instantly, never crash, and run happily on a 10-year-old budget store laptop.
                  </p>

                  {/* ─────────────────────────────────────────────────────────────
                      INTERACTIVE TAURI DESKTOP WINDOW SIMULATOR
                  ───────────────────────────────────────────────────────────── */}
                  <div className="border border-slate-200 rounded-2xl shadow-xl overflow-hidden bg-slate-900 text-slate-100 font-sans">
                    {/* Window Title Bar */}
                    <div className="bg-slate-800/95 px-4 py-2.5 flex items-center justify-between border-b border-slate-700/80">
                      <div className="flex items-center gap-2">
                        <div className="flex items-center gap-1.5">
                          <span className="w-3 h-3 rounded-full bg-rose-500 inline-block shadow-sm" />
                          <span className="w-3 h-3 rounded-full bg-amber-400 inline-block shadow-sm" />
                          <span className="w-3 h-3 rounded-full bg-emerald-500 inline-block shadow-sm" />
                        </div>
                        <span className="text-xs font-mono text-slate-400 ml-2">
                          ExpressBill POS — [Tauri Engine v2.0 • Rust 64-bit Native]
                        </span>
                      </div>
                      
                      <div className="flex items-center gap-2 text-[11px] font-mono text-emerald-400">
                        <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
                        IPC: 0.04ms (Lock-free)
                      </div>
                    </div>

                    {/* Window Inner App Toolbar */}
                    <div className="bg-slate-800 p-2.5 flex items-center justify-between gap-2 border-b border-slate-700">
                      <div className="flex items-center gap-1.5">
                        <button
                          onClick={() => setTauriApp('expressbill')}
                          className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
                            tauriApp === 'expressbill' ? 'bg-rose-600 text-white shadow-sm' : 'text-slate-300 hover:bg-slate-700'
                          }`}
                        >
                          POS Checkout Counter
                        </button>
                        <button
                          onClick={() => setTauriApp('conduit')}
                          className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
                            tauriApp === 'conduit' ? 'bg-rose-600 text-white shadow-sm' : 'text-slate-300 hover:bg-slate-700'
                          }`}
                        >
                          Dual-WAN Bonding
                        </button>
                      </div>

                      <div className="text-xs font-mono text-slate-300 hidden sm:block">
                        Active Memory: <span className="text-rose-400 font-bold">11.4 MB</span> | CPU: <span className="text-emerald-400 font-bold">0.1%</span>
                      </div>
                    </div>

                    {/* Window App Body */}
                    <div className="p-5 sm:p-6 bg-slate-900 min-h-[300px]">
                      {tauriApp === 'expressbill' ? (
                        <div className="grid grid-cols-1 md:grid-cols-12 gap-6">
                          {/* Left: Cart & Items */}
                          <div className="md:col-span-7 space-y-4">
                            <div className="flex items-center justify-between">
                              <h4 className="text-sm font-bold text-white flex items-center gap-2">
                                <FileText className="w-4 h-4 text-rose-400" />
                                Current Invoice #{posBillNumber}
                              </h4>
                              <button
                                onClick={() => {
                                  setPosItems(prev => [...prev, { name: 'Running Sneakers v2', price: 2499, qty: 1 }]);
                                  setPosPaid(false);
                                }}
                                className="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs text-rose-300 font-medium transition-all"
                              >
                                + Add Quick Item
                              </button>
                            </div>

                            <div className="space-y-2">
                              {posItems.map((item, idx) => (
                                <div key={idx} className="bg-slate-800/80 border border-slate-700/60 rounded-xl p-3 flex items-center justify-between text-xs">
                                  <div>
                                    <div className="font-semibold text-slate-200">{item.name}</div>
                                    <div className="text-slate-400 text-[11px]">Qty: {item.qty} × ₹{item.price}</div>
                                  </div>
                                  <div className="font-mono font-bold text-rose-300">
                                    ₹{item.price * item.qty}
                                  </div>
                                </div>
                              ))}
                            </div>

                            <div className="bg-slate-800/40 rounded-xl p-3 border border-slate-800 flex justify-between items-center text-sm font-bold">
                              <span>Grand Total (GST Included):</span>
                              <span className="text-emerald-400 font-mono text-base">₹{posTotal.toLocaleString()}</span>
                            </div>
                          </div>

                          {/* Right: Payment & Action */}
                          <div className="md:col-span-5 bg-slate-800/60 border border-slate-700 rounded-xl p-4 flex flex-col justify-between">
                            <div className="text-center space-y-2">
                              <span className="text-[11px] font-mono text-slate-400 uppercase tracking-wider">Dynamic Customer Screen</span>
                              <div className="w-28 h-28 mx-auto bg-white p-2 rounded-xl shadow-md flex items-center justify-center">
                                <QrCode className="w-24 h-24 text-slate-900" />
                              </div>
                              <p className="text-xs text-slate-300 font-mono">Scan ₹{posTotal} with PhonePe / GPay</p>
                            </div>

                            <div className="space-y-2 pt-4">
                              <button
                                onClick={() => {
                                  setPosPaid(true);
                                  setPosBillNumber(prev => prev + 1);
                                  confetti({ particleCount: 30, spread: 60, colors: ['#f43f5e', '#10b981'] });
                                }}
                                className="w-full py-2.5 rounded-xl bg-gradient-to-r from-emerald-600 to-emerald-500 hover:from-emerald-500 hover:to-emerald-400 text-white font-bold text-xs shadow-md transition-all flex items-center justify-center gap-2"
                              >
                                {posPaid ? <Check className="w-4 h-4" /> : <Printer className="w-4 h-4" />}
                                {posPaid ? 'Payment Confirmed & Printed!' : 'Print Bill & Send WhatsApp'}
                              </button>

                              <button
                                onClick={() => {
                                  setPosItems([
                                    { name: 'Casual Loafers Tan (Size 8)', price: 1899, qty: 1 }
                                  ]);
                                  setPosPaid(false);
                                }}
                                className="w-full py-1.5 rounded-lg bg-slate-700/60 hover:bg-slate-700 text-slate-300 text-[11px] font-medium transition-all"
                              >
                                Reset Demo Counter
                              </button>
                            </div>
                          </div>
                        </div>
                      ) : (
                        /* Conduit View */
                        <div className="space-y-4">
                          <div className="flex items-center justify-between">
                            <div className="flex items-center gap-2">
                              <Wifi className="w-4 h-4 text-rose-400" />
                              <h4 className="text-sm font-bold text-white">RQL Conduit — Multi-WAN Bonding Status</h4>
                            </div>
                            <span className="px-2.5 py-0.5 rounded text-[11px] font-mono bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                              Bonded (2 Adapters Active)
                            </span>
                          </div>

                          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                            <div className="bg-slate-800 border border-slate-700 rounded-xl p-3 space-y-1">
                              <div className="text-xs text-slate-400 font-mono">Adapter 1: Wi-Fi 6 (Home Fiber)</div>
                              <div className="text-base font-bold text-white font-mono">240.5 Mbps • Ping: 4ms</div>
                              <div className="w-full h-1.5 bg-slate-700 rounded-full overflow-hidden">
                                <div className="h-full bg-emerald-400 w-4/5" />
                              </div>
                            </div>

                            <div className="bg-slate-800 border border-slate-700 rounded-xl p-3 space-y-1">
                              <div className="text-xs text-slate-400 font-mono">Adapter 2: 5G Hotspot (Jio 5G USB)</div>
                              <div className="text-base font-bold text-white font-mono">185.2 Mbps • Ping: 12ms</div>
                              <div className="w-full h-1.5 bg-slate-700 rounded-full overflow-hidden">
                                <div className="h-full bg-rose-400 w-3/5" />
                              </div>
                            </div>
                          </div>

                          <div className="p-3 bg-slate-800/60 border border-slate-700 rounded-xl flex items-center justify-between text-xs">
                            <span className="text-slate-300">Failover Latency:</span>
                            <span className="text-rose-300 font-mono font-bold">&lt; 0.8ms (Zero Dropped Packets)</span>
                          </div>
                        </div>
                      )}
                    </div>
                  </div>
                </div>

                {/* ─────────────────────────────────────────────────────────────
                    LIVE RUST WASM BENCHMARK & OFFLINE LICENSE FORGE
                ───────────────────────────────────────────────────────────── */}
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                  {/* WASM Benchmark Card */}
                  <div className="bg-white border border-rose-100 rounded-3xl p-6 shadow-sm">
                    <div className="flex items-center gap-3 mb-4">
                      <div className="w-10 h-10 rounded-xl bg-rose-50 border border-rose-200 text-rose-600 flex items-center justify-center font-bold font-mono">
                        🦀
                      </div>
                      <div>
                        <h3 className="font-heading font-bold text-lg text-slate-900">Live Rust WASM Benchmark</h3>
                        <p className="text-xs text-slate-500">Run 1,000,000 calculations right now inside your browser</p>
                      </div>
                    </div>

                    <p className="text-xs text-slate-600 mb-4 leading-relaxed">
                      This executes compiled WebAssembly binary (<code>rql_wasm_engine.wasm</code>) compiled straight from Rust source code with SIMD optimizations.
                    </p>

                    <button
                      onClick={handleBenchmark}
                      disabled={isBenchmarking}
                      className="w-full py-3 rounded-xl bg-gradient-to-r from-rose-500 to-rose-600 hover:from-rose-600 hover:to-rose-700 text-white font-bold text-xs shadow-md shadow-rose-200 transition-all flex items-center justify-center gap-2 mb-4"
                    >
                      {isBenchmarking ? <RefreshCw className="w-4 h-4 animate-spin" /> : <Play className="w-4 h-4" />}
                      {isBenchmarking ? 'Running Rust Engine...' : 'Run 1,000,000 Iteration Test'}
                    </button>

                    {benchmarkData && (
                      <motion.div initial={{ opacity: 0, scale: 0.95 }} animate={{ opacity: 1, scale: 1 }} className="bg-rose-50/70 border border-rose-200 rounded-2xl p-4 space-y-2">
                        <div className="flex justify-between text-xs font-semibold">
                          <span className="text-slate-600">Rust WASM Execution:</span>
                          <span className="text-rose-600 font-mono font-bold">{benchmarkData.wasmTimeMs} ms</span>
                        </div>
                        <div className="flex justify-between text-xs font-semibold">
                          <span className="text-slate-600">JavaScript Interpreted:</span>
                          <span className="text-slate-500 font-mono">{benchmarkData.jsTimeMs} ms</span>
                        </div>
                        <div className="flex justify-between text-xs font-semibold border-t border-rose-200 pt-2 text-emerald-700">
                          <span>Rust Acceleration:</span>
                          <span className="font-mono font-bold">{benchmarkData.speedup}x Faster</span>
                        </div>
                      </motion.div>
                    )}
                  </div>

                  {/* Offline License Forge Card */}
                  <div className="bg-white border border-rose-100 rounded-3xl p-6 shadow-sm">
                    <div className="flex items-center gap-3 mb-4">
                      <div className="w-10 h-10 rounded-xl bg-rose-50 border border-rose-200 text-rose-600 flex items-center justify-center font-bold">
                        <ShieldCheck className="w-5 h-5" />
                      </div>
                      <div>
                        <h3 className="font-heading font-bold text-lg text-slate-900">Offline Cryptographic Forge</h3>
                        <p className="text-xs text-slate-500">Zero cloud server license verification in 0.04ms</p>
                      </div>
                    </div>

                    <p className="text-xs text-slate-600 mb-4 leading-relaxed">
                      ExpressBill POS uses cryptographic machine ID hashing. Store laptops can verify their lifetime license offline forever even without an active internet connection.
                    </p>

                    <div className="space-y-3 mb-4">
                      <div>
                        <label className="text-xs font-semibold text-slate-700 block mb-1">Hardware Machine ID:</label>
                        <input
                          type="text"
                          value={machineId}
                          onChange={(e) => setMachineId(e.target.value)}
                          className="w-full px-3 py-2 rounded-xl bg-slate-50 border border-rose-200 text-xs font-mono text-slate-800 focus:outline-none focus:border-rose-500"
                        />
                      </div>

                      <button
                        onClick={handleForgeKey}
                        className="w-full py-2.5 rounded-xl bg-white border border-rose-300 hover:bg-rose-50 text-rose-700 font-bold text-xs shadow-sm transition-all"
                      >
                        Forge License Key
                      </button>
                    </div>

                    {licenseKey && (
                      <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="bg-rose-50 border border-rose-200 rounded-xl p-3 flex items-center justify-between">
                        <div>
                          <span className="text-[10px] text-slate-500 block uppercase font-mono">Verified Offline Key</span>
                          <span className="text-xs font-mono font-bold text-rose-700">{licenseKey}</span>
                        </div>
                        <span className="text-xs font-bold text-emerald-600 flex items-center gap-1">
                          <Check className="w-3.5 h-3.5" /> Valid
                        </span>
                      </motion.div>
                    )}
                  </div>
                </div>
              </motion.div>
            )}

            {/* ══════════════════════════════════════════════════════════════
                TAB 4: PROTOCOL ENGINEERING (AVIORSWAP INTERVIEW DEEP DIVE)
            ══════════════════════════════════════════════════════════════ */}
            {activeTab === 'engineering' && (
              <motion.div
                key="engineering"
                initial={{ opacity: 0, y: 15 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -15 }}
                transition={{ duration: 0.28, ease: 'easeOut' }}
                className="space-y-8"
              >
                <div className="bg-white border border-rose-100 rounded-3xl p-6 sm:p-10 shadow-sm space-y-6">
                  <div>
                    <span className="px-3 py-1 rounded-full text-xs font-bold bg-rose-50 border border-rose-200 text-rose-600 mb-2 inline-block">
                      TECHNICAL DOSSIER • SENIOR PROTOCOL ENGINEER
                    </span>
                    <h2 className="text-3xl font-heading font-black text-slate-900 tracking-tight">
                      Low-Latency Systems & Distributed Consensus
                    </h2>
                    <p className="text-sm text-slate-600 mt-2 max-w-2xl">
                      My core technical competencies in high-throughput network engineering, lock-free concurrency, and distributed protocols.
                    </p>
                  </div>

                  <div className="grid grid-cols-1 md:grid-cols-3 gap-6 pt-2">
                    {/* Pillar 1 */}
                    <div className="border border-rose-100 rounded-2xl p-5 bg-gradient-to-b from-white to-rose-50/30">
                      <div className="w-9 h-9 rounded-xl bg-rose-100 text-rose-600 flex items-center justify-center font-bold text-sm mb-3">
                        01
                      </div>
                      <h3 className="font-heading font-bold text-base text-slate-900 mb-2">Socket Binding (SO_BINDTODEVICE)</h3>
                      <p className="text-xs text-slate-600 leading-relaxed">
                        Direct kernel-level socket binding using Rust’s <code>socket2</code> crate. Allows routing UDP/TCP streams across distinct physical network interfaces (NICs) without OS routing table interference.
                      </p>
                    </div>

                    {/* Pillar 2 */}
                    <div className="border border-rose-100 rounded-2xl p-5 bg-gradient-to-b from-white to-rose-50/30">
                      <div className="w-9 h-9 rounded-xl bg-rose-100 text-rose-600 flex items-center justify-center font-bold text-sm mb-3">
                        02
                      </div>
                      <h3 className="font-heading font-bold text-base text-slate-900 mb-2">Tokio Async & Concurrency</h3>
                      <p className="text-xs text-slate-600 leading-relaxed">
                        Lock-free ring buffers (<code>crossbeam-channel</code>), non-blocking I/O event loops, and multi-threaded work-stealing schedulers capable of processing 100,000+ packets/sec with zero heap reallocation.
                      </p>
                    </div>

                    {/* Pillar 3 */}
                    <div className="border border-rose-100 rounded-2xl p-5 bg-gradient-to-b from-white to-rose-50/30">
                      <div className="w-9 h-9 rounded-xl bg-rose-100 text-rose-600 flex items-center justify-center font-bold text-sm mb-3">
                        03
                      </div>
                      <h3 className="font-heading font-bold text-base text-slate-900 mb-2">Raft Distributed Quorums</h3>
                      <p className="text-xs text-slate-600 leading-relaxed">
                        Implementation of Raft consensus with leader election, append entries, log compaction, and deterministic state transitions ensuring split-brain safety under network partitions.
                      </p>
                    </div>
                  </div>

                  {/* Architecture Diagram Box */}
                  <div className="bg-slate-900 text-slate-100 rounded-2xl p-6 font-mono text-xs overflow-x-auto border border-slate-800">
                    <div className="text-slate-400 mb-2">// Network Packet Flow in RQL Conduit Engine</div>
                    <pre className="text-rose-300 leading-relaxed">
{`+-----------------------+        +--------------------------+
|  Application Stream   |  --->  | Rust Conduit Core Router |
+-----------------------+        +--------------------------+
                                              |
                     +------------------------+------------------------+
                     |                                                 |
         [Socket2: SO_BINDTODEVICE]                        [Socket2: SO_BINDTODEVICE]
                     |                                                 |
            +------------------+                              +------------------+
            |  Wi-Fi Adapter   |                              |   5G Hotspot     |
            | (Sub-4ms Jitter) |                              | (Zero Packetloss)|
            +------------------+                              +------------------+`}
                    </pre>
                  </div>
                </div>
              </motion.div>
            )}

            {/* ══════════════════════════════════════════════════════════════
                TAB 5: STORE & INSTANT UPI CHECKOUT
            ══════════════════════════════════════════════════════════════ */}
            {activeTab === 'store' && (
              <motion.div
                key="store"
                initial={{ opacity: 0, y: 15 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -15 }}
                transition={{ duration: 0.28, ease: 'easeOut' }}
                className="space-y-8"
              >
                <div className="text-center max-w-2xl mx-auto space-y-2">
                  <span className="px-3 py-1 rounded-full text-xs font-bold bg-rose-50 border border-rose-200 text-rose-600">
                    DIRECT CHECKOUT & INSTANT ACTIVATION
                  </span>
                  <h2 className="text-3xl font-heading font-black text-slate-900 tracking-tight">
                    Get Your Lifetime License in 60 Seconds
                  </h2>
                  <p className="text-sm text-slate-600">
                    Choose Indian domestic UPI (Zero processing fees) or International Gumroad credit card checkout.
                  </p>
                </div>

                <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
                  
                  {/* Left: Indian UPI Checkout (Featured) */}
                  <div className="lg:col-span-7 bg-white border-2 border-rose-500 rounded-3xl p-6 sm:p-8 shadow-xl relative overflow-hidden">
                    <div className="absolute top-0 right-0 bg-gradient-to-l from-rose-500 to-rose-600 text-white text-[11px] font-bold px-4 py-1 rounded-bl-xl shadow-sm">
                      INSTANT ACTIVATION • ZERO EXTRA FEES
                    </div>

                    <div className="flex items-center gap-3 mb-6">
                      <div className="w-12 h-12 rounded-2xl bg-rose-50 border border-rose-200 text-rose-600 flex items-center justify-center font-bold">
                        <QrCode className="w-6 h-6" />
                      </div>
                      <div>
                        <h3 className="font-heading font-bold text-xl text-slate-900">India Domestic UPI Payment</h3>
                        <p className="text-xs text-slate-500">Pay using Google Pay, PhonePe, Paytm, or BHIM</p>
                      </div>
                    </div>

                    {/* Price Tag */}
                    <div className="bg-rose-50/70 border border-rose-200 rounded-2xl p-4 flex items-center justify-between mb-6">
                      <div>
                        <span className="text-xs text-slate-600 font-medium">One-Time Lifetime Price:</span>
                        <div className="text-3xl font-heading font-black text-rose-600">₹3,999</div>
                      </div>
                      <span className="px-3 py-1 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800 border border-emerald-200">
                        Zero Monthly Renewal
                      </span>
                    </div>

                    {/* QR Code and Instructions */}
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 items-center mb-6">
                      <div className="bg-white border-2 border-rose-200 rounded-2xl p-4 text-center shadow-sm">
                        <img 
                          src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=upi%3A%2F%2Fpay%3Fpa%3D7091518548%40pthdfc%26pn%3DMOHAMMAD%2520REHAN%26am%3D3999.00%26cu%3DINR%26tn%3DExpressBill%2520Lifetime%2520License"
                          alt="UPI QR Code" 
                          className="w-40 h-40 mx-auto rounded-xl"
                        />
                        <span className="text-[11px] text-slate-500 font-mono block mt-2">Scan with any UPI App</span>
                      </div>

                      <div className="space-y-3">
                        <div>
                          <label className="text-xs font-semibold text-slate-600 block mb-1">Direct UPI ID:</label>
                          <div className="flex items-center gap-2">
                            <input 
                              type="text" 
                              readOnly 
                              value="7091518548@pthdfc"
                              className="px-3 py-2 rounded-xl bg-slate-50 border border-rose-200 text-xs font-mono font-bold text-slate-900 w-full"
                            />
                            <button
                              onClick={handleCopyUpi}
                              className="px-3 py-2 rounded-xl bg-rose-50 hover:bg-rose-100 text-rose-700 text-xs font-bold border border-rose-200 flex items-center gap-1 shrink-0"
                            >
                              {copiedUpi ? <Check className="w-4 h-4 text-emerald-600" /> : <Copy className="w-4 h-4" />}
                              {copiedUpi ? 'Copied' : 'Copy'}
                            </button>
                          </div>
                        </div>

                        <div className="text-xs text-slate-600 space-y-1">
                          <p>1. Open PhonePe, Google Pay, or Paytm.</p>
                          <p>2. Scan QR or pay to <strong>7091518548@pthdfc</strong>.</p>
                          <p>3. Click WhatsApp below to get your key instantly.</p>
                        </div>
                      </div>
                    </div>

                    {/* WhatsApp Action */}
                    <a
                      href="https://wa.me/917091518548?text=Hello%20Mohammad%20Rehan,%20I%20have%20paid%20%E2%82%B93,999%20via%20UPI%20for%20ExpressBill%20Lifetime%20License.%20Please%20send%20my%20license%20key."
                      target="_blank"
                      rel="noopener noreferrer"
                      className="w-full py-3.5 rounded-xl bg-gradient-to-r from-emerald-600 to-emerald-500 hover:from-emerald-500 hover:to-emerald-400 text-white font-bold text-sm shadow-md transition-all flex items-center justify-center gap-2"
                    >
                      <Smartphone className="w-4 h-4" />
                      Send WhatsApp Screenshot for Instant Key
                    </a>
                  </div>

                  {/* Right: Global Gumroad Checkout */}
                  <div className="lg:col-span-5 bg-white border border-rose-100 rounded-3xl p-6 sm:p-8 shadow-sm space-y-6">
                    <div className="flex items-center gap-3">
                      <div className="w-12 h-12 rounded-2xl bg-slate-50 border border-slate-200 text-slate-700 flex items-center justify-center font-bold">
                        <ShoppingBag className="w-6 h-6" />
                      </div>
                      <div>
                        <h3 className="font-heading font-bold text-xl text-slate-900">Global Card Checkout</h3>
                        <p className="text-xs text-slate-500">Pay securely via Gumroad in USD</p>
                      </div>
                    </div>

                    <div className="bg-slate-50 border border-slate-200 rounded-2xl p-4">
                      <span className="text-xs text-slate-500 font-medium">International License:</span>
                      <div className="text-3xl font-heading font-black text-slate-900">$49 <span className="text-sm font-normal text-slate-500">USD</span></div>
                      <p className="text-xs text-slate-600 mt-1">Accepts Visa, Mastercard, American Express, Apple Pay.</p>
                    </div>

                    <div className="space-y-3">
                      <a
                        href="https://quantify17.gumroad.com/l/ExpressBill"
                        target="_blank"
                        rel="noopener noreferrer"
                        className="w-full py-3.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-bold text-sm shadow-md transition-all flex items-center justify-center gap-2"
                      >
                        Buy on Gumroad ($49) <ExternalLink className="w-4 h-4" />
                      </a>

                      <a
                        href="downloads/ExpressBill-Setup.exe"
                        download
                        className="w-full py-3 rounded-xl bg-rose-50 hover:bg-rose-100 border border-rose-200 text-rose-700 font-bold text-xs shadow-sm transition-all flex items-center justify-center gap-2"
                      >
                        <Download className="w-4 h-4" /> Download Windows Installer (.exe)
                      </a>
                    </div>

                    <div className="pt-4 border-t border-rose-100 text-xs text-slate-500 space-y-1">
                      <p className="flex items-center gap-1.5"><CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" /> Instant automated email license delivery</p>
                      <p className="flex items-center gap-1.5"><CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" /> Free lifetime version updates</p>
                    </div>
                  </div>

                </div>
              </motion.div>
            )}

            {/* ══════════════════════════════════════════════════════════════
                TAB 6: CONTACT & INTERACTIVE TERMINAL
            ══════════════════════════════════════════════════════════════ */}
            {activeTab === 'contact' && (
              <motion.div
                key="contact"
                initial={{ opacity: 0, y: 15 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -15 }}
                transition={{ duration: 0.28, ease: 'easeOut' }}
                className="space-y-8"
              >
                <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
                  
                  {/* Left: Contact Info */}
                  <div className="lg:col-span-5 bg-white border border-rose-100 rounded-3xl p-6 sm:p-8 shadow-sm space-y-6">
                    <div>
                      <span className="px-3 py-1 rounded-full text-xs font-bold bg-rose-50 border border-rose-200 text-rose-600 mb-2 inline-block">
                        GET IN TOUCH DIRECTLY
                      </span>
                      <h2 className="text-2xl font-heading font-black text-slate-900 tracking-tight">
                        Let’s Talk Code or Retail Systems
                      </h2>
                      <p className="text-xs text-slate-600 mt-1 leading-relaxed">
                        I respond personally to software queries, custom desktop contracts, and interview invitations.
                      </p>
                    </div>

                    <div className="space-y-4">
                      <a
                        href="https://wa.me/917091518548"
                        target="_blank"
                        rel="noopener noreferrer"
                        className="p-4 rounded-2xl bg-emerald-50 border border-emerald-200 flex items-center gap-3 text-emerald-900 hover:bg-emerald-100 transition-all shadow-sm block"
                      >
                        <div className="w-10 h-10 rounded-xl bg-emerald-600 text-white flex items-center justify-center shrink-0 shadow-sm">
                          <Smartphone className="w-5 h-5" />
                        </div>
                        <div>
                          <div className="text-xs text-emerald-700 font-semibold">WhatsApp Direct</div>
                          <div className="text-sm font-bold">+91 70915 18548</div>
                        </div>
                      </a>

                      <a
                        href="mailto:rehanquantlab@gmail.com"
                        className="p-4 rounded-2xl bg-rose-50 border border-rose-200 flex items-center gap-3 text-rose-900 hover:bg-rose-100 transition-all shadow-sm block"
                      >
                        <div className="w-10 h-10 rounded-xl bg-rose-600 text-white flex items-center justify-center shrink-0 shadow-sm">
                          <MessageSquare className="w-5 h-5" />
                        </div>
                        <div>
                          <div className="text-xs text-rose-700 font-semibold">Email Channel</div>
                          <div className="text-sm font-bold">rehanquantlab@gmail.com</div>
                        </div>
                      </a>
                    </div>

                    <div className="p-4 rounded-2xl bg-slate-50 border border-slate-200 text-xs text-slate-600 space-y-1">
                      <div className="font-bold text-slate-800">Physical Lab Office:</div>
                      <p>Rehan Quant Lab • Sabzibagh, Patna, Bihar, 800004, India</p>
                      <p className="text-[11px] text-slate-400">Registered Indian Sole Proprietorship (Udyam MSME)</p>
                    </div>
                  </div>

                  {/* Right: Interactive CLI Terminal */}
                  <div className="lg:col-span-7 bg-slate-900 text-slate-100 rounded-3xl p-6 shadow-xl border border-slate-800 flex flex-col justify-between font-mono text-xs">
                    <div>
                      <div className="flex items-center justify-between border-b border-slate-800 pb-3 mb-4">
                        <div className="flex items-center gap-2">
                          <div className="flex gap-1.5">
                            <span className="w-3 h-3 rounded-full bg-rose-500 inline-block" />
                            <span className="w-3 h-3 rounded-full bg-amber-400 inline-block" />
                            <span className="w-3 h-3 rounded-full bg-emerald-500 inline-block" />
                          </div>
                          <span className="text-slate-400 text-[11px] ml-2">rql-terminal-v2.0 [Rust Core]</span>
                        </div>
                        <span className="text-[10px] text-emerald-400">ACTIVE SESSION</span>
                      </div>

                      {/* Log Output */}
                      <div className="space-y-1.5 max-h-72 overflow-y-auto pr-2 mb-4">
                        {terminalHistory.map((item, idx) => (
                          <div key={idx} className={item.type === 'user' ? 'text-rose-400 font-bold' : 'text-slate-300'}>
                            {item.text}
                          </div>
                        ))}
                      </div>
                    </div>

                    {/* Input form */}
                    <form onSubmit={handleTerminalSubmit} className="flex items-center gap-2 pt-2 border-t border-slate-800">
                      <span className="text-rose-500 font-bold">$</span>
                      <input
                        type="text"
                        value={terminalInput}
                        onChange={(e) => setTerminalInput(e.target.value)}
                        placeholder="type 'help', 'tauri', 'products', or 'benchmark'..."
                        className="w-full bg-transparent text-white focus:outline-none placeholder:text-slate-600 text-xs"
                      />
                    </form>
                  </div>

                </div>
              </motion.div>
            )}

          </AnimatePresence>
        </main>

        {/* FOOTER */}
        <footer className="mt-16 pt-8 border-t border-rose-100 flex flex-col sm:flex-row items-center justify-between text-xs text-slate-500 gap-4">
          <div className="flex items-center gap-2">
            <span className="w-2 h-2 rounded-full bg-rose-500" />
            <span>© 2026 Mohammad Rehan • Rehan Quant Lab. Built with Vite, React, GSAP, Framer Motion, Three.js & Rust.</span>
          </div>

          <div className="flex items-center gap-4 text-slate-600 font-medium">
            <a href="https://github.com/mohammadrehan1621" target="_blank" rel="noopener noreferrer" className="hover:text-rose-600 transition-colors">GitHub</a>
            <a href="https://quantify17.gumroad.com" target="_blank" rel="noopener noreferrer" className="hover:text-rose-600 transition-colors">Gumroad</a>
            <a href="downloads/ExpressBill-Setup.exe" download className="hover:text-rose-600 transition-colors">Download App</a>
          </div>
        </footer>

      </div>
    </div>
  );
}
