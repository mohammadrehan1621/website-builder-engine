/**
 * RQL Sovereign Motion & Visual Craft Engine
 * Integrates:
 * - Lenis Smooth Momentum Scrolling (Inertial physics with mobile touch preservation)
 * - Emil Kowalski Tactile Physics (Mechanical scale(0.97) micro-clicks, spring damping)
 * - React Bits Spotlight Luminescence (Light-theme cursor-following sheen)
 * - Magnetic Button Attraction (Spatial pull on primary CTAs)
 * - Hardware-Accelerated 60fps RAF Staggered Batch Reveals
 * - Strict Separation: Purely frontend enhancement; 100% zero backend side-effects
 * 100% 7-Bit ASCII Compliant
 */
(function() {
  'use strict';

  var isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

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

  // 2. React Bits Spotlight Hover Sheen (Light-Theme Edition)
  function initSpotlights() {
    if (isReducedMotion) return;

    var selector = '.spotlight-card, .bento-card-spring, #commercial-products-grid > div';
    var cards = document.querySelectorAll(selector);

    cards.forEach(function(card) {
      card.style.position = card.style.position || 'relative';
      
      var ticking = false;
      card.addEventListener('pointermove', function(e) {
        if (!ticking) {
          window.requestAnimationFrame(function() {
            var rect = card.getBoundingClientRect();
            var x = e.clientX - rect.left;
            var y = e.clientY - rect.top;
            card.style.setProperty('--mouse-x', x + 'px');
            card.style.setProperty('--mouse-y', y + 'px');
            ticking = false;
          });
          ticking = true;
        }
      });
    });
  }

  // 3. Emil Kowalski Tactile Button Compression
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

  // Self-Executing DOM Initialization
  function boot() {
    initLenis();
    initSpotlights();
    initTactileButtons();
    initMagneticButtons();
    initStaggeredReveals();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
