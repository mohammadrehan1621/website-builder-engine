/**
 * RQL Sovereign Motion & Visual Craft Engine v3.0
 * Integrates:
 * - Lenis Smooth Momentum Scrolling (Inertial physics with mobile touch preservation)
 * - 3D Gyroscope Perspective Card Tilt with Specular Mouse Glare (Apple Card physics)
 * - Emil Kowalski Tactile Physics (Mechanical scale(0.97) micro-clicks, spring damping)
 * - Animated Laser Border Beams for VIP Flagships
 * - Live Scroll-Triggered Stat Odometers (Quartic spring count-up)
 * - Apple-Grade Floating Feedback Toasts (Spring capsule popup)
 * - Top Laser Reading Progress Bar (Hardware-accelerated viewport apex indicator)
 * - One-Click Discount Code Clipboard Binding (PIONEER70 & PIONEER20)
 * - Quick-Search Keyboard Shortcut (Slash / or Ctrl+K focus)
 * - 100% 7-Bit ASCII Compliant - Zero Unicode / Zero Dependencies
 */
(function() {
  'use strict';

  var isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var isTouchDevice = window.matchMedia('(hover: none)').matches;

  // 1. Lenis Smooth Momentum Scrolling
  function initLenis() {
    if (isReducedMotion || typeof window.Lenis === 'undefined') return;

    try {
      var lenis = new window.Lenis({
        duration: 1.15,
        easing: function(t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); },
        direction: 'vertical',
        gestureDirection: 'vertical',
        smooth: true,
        mouseMultiplier: 1.0,
        smoothTouch: false, // Keep native touch responsive on iOS/Android
        touchMultiplier: 2
      });

      window.rqlLenis = lenis;

      function raf(time) {
        lenis.raf(time);
        requestAnimationFrame(raf);
      }
      requestAnimationFrame(raf);

      // Handle anchor links with smooth scroll
      document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
          var targetId = this.getAttribute('href');
          if (targetId && targetId !== '#' && targetId.length > 1) {
            var targetEl = document.querySelector(targetId);
            if (targetEl) {
              e.preventDefault();
              lenis.scrollTo(targetEl, { offset: -80, duration: 1.2 });
            }
          }
        });
      });

      // Freeze / Resume scroll on Modal Open / Close
      var observer = new MutationObserver(function() {
        var hasOpenModal = document.querySelector('#indian-desk-modal:not(.hidden), #briefing-modal:not(.hidden), #evaluation-modal:not(.hidden), #video-walkthrough-modal:not(.hidden)');
        if (hasOpenModal) {
          lenis.stop();
        } else {
          lenis.start();
        }
      });
      observer.observe(document.body, { attributes: true, subtree: true, attributeFilter: ['class'] });
    } catch (err) {
      console.warn('[RQL Motion] Lenis init fallback:', err);
    }
  }

  // 2. 3D Gyroscope Perspective Card Tilt & Specular Mouse Glare
  function init3DTiltCards() {
    if (isReducedMotion || isTouchDevice) return;

    var selector = '[data-product-card="true"], .bento-card-spring, .spotlight-card';
    var cards = document.querySelectorAll(selector);

    cards.forEach(function(card) {
      var rect = null;
      var rafId = null;

      function onPointerEnter() {
        rect = card.getBoundingClientRect();
      }

      function onPointerMove(e) {
        if (!rect) rect = card.getBoundingClientRect();
        var x = e.clientX - rect.left;
        var y = e.clientY - rect.top;

        card.style.setProperty('--mouse-x', x + 'px');
        card.style.setProperty('--mouse-y', y + 'px');

        if (rafId) cancelAnimationFrame(rafId);
        rafId = requestAnimationFrame(function() {
          var normX = (x / rect.width) * 2 - 1;
          var normY = (y / rect.height) * 2 - 1;
          var tiltX = (-normY * 4.2).toFixed(2);
          var tiltY = (normX * 4.2).toFixed(2);
          card.style.transform = 'perspective(1000px) rotateX(' + tiltX + 'deg) rotateY(' + tiltY + 'deg) translateY(-3px) scale3d(1.012, 1.012, 1.012)';
        });
      }

      function onPointerLeave() {
        if (rafId) cancelAnimationFrame(rafId);
        rect = null;
        card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0px) scale3d(1, 1, 1)';
        card.style.transition = 'transform 0.45s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease, border-color 0.25s ease';
      }

      card.addEventListener('pointerenter', onPointerEnter);
      card.addEventListener('pointermove', onPointerMove);
      card.addEventListener('pointerleave', onPointerLeave);
    });
  }

  // 3. Emil Kowalski Tactile Button Springs
  function initTactileButtons() {
    var buttons = document.querySelectorAll('.btn-spring, button[role="button"], a[role="button"]');
    buttons.forEach(function(btn) {
      btn.addEventListener('pointerdown', function() {
        this.style.transform = 'translateY(1px) scale(0.97)';
        this.style.transition = 'transform 50ms cubic-bezier(0.16, 1, 0.3, 1)';
      });
      function reset() {
        this.style.transform = '';
        this.style.transition = 'transform 240ms cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.2s ease';
      }
      btn.addEventListener('pointerup', reset);
      btn.addEventListener('pointerleave', reset);
      btn.addEventListener('pointercancel', reset);
    });
  }

  // 4. Magnetic Micro-Attraction for Primary CTAs
  function initMagneticButtons() {
    if (isReducedMotion || window.innerWidth < 1024) return;

    var magnetics = document.querySelectorAll('.btn-magnetic');
    magnetics.forEach(function(el) {
      el.addEventListener('mousemove', function(e) {
        var rect = el.getBoundingClientRect();
        var centerX = rect.left + rect.width / 2;
        var centerY = rect.top + rect.height / 2;
        var deltaX = (e.clientX - centerX) * 0.22;
        var deltaY = (e.clientY - centerY) * 0.22;
        el.style.transform = 'translate3d(' + deltaX + 'px, ' + deltaY + 'px, 0) scale(1.02)';
      });
      el.addEventListener('mouseleave', function() {
        el.style.transform = 'translate3d(0, 0, 0) scale(1)';
        el.style.transition = 'transform 300ms cubic-bezier(0.34, 1.56, 0.64, 1)';
      });
    });
  }

  // 5. High-Speed Physics Staggered Card Entrance
  function initStaggeredReveals() {
    if (isReducedMotion) return;

    var revealTargets = document.querySelectorAll('.motion-stagger-item');
    if (!revealTargets.length) return;

    if ('IntersectionObserver' in window) {
      var revealObserver = new IntersectionObserver(function(entries, obs) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('motion-revealed');
            obs.unobserve(entry.target);
          }
        });
      }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

      revealTargets.forEach(function(el, idx) {
        el.style.setProperty('--stagger-index', idx % 6);
        revealObserver.observe(el);
      });
    } else {
      revealTargets.forEach(function(el) { el.classList.add('motion-revealed'); });
    }
  }

  // 6. Live Scroll-Triggered Stat Odometers
  function initOdometers() {
    if (isReducedMotion) return;
    var targets = document.querySelectorAll('.stat-odometer, [data-odometer]');
    if (!targets.length) return;

    if ('IntersectionObserver' in window) {
      var observer = new IntersectionObserver(function(entries, obs) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            var el = entry.target;
            var endVal = parseFloat(el.getAttribute('data-odometer') || el.innerText.replace(/[^0-9.]/g, ''));
            var prefix = el.getAttribute('data-odometer-prefix') || '';
            var suffix = el.getAttribute('data-odometer-suffix') || '';
            var duration = 1400;
            var startTimestamp = null;

            function step(timestamp) {
              if (!startTimestamp) startTimestamp = timestamp;
              var progress = Math.min((timestamp - startTimestamp) / duration, 1);
              // Quartic ease out: 1 - pow(1 - progress, 4)
              var easeProgress = 1 - Math.pow(1 - progress, 4);
              var currentVal = Math.floor(easeProgress * endVal);
              el.innerText = prefix + currentVal.toLocaleString('en-US') + suffix;
              if (progress < 1) {
                window.requestAnimationFrame(step);
              } else {
                el.innerText = prefix + endVal.toLocaleString('en-US') + suffix;
              }
            }
            window.requestAnimationFrame(step);
            obs.unobserve(el);
          }
        });
      }, { threshold: 0.2 });

      targets.forEach(function(el) { observer.observe(el); });
    }
  }

  // 7. Apple-Grade Floating Feedback Toasts
  window.showRQLToast = function(message, type) {
    var existing = document.getElementById('rql-global-toast');
    if (existing && existing.parentNode) {
      existing.parentNode.removeChild(existing);
    }

    var toast = document.createElement('div');
    toast.id = 'rql-global-toast';
    toast.setAttribute('role', 'status');
    toast.setAttribute('aria-live', 'polite');
    toast.className = 'rql-toast-spring fixed top-5 left-1/2 -translate-x-1/2 z-[99999] bg-slate-950/95 text-white px-4 py-2.5 rounded-full shadow-2xl border border-slate-700/80 backdrop-blur-md flex items-center gap-2.5 text-xs font-mono font-bold tracking-tight';

    var iconColor = type === 'info' ? 'text-cyan-400' : 'text-emerald-400';
    var iconSvg = '<svg class="w-4 h-4 ' + iconColor + ' shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>';
    toast.innerHTML = iconSvg + '<span>' + message + '</span>';
    document.body.appendChild(toast);

    setTimeout(function() {
      toast.classList.add('rql-toast-visible');
    }, 15);

    setTimeout(function() {
      toast.classList.remove('rql-toast-visible');
      setTimeout(function() {
        if (toast && toast.parentNode) toast.parentNode.removeChild(toast);
      }, 350);
    }, 2800);
  };

  // 8. Top Laser Reading Progress Bar
  function initScrollProgress() {
    var existing = document.getElementById('rql-scroll-progress');
    if (existing) return;

    var bar = document.createElement('div');
    bar.id = 'rql-scroll-progress';
    document.body.appendChild(bar);

    function update() {
      var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      var docHeight = document.documentElement.scrollHeight - window.innerHeight;
      var progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
      bar.style.width = Math.min(100, Math.max(0, progress)) + '%';
    }

    window.addEventListener('scroll', update, { passive: true });
    update();
  }

  // 9. Interactive Discount Code Clipboard Binding
  function initDiscountCodeCopy() {
    var discountBadges = document.querySelectorAll('[data-copy-discount], .discount-pill, a[title*="PIONEER"]');
    discountBadges.forEach(function(badge) {
      badge.classList.add('discount-copy-pill');
      badge.addEventListener('click', function(e) {
        var code = badge.getAttribute('data-copy-discount') || (badge.innerText.indexOf('PIONEER70') !== -1 ? 'PIONEER70' : (badge.innerText.indexOf('PIONEER20') !== -1 ? 'PIONEER20' : ''));
        if (code && navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(code).then(function() {
            if (window.showRQLToast) {
              window.showRQLToast('Pass ' + code + ' Copied! Auto-applied at checkout', 'success');
            }
          }).catch(function() {
            // Silently fallback without disruption
          });
        }
      });
    });
  }

  // 10. Quick-Search Keyboard Shortcut (Slash / or Ctrl+K)
  function initQuickSearch() {
    window.addEventListener('keydown', function(e) {
      if (e.target && (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA')) return;

      if (e.key === '/' || ((e.ctrlKey || e.metaKey) && (e.key === 'k' || e.key === 'K'))) {
        var searchInput = document.getElementById('suite-search-input') || document.querySelector('input[type="search"]') || document.querySelector('input[placeholder*="Search"]');
        if (searchInput && document.activeElement !== searchInput) {
          e.preventDefault();
          searchInput.focus();
          searchInput.scrollIntoView({ behavior: 'smooth', block: 'center' });
          if (window.showRQLToast) {
            window.showRQLToast('Quick Search: Type to filter software suites', 'info');
          }
        }
      }
    });
  }

  // Self-Executing DOM Initialization
  function boot() {
    initLenis();
    init3DTiltCards();
    initTactileButtons();
    initMagneticButtons();
    initStaggeredReveals();
    initOdometers();
    initScrollProgress();
    initDiscountCodeCopy();
    initQuickSearch();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
