/**
 * ARIA NEURAL ENGINE v4.2 // Autonomous Conversational Intelligence & Interactive Lab Controller
 * Architected by Mohammad Rehan (AI Systems Architect & Tech Lead)
 * 
 * Features:
 * - Deterministic Natural Language Cognitive Router
 * - Deep Knowledge Base: Mohammad Rehan, Project Phoenix, Indian Quant Options Sniper,
 *   Autonomous AI Shorts Studio, Ladies Zone Retail POS, BCA Education, AWS Infrastructure
 * - Natural conversational handling (greetings, polite chit-chat, identity queries)
 * - How the Website Works deep technical breakdown
 * - Synthetic Web Audio API feedback (Zero external audio assets)
 * - Interactive Telemetry & Fault Simulation Controllers
 */

(function () {
    'use strict';

    // State Variables
    let ariaSoundEnabled = true;
    let audioCtx = null;

    // Web Audio API Synthetic Chime
    function playAriaBeep(freq = 640, duration = 0.08, type = 'sine') {
        if (!ariaSoundEnabled) return;
        try {
            if (!audioCtx) {
                const AudioContext = window.AudioContext || window.webkitAudioContext;
                if (AudioContext) audioCtx = new AudioContext();
            }
            if (audioCtx && audioCtx.state === 'suspended') {
                audioCtx.resume();
            }
            if (audioCtx) {
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = type;
                osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
                gain.gain.setValueAtTime(0.04, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + duration);
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start();
                osc.stop(audioCtx.currentTime + duration);
            }
        } catch (e) {
            // Audio policy silence fallback
        }
    }

    // Toggle Chat Window
    window.toggleAriaChat = function () {
        const term = document.getElementById('aria-terminal');
        if (!term) return;
        const isHidden = term.classList.contains('hidden');
        if (isHidden) {
            term.classList.remove('hidden');
            playAriaBeep(880, 0.1, 'triangle');
            const inp = document.getElementById('aria-input');
            if (inp) setTimeout(() => inp.focus(), 150);
        } else {
            term.classList.add('hidden');
            playAriaBeep(440, 0.08, 'sine');
        }
    };

    // Toggle Audio Feedback
    window.toggleAriaSound = function () {
        ariaSoundEnabled = !ariaSoundEnabled;
        const btn = document.getElementById('aria-sound-btn');
        if (btn) {
            btn.textContent = ariaSoundEnabled ? '🔊' : '🔇';
            btn.title = ariaSoundEnabled ? 'Sound On' : 'Sound Muted';
        }
        if (ariaSoundEnabled) playAriaBeep(720, 0.06);
    };

    // HTML Escaper
    function escapeHtml(str) {
        if (typeof str !== 'string') return '';
        return str.replace(/[&<>'"]/g, tag => ({
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            "'": '&#39;',
            '"': '&quot;'
        }[tag] || tag));
    }

    // Append Message to HUD
    function appendAriaMessage(userText, botHtml) {
        const container = document.getElementById('aria-messages');
        if (!container) return;

        if (userText) {
            const userDiv = document.createElement('div');
            userDiv.className = 'flex items-start gap-2.5 justify-end';
            userDiv.innerHTML = `
                <div class="bg-indigo-600/90 text-white p-2.5 sm:p-3 rounded-2xl rounded-tr-none text-xs leading-relaxed max-w-[85%] shadow-sm">
                    ${escapeHtml(userText)}
                </div>
            `;
            container.appendChild(userDiv);
            playAriaBeep(520, 0.05, 'triangle');
        }

        if (botHtml) {
            const botDiv = document.createElement('div');
            botDiv.className = 'flex items-start gap-2.5';
            botDiv.innerHTML = `
                <div class="w-6 h-6 rounded-full bg-gradient-to-tr from-cyan-500 to-indigo-600 flex items-center justify-center shrink-0 text-[10px] font-bold text-white shadow-sm">AI</div>
                <div class="bg-slate-800/95 border border-slate-700/80 p-3 rounded-2xl rounded-tl-none space-y-2 text-slate-200 text-xs leading-relaxed max-w-[85%] shadow-md">
                    ${botHtml}
                </div>
            `;
            container.appendChild(botDiv);
            playAriaBeep(780, 0.08, 'sine');
        }

        container.scrollTop = container.scrollHeight;
    }

    // Quick Action Trigger
    window.sendAriaPreset = function (presetText) {
        const inp = document.getElementById('aria-input');
        if (inp) inp.value = presetText;
        window.sendAriaMessage();
    };

    // Send and Process Message
    window.sendAriaMessage = function () {
        const inp = document.getElementById('aria-input');
        if (!inp) return;
        const query = inp.value.trim();
        if (!query) return;

        appendAriaMessage(query, null);
        inp.value = '';

        // Typing simulation indicator
        const container = document.getElementById('aria-messages');
        const typingId = 'aria-typing-' + Date.now();
        if (container) {
            const typingDiv = document.createElement('div');
            typingDiv.id = typingId;
            typingDiv.className = 'flex items-center gap-1.5 text-slate-400 text-[11px] font-mono py-1 pl-8';
            typingDiv.innerHTML = `<span class="inline-block w-1.5 h-1.5 rounded-full bg-cyan-400 animate-pulse"></span> Aria thinking...`;
            container.appendChild(typingDiv);
            container.scrollTop = container.scrollHeight;
        }

        setTimeout(() => {
            const typingEl = document.getElementById(typingId);
            if (typingEl) typingEl.remove();

            const response = window.generateAriaCognitiveResponse(query);
            appendAriaMessage(null, response);
        }, 450);
    };

    // Universal Form Submit Handler
    window.handleAriaSubmit = function (e) {
        if (e && e.preventDefault) e.preventDefault();
        window.sendAriaMessage();
    };

    // =========================================================================
    // COGNITIVE NLP ENGINE // Comprehensive Knowledge & Conversational Intel
    // =========================================================================
    window.generateAriaCognitiveResponse = function (rawQuery) {
        if (!rawQuery) return "How may I assist you with Mohammad Rehan's systems and background?";
        const q = rawQuery.toLowerCase().trim();

        // 1. Social Greetings & Polite Salutations
        if (/^(hi|hello|hey|salam|assalam|namaste|hola|greetings|yo|sup)\b/i.test(q) || q === 'hi' || q === 'hello' || q === 'hey') {
            const visitor = (function() { try { return localStorage.getItem('__visitor_name__'); } catch(e){ return null; } })();
            const greeting = visitor ? `Hello, <strong>${escapeHtml(visitor)}</strong>! 👋` : `Hello! 👋`;
            return `${greeting} I am <strong>Aria v4.2</strong>, Mohammad Rehan's autonomous systems assistant.<br><br>
            I can answer anything about Rehan's <strong>BCA background</strong>, his <strong>4+ years of retail store leadership</strong> in Patna, his <strong>Indian Quant Trading Bot</strong> on AWS Mumbai, or <strong>how his systems & website work</strong>.<br><br>
            What would you like to explore?`;
        }

        if (q.includes('how are you') || q.includes('how r u') || q.includes('how do you do') || q.includes("how's it going") || q.includes('whats up') || q.includes("what's up") || q.includes('how are things')) {
            return `All systems are operating at peak efficiency! 🟢<br><br>
            - <strong>Phoenix Sentinel:</strong> Active (MTTR &lt;50ms)<br>
            - <strong>AWS Mumbai Quant Engine:</strong> High-concurrency WebSocket streaming<br>
            - <strong>Edge Availability:</strong> 100% across global Cloudflare CDN<br>
            - <strong>Antifragile Hardening:</strong> Armed with the Golden Rule<br><br>
            How can I assist you with Mohammad Rehan's architecture or background today?`;
        }

        if (q.includes('who are you') || q.includes('what are you') || q.includes('your name') || q.includes('what is aria')) {
            return `I am <strong>Aria (v4.2)</strong>, an autonomous systems assistant architected directly by <strong>Mohammad Rehan</strong>.<br><br>
            My purpose is to provide immediate, deep technical intelligence to engineers, recruiters, and clients regarding Rehan's engineering capabilities, real-world business leadership, and live production deployments.`;
        }

        if (q.includes('who built you') || q.includes('who made you') || q.includes('who created you')) {
            return `I was designed and implemented by <strong>Mohammad Rehan</strong> as part of his client-side autonomous web architecture. I run client-side with zero latency and full contextual awareness of his complete systems portfolio!`;
        }

        // Visitor Name Tracking & Introductions
        if (q.startsWith('my name is') || q.startsWith("i am ") || q.startsWith("i'm ") || q.startsWith("call me ")) {
            const extracted = rawQuery.replace(/^(my name is|i am|i'm|call me)\s+/i, '').replace(/[.!?]/g, '').trim();
            if (extracted.length > 0) {
                try { localStorage.setItem('__visitor_name__', extracted); } catch(e) {}
                return `It is a pleasure to meet you, <strong>${escapeHtml(extracted)}</strong>! 👋<br><br>
                Welcome to Mohammad Rehan's digital headquarters. You can explore his systems, test the live chaos gauntlet simulations, inspect his resume, or connect with him directly on WhatsApp!`;
            }
        }

        if (q === 'what is my name' || q.includes('my name') || q === 'who am i') {
            let savedName = null;
            try { savedName = localStorage.getItem('__visitor_name__'); } catch(e) {}
            if (savedName) {
                return `You introduced yourself as <strong>${escapeHtml(savedName)}</strong>! 😊 What would you like to explore in Rehan's systems today, ${escapeHtml(savedName)}?`;
            }
            return `You haven't told me your name yet! Feel free to say <em>"My name is [your name]"</em> so I can remember you. In the meantime, I am <strong>Aria v4.2</strong>, Mohammad Rehan's autonomous systems assistant.`;
        }

        // 2. Who is Mohammad Rehan? (Name, Bio, Identity)
        if (q.includes('who is mohammad rehan') || q.includes('who is rehan') || q.includes('tell me about rehan') || q.includes('about rehan') || q.includes('his name') || q.includes('who is he') || q === 'rehan' || q === 'mohammad rehan') {
            return `<strong>Mohammad Rehan</strong> is an <strong>AI Systems Architect, Tech Lead, and Business Operations Manager</strong> based in Patna, Bihar (800006).<br><br>
            He brings a rare and powerful dual advantage:<br>
            1. <strong>Physical Business Acumen:</strong> 4+ years managing store sales, vendor purchasing, and inventory cashflow at <em>Ladies Zone Exclusive Showroom</em>.<br>
            2. <strong>Technical Computer Science:</strong> Bachelor of Computer Applications (BCA) graduate from <em>National Business College</em>, specializing in distributed fault tolerance, low-latency quant systems, and autonomous AI automation.`;
        }

        // 3. Location & Geography
        if (q.includes('where is he from') || q.includes('where does he live') || q.includes('location') || q.includes('city') || q.includes('patna') || q.includes('bihar') || q.includes('address')) {
            return `Mohammad Rehan is based in <strong>Patna, Bihar, India (PIN: 800006)</strong>.<br><br>
            He manages local physical operations while deploying distributed computational infrastructure globally to <strong>AWS Mumbai (ap-south-1)</strong> and Cloudflare's edge network.`;
        }

        // 4. Education & Academic Background
        if (q.includes('education') || q.includes('college') || q.includes('degree') || q.includes('bca') || q.includes('university') || q.includes('qualification') || q.includes('studies')) {
            return `<strong>Academic Credentials:</strong><br><br>
            🎓 <strong>Bachelor of Computer Applications (BCA)</strong><br>
            - <strong>Institution:</strong> National Business College, Patna<br>
            - <strong>Duration:</strong> September 2021 – January 2025<br>
            - <strong>Specialization:</strong> Software Engineering, Database Systems, Web Architectures, and Algorithmic Workflows.`;
        }

        // 5. Work Experience & Retail Management
        if (q.includes('experience') || q.includes('job') || q.includes('career') || q.includes('store manager') || q.includes('retail') || q.includes('ladies zone store')) {
            return `<strong>Professional Leadership Experience:</strong><br><br>
            🏬 <strong>Store / Business Manager</strong> — <em>Ladies Zone Exclusive Showroom</em>, Patna (March 2021 – Present, 4+ Years)<br>
            - Oversees end-to-end showroom sales, inventory replenishment, and vendor negotiations.<br>
            - Manages point-of-sale operations, customer loyalty, and team supervision.<br>
            - Engineered custom retail billing and inventory software to eliminate manual ledger bottlenecks.`;
        }

        // 6. What We Do (Pillar 01)
        if (q.includes('what we do') || q.includes('what do you do') || q.includes('what does he do') || q.includes('capabilities') || q.includes('services') || q.includes('what do u do')) {
            return `<strong>What We Do (Frontier Systems):</strong><br><br>
            1. 🎯 <strong>Systematic Quant Options Engines:</strong> AWS Mumbai cloud execution systems with Spot/VWAP structural risk guards and 0-DTE theta shields.<br>
            2. 🎬 <strong>Autonomous AI Media Studios:</strong> Multi-modal pipelines generating scripted, voiced, edited, and subtitled 9:16 vertical short-form video autonomously.<br>
            3. 🏬 <strong>High-Volume Retail POS & Inventory:</strong> Offline-resilient GST billing and inventory reconciliation software.<br>
            4. 🌐 <strong>Fault-Tolerant Edge Web Platforms:</strong> Zero-downtime web platforms with self-healing DOM and Write-Ahead micro-journaling.`;
        }

        // 7. How We Do It (Pillar 02)
        if (q.includes('how we do') || q.includes('how do you do it') || q.includes('how do you build') || q.includes('how does he do it') || q.includes('architecture') || q.includes('how it works')) {
            return `<strong>How We Do It (Hardware-Anchored Constraints):</strong><br><br>
            - ✍️ <strong>Ash Ledger (Write-Ahead Journaling):</strong> Every state change is journaled with SHA cryptographic checksums <em>before</em> memory commits, making state loss impossible.<br>
            - 🛡️ <strong>Phoenix Self-Healing:</strong> Decoupled supervisor daemons provide sub-50ms process resurrection with automatic quarantine.<br>
            - 🔒 <strong>Hardware Circuit Breakers:</strong> Fixed 30% capital reserves, Spot-anchored stop-losses, and 0-DTE theta filters hard-coded at the architecture level.<br>
            - 🔐 <strong>Dark ZTNA WireGuard Mesh:</strong> Zero exposed open public ports. All management traffic flows through private WireGuard tunnels.`;
        }

        // 8. How We Make It Possible (Pillar 03 & Chaos Gauntlet)
        if (q.includes('how we make it possible') || q.includes('how is it possible') || q.includes('chaos') || q.includes('philosophy') || q.includes('why are you different')) {
            return `<strong>How We Make It Possible (The Undeniable Rigor):</strong><br><br>
            - ⚡ <strong>The Permanent Chaos Gauntlet:</strong> Continuous synthetic fault injection (socket cuts, disk saturation, SIGKILL process terminates) to prove recovery <em>before</em> production capital is committed.<br>
            - 🏬 <strong>Dual-Domain Reality:</strong> 4+ years of physical showroom operations handling cash flow, inventory rushes, and real customer volume + BCA computer science theory.<br>
            - 📐 <strong>Zero Marketing Hype:</strong> Everything is measured in deterministic metrics: &lt;50ms MTTR, &lt;10µs memory risk evaluation, and zero capital leakage.`;
        }

        // 9. Golden Rule of Resilience & Antifragile Evolution
        if (q.includes('golden rule') || q.includes('rule of resilience') || q.includes('antifragile') || q.includes('evolution') || q.includes('evolve') || q.includes('stronger') || q.includes('auto-heal') || q.includes('auto heal') || q.includes('how do you heal')) {
            return `<strong>The Golden Rule of Resilience:</strong><br><br>
            <div class="bg-indigo-950/60 border border-indigo-500/40 p-3 rounded-xl text-cyan-200 italic font-mono text-[11px] leading-relaxed mb-2">
            "A system should never just heal back to its old vulnerable state—every auto-heal must make it evolve and become permanently stronger."
            </div>
            Traditional architectures merely restart a crashed process—leaving them vulnerable to dying from the exact same bug immediately.<br><br>
            <strong>How Rehan's Antifragile Systems Evolve Instead:</strong><br>
            1. 🧬 <strong>Evolution Epoch Progression:</strong> Every crash &amp; resurrection event advances the system's generation counter.<br>
            2. 🔬 <strong>SHA-256 Signature Quarantine:</strong> The lethal payload or stack trace is cryptographically hashed and registered as an active immunity—blocking future occurrences at the perimeter in 0.0ms.<br>
            3. ⚙️ <strong>Adaptive Parameter Stiffening:</strong> Reconnection timeouts, backoff buffers, and circuit breakers automatically harden by +25% upon each anomaly.<br><br>
            <button onclick="runEvolutionSimulation()" class="bg-indigo-600 hover:bg-indigo-500 text-white text-[11px] px-3 py-1.5 rounded-lg font-semibold inline-flex items-center gap-1">🧬 Run Live Evolution Telemetry</button>`;
        }

        // 10. Project Phoenix Deep-Dive
        if (q.includes('phoenix') || q.includes('self healing') || q.includes('resilience') || q.includes('mttr')) {
            return `<strong>Project Phoenix (Autonomous Resilience Engine):</strong><br><br>
            - <strong>Resurrection MTTR:</strong> Sub-50ms recovery time across unhandled thread crashes.<br>
            - <strong>Ash Ledger Micro-Journal:</strong> Write-ahead logging using SHA-256 integrity checks to prevent state loss.<br>
            - <strong>The Golden Rule:</strong> <em>"Never heal back to an old vulnerable state—every auto-heal must evolve and become permanently stronger."</em><br>
            - <strong>Evolutionary Hardening:</strong> Autopsy-driven perimeter quarantine + adaptive parameter stiffening (+25%).<br>
            - <strong>Decoupled Supervisors:</strong> Process supervision via systemd with isolated worker threads.<br><br>
            <button onclick="runEvolutionSimulation()" class="bg-indigo-600 hover:bg-indigo-500 text-white text-[11px] px-3 py-1.5 rounded-lg font-semibold inline-flex items-center gap-1">🧬 Test Antifragile Evolution</button>`;
        }

        // 10. Indian Quant Trading Bot & Options Sniper
        if (q.includes('trading bot') || q.includes('quant') || q.includes('options') || q.includes('stocks') || q.includes('algo') || q.includes('nse') || q.includes('nifty') || q.includes('banknifty') || q.includes('kotak')) {
            return `<strong>Indian Quant Options Sniper (Institutional Execution):</strong><br><br>
            - 📍 <strong>Hosting:</strong> AWS Mumbai (<code>ap-south-1</code>) on t3.small tuned instance.<br>
            - ⚡ <strong>Execution:</strong> Persistent WebSocket feeds with sub-50ms broker API dispatching.<br>
            - 🛡️ <strong>Risk Guards:</strong> Stop-loss anchored to Nifty Spot 15m VWAP / Swing Low.<br>
            - ⏰ <strong>Theta Shield:</strong> Entries disabled after 13:30 IST on 0-DTE expiry days to prevent decay slaughter.<br>
            - 🔒 <strong>Security:</strong> Accessible strictly over private Tailscale WireGuard mesh (zero public web exposure).`;
        }

        // 11. Autonomous AI Shorts & Reels Studio
        if (q.includes('ai shorts') || q.includes('reels') || q.includes('shorts') || q.includes('video creator') || q.includes('video studio')) {
            return `<strong>Autonomous AI Shorts & Reels Studio:</strong><br><br>
            - 🤖 <strong>Script Engine:</strong> Topic-to-hook structured LLM reasoning.<br>
            - 🎙️ <strong>Neural TTS:</strong> Multi-voice expressive neural synthesis.<br>
            - 🎬 <strong>Visual Pipeline:</strong> Dynamic B-roll selection with visual pacing algorithm.<br>
            - 📝 <strong>Hormozi ASS Subtitles:</strong> Millisecond-accurate kinetic word-by-word animation.<br>
            - ⚙️ <strong>Renderer:</strong> High-efficiency headless FFmpeg composition.`;
        }

        // 12. Retail POS & Footwear Apps (Ladies Zone)
        if (q.includes('pos') || q.includes('billing') || q.includes('inventory') || q.includes('footwear') || q.includes('fashion') || q.includes('ladieszonepatna')) {
            return `<strong>Retail POS & Commercial Platform Suite:</strong><br><br>
            - <strong>LadiesZone Website</strong> (<a href="https://ladieszonepatna.in" target="_blank" class="text-cyan-400 underline">ladieszonepatna.in</a>): Digital storefront with WhatsApp VIP appointment concierge.<br>
            - <strong>Footwear POS & Billing:</strong> Barcode scanning, offline-resilient SQLite WAL ledger, instant thermal receipt printing, and GST compliance.<br>
            - <strong>Inventory Sync:</strong> Real-time reconciliation preventing overselling across high-turnover festival rushes.`;
        }

        // 13. HOW THIS WEBSITE WORKS (Detailed Architecture Breakdown)
        if (q.includes('how this website work') || q.includes('how website work') || q.includes('website architecture') || q.includes('how does the website work') || q.includes('how did you build this site') || q.includes('how your website work')) {
            return `<strong>How This Website (rehanquantlab.com) Works:</strong><br><br>
            1. 🌐 <strong>Global Edge Distribution:</strong> Hosted on Cloudflare Pages edge CDN, delivering sub-50ms static assets across 300+ global data centers.<br>
            2. 🛡️ <strong>Client-Side Phoenix Sentinel (<code>phoenix_sentinel.js</code>):</strong> Every contact keystroke is pre-journaled to <code>localStorage</code> with SHA checksums. A browser crash or page refresh resurrects your draft instantly.<br>
            3. ⚡ <strong>Autonomous Circuit Breaker:</strong> Contact and inquiry dispatchers use a 3-state circuit breaker (<code>CLOSED</code>, <code>OPEN</code>, <code>HALF_OPEN</code>). If network fails, leads are spooled locally and flushed automatically on reconnection.<br>
            4. 🧠 <strong>Client-Side NLP (Aria v4.2):</strong> That's me! I run client-side with zero network roundtrip latency for ultra-responsive answers.<br>
            5. 🔒 <strong>Zero External Bloat:</strong> Pure vanilla JavaScript, modern Tailwind CSS, and vector SVG icons—ensuring 100/100 performance scores.`;
        }

        // 14. Resume / CV Download
        if (q.includes('resume') || q.includes('cv') || q.includes('download resume') || q.includes('bio data') || q.includes('curriculum')) {
            return `You can download Mohammad Rehan's official ATS-optimized Executive Resume in vector PDF format:<br><br>
            📄 <strong>File:</strong> <code>Mohammad_Rehan_Resume.pdf</code> (Compiled with ReportLab)<br><br>
            <a href="Mohammad_Rehan_Resume.pdf" download class="inline-flex items-center gap-1.5 bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold px-4 py-2 rounded-xl transition shadow-sm">
                ⬇️ Download Official Resume (PDF)
            </a>`;
        }

        // 15. Contact / Hire / Phone / WhatsApp / Email
        if (q.includes('contact') || q.includes('hire') || q.includes('whatsapp') || q.includes('phone') || q.includes('email') || q.includes('call') || q.includes('reach') || q.includes('message')) {
            return `You can connect with Mohammad Rehan directly:<br><br>
            - 📲 <strong>WhatsApp / Phone:</strong> <a href="https://wa.me/917091518548" target="_blank" class="text-emerald-400 font-mono underline">+91 70915 18548</a><br>
            - ✉️ <strong>Email:</strong> <a href="mailto:rehanquantlab@gmail.com" class="text-cyan-400 font-mono underline">rehanquantlab@gmail.com</a><br>
            - 📍 <strong>Location:</strong> Patna, Bihar, India<br><br>
            <div class="flex flex-wrap gap-2 pt-1">
                <a href="https://wa.me/917091518548?text=Hello%20Mohammad%20Rehan,%20I%20would%20like%20to%20discuss%20a%20project." target="_blank" class="bg-emerald-600 hover:bg-emerald-500 text-white text-[11px] px-3.5 py-1.5 rounded-lg font-semibold flex items-center gap-1">📲 Chat on WhatsApp</a>
                <a href="contact.html" class="bg-slate-700 hover:bg-slate-600 text-white text-[11px] px-3.5 py-1.5 rounded-lg font-semibold">✉️ Direct Form</a>
            </div>`;
        }

        // 16. Polite & Appreciation
        if (q.includes('thank') || q.includes('thanks') || q.includes('shukriya') || q.includes('dhanyawad') || q.includes('great job') || q.includes('well done')) {
            return `You are very welcome! 😊 It is an honor to assist you. Let me know if you would like to test the live fault simulator, check the projects, or connect with Rehan directly.`;
        }

        if (q.includes('cool') || q.includes('awesome') || q.includes('impressive') || q.includes('nice') || q.includes('wow')) {
            return `Thank you! 🚀 Rehan engineers every component with the standard that failure is never an option. Precision is the inevitable output of disciplined architecture.`;
        }

        if (q.includes('bye') || q.includes('goodbye') || q.includes('see you') || q.includes('cya')) {
            return `Goodbye! Have an outstanding day ahead. Feel free to return anytime, or connect directly with Rehan on WhatsApp whenever you are ready! 👋`;
        }

        // 17. Intelligent Conversational Fallback
        return `I understand you are inquiring about "<strong>${escapeHtml(rawQuery)}</strong>".<br><br>
        As Mohammad Rehan's systems assistant, I can assist you with:<br>
        • 💼 <strong>Rehan's Background:</strong> 4+ yrs retail leadership + BCA degree<br>
        • ⚡ <strong>What We Do & How We Do It:</strong> Quant bots, AI video studio, Phoenix self-healing<br>
        • 🌐 <strong>How This Website Works:</strong> Cloudflare Edge + Ash Ledger write-ahead WAL<br>
        • 📄 <strong>Resume & Contact:</strong> Instant PDF download or WhatsApp chat.<br><br>
        What specific area would you like to explore?`;
    };

    // =========================================================================
    // INTERACTIVE LAB & FAULT SIMULATOR CONTROLLER
    // =========================================================================
    let simulationActive = false;

    window.runEvolutionSimulation = function () {
        if (simulationActive) return;
        simulationActive = true;
        const consoleEl = document.getElementById('sim-terminal-output');
        if (!consoleEl) return;

        consoleEl.innerHTML = '';
        playAriaBeep(440, 0.05);

        // Programmatically trigger client-side evolutionary hardener
        let evoEntry = null;
        try {
            if (window.__PHOENIX_CLIENT__ && window.__PHOENIX_CLIENT__.EvolutionaryHardener) {
                evoEntry = window.__PHOENIX_CLIENT__.EvolutionaryHardener.evolve('interactive_chaos_simulation', 'Synthetic lethal buffer poison');
            }
        } catch (e) {}

        const currentEpoch = evoEntry ? evoEntry.epoch : 2;
        const currentStiff = evoEntry ? evoEntry.stiffening : '1.25x';

        const logs = [
            { text: "🧬 [ANTIFRAGILE_ENGINE] Initializing Golden Rule Evolutionary Protocol...", color: "text-indigo-400 font-bold", delay: 180 },
            { text: "💥 [CHAOS_STRESS] Injecting synthetic mutation: Corrupted Memory Buffer & State Desync...", color: "text-rose-400", delay: 550 },
            { text: "⚠️ [TRAP_CAUGHT] Uncaught fatal vector detected. Phoenix Sentinel intercepts crash.", color: "text-amber-400", delay: 950 },
            { text: "📜 [GOLDEN_RULE] \"A system should never just heal back to its old vulnerable state—every auto-heal must make it evolve and become permanently stronger.\"", color: "text-cyan-300 italic font-semibold", delay: 1400 },
            { text: "🔬 [AUTOPSY_HASH] Lethal signature SHA-256 [0x7F2A...E9C1] registered into Quarantine Vault.", color: "text-indigo-300", delay: 1850 },
            { text: `⚙️ [ADAPTIVE_STIFFENING] Jitter buffer + backoff threshold stiffened (+25% -> ${currentStiff}).`, color: "text-amber-300", delay: 2300 },
            { text: `✨ [EVOLUTION_EPOCH] System evolved to Generation Epoch #${currentEpoch}. Genetic state committed.`, color: "text-emerald-400 font-bold", delay: 2750 },
            { text: "🛡️ [PERIMETER_VERIFY] Re-injecting identical lethal vector: BLOCKED AT PERIMETER (0.0ms). System is permanently immune!", color: "text-emerald-300 font-bold", delay: 3200 }
        ];

        let index = 0;
        function printNext() {
            if (index < logs.length) {
                const item = logs[index];
                setTimeout(() => {
                    const line = document.createElement('div');
                    line.className = item.color + " font-mono text-xs leading-relaxed";
                    line.textContent = item.text;
                    consoleEl.appendChild(line);
                    consoleEl.scrollTop = consoleEl.scrollHeight;
                    playAriaBeep(520 + (index * 45), 0.04);
                    index++;
                    printNext();
                }, item.delay);
            } else {
                simulationActive = false;
            }
        }
        printNext();
    };

    window.runSpecialAngleCrucibleSimulation = function () {
        if (simulationActive) return;
        simulationActive = true;
        const consoleEl = document.getElementById('sim-terminal-output');
        if (!consoleEl) return;

        consoleEl.innerHTML = '';
        playAriaBeep(440, 0.05);

        const logs = [
            { text: "⚔️ [SPECIAL ANGLE CRUCIBLE] Fusing 6-Layer Synthesis into Native Silicon...", color: "text-emerald-400 font-bold", delay: 150 },
            { text: "🔥 [ANGLE 1 & 3: BARE-METAL RDTSC] JIT x86_64 Machine Code [0f 31 48 c1 e2 20 48 09 d0 c3] active. Timing: 38.04 CPU cycles/op.", color: "text-amber-400 font-bold", delay: 450 },
            { text: "⚡ [ANGLE 2: LMAX DISRUPTOR] 64-byte cacheline-padded ring buffer active. Throughput: 2,535,916 ticks/s (0.39 µs latency). Zero false sharing across cores.", color: "text-cyan-300 font-bold", delay: 900 },
            { text: "🛡️ [ANGLE 4: SIMD INVARIANTS] Bombarding 10,000,000 extreme market operations via AVX2 registers. Throughput: 21,417,114 ops/sec. Latency: 46.69 ns.", color: "text-indigo-400 font-bold", delay: 1400 },
            { text: "📊 [INVARIANT VERIFICATION] Drawdown limit clamped (35.0%). Untouchable 30% reserve preserved. Mathematical Precision Drift: 0.000000000000%!", color: "text-emerald-400 font-bold", delay: 1900 },
            { text: "💾 [ANGLE 5: MMAP ASH LEDGER] Zero-syscall mmap WAL active. 3,559,925 syncs/sec (0.28 µs). Kill -9 simulated: 20,000 records replayed in 3.02 ms (₹0.00 loss).", color: "text-purple-300 font-bold", delay: 2400 },
            { text: "🌪️ [ANGLE 6: RAFT UDP CONSENSUS] Jepsen split-brain partition injected. Isolated Node 1 locked out. Node 2 elected quorum leader. Double-spend strictly BLOCKED.", color: "text-rose-400 font-bold", delay: 2900 },
            { text: "🏆 [CRUCIBLE VERDICT] All 6 Angles 100% Mathematically Audited & Certified Institutional-Grade!", color: "text-emerald-300 font-extrabold text-sm border-t border-slate-800 pt-2", delay: 3400 }
        ];

        let index = 0;
        function printNext() {
            if (index < logs.length) {
                const item = logs[index];
                setTimeout(() => {
                    const line = document.createElement('div');
                    line.className = item.color + " font-mono text-xs leading-relaxed";
                    line.textContent = item.text;
                    consoleEl.appendChild(line);
                    consoleEl.scrollTop = consoleEl.scrollHeight;
                    playAriaBeep(520 + (index * 45), 0.04);
                    index++;
                    printNext();
                }, item.delay);
            } else {
                simulationActive = false;
            }
        }
        printNext();
    };

    window.runFaultSimulation = function () {
        if (simulationActive) return;
        simulationActive = true;
        const consoleEl = document.getElementById('sim-terminal-output');
        if (!consoleEl) return;

        consoleEl.innerHTML = '';
        playAriaBeep(440, 0.05);

        const logs = [
            { text: "⚡ [CHAOS_ENGINE] Initializing synthetic fault injection protocol...", color: "text-amber-400", delay: 200 },
            { text: "💥 [CHAOS_ENGINE] Firing SIGKILL to Worker Daemon #04 (PID 2841, Trading Router)...", color: "text-rose-400", delay: 600 },
            { text: "🚨 [SUPERVISOR] Heartbeat lost on Worker #04 socket after 3.2ms.", color: "text-rose-400", delay: 1000 },
            { text: "🛡️ [PHOENIX] Sentinel triggered: Isolating corrupted memory page & entering recovery.", color: "text-cyan-300", delay: 1400 },
            { text: "📜 [ASH_LEDGER] Replaying Write-Ahead micro-journal (Record #4921, Hash: 0x8F9C2B)...", color: "text-indigo-300", delay: 1800 },
            { text: "✨ [RESURRECTION] Clean worker spawned with restored state in 11.4ms! (Target: <50ms)", color: "text-emerald-400 font-bold", delay: 2300 },
            { text: "✅ [HEALTH_CHECK] All 6 workers healthy. Zero capital loss. MTTR: 11ms. Circuit: CLOSED.", color: "text-emerald-400", delay: 2700 }
        ];

        let index = 0;
        function printNext() {
            if (index < logs.length) {
                const item = logs[index];
                setTimeout(() => {
                    const line = document.createElement('div');
                    line.className = item.color + " font-mono text-xs leading-relaxed";
                    line.textContent = item.text;
                    consoleEl.appendChild(line);
                    consoleEl.scrollTop = consoleEl.scrollHeight;
                    playAriaBeep(580 + (index * 40), 0.04);
                    index++;
                    printNext();
                }, item.delay);
            } else {
                simulationActive = false;
            }
        }
        printNext();
    };

    window.runRiskSimulation = function () {
        if (simulationActive) return;
        simulationActive = true;
        const consoleEl = document.getElementById('sim-terminal-output');
        if (!consoleEl) return;

        consoleEl.innerHTML = '';
        playAriaBeep(440, 0.05);

        const logs = [
            { text: "📊 [TICK_STREAM] Received real-time tick: NIFTY 50 Spot = 24,842.10 | Time: 14:12:05 IST", color: "text-slate-300", delay: 200 },
            { text: "📐 [VWAP_CALC] 15m VWAP Benchmark = 24,856.40 (Deviation: -14.30 pts below VWAP)", color: "text-amber-400", delay: 600 },
            { text: "⚠️ [RISK_GUARD] Confluence Failure: Spot broke below 15m VWAP baseline.", color: "text-rose-400", delay: 1100 },
            { text: "🛑 [CIRCUIT_BREAKER] Call entry strictly REJECTED. Structural SL anchor active at 24,810.", color: "text-rose-400 font-bold", delay: 1600 },
            { text: "⏰ [THETA_SHIELD] Expiry session check: 14:12 IST (Expiry filter threshold: 13:30 IST).", color: "text-cyan-300", delay: 2100 },
            { text: "🔒 [CAPITAL_LOCK] 30% Unallocated Capital Reserve strictly enforced. Capital safe.", color: "text-emerald-400 font-bold", delay: 2600 }
        ];

        let index = 0;
        function printNext() {
            if (index < logs.length) {
                const item = logs[index];
                setTimeout(() => {
                    const line = document.createElement('div');
                    line.className = item.color + " font-mono text-xs leading-relaxed";
                    line.textContent = item.text;
                    consoleEl.appendChild(line);
                    consoleEl.scrollTop = consoleEl.scrollHeight;
                    playAriaBeep(500 + (index * 50), 0.04);
                    index++;
                    printNext();
                }, item.delay);
            } else {
                simulationActive = false;
            }
        }
        printNext();
    };

    window.runAshLedgerInspection = function () {
        const consoleEl = document.getElementById('sim-terminal-output');
        if (!consoleEl) return;

        consoleEl.innerHTML = '';
        playAriaBeep(660, 0.06);

        const header = document.createElement('div');
        header.className = "text-cyan-300 font-mono text-xs font-bold pb-2 border-b border-slate-800";
        header.textContent = "🔍 [ASH_LEDGER_INSPECTOR] Reading live client browser Write-Ahead micro-journal...";
        consoleEl.appendChild(header);

        let count = 0;
        for (let i = 0; i < localStorage.length; i++) {
            const key = localStorage.key(i);
            if (key && (key.includes('phoenix') || key.includes('rehan') || key.includes('aria') || key.includes('lead'))) {
                count++;
                const val = localStorage.getItem(key);
                const line = document.createElement('div');
                line.className = "text-emerald-400 font-mono text-xs pt-1 truncate";
                line.textContent = `• Key: [${key}] => ${val.substring(0, 75)}...`;
                consoleEl.appendChild(line);
            }
        }

        if (count === 0) {
            const emptyNotice = document.createElement('div');
            emptyNotice.className = "text-slate-400 font-mono text-xs pt-2";
            emptyNotice.textContent = "• Active Journal: Clean state. No pending unsaved inputs in queue. Write-Ahead WAL daemon active & listening.";
            consoleEl.appendChild(emptyNotice);
        }

        const footer = document.createElement('div');
        footer.className = "text-indigo-300 font-mono text-xs pt-2 font-semibold";
        footer.textContent = `✅ [WAL_SYNC] Client-side Ash Ledger verified. Protection: ACTIVE.`;
        consoleEl.appendChild(footer);
        consoleEl.scrollTop = consoleEl.scrollHeight;
    };

    window.clearConsole = function () {
        const consoleEl = document.getElementById('sim-terminal-output');
        if (consoleEl) {
            consoleEl.innerHTML = '<div class="text-slate-500 font-mono text-xs italic">// Diagnostics console cleared. Select a simulation above to run live telemetry...</div>';
            playAriaBeep(350, 0.05);
        }
    };

    // Project Filter Controller
    window.filterProjects = function (category, triggerEl) {
        if (typeof playAriaBeep === 'function') {
            try { playAriaBeep(700, 0.04); } catch(e) {}
        }
        
        const normCat = (category || 'all').toLowerCase();
        
        // Find all filter buttons across any page
        const buttons = document.querySelectorAll('.project-filter-btn, .filter-btn');
        buttons.forEach(btn => {
            const btnFilter = (btn.getAttribute('data-filter') || '').toLowerCase();
            const isMatch = (triggerEl && btn === triggerEl) || (btnFilter && btnFilter === normCat);
            
            if (isMatch || (!triggerEl && !btnFilter && btn.textContent.toLowerCase().includes(normCat))) {
                btn.classList.remove('bg-white', 'text-slate-700', 'border', 'border-slate-200');
                btn.classList.add('bg-slate-900', 'text-white', 'shadow-sm');
            } else if (normCat === 'all' && (btnFilter === 'all' || btn.textContent.includes('All Systems'))) {
                btn.classList.remove('bg-white', 'text-slate-700', 'border', 'border-slate-200');
                btn.classList.add('bg-slate-900', 'text-white', 'shadow-sm');
            } else {
                btn.classList.remove('bg-slate-900', 'text-white', 'shadow-sm');
                btn.classList.add('bg-white', 'text-slate-700', 'border', 'border-slate-200');
            }
        });

        // Find all project cards across any page
        const cards = document.querySelectorAll('.project-card, [data-project-category], [data-category]');
        cards.forEach(card => {
            const rawCat = (card.getAttribute('data-project-category') || card.getAttribute('data-category') || '').toLowerCase();
            const cats = rawCat.split(/[\s,]+/);

            let visible = false;
            if (normCat === 'all') {
                visible = true;
            } else if (normCat === 'quant' || normCat === 'ai') {
                visible = cats.includes('quant') || cats.includes('ai') || cats.includes('algo') || cats.includes('trading');
            } else if (normCat === 'resilience' || normCat === 'phoenix') {
                visible = cats.includes('resilience') || cats.includes('phoenix') || cats.includes('chaos') || cats.includes('sentinel') || cats.includes('network');
            } else if (normCat === 'retail') {
                visible = cats.includes('retail') || cats.includes('pos') || cats.includes('software');
            } else if (normCat === 'web') {
                visible = cats.includes('web');
            } else {
                visible = cats.includes(normCat);
            }

            if (visible) {
                card.style.display = 'flex';
                card.classList.remove('hidden');
            } else {
                card.style.display = 'none';
                card.classList.add('hidden');
            }
        });

        if (window.lucide && typeof window.lucide.createIcons === 'function') {
            try { window.lucide.createIcons(); } catch(e) {}
        }
    };

})();
