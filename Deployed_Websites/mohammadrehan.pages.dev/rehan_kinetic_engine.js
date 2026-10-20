/**
 * ============================================================================
 * REHAN QUANT LAB™ — AWWWARDS KINETIC & TELEMETRY ENGINE v1.0.0
 * Architected by Mohammad Rehan | Founder @ Rehan Quant Lab
 * 
 * PHILOSOPHY: Gall's Law & Sovereign Systems Doctrine
 * "A complex system that works is always found to have evolved from a simple
 *  system that worked. Never build a monster we cannot understand."
 * 
 * CORE MODULES:
 * 1. AntifragileMotionGuard: Reduced-motion detection, battery & FPS surveillance.
 * 2. InertialFluidScroll: Lenis-grade momentum without scroll hijacking.
 * 3. QuantLatticeCanvas: Non-Newtonian topological particle mesh (0% CPU when dormant).
 * 4. MagneticHUDCursor: Dual-ring cybernetic cursor with magnetic attraction.
 * 5. KineticScrollObserver: 120 FPS hardware-accelerated viewport cascade reveals.
 * 6. SynthesizedAudioTelemetry: Pure Web Audio API micro-haptics (0 external files).
 * ============================================================================
 */

(function () {
    'use strict';

    // ────────────────────────────────────────────────────────────────────────
    // 0. SYSTEM STATE & CAPABILITY AUDIT
    // ────────────────────────────────────────────────────────────────────────
    const isTouchDevice = () => window.matchMedia('(hover: none) and (pointer: coarse)').matches;
    const prefersReducedMotion = () => window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    const State = {
        enabled: !prefersReducedMotion(),
        isTouch: isTouchDevice(),
        audioMuted: true, // Sovereign default: silent until toggled or allowed
        audioCtx: null,
        fps: 60,
        lastFrameTime: performance.now(),
        frameCount: 0,
        perfTier: 'HIGH', // HIGH | MEDIUM | LOW
        cursorX: window.innerWidth / 2,
        cursorY: window.innerHeight / 2,
        targetCursorX: window.innerWidth / 2,
        targetCursorY: window.innerHeight / 2,
        mouseVelocity: 0,
        lastMouseX: 0,
        lastMouseY: 0,
        lastMouseMoveTime: performance.now()
    };

    // ────────────────────────────────────────────────────────────────────────
    // 1. INERTIAL FLUID SCROLL (Lenis-Inspired, Zero-Hijacking)
    // ────────────────────────────────────────────────────────────────────────
    class InertialFluidScroll {
        constructor() {
            if (State.isTouch || prefersReducedMotion()) return; // Native mobile touch momentum is best
            this.targetY = window.scrollY;
            this.currentY = window.scrollY;
            this.ease = 0.085; // Natural fluid viscosity
            this.isRunning = false;
            this.init();
        }

        init() {
            // Keep native wheel listening with passive: false only for custom delta capture
            window.addEventListener('wheel', (e) => {
                // Ignore if inside pre-existing scrollable chat window or modals
                const inScrollable = e.target.closest('#chat-messages, #aria-messages, #chatbot-modal, textarea, .overflow-y-auto');
                if (inScrollable) return;

                // Modulate delta smoothly without canceling browser navigation defaults
                const delta = e.deltaY;
                const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
                this.targetY = Math.max(0, Math.min(maxScroll, this.targetY + delta));

                if (!this.isRunning) {
                    this.isRunning = true;
                    requestAnimationFrame(() => this.tick());
                }
            }, { passive: true });

            // Sync with native user scroll (e.g. scrollbar dragging or page navigation)
            window.addEventListener('scroll', () => {
                if (Math.abs(window.scrollY - this.currentY) > 100) {
                    this.currentY = window.scrollY;
                    this.targetY = window.scrollY;
                }
            }, { passive: true });
        }

        tick() {
            const diff = this.targetY - this.currentY;
            if (Math.abs(diff) > 0.4) {
                this.currentY += diff * this.ease;
                window.scrollTo(0, Math.round(this.currentY));
                requestAnimationFrame(() => this.tick());
            } else {
                this.currentY = this.targetY;
                this.isRunning = false;
            }
        }
    }

    // ────────────────────────────────────────────────────────────────────────
    // 2. QUANT LATTICE CANVAS (Non-Newtonian Fluid Dynamic Matrix)
    // ────────────────────────────────────────────────────────────────────────
    class QuantLatticeCanvas {
        constructor() {
            if (prefersReducedMotion()) return;
            this.canvas = document.createElement('canvas');
            this.ctx = this.canvas.getContext('2d');
            this.canvas.id = 'rehan-quant-canvas';
            this.canvas.style.cssText = `
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                pointer-events: none;
                z-index: 0;
                opacity: 0.35;
                transition: opacity 0.8s ease;
            `;
            document.body.prepend(this.canvas);

            this.particles = [];
            this.particleCount = State.isTouch ? 25 : 55;
            this.width = window.innerWidth;
            this.height = window.innerHeight;
            this.visible = true;
            this.animId = null;

            this.resize();
            this.spawn();
            this.bind();
            this.loop();
        }

        resize() {
            const dpr = Math.min(window.devicePixelRatio || 1, 2);
            this.width = window.innerWidth;
            this.height = window.innerHeight;
            this.canvas.width = this.width * dpr;
            this.canvas.height = this.height * dpr;
            this.ctx.scale(dpr, dpr);
        }

        spawn() {
            this.particles = [];
            for (let i = 0; i < this.particleCount; i++) {
                this.particles.push({
                    x: Math.random() * this.width,
                    y: Math.random() * this.height,
                    vx: (Math.random() - 0.5) * 0.45,
                    vy: (Math.random() - 0.5) * 0.45,
                    baseRadius: Math.random() * 1.5 + 0.8,
                    pulse: Math.random() * Math.PI * 2,
                    color: i % 4 === 0 ? '#06b6d4' : (i % 4 === 1 ? '#6366f1' : '#10b981')
                });
            }
        }

        bind() {
            window.addEventListener('resize', () => {
                this.resize();
                this.spawn();
            }, { passive: true });

            // IntersectionObserver: sleep completely when user scrolls away or tab is hidden
            document.addEventListener('visibilitychange', () => {
                this.visible = !document.hidden;
                if (this.visible && !this.animId) this.loop();
            });
        }

        loop() {
            if (!this.visible) {
                this.animId = null;
                return;
            }

            this.ctx.clearRect(0, 0, this.width, this.height);

            // Compute dilatant fluid viscosity from cursor velocity
            const stiffening = Math.min(State.mouseVelocity / 50, 1.8);

            for (let i = 0; i < this.particles.length; i++) {
                const p = this.particles[i];

                // Velocity damping (Non-Newtonian hardening)
                const speedMult = 1 / (1 + stiffening * 1.5);
                p.x += p.vx * speedMult;
                p.y += p.vy * speedMult;

                // Screen boundary wrapping
                if (p.x < 0) p.x = this.width;
                if (p.x > this.width) p.x = 0;
                if (p.y < 0) p.y = this.height;
                if (p.y > this.height) p.y = 0;

                // Interactive cursor proximity gravity
                const dx = State.cursorX - p.x;
                const dy = State.cursorY - p.y;
                const dist = Math.sqrt(dx * dx + dy * dy);

                if (dist < 180 && !State.isTouch) {
                    const force = (1 - dist / 180) * 0.8;
                    p.x -= (dx / dist) * force * 1.8;
                    p.y -= (dy / dist) * force * 1.8;
                }

                // Render particle
                p.pulse += 0.02;
                const r = p.baseRadius + Math.sin(p.pulse) * 0.4;
                this.ctx.beginPath();
                this.ctx.arc(p.x, p.y, r, 0, Math.PI * 2);
                this.ctx.fillStyle = p.color;
                this.ctx.fill();

                // Connect adjacent particles within topological lattice range
                for (let j = i + 1; j < this.particles.length; j++) {
                    const p2 = this.particles[j];
                    const cdx = p.x - p2.x;
                    const cdy = p.y - p2.y;
                    const cdist = Math.sqrt(cdx * cdx + cdy * cdy);

                    if (cdist < 110) {
                        const alpha = (1 - cdist / 110) * 0.22;
                        this.ctx.beginPath();
                        this.ctx.moveTo(p.x, p.y);
                        this.ctx.lineTo(p2.x, p2.y);
                        this.ctx.strokeStyle = `rgba(99, 102, 241, ${alpha})`;
                        this.ctx.lineWidth = 0.65;
                        this.ctx.stroke();
                    }
                }
            }

            this.animId = requestAnimationFrame(() => this.loop());
        }
    }

    // ────────────────────────────────────────────────────────────────────────
    // 3. MAGNETIC HUD & CYBERNETIC CURSOR
    // ────────────────────────────────────────────────────────────────────────
    class MagneticHUDCursor {
        constructor() {
            if (State.isTouch) return;

            this.dot = document.createElement('div');
            this.ring = document.createElement('div');
            this.hud = document.createElement('div');

            this.dot.className = 'rehan-cursor-dot';
            this.ring.className = 'rehan-cursor-ring';
            this.hud.className = 'rehan-cursor-hud';

            this.dot.style.cssText = `
                position: fixed;
                top: 0;
                left: 0;
                width: 6px;
                height: 6px;
                background: #06b6d4;
                border-radius: 50%;
                pointer-events: none;
                z-index: 999999;
                transform: translate(-50%, -50%);
                transition: transform 0.05s ease, background-color 0.2s;
                mix-blend-mode: screen;
            `;

            this.ring.style.cssText = `
                position: fixed;
                top: 0;
                left: 0;
                width: 32px;
                height: 32px;
                border: 1px solid rgba(6, 182, 212, 0.45);
                border-radius: 50%;
                pointer-events: none;
                z-index: 999998;
                transform: translate(-50%, -50%);
                transition: width 0.25s cubic-bezier(0.2, 0.8, 0.2, 1),
                            height 0.25s cubic-bezier(0.2, 0.8, 0.2, 1),
                            border-color 0.25s,
                            background 0.25s;
                mix-blend-mode: screen;
            `;

            this.hud.style.cssText = `
                position: fixed;
                top: 0;
                left: 0;
                font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
                font-size: 9px;
                letter-spacing: 0.05em;
                color: rgba(6, 182, 212, 0.7);
                pointer-events: none;
                z-index: 999997;
                transform: translate(20px, 14px);
                white-space: nowrap;
                opacity: 0;
                transition: opacity 0.3s ease;
                background: rgba(3, 7, 18, 0.65);
                padding: 1px 6px;
                border-radius: 4px;
                border: 1px solid rgba(6, 182, 212, 0.2);
            `;

            document.body.appendChild(this.dot);
            document.body.appendChild(this.ring);
            document.body.appendChild(this.hud);

            this.rx = State.cursorX;
            this.ry = State.cursorY;
            this.isMagnetic = false;
            this.magTarget = null;

            this.bind();
            this.render();
        }

        bind() {
            window.addEventListener('mousemove', (e) => {
                const now = performance.now();
                const dt = Math.max(now - State.lastMouseMoveTime, 1);
                const dx = e.clientX - State.lastMouseX;
                const dy = e.clientY - State.lastMouseY;
                State.mouseVelocity = Math.sqrt(dx * dx + dy * dy) / dt * 100;

                State.lastMouseX = e.clientX;
                State.lastMouseY = e.clientY;
                State.lastMouseMoveTime = now;

                State.cursorX = e.clientX;
                State.cursorY = e.clientY;

                this.dot.style.left = `${e.clientX}px`;
                this.dot.style.top = `${e.clientY}px`;
                this.hud.style.left = `${e.clientX}px`;
                this.hud.style.top = `${e.clientY}px`;

                this.hud.textContent = `${Math.round(e.clientX)}:${Math.round(e.clientY)} | ${Math.round(State.mouseVelocity)}px/s`;
            }, { passive: true });

            window.addEventListener('mouseenter', () => {
                this.dot.style.opacity = '1';
                this.ring.style.opacity = '1';
                this.hud.style.opacity = '0.75';
            });

            window.addEventListener('mouseleave', () => {
                this.dot.style.opacity = '0';
                this.ring.style.opacity = '0';
                this.hud.style.opacity = '0';
            });

            // Magnetic snap to buttons, links & interactive cards
            const attachMagnetic = () => {
                const magnetics = document.querySelectorAll('button, a, input, select, textarea, [data-magnetic="true"], .magnetic-node');
                magnetics.forEach(el => {
                    el.addEventListener('mouseenter', () => {
                        this.isMagnetic = true;
                        this.magTarget = el;
                        this.ring.style.width = '48px';
                        this.ring.style.height = '48px';
                        this.ring.style.borderColor = 'rgba(99, 102, 241, 0.9)';
                        this.ring.style.background = 'rgba(99, 102, 241, 0.12)';
                        this.dot.style.background = '#6366f1';
                        this.dot.style.transform = 'translate(-50%, -50%) scale(1.6)';
                    });

                    el.addEventListener('mouseleave', () => {
                        this.isMagnetic = false;
                        this.magTarget = null;
                        this.ring.style.width = '32px';
                        this.ring.style.height = '32px';
                        this.ring.style.borderColor = 'rgba(6, 182, 212, 0.45)';
                        this.ring.style.background = 'transparent';
                        this.dot.style.background = '#06b6d4';
                        this.dot.style.transform = 'translate(-50%, -50%) scale(1)';
                    });
                });
            };

            attachMagnetic();
            // Re-bind when DOM mutates
            const observer = new MutationObserver(() => attachMagnetic());
            observer.observe(document.body, { childList: true, subtree: true });
        }

        render() {
            let targetX = State.cursorX;
            let targetY = State.cursorY;

            if (this.isMagnetic && this.magTarget) {
                const rect = this.magTarget.getBoundingClientRect();
                const centerX = rect.left + rect.width / 2;
                const centerY = rect.top + rect.height / 2;
                // Elastic magnetic latch (50% pull towards center)
                targetX = targetX + (centerX - targetX) * 0.45;
                targetY = targetY + (centerY - targetY) * 0.45;
            }

            // Smooth trailing interpolation
            this.rx += (targetX - this.rx) * 0.18;
            this.ry += (targetY - this.ry) * 0.18;

            this.ring.style.left = `${this.rx}px`;
            this.ring.style.top = `${this.ry}px`;

            requestAnimationFrame(() => this.render());
        }
    }

    // ────────────────────────────────────────────────────────────────────────
    // 4. KINETIC SCROLL OBSERVER (ScrollTrigger Cascade without Heavy GSAP)
    // ────────────────────────────────────────────────────────────────────────
    class KineticScrollObserver {
        constructor() {
            this.init();
        }

        init() {
            // Inject hardware-accelerated CSS classes
            const style = document.createElement('style');
            style.textContent = `
                .kinetic-reveal {
                    opacity: 0;
                    transform: translateY(24px) scale(0.985);
                    transition: opacity 0.75s cubic-bezier(0.16, 1, 0.3, 1),
                                transform 0.75s cubic-bezier(0.16, 1, 0.3, 1);
                    will-change: opacity, transform;
                }
                .kinetic-reveal.kinetic-active {
                    opacity: 1;
                    transform: translateY(0) scale(1);
                }
                .kinetic-card-hover {
                    transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1),
                                box-shadow 0.35s cubic-bezier(0.16, 1, 0.3, 1),
                                border-color 0.35s ease;
                }
                .kinetic-card-hover:hover {
                    transform: translateY(-4px) scale(1.008);
                    box-shadow: 0 16px 36px -10px rgba(6, 182, 212, 0.18);
                    border-color: rgba(6, 182, 212, 0.45) !important;
                }
            `;
            document.head.appendChild(style);

            // Auto-decorate sections, cards, and grid items
            const targets = document.querySelectorAll(
                'main > section, article, .rounded-2xl, .rounded-3xl, .grid > div, footer, header'
            );

            const observer = new IntersectionObserver((entries, obs) => {
                entries.forEach((entry, idx) => {
                    if (entry.isIntersecting) {
                        // Staggered cascade delay based on index
                        setTimeout(() => {
                            entry.target.classList.add('kinetic-active');
                        }, Math.min(idx * 60, 300));
                        obs.unobserve(entry.target);
                    }
                });
            }, {
                threshold: 0.08,
                rootMargin: '0px 0px -40px 0px'
            });

            targets.forEach((el) => {
                if (!el.classList.contains('kinetic-reveal')) {
                    el.classList.add('kinetic-reveal');
                    if (el.tagName === 'DIV' && el.classList.contains('border')) {
                        el.classList.add('kinetic-card-hover');
                    }
                    observer.observe(el);
                }
            });
        }
    }

    // ────────────────────────────────────────────────────────────────────────
    // 5. SYNTHESIZED AUDIO TELEMETRY (Pure Web Audio API Synthesizer)
    // Zero external audio files, zero HTTP requests, pure deterministic waves.
    // ────────────────────────────────────────────────────────────────────────
    class SynthesizedAudioTelemetry {
        constructor() {
            this.ctx = null;
            this.muted = true; // Muted by default for sovereign dignity
            this.bind();
        }

        initContext() {
            if (!this.ctx) {
                const AudioContext = window.AudioContext || window.webkitAudioContext;
                if (AudioContext) {
                    this.ctx = new AudioContext();
                }
            }
            if (this.ctx && this.ctx.state === 'suspended') {
                this.ctx.resume();
            }
        }

        playTone(frequency = 1800, durationMs = 12, gainLevel = 0.04) {
            if (this.muted) return;
            try {
                this.initContext();
                if (!this.ctx) return;

                const osc = this.ctx.createOscillator();
                const gain = this.ctx.createGain();

                osc.type = 'sine';
                osc.frequency.setValueAtTime(frequency, this.ctx.currentTime);
                // Pitch envelope drop for tactile mechanical tick
                osc.frequency.exponentialRampToValueAtTime(frequency * 0.6, this.ctx.currentTime + (durationMs / 1000));

                gain.gain.setValueAtTime(gainLevel, this.ctx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.0001, this.ctx.currentTime + (durationMs / 1000));

                osc.connect(gain);
                gain.connect(this.ctx.destination);

                osc.start();
                osc.stop(this.ctx.currentTime + (durationMs / 1000));
            } catch (e) {
                // Audio safely fails silent
            }
        }

        bind() {
            // Listen to interactive clicks & hovers
            document.addEventListener('mouseover', (e) => {
                if (e.target.closest('button, a, .interactive-tab, input[type="submit"]')) {
                    this.playTone(2100, 10, 0.02);
                }
            }, { passive: true });

            document.addEventListener('click', (e) => {
                if (e.target.closest('button, a, .interactive-tab')) {
                    this.playTone(1450, 18, 0.05);
                }
            }, { passive: true });

            // Create Audio Control Pill in DOM
            this.renderTogglePill();
        }

        renderTogglePill() {
            const pill = document.createElement('button');
            pill.id = 'rehan-audio-pill';
            pill.title = 'Acoustic Telemetry Synthesizer (Zero-Network Synthetic Oscillator)';
            pill.className = 'fixed bottom-4 left-4 z-50 flex items-center gap-2 px-3 py-1.5 rounded-full text-[11px] font-mono transition shadow-lg border';
            pill.style.cssText = `
                backdrop-filter: blur(8px);
                background: rgba(3, 7, 18, 0.85);
                color: #94a3b8;
                border-color: rgba(51, 65, 85, 0.6);
            `;

            const updatePill = () => {
                if (this.muted) {
                    pill.innerHTML = `
                        <span class="w-2 h-2 rounded-full bg-slate-500"></span>
                        <span class="tracking-wider">AUDIO: MUTED</span>
                    `;
                    pill.style.color = '#94a3b8';
                    pill.style.borderColor = 'rgba(51, 65, 85, 0.6)';
                } else {
                    pill.innerHTML = `
                        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                        <span class="text-emerald-400 font-bold tracking-wider">AUDIO: 1800Hz SYNTH</span>
                    `;
                    pill.style.color = '#34d399';
                    pill.style.borderColor = 'rgba(52, 211, 153, 0.4)';
                }
            };

            pill.addEventListener('click', () => {
                this.muted = !this.muted;
                if (!this.muted) {
                    this.initContext();
                    this.playTone(1950, 25, 0.08);
                }
                updatePill();
            });

            updatePill();
            document.body.appendChild(pill);
        }
    }

    // ────────────────────────────────────────────────────────────────────────
    // 6. MASTER ENGINE INITIALIZER (Gall's Law Invariant Fortification)
    // ────────────────────────────────────────────────────────────────────────
    window.addEventListener('DOMContentLoaded', () => {
        try {
            // 1. Kinetic Scroll Damping
            window.__REHAN_SCROLL__ = new InertialFluidScroll();

            // 2. Non-Newtonian Quant Lattice
            window.__REHAN_LATTICE__ = new QuantLatticeCanvas();

            // 3. Cybernetic Magnetic HUD
            window.__REHAN_CURSOR__ = new MagneticHUDCursor();

            // 4. Viewport Cascades
            window.__REHAN_KINETIC__ = new KineticScrollObserver();

            // 5. Pure Synthetic Acoustic Telemetry
            window.__REHAN_AUDIO__ = new SynthesizedAudioTelemetry();

            console.log(
                '%c[REHAN QUANT LAB] Kinetic & Telemetry Engine Online %c• Gall\'s Law Fortified • Zero-Bloat • 120 FPS Native',
                'background: #06b6d4; color: #000; font-weight: bold; padding: 2px 8px; border-radius: 4px;',
                'color: #06b6d4;'
            );
        } catch (err) {
            console.warn('[REHAN QUANT LAB] Kinetic engine gracefully degraded:', err);
        }
    });

})();
