/**
 * Lively Motion & Institutional GUI Engine v5.0
 * Rehan Quant Lab (c) 2026
 * Ultra-responsive 60fps animations, interactive neural mesh, rotating live ticker & card spotlight
 */

document.addEventListener('DOMContentLoaded', () => {
    // -------------------------------------------------------------
    // 1. Dynamic Rotating Announcement Ticker
    // -------------------------------------------------------------
    const tickerContainer = document.getElementById('ticker-content');
    const tickerAction = document.getElementById('ticker-action');
    const tickerLabel = document.getElementById('ticker-label');

    const tickerItems = [
        {
            label: "\u2B50 NEW RELEASE:",
            labelColor: "text-emerald-400",
            html: "<strong>RQL DocumentShield&trade;</strong> &bull; Enterprise Forensic PDF Redactor (<span class='text-emerald-400 font-bold'>$199 USD / &#8377;18,887</span>)",
            url: "https://quantify17.gumroad.com/l/rql-documentshield",
            actionText: "Instant Checkout",
            actionColor: "text-emerald-400"
        },
        {
            label: "\u2B50 NEW RELEASE:",
            labelColor: "text-sky-400",
            html: "<strong>RQL WhisperVault&trade;</strong> &bull; Air-Gapped AI Speech Intelligence (<span class='text-sky-400 font-bold'>$199 USD / &#8377;18,887</span>)",
            url: "https://quantify17.gumroad.com/l/rql-whispervault",
            actionText: "Instant Checkout",
            actionColor: "text-sky-400"
        },
        {
            label: "\uD83D\uDC51 SOURCE CODE VIP:",
            labelColor: "text-amber-400",
            html: "<strong>Enterprise Source Code Edition</strong> (&#8377;75,835) &bull; Direct Founder WhatsApp Onboarding",
            url: "https://wa.me/917091518548?text=Hello%20Mohammad%20Rehan,%20I%20want%20to%20acquire%20the%20Enterprise%20Source%20Code%20Edition%20(%E2%82%B975,835).%20Please%20assist%20with%20founder%20onboarding.",
            actionText: "VIP WhatsApp",
            actionColor: "text-amber-400"
        },
        {
            label: "SOVEREIGN TITAN:",
            labelColor: "text-teal-400",
            html: "<strong>100% Pure Native Rust</strong> &bull; Zero Cloud Telemetry &bull; Lifetime Desktop License",
            url: "store.html",
            actionText: "Commercial Suites (2)",
            actionColor: "text-teal-400"
        }
    ];

    if (tickerContainer && tickerAction) {
        let tickerIdx = 0;
        setInterval(() => {
            tickerIdx = (tickerIdx + 1) % tickerItems.length;
            const item = tickerItems[tickerIdx];

            tickerContainer.style.opacity = '0';
            setTimeout(() => {
                if (tickerLabel) {
                    tickerLabel.textContent = item.label;
                    tickerLabel.className = `${item.labelColor} font-bold uppercase text-[10px] tracking-wider shrink-0`;
                }
                tickerContainer.innerHTML = item.html;
                tickerAction.href = item.url;
                tickerAction.className = `${item.actionColor} hover:underline font-bold transition flex items-center gap-1 font-mono`;
                tickerContainer.style.opacity = '1';
            }, 300);
        }, 4500);
    }

    // -------------------------------------------------------------
    // 2. Interactive Card Cursor Spotlight (Stripe / Linear Effect)
    // -------------------------------------------------------------
    const cards = document.querySelectorAll('.project-card, .hover-lift-card, #hero-profile-card');
    cards.forEach(card => {
        card.style.position = 'relative';
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            card.style.setProperty('--mouse-x', `${x}px`);
            card.style.setProperty('--mouse-y', `${y}px`);
        });
    });

    // -------------------------------------------------------------
    // 3. Highlight Active Nav Tab
    // -------------------------------------------------------------
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('nav a').forEach(link => {
        const href = link.getAttribute('href');
        if (href && (href === currentPath || (currentPath === '' && href === 'index.html'))) {
            link.classList.add('text-slate-900', 'font-bold', 'bg-slate-100', 'px-3', 'py-1', 'rounded-lg');
            link.classList.remove('text-slate-600');
        }
    });

    // -------------------------------------------------------------
    // 4. Staggered 60fps Scroll Reveal
    // -------------------------------------------------------------
    const revealTargets = document.querySelectorAll(
        'section, .project-card, .hover-lift-card, .grid > div, footer'
    );

    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -40px 0px',
        threshold: 0.05
    };

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    revealTargets.forEach((el, index) => {
        if (!el.classList.contains('reveal-on-scroll')) {
            el.classList.add('reveal-on-scroll');
            const delay = (index % 4) * 75;
            if (delay > 0) el.style.transitionDelay = `${delay}ms`;
        }
        revealObserver.observe(el);
    });

    // -------------------------------------------------------------
    // 5. Header Dynamic Glass Density on Scroll
    // -------------------------------------------------------------
    const header = document.querySelector('header');
    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 20) {
                header.classList.add('shadow-md');
            } else {
                header.classList.remove('shadow-md');
            }
        }, { passive: true });
    }

    // -------------------------------------------------------------
    // 6. Universal Interactive Neural Constellation Mesh
    // -------------------------------------------------------------
    const canvas = document.getElementById('neural-mesh-canvas');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        let width = canvas.width = canvas.parentElement.offsetWidth || window.innerWidth;
        let height = canvas.height = canvas.parentElement.offsetHeight || 600;

        window.addEventListener('resize', () => {
            if (canvas.parentElement) {
                width = canvas.width = canvas.parentElement.offsetWidth;
                height = canvas.height = canvas.parentElement.offsetHeight;
            }
        });

        const particles = [];
        const count = Math.min(45, Math.floor(width / 35));

        for (let i = 0; i < count; i++) {
            particles.push({
                x: Math.random() * width,
                y: Math.random() * height,
                vx: (Math.random() - 0.5) * 0.7,
                vy: (Math.random() - 0.5) * 0.7,
                r: Math.random() * 2 + 1.2,
                color: Math.random() > 0.4 ? 'rgba(56, 189, 248, ' : 'rgba(16, 185, 129, '
            });
        }

        let mouse = { x: -1000, y: -1000 };
        window.addEventListener('mousemove', (e) => {
            const rect = canvas.getBoundingClientRect();
            mouse.x = e.clientX - rect.left;
            mouse.y = e.clientY - rect.top;
        });

        function animateConstellation() {
            if (document.hidden) {
                requestAnimationFrame(animateConstellation);
                return;
            }
            ctx.clearRect(0, 0, width, height);

            for (let i = 0; i < particles.length; i++) {
                const p = particles[i];
                p.x += p.vx;
                p.y += p.vy;

                if (p.x < 0 || p.x > width) p.vx *= -1;
                if (p.y < 0 || p.y > height) p.vy *= -1;

                // Mouse interaction repulsion/attraction
                const dxm = mouse.x - p.x;
                const dym = mouse.y - p.y;
                const distm = Math.sqrt(dxm * dxm + dym * dym);
                if (distm < 120) {
                    p.x -= (dxm / distm) * 0.8;
                    p.y -= (dym / distm) * 0.8;
                }

                // Draw Particle Dot
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
                ctx.fillStyle = p.color + '0.7)';
                ctx.fill();

                // Draw Connecting Filaments
                for (let j = i + 1; j < particles.length; j++) {
                    const p2 = particles[j];
                    const dx = p.x - p2.x;
                    const dy = p.y - p2.y;
                    const dist = Math.sqrt(dx * dx + dy * dy);

                    if (dist < 105) {
                        ctx.beginPath();
                        ctx.moveTo(p.x, p.y);
                        ctx.lineTo(p2.x, p2.y);
                        ctx.strokeStyle = `rgba(56, 189, 248, ${(1 - dist / 105) * 0.25})`;
                        ctx.lineWidth = 0.8;
                        ctx.stroke();
                    }
                }
            }
            requestAnimationFrame(animateConstellation);
        }
        animateConstellation();
    }

    // -------------------------------------------------------------
    // 7. Refresh Lucide Icons
    // -------------------------------------------------------------
    if (window.lucide && typeof window.lucide.createIcons === 'function') {
        window.lucide.createIcons();
    }
});
