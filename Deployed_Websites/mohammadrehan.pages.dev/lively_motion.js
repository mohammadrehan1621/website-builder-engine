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
            label: "\u2B50 NEW RELEASE:",
            labelColor: "text-amber-400",
            html: "<strong>RQL Sovereign Retail POS&trade;</strong> &bull; Offline Barcode &amp; Thermal Billing (<span class='text-amber-400 font-bold'>$199 USD / &#8377;16,500</span>)",
            url: "https://quantify17.gumroad.com/l/rql-retailpos",
            actionText: "Instant Checkout",
            actionColor: "text-amber-400"
        },
        {
            label: "\u2B50 NEW RELEASE:",
            labelColor: "text-orange-400",
            html: "<strong>RQL StoreChain&trade;</strong> &bull; 5-Till LAN Mesh &amp; Branch Sync (<span class='text-orange-400 font-bold'>$299 USD / &#8377;24,999</span>)",
            url: "https://quantify17.gumroad.com/l/rql-storechain",
            actionText: "Instant Checkout",
            actionColor: "text-orange-400"
        },
        {
            label: "\u2B50 NEW RELEASE:",
            labelColor: "text-cyan-400",
            html: "<strong>RQL Conduit&trade;</strong> &bull; Pure-Rust Offline Internet Bonding &amp; Failover (<span class='text-cyan-400 font-bold'>From $99 USD</span>)",
            url: "https://quantify17.gumroad.com/l/rql-conduit",
            actionText: "Instant Checkout",
            actionColor: "text-cyan-400"
        },
        {
            label: "\uD83D\uDC51 SOURCE CODE VIP:",
            labelColor: "text-purple-400",
            html: "<strong>Enterprise Source Code Edition</strong> (&#8377;75,835) &bull; Direct Founder WhatsApp Onboarding",
            url: "https://wa.me/917091518548?text=Hello%20Mohammad%20Rehan,%20I%20want%20to%20acquire%20the%20Enterprise%20Source%20Code%20Edition%20(%E2%82%B975,835).%20Please%20assist%20with%20founder%20onboarding.",
            actionText: "VIP WhatsApp",
            actionColor: "text-purple-400"
        },
        {
            label: "SOVEREIGN TITAN:",
            labelColor: "text-teal-400",
            html: "<strong>100% Pure Native Rust</strong> &bull; Zero Cloud Telemetry &bull; Lifetime Desktop License",
            url: "store.html",
            actionText: "Commercial Suites (13)",
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
    // 7. Refresh Lucide Icons
    // -------------------------------------------------------------
    if (window.lucide && typeof window.lucide.createIcons === 'function') {
        window.lucide.createIcons();
    }
    const cookieBanner = document.getElementById('cookie-banner');
    if (cookieBanner && localStorage.getItem('cookie_consent_accepted') === 'true') {
        cookieBanner.remove();
    }
});

window.acceptCookies = function() {
    const banner = document.getElementById('cookie-banner');
    if (banner) {
        try {
            localStorage.setItem('cookie_consent_accepted', 'true');
        } catch (e) {}
        banner.style.opacity = '0';
        banner.style.pointerEvents = 'none';
        setTimeout(() => banner.remove(), 250);
    }
};
window.dismissCookies = function() {
    window.acceptCookies();
};
