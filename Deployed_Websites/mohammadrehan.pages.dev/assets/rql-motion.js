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

  // 10. Synthesized Tactile Audio Engine (Web Audio API - 0 KB External Assets)
  var audioCtx = null;
  function getAudioContext() {
    if (!audioCtx && (window.AudioContext || window.webkitAudioContext)) {
      try {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      } catch (e) {
        audioCtx = null;
      }
    }
    if (audioCtx && audioCtx.state === 'suspended') {
      audioCtx.resume().catch(function() {});
    }
    return audioCtx;
  }

  window.playTactileClick = function(type) {
    if (localStorage.getItem('rql_sound_muted') === 'true') return;
    try {
      var ctx = getAudioContext();
      if (!ctx) return;
      var now = ctx.currentTime;
      var osc = ctx.createOscillator();
      var gain = ctx.createGain();
      osc.connect(gain);
      gain.connect(ctx.destination);

      if (type === 'success') {
        osc.type = 'sine';
        osc.frequency.setValueAtTime(520, now);
        osc.frequency.exponentialRampToValueAtTime(880, now + 0.08);
        gain.gain.setValueAtTime(0.035, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.08);
        osc.start(now);
        osc.stop(now + 0.08);
      } else if (type === 'toggle') {
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(600, now);
        gain.gain.setValueAtTime(0.025, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.04);
        osc.start(now);
        osc.stop(now + 0.04);
      } else {
        // Subtle crisp mechanical click
        osc.type = 'sine';
        osc.frequency.setValueAtTime(750, now);
        osc.frequency.exponentialRampToValueAtTime(320, now + 0.035);
        gain.gain.setValueAtTime(0.03, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.035);
        osc.start(now);
        osc.stop(now + 0.035);
      }
    } catch (e) {
      // Audio autoplay restrictions silently swallowed
    }
  };

  // 11. Raycast-Style Global Command Palette (Ctrl+K / Cmd+K / Slash)
  var RQL_PALETTE_DATA = [
    // 31 Commercial Suites
    { id: 'rql-documentshield', suiteNum: '01', section: 'suites', title: 'RQL DocumentShield', cat: 'Security & Privacy', tag: 'VIP Flagship 01', price: '$179 ($53.70)', url: 'store.html#rql-documentshield', desc: 'Enterprise PDF Redactor & Permanent Vector Metadata Purge', keywords: ['pdf', 'redact', 'redaction', 'purge', 'metadata', 'adobe', 'acrobat', 'vector', '01', '1', 'suite 1'] },
    { id: 'rql-whispervault', suiteNum: '02', section: 'suites', title: 'RQL WhisperVault', cat: 'Media & Audio', tag: 'VIP Flagship 02', price: '$149 ($44.70)', url: 'store.html#rql-whispervault', desc: '100% Offline Whisper AI Audio Transcription & Subtitles', keywords: ['whisper', 'audio', 'voice', 'transcribe', 'transcription', 'subtitles', 'speech', 'otter', '02', '2', 'suite 2'] },
    { id: 'rql-retailpos', suiteNum: '03', section: 'suites', title: 'RQL Retail POS', cat: 'Retail POS & Billing', tag: 'VIP Flagship 03', price: '$169 ($50.70)', url: 'store.html#rql-retailpos', desc: 'Sub-1ms Air-Gapped Retail Point of Sale & Thermal Engine', keywords: ['pos', 'retail', 'billing', 'thermal', 'barcode', 'lan', 'offline', 'counter', '03', '3', 'suite 3'] },
    { id: 'rql-storechain', suiteNum: '04', section: 'suites', title: 'RQL StoreChain', cat: 'Retail POS & Billing', tag: 'Commercial 04', price: '$299 ($89.70)', url: 'store.html#rql-storechain', desc: 'Multi-Counter LAN Billing & Multi-Branch Data Sync', keywords: ['chain', 'lan', 'sync', 'branch', 'store', 'multi-counter', '04', '4', 'suite 4'] },
    { id: 'rql-conduit', suiteNum: '05', section: 'suites', title: 'RQL Conduit', cat: 'Systems & Network', tag: 'Commercial 05', price: '$129 ($38.70)', url: 'store.html#rql-conduit', desc: 'Dual-WAN Internet Bonding, Aggregation & Failover Daemon', keywords: ['bonding', 'dual-wan', 'failover', 'network', 'router', 'aggregation', '05', '5', 'suite 5'] },
    { id: 'rql-hashcheck', suiteNum: '06', section: 'suites', title: 'RQL HashCheck', cat: 'Security & Privacy', tag: 'Commercial 06', price: '$39 ($11.70)', url: 'store.html#rql-hashcheck', desc: 'SHA-256 / SHA-512 Stream Cryptographic File Integrity', keywords: ['hash', 'sha256', 'sha512', 'checksum', 'verify', 'integrity', 'crypto', '06', '6', 'suite 6'] },
    { id: 'rql-qrstudio', suiteNum: '07', section: 'suites', title: 'RQL QRStudio', cat: 'Retail POS & Billing', tag: 'Commercial 07', price: '$79 ($23.70)', url: 'store.html#rql-qrstudio', desc: 'Offline Vector UPI QR & Barcode Generator Studio', keywords: ['qr', 'upi', 'barcode', 'vector', 'svg', 'payment', 'canvas', '07', '7', 'suite 7'] },
    { id: 'rql-textdiff', suiteNum: '08', section: 'suites', title: 'RQL TextDiff', cat: 'Systems & Network', tag: 'Commercial 08', price: '$99 ($29.70)', url: 'store.html#rql-textdiff', desc: 'Side-by-Side Visual Code & Text Difference Comparator', keywords: ['diff', 'compare', 'text diff', 'code diff', 'side by side', 'syntax', '08', '8', 'suite 8'] },
    { id: 'rql-renamer', suiteNum: '09', section: 'suites', title: 'RQL Renamer', cat: 'Systems & Network', tag: 'Commercial 09', price: '$49 ($14.70)', url: 'store.html#rql-renamer', desc: 'High-Speed Bulk Regex File & Photo Reorganizer', keywords: ['rename', 'batch', 'bulk', 'regex', 'organize', 'photo', 'files', '09', '9', 'suite 9'] },
    { id: 'rql-tageditor', suiteNum: '10', section: 'suites', title: 'RQL TagEditor', cat: 'Media & Audio', tag: 'Commercial 10', price: '$59 ($17.70)', url: 'store.html#rql-tageditor', desc: 'Lossless ID3 & FLAC Audio Metadata & Album Art Editor', keywords: ['id3', 'tag', 'flac', 'mp3', 'album art', 'music', 'metadata', '10', 'suite 10'] },
    { id: 'rql-fontviewer', suiteNum: '11', section: 'suites', title: 'RQL FontViewer', cat: 'Systems & Network', tag: 'Commercial 11', price: '$49 ($14.70)', url: 'store.html#rql-fontviewer', desc: 'Desktop Typography Glyph Inspector & OTF/TTF Manager', keywords: ['font', 'ttf', 'otf', 'glyph', 'typography', 'inspector', '11', 'suite 11'] },
    { id: 'rql-dpdpshield', suiteNum: '12', section: 'suites', title: 'RQL DPDPShield', cat: 'Legal & Compliance', tag: 'Commercial 12', price: '$89 ($26.70)', url: 'store.html#rql-dpdpshield', desc: 'DPDP Act 2023 & GDPR Corporate Compliance Sanitizer', keywords: ['dpdp', 'gdpr', 'privacy', 'compliance', 'personal data', 'sanitizer', 'audit', '12', 'suite 12'] },
    { id: 'rql-pricetag', suiteNum: '13', section: 'suites', title: 'RQL PriceTag', cat: 'Retail POS & Billing', tag: 'Commercial 13', price: '$79 ($23.70)', url: 'store.html#rql-pricetag', desc: 'Thermal Barcode Price Tag & Shelf Label Design Studio', keywords: ['price tag', 'shelf', 'label', 'thermal', 'barcode', 'retail', '13', 'suite 13'] },
    { id: 'rql-invoicegen', suiteNum: '14', section: 'suites', title: 'RQL InvoiceGen', cat: 'Retail POS & Billing', tag: 'Commercial 14', price: '$89 ($26.70)', url: 'store.html#rql-invoicegen', desc: 'Offline GST Tax Invoice Studio & Dynamic UPI QR Engine', keywords: ['invoice', 'gst', 'tax', 'bill', 'upi', 'accounting', 'pdf invoice', '14', 'suite 14'] },
    { id: 'rql-csvformat', suiteNum: '15', section: 'suites', title: 'RQL CSVFormat', cat: 'Systems & Network', tag: 'Commercial 15', price: '$79 ($23.70)', url: 'store.html#rql-csvformat', desc: 'Multi-Gigabyte CSV Sanitizer, Deduplication & Transform', keywords: ['csv', 'excel', 'data', 'dedup', 'sanitize', 'transform', 'gigabyte', '15', 'suite 15'] },
    { id: 'rql-pdfmerge', suiteNum: '16', section: 'suites', title: 'RQL PDFMerge', cat: 'Legal & Compliance', tag: 'Commercial 16', price: '$119 ($35.70)', url: 'store.html#rql-pdfmerge', desc: 'Air-Gapped PDF Combiner, Splitter & Legal Bates Stamper', keywords: ['pdf merge', 'split', 'bates', 'bates stamp', 'legal pdf', 'combine', '16', 'suite 16'] },
    { id: 'rql-taxledger', suiteNum: '17', section: 'suites', title: 'RQL TaxLedger', cat: 'Legal & Compliance', tag: 'VIP Flagship 17', price: '$119 ($35.70)', url: 'store.html#rql-taxledger', desc: '20-Feature Indian Double-Entry Accounting & GSTR-1 Studio', keywords: ['tax', 'ledger', 'accounting', 'gstr1', 'gstr', 'tally', 'balance sheet', '17', 'suite 17'] },
    { id: 'rql-fileshredder', suiteNum: '18', section: 'suites', title: 'RQL FileShredder', cat: 'Security & Privacy', tag: 'Commercial 18', price: '$59 ($17.70)', url: 'store.html#rql-fileshredder', desc: 'DoD 5220.22-M Permanent Forensic Data Destruction', keywords: ['shred', 'wipe', 'delete', 'dod', 'gutmann', 'forensic', 'destroy', '18', 'suite 18'] },
    { id: 'rql-clipvault', suiteNum: '19', section: 'suites', title: 'RQL ClipVault', cat: 'Security & Privacy', tag: 'Commercial 19', price: '$39 ($31.20)', url: 'store.html#rql-clipvault', desc: 'Encrypted AES-256 Local Clipboard Memory Vault', keywords: ['clipboard', 'clip', 'aes256', 'encrypted', 'history', 'paste', '19', 'suite 19'] },
    { id: 'rql-imagebatch', suiteNum: '20', section: 'suites', title: 'RQL ImageBatch', cat: 'Media & Audio', tag: 'Commercial 20', price: '$69 ($55.20)', url: 'store.html#rql-imagebatch', desc: 'SIMD Multi-Threaded Batch Image Resizer & WebP Converter', keywords: ['image', 'webp', 'batch', 'resize', 'compress', 'simd', 'photo', '20', 'suite 20'] },
    { id: 'rql-audioextract', suiteNum: '21', section: 'suites', title: 'RQL AudioExtract', cat: 'Media & Audio', tag: 'Commercial 21', price: '$59 ($47.20)', url: 'store.html#rql-audioextract', desc: 'Lossless MP4/MKV to MP3/WAV/FLAC Audio Demuxer', keywords: ['audio', 'extract', 'demux', 'mp4', 'mkv', 'mp3', 'wav', 'soundtrack', '21', 'suite 21'] },
    { id: 'rql-subtitlesync', suiteNum: '22', section: 'suites', title: 'RQL SubtitleSync', cat: 'Media & Audio', tag: 'Commercial 22', price: '$49 ($39.20)', url: 'store.html#rql-subtitlesync', desc: 'Millisecond SRT/VTT Subtitle Timing & Encoding Calibrator', keywords: ['subtitle', 'srt', 'vtt', 'sync', 'timing', 'delay', 'caption', '22', 'suite 22'] },
    { id: 'rql-spacemap', suiteNum: '23', section: 'suites', title: 'RQL SpaceMap', cat: 'Systems & Network', tag: 'Commercial 23', price: '$79 ($63.20)', url: 'store.html#rql-spacemap', desc: 'High-Speed Multi-Terabyte Treemap Storage Visualizer', keywords: ['disk', 'storage', 'space', 'treemap', 'visualize', 'terabyte', 'cleanup', '23', 'suite 23'] },
    { id: 'rql-docprotect', suiteNum: '24', section: 'suites', title: 'RQL DocProtect', cat: 'Security & Privacy', tag: 'Commercial 24', price: '$89 ($71.20)', url: 'store.html#rql-docprotect', desc: 'Local Zero-Telemetry AES-GCM-256 PDF Password Encryption', keywords: ['pdf protect', 'encrypt', 'password', 'aes-gcm', 'security', 'lock', '24', 'suite 24'] },
    { id: 'rql-cashdrawer', suiteNum: '25', section: 'suites', title: 'RQL CashDrawer', cat: 'Retail POS & Billing', tag: 'Commercial 25', price: '$59 ($47.20)', url: 'store.html#rql-cashdrawer', desc: 'Deterministic RJ12 Pulse Cash Drawer Trigger Utility', keywords: ['drawer', 'cash', 'rj12', 'pulse', 'pos hardware', 'retail', '25', 'suite 25'] },
    { id: 'rql-receiptprinter', suiteNum: '26', section: 'suites', title: 'RQL ReceiptPrinter', cat: 'Retail POS & Billing', tag: 'Commercial 26', price: '$69 ($55.20)', url: 'store.html#rql-receiptprinter', desc: 'Direct-to-USB/LAN Raw Thermal ESC/POS Print Spooler', keywords: ['receipt', 'thermal', 'escpos', 'print', 'spooler', 'usb', 'lan', '26', 'suite 26'] },
    { id: 'rql-clauseforge', suiteNum: '27', section: 'suites', title: 'RQL ClauseForge', cat: 'Legal & Compliance', tag: 'Commercial 27', price: '$129 ($103.20)', url: 'store.html#rql-clauseforge', desc: 'Deterministic Legal Contract Compiler & Master Precedent Vault', keywords: ['contract', 'legal', 'clause', 'precedent', 'agreement', 'law', '27', 'suite 27'] },
    { id: 'rql-archivemaster', suiteNum: '28', section: 'suites', title: 'RQL ArchiveMaster', cat: 'Systems & Network', tag: 'Commercial 28', price: '$89 ($71.20)', url: 'store.html#rql-archivemaster', desc: 'High-Ratio Multithreaded 7z/ZIP/TAR Compression Archiver', keywords: ['zip', '7z', 'tar', 'compress', 'archive', 'extract', '28', 'suite 28'] },
    { id: 'rql-socketshield', suiteNum: '29', section: 'suites', title: 'RQL SocketShield', cat: 'Security & Privacy', tag: 'VIP Flagship 29', price: '$189 ($56.70)', url: 'store.html#rql-socketshield', desc: 'Live Windows Socket Sentry & Outbound Telemetry Trapper', keywords: ['socket', 'telemetry', 'firewall', 'sentry', 'trap', 'network', 'sniffer', '29', 'suite 29'] },
    { id: 'rql-pingpulse', suiteNum: '30', section: 'suites', title: 'RQL PingPulse', cat: 'Systems & Network', tag: 'VIP Flagship 30', price: '$139 ($111.20)', url: 'store.html#rql-pingpulse', desc: 'Microsecond ICMP Latency & Outage Packet Sentry', keywords: ['ping', 'latency', 'icmp', 'packet', 'jitter', 'uptime', 'monitor', '30', 'suite 30'] },
    { id: 'rql-foldersync', suiteNum: '31', section: 'suites', title: 'RQL FolderSync', cat: 'Systems & Network', tag: 'Commercial 31', price: '$129 ($103.20)', url: 'store.html#rql-foldersync', desc: 'Parallel Multi-Drive Directory Mirror & Backup Engine', keywords: ['folder', 'sync', 'backup', 'mirror', 'drive', 'directory', 'raid', '31', 'suite 31'] },

    // 10 Dedicated Landing & Comparison Pages
    { id: 'lp-documentshield', section: 'flagships', badge: 'DOC', title: 'RQL DocumentShield (Flagship Page)', cat: 'Dedicated Landing Page', tag: 'Live Sandbox', price: '$179 ($53.70)', url: 'documentshield.html', desc: 'Enterprise PDF Redaction deep dive with in-browser live vector sandbox', keywords: ['documentshield', 'pdf', 'landing page', 'redact', 'sandbox'] },
    { id: 'lp-whispervault', section: 'flagships', badge: 'DOC', title: 'RQL WhisperVault (Flagship Page)', cat: 'Dedicated Landing Page', tag: 'Air-Gapped AI', price: '$149 ($44.70)', url: 'whispervault.html', desc: '100% offline local CPU Whisper AI transcription and subtitle specs', keywords: ['whispervault', 'whisper', 'landing page', 'audio', 'transcribe'] },
    { id: 'lp-retailpos', section: 'flagships', badge: 'DOC', title: 'RQL Retail POS (Flagship Page)', cat: 'Dedicated Landing Page', tag: 'Sub-1ms POS', price: '$169 ($50.70)', url: 'retailpos.html', desc: 'Air-gapped retail point-of-sale architecture & thermal ESC/POS engine', keywords: ['retailpos', 'pos', 'landing page', 'retail', 'billing'] },
    { id: 'lp-taxledger', section: 'flagships', badge: 'DOC', title: 'RQL TaxLedger (Flagship Page)', cat: 'Dedicated Landing Page', tag: 'GSTR-1 Studio', price: '$119 ($35.70)', url: 'taxledger.html', desc: 'Indian double-entry accounting, GST compliance, and GSTR-1 JSON ledger', keywords: ['taxledger', 'tax', 'gst', 'landing page', 'accounting'] },
    { id: 'lp-conduit', section: 'flagships', badge: 'DOC', title: 'RQL Conduit (Flagship Page)', cat: 'Dedicated Landing Page', tag: 'WAN Bonding', price: '$129 ($38.70)', url: 'conduit.html', desc: 'Dual-WAN internet bonding daemon, failover engine & packet scheduler', keywords: ['conduit', 'bonding', 'failover', 'landing page', 'network'] },
    { id: 'lp-dpdpshield', section: 'flagships', badge: 'DOC', title: 'RQL DPDPShield (Flagship Page)', cat: 'Dedicated Landing Page', tag: 'DPDP Act 2023', price: '$89 ($26.70)', url: 'dpdpshield.html', desc: 'Statutory personal data compliance sanitizer under DPDP Act 2023 & GDPR', keywords: ['dpdpshield', 'dpdp', 'gdpr', 'compliance', 'landing page'] },
    { id: 'lp-textdiff', section: 'flagships', badge: 'DOC', title: 'RQL TextDiff (Flagship Page)', cat: 'Dedicated Landing Page', tag: 'Visual Diff', price: '$99 ($29.70)', url: 'textdiff.html', desc: 'Side-by-side visual difference comparator with live in-browser engine', keywords: ['textdiff', 'diff', 'comparator', 'landing page', 'code'] },
    { id: 'lp-adobe-alternative', section: 'flagships', badge: 'DOC', title: 'Adobe Acrobat Alternative', cat: 'Competitor Comparison', tag: 'No Cloud', price: 'Perpetual', url: 'adobe-acrobat-alternative.html', desc: 'Why engineering and law teams switch from Adobe Creative Cloud to air-gapped Rust', keywords: ['adobe', 'acrobat', 'alternative', 'comparison', 'pdf'] },
    { id: 'lp-otter-alternative', section: 'flagships', badge: 'DOC', title: 'Otter.ai Offline Alternative', cat: 'Competitor Comparison', tag: 'Zero Server', price: 'Perpetual', url: 'otter-ai-alternative.html', desc: 'Zero cloud leaks: why executive boardrooms choose local Whisper AI over Otter', keywords: ['otter', 'otter.ai', 'alternative', 'comparison', 'transcription'] },
    { id: 'lp-pos-comparison', section: 'flagships', badge: 'DOC', title: 'Offline POS vs Cloud POS', cat: 'Competitor Comparison', tag: 'Zero Downtime', price: 'Architecture', url: 'offline-pos-vs-cloud-pos.html', desc: 'The definitive architectural comparison: sub-1ms local Rust vs cloud POS failure modes', keywords: ['pos comparison', 'cloud pos', 'offline pos', 'toast', 'square'] },

    // 5 Free In-Browser Tools
    { id: 'tool-webp', section: 'tools', badge: 'RAM', title: 'WebP Converter & Compressor', cat: 'Free Browser Tools', tag: 'RAM SIMD', price: 'Free', url: 'tools/offline-webp-compressor.html', desc: '80-92% image compression in browser memory without server upload', keywords: ['webp', 'tool', 'compress', 'image', 'converter'] },
    { id: 'tool-pdf', section: 'tools', badge: 'RAM', title: 'Forensic PDF Redactor', cat: 'Free Browser Tools', tag: 'RAM Blackout', price: 'Free', url: 'tools/offline-pdf-redactor.html', desc: 'Permanent destructive vector redaction in browser RAM', keywords: ['pdf', 'tool', 'redact', 'blackout', 'forensic'] },
    { id: 'tool-hash', section: 'tools', badge: 'RAM', title: 'SHA-256 Checksum Verifier', cat: 'Free Browser Tools', tag: 'Web Crypto', price: 'Free', url: 'tools/sha256-checksum-verifier.html', desc: 'Instant cryptographic bit-accuracy hash calculation', keywords: ['hash', 'sha256', 'tool', 'checksum', 'crypto'] },
    { id: 'tool-diff', section: 'tools', badge: 'RAM', title: 'Visual Text & Code Diff', cat: 'Free Browser Tools', tag: 'Diff Engine', price: 'Free', url: 'tools/offline-text-diff.html', desc: 'Side-by-side visual difference highlighting in browser memory', keywords: ['diff', 'tool', 'compare', 'code diff'] },
    { id: 'tool-qr', section: 'tools', badge: 'RAM', title: 'Vector QR Code Generator', cat: 'Free Browser Tools', tag: 'Vector Canvas', price: 'Free', url: 'tools/offline-qr-code-generator.html', desc: 'Offline vector UPI QR codes & barcodes with zero telemetry', keywords: ['qr', 'tool', 'upi', 'barcode', 'vector'] },

    // 10 Pages & Portals
    { id: 'page-store', section: 'portals', badge: 'PAGE', title: 'Commercial Store (31 Suites)', cat: 'Pages & Portals', tag: 'Primary Hub', price: '', url: 'store.html', desc: 'Browse all 31 air-gapped Rust software flagships & discounts', keywords: ['store', 'catalog', 'shop', 'pricing', 'discount', '31'] },
    { id: 'page-projects', section: 'portals', badge: 'PAGE', title: 'Systems Engineering Portfolio', cat: 'Pages & Portals', tag: 'Portfolio', price: '', url: 'projects.html', desc: 'Architectural blueprints, mathematical invariants & case studies', keywords: ['portfolio', 'projects', 'architecture', 'case studies'] },
    { id: 'page-experience', section: 'portals', badge: 'PAGE', title: 'Professional Experience & Radar', cat: 'Pages & Portals', tag: 'Founder Bio', price: '', url: 'experience.html', desc: '4+ years retail management, BCA & systems architecture radar', keywords: ['experience', 'bio', 'founder', 'resume', 'skills'] },
    { id: 'page-security', section: 'portals', badge: 'PAGE', title: 'Security & Trust Registry', cat: 'Pages & Portals', tag: 'Audit', price: '', url: 'security.html', desc: 'Microsoft Defender WDSI clean whitelist & SHA-256 proofs', keywords: ['security', 'trust', 'defender', 'wdsi', 'whitelist', 'audit'] },
    { id: 'page-aegis', section: 'portals', badge: 'PAGE', title: 'Aegis Process Middleware', cat: 'Pages & Portals', tag: 'Systems', price: '', url: 'aegis.html', desc: 'High-availability deterministic local process sentinel', keywords: ['aegis', 'middleware', 'sentinel', 'watchdog', 'daemon'] },
    { id: 'page-contact', section: 'portals', badge: 'PAGE', title: 'Contact & Executive Dispatch', cat: 'Pages & Portals', tag: 'Founder Direct', price: '', url: 'contact.html', desc: 'Direct briefing, email, and WhatsApp founder consultation', keywords: ['contact', 'briefing', 'email', 'whatsapp', 'call'] },
    { id: 'page-changelog', section: 'portals', badge: 'PAGE', title: 'Changelog & System Ledger', cat: 'Pages & Portals', tag: 'Releases', price: '', url: 'changelog.html', desc: 'Chronological release ledger & Win32 updates', keywords: ['changelog', 'releases', 'history', 'updates'] },
    { id: 'page-legal', section: 'portals', badge: 'PAGE', title: 'Legal & Commercial Governance', cat: 'Pages & Portals', tag: 'EULA', price: '', url: 'legal.html', desc: 'Statutory EULA, zero-telemetry covenants & DPDP Act compliance', keywords: ['legal', 'eula', 'terms', 'privacy policy', 'refund'] },
    { id: 'page-tools', section: 'portals', badge: 'PAGE', title: 'Free Sovereign Browser Tools', cat: 'Pages & Portals', tag: 'Web Tools', price: '', url: 'tools/index.html', desc: 'Five 100% in-browser RAM utilities that work offline', keywords: ['tools hub', 'web tools', 'free'] },
    { id: 'page-research', section: 'portals', badge: 'PAGE', title: 'Engineering Research Papers', cat: 'Pages & Portals', tag: 'Monographs', price: '', url: 'research/index.html', desc: 'In-depth systems monographs on pure native Rust and memory', keywords: ['research', 'papers', 'monographs', 'whitepaper'] },

    // 5 Quick Actions
    { id: 'act-briefing', section: 'actions', badge: 'ACT', title: 'Schedule 20-Min Technical Briefing', cat: 'Quick Actions', tag: 'Calendly', price: 'Free', url: 'https://calendly.com/rehanquantlab', desc: 'Book a 1-on-1 systems briefing with Founder Mohammad Rehan', keywords: ['briefing', 'calendly', 'meeting', 'schedule', 'call'] },
    { id: 'act-whatsapp', section: 'actions', badge: 'ACT', title: 'Chat Directly on WhatsApp', cat: 'Quick Actions', tag: 'Instant', price: '', url: 'https://wa.me/917091518548?text=Hello%20Rehan,%20I%20am%20reaching%20out%20from%20your%20command%20palette.', desc: 'Open direct WhatsApp chat (+91 70915 18548)', keywords: ['whatsapp', 'chat', 'message', 'support'] },
    { id: 'act-email', section: 'actions', badge: 'ACT', title: 'Copy Founder Email', cat: 'Quick Actions', tag: 'Clipboard', price: '', action: 'copy_email', desc: 'Copy founder@rehanquantlab.com to clipboard', keywords: ['email', 'copy', 'mail', 'inbox'] },
    { id: 'act-resume', section: 'actions', badge: 'ACT', title: 'Download Resume (PDF)', cat: 'Quick Actions', tag: 'Download', price: '', url: 'Mohammad_Rehan_Resume.pdf', desc: 'Download Mohammad Rehan verified resume document', keywords: ['resume', 'cv', 'pdf', 'download resume'] },
    { id: 'act-dare', section: 'actions', badge: 'ACT', title: 'Take 5-Sec Air-Gap Challenge', cat: 'Quick Actions', tag: 'Interactive', price: '', url: 'store.html#sovereign-sandbox-section', desc: 'Unplug your internet and test our algorithms live', keywords: ['air-gap', 'challenge', 'offline test', 'sandbox'] }
  ];

  var paletteOpen = false;
  var paletteActiveIdx = 0;
  var paletteFiltered = [];
  var paletteActiveTab = 'all';

  function buildPaletteDOM() {
    if (document.getElementById('rql-palette-backdrop')) return;

    var backdrop = document.createElement('div');
    backdrop.id = 'rql-palette-backdrop';
    backdrop.setAttribute('role', 'dialog');
    backdrop.setAttribute('aria-modal', 'true');
    backdrop.setAttribute('aria-label', 'Command Palette');

    var modalHtml = [
      '<div id="rql-palette-modal">',
      '  <div class="p-3.5 sm:p-4 border-b border-slate-800 flex items-center gap-3 bg-slate-950/90">',
      '    <svg class="w-5 h-5 text-indigo-400 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">',
      '      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />',
      '    </svg>',
      '    <input id="rql-palette-input" type="text" autocomplete="off" spellcheck="false" placeholder="Search 31 Rust suites, portals, free tools, or actions..." class="w-full bg-transparent text-white placeholder-slate-500 font-sans text-sm sm:text-base outline-none pr-2" />',
      '    <span id="rql-palette-count" class="hidden sm:inline-block text-[11px] font-mono text-slate-500 font-bold shrink-0">56 Items</span>',
      '    <kbd class="hidden sm:inline-block bg-slate-900 border border-slate-700 text-slate-400 text-[10px] font-mono px-2 py-0.5 rounded font-bold shrink-0">ESC</kbd>',
      '    <button id="rql-palette-close-btn" class="sm:hidden text-slate-400 hover:text-white p-1" aria-label="Close palette">',
      '      <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>',
      '    </button>',
      '  </div>',
      '  <div class="rql-palette-tabs">',
      '    <button type="button" class="rql-palette-tab active" data-tab="all">All (56)</button>',
      '    <button type="button" class="rql-palette-tab" data-tab="suites">31 Suites</button>',
      '    <button type="button" class="rql-palette-tab" data-tab="flagships">Landing Pages (10)</button>',
      '    <button type="button" class="rql-palette-tab" data-tab="tools">Free Web Tools (5)</button>',
      '    <button type="button" class="rql-palette-tab" data-tab="portals">Portals (10)</button>',
      '    <button type="button" class="rql-palette-tab" data-tab="actions">Actions (5)</button>',
      '  </div>',
      '  <div id="rql-palette-results" data-lenis-prevent="true" class="overflow-y-auto p-2 sm:p-3 space-y-1 divide-y divide-slate-800/40 text-xs font-sans" style="max-height: 440px; overscroll-behavior: contain;">',
      '  </div>',
      '  <div class="p-3 bg-slate-950 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-2 text-[11px] font-mono text-slate-500">',
      '    <div class="flex items-center gap-3">',
      '      <span><kbd class="bg-slate-900 px-1.5 py-0.5 rounded text-slate-400 border border-slate-800">&uarr;&darr;</kbd> Navigate</span>',
      '      <span><kbd class="bg-slate-900 px-1.5 py-0.5 rounded text-slate-400 border border-slate-800">Enter</kbd> Select</span>',
      '    </div>',
      '    <span class="text-emerald-400 font-bold">100% Offline Rust Ecosystem</span>',
      '  </div>',
      '</div>'
    ].join('\n');

    backdrop.innerHTML = modalHtml;
    document.body.appendChild(backdrop);

    backdrop.addEventListener('click', function(e) {
      if (e.target === backdrop) window.closeRQLPalette();
    });

    var closeBtn = document.getElementById('rql-palette-close-btn');
    if (closeBtn) {
      closeBtn.addEventListener('click', function() {
        window.closeRQLPalette();
      });
    }

    var tabs = backdrop.querySelectorAll('.rql-palette-tab');
    tabs.forEach(function(tab) {
      tab.addEventListener('click', function() {
        tabs.forEach(function(t) { t.classList.remove('active'); });
        tab.classList.add('active');
        paletteActiveTab = tab.getAttribute('data-tab');
        var inputEl = document.getElementById('rql-palette-input');
        var q = inputEl ? inputEl.value.trim().toLowerCase() : '';
        renderPaletteResults(q);
        if (window.playTactileClick) window.playTactileClick('toggle');
      });
    });

    var input = document.getElementById('rql-palette-input');
    if (input) {
      input.addEventListener('input', function() {
        renderPaletteResults(this.value.trim().toLowerCase());
      });

      input.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowDown') {
          e.preventDefault();
          paletteActiveIdx = Math.min(paletteFiltered.length - 1, paletteActiveIdx + 1);
          updatePaletteActiveUI();
          if (window.playTactileClick) window.playTactileClick('click');
        } else if (e.key === 'ArrowUp') {
          e.preventDefault();
          paletteActiveIdx = Math.max(0, paletteActiveIdx - 1);
          updatePaletteActiveUI();
          if (window.playTactileClick) window.playTactileClick('click');
        } else if (e.key === 'Enter') {
          e.preventDefault();
          executePaletteItem(paletteFiltered[paletteActiveIdx]);
        } else if (e.key === 'Escape') {
          e.preventDefault();
          window.closeRQLPalette();
        }
      });
    }
  }

  function updatePaletteActiveUI() {
    var items = document.querySelectorAll('.rql-palette-item');
    items.forEach(function(el, i) {
      if (i === paletteActiveIdx) {
        el.classList.add('rql-item-active');
        el.scrollIntoView({ block: 'nearest' });
      } else {
        el.classList.remove('rql-item-active');
      }
    });
  }

  function executePaletteItem(item) {
    if (!item) return;
    if (window.playTactileClick) window.playTactileClick('success');
    window.closeRQLPalette();

    if (item.action === 'copy_email') {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText('founder@rehanquantlab.com').then(function() {
          if (window.showRQLToast) window.showRQLToast('Email copied: founder@rehanquantlab.com', 'success');
        });
      }
      return;
    }

    if (item.url) {
      var isCurrentStore = window.location.pathname.indexOf('store') !== -1;
      if (item.url.indexOf('store.html#') !== -1 && isCurrentStore) {
        var hash = item.url.split('#')[1];
        if (hash) {
          window.location.hash = hash;
          return;
        }
      }
      if (item.url.indexOf('http') === 0) {
        window.open(item.url, '_blank', 'noopener,noreferrer');
      } else {
        window.location.href = item.url;
      }
    }
  }

  function renderPaletteResults(query) {
    var container = document.getElementById('rql-palette-results');
    var countEl = document.getElementById('rql-palette-count');
    if (!container) return;

    var baseData = RQL_PALETTE_DATA;
    if (paletteActiveTab !== 'all') {
      baseData = RQL_PALETTE_DATA.filter(function(item) {
        return item.section === paletteActiveTab;
      });
    }

    if (!query) {
      paletteFiltered = baseData;
    } else {
      // Smart search: special handling for "31", "31 suites", "suites", "all"
      if (query === '31' || query === '31 suites' || query === 'all suites' || query === 'suites' || query === 'commercial') {
        var allSuites = RQL_PALETTE_DATA.filter(function(i) { return i.section === 'suites'; });
        var storeHub = RQL_PALETTE_DATA.filter(function(i) { return i.id === 'page-store'; });
        var folderSync = RQL_PALETTE_DATA.filter(function(i) { return i.id === 'rql-foldersync'; });
        var otherSuites = allSuites.filter(function(i) { return i.id !== 'rql-foldersync'; });
        paletteFiltered = storeHub.concat(folderSync).concat(otherSuites);
      } else {
        var scored = [];
        var numMatch = query.replace(/[^0-9]/g, '');
        var paddedNum = numMatch.length === 1 ? '0' + numMatch : numMatch;

        baseData.forEach(function(item) {
          var score = 0;
          var titleL = item.title.toLowerCase();
          var descL = item.desc.toLowerCase();
          var catL = item.cat.toLowerCase();
          var tagL = (item.tag || '').toLowerCase();

          // Exact suite number match (e.g. searching "12" or "suite 12")
          if (item.suiteNum && (item.suiteNum === paddedNum || item.suiteNum === numMatch)) {
            score += 150;
          }

          if (titleL === query) {
            score += 120;
          } else if (titleL.indexOf(query) === 0) {
            score += 90;
          } else if (titleL.indexOf(query) !== -1) {
            score += 70;
          }

          if (item.keywords && item.keywords.some(function(k) { return k.indexOf(query) !== -1; })) {
            score += 60;
          }

          if (tagL.indexOf(query) !== -1) {
            score += 45;
          }

          if (catL.indexOf(query) !== -1) {
            score += 35;
          }

          if (descL.indexOf(query) !== -1) {
            score += 20;
          }

          if (score > 0) {
            scored.push({ item: item, score: score });
          }
        });

        scored.sort(function(a, b) { return b.score - a.score; });
        paletteFiltered = scored.map(function(s) { return s.item; });
      }
    }

    if (countEl) {
      countEl.textContent = paletteFiltered.length + (paletteFiltered.length === 1 ? ' Match' : ' Matches');
    }

    paletteActiveIdx = 0;

    if (paletteFiltered.length === 0) {
      container.innerHTML = [
        '<div class="p-8 text-center space-y-2">',
        '  <div class="text-slate-400 font-bold text-sm">No software suites or pages found for "' + query.replace(/</g, '&lt;') + '"</div>',
        '  <p class="text-slate-500 text-xs">Try searching for "PDF", "POS", "Whisper", "Rust", "Hash", "SLA", "31", or "Contact".</p>',
        '</div>'
      ].join('');
      return;
    }

    var html = [];
    var currentSection = '';

    paletteFiltered.forEach(function(item, idx) {
      // Group by logical section when browsing or filtering without single query
      var sectionLabel = '';
      if (!query || paletteActiveTab === 'all') {
        if (item.section !== currentSection) {
          currentSection = item.section;
          if (currentSection === 'suites') {
            sectionLabel = 'Commercial Suites (31 Air-Gapped Workstations)';
          } else if (currentSection === 'flagships') {
            sectionLabel = 'Dedicated Flagship Landing Pages & Comparisons';
          } else if (currentSection === 'tools') {
            sectionLabel = 'Free In-Browser Web Tools (RAM SIMD)';
          } else if (currentSection === 'portals') {
            sectionLabel = 'Pages & Citadel Portals';
          } else if (currentSection === 'actions') {
            sectionLabel = 'Quick Actions & Executive Dispatch';
          } else {
            sectionLabel = item.cat;
          }
          html.push('<div class="rql-section-header">' + sectionLabel + '</div>');
        }
      }

      var activeClass = idx === 0 ? ' rql-item-active' : '';
      var priceBadge = item.price ? '<span class="text-emerald-400 font-mono font-bold text-xs shrink-0">' + item.price + '</span>' : '';
      var tagBadge = item.tag ? '<span class="px-2 py-0.5 rounded bg-slate-900 border border-slate-800 text-[10px] font-mono text-cyan-300 font-bold shrink-0">' + item.tag + '</span>' : '';

      // Determine left badge display (true suite number for suites, badge for others)
      var leftBadge = '';
      if (item.suiteNum) {
        leftBadge = item.suiteNum;
      } else if (item.badge) {
        leftBadge = item.badge;
      } else {
        leftBadge = (idx < 9 ? '0' + (idx + 1) : (idx + 1));
      }

      html.push([
        '<div class="rql-palette-item' + activeClass + '" data-idx="' + idx + '">',
        '  <div class="flex items-center gap-3 overflow-hidden pr-2">',
        '    <div class="w-8 h-8 rounded-lg bg-slate-900 border border-slate-800 text-indigo-400 flex items-center justify-center shrink-0 font-mono font-bold text-xs">',
        '      ' + leftBadge,
        '    </div>',
        '    <div class="overflow-hidden">',
        '      <div class="font-bold text-white text-xs truncate flex items-center gap-2">',
        '        <span>' + item.title + '</span>',
        '        ' + tagBadge,
        '      </div>',
        '      <div class="text-slate-400 text-[11px] truncate mt-0.5">' + item.desc + '</div>',
        '    </div>',
        '  </div>',
        '  ' + priceBadge,
        '</div>'
      ].join(''));
    });

    container.innerHTML = html.join('');

    var renderedItems = container.querySelectorAll('.rql-palette-item');
    renderedItems.forEach(function(el) {
      el.addEventListener('mouseenter', function() {
        var idx = parseInt(this.getAttribute('data-idx'), 10);
        if (!isNaN(idx)) {
          paletteActiveIdx = idx;
          updatePaletteActiveUI();
        }
      });
      el.addEventListener('click', function() {
        var idx = parseInt(this.getAttribute('data-idx'), 10);
        if (!isNaN(idx)) {
          executePaletteItem(paletteFiltered[idx]);
        }
      });
    });
  }

  window.openRQLPalette = function() {
    buildPaletteDOM();
    var backdrop = document.getElementById('rql-palette-backdrop');
    var input = document.getElementById('rql-palette-input');
    if (!backdrop || !input) return;

    paletteOpen = true;
    backdrop.classList.add('rql-palette-open');
    input.value = '';
    paletteActiveTab = 'all';
    var tabs = backdrop.querySelectorAll('.rql-palette-tab');
    tabs.forEach(function(t) {
      if (t.getAttribute('data-tab') === 'all') {
        t.classList.add('active');
      } else {
        t.classList.remove('active');
      }
    });
    renderPaletteResults('');
    setTimeout(function() {
      input.focus();
    }, 50);

    if (window.playTactileClick) window.playTactileClick('toggle');
    if (window.rqlLenis) window.rqlLenis.stop();
  };

  window.closeRQLPalette = function() {
    var backdrop = document.getElementById('rql-palette-backdrop');
    if (!backdrop) return;
    paletteOpen = false;
    backdrop.classList.remove('rql-palette-open');
    if (window.rqlLenis) window.rqlLenis.start();
  };

  // 12. Global Keyboard Shortcut for Command Palette (Ctrl+K, Cmd+K, Slash)
  function initCommandPalette() {
    window.addEventListener('keydown', function(e) {
      if ((e.ctrlKey || e.metaKey) && (e.key === 'k' || e.key === 'K')) {
        e.preventDefault();
        if (paletteOpen) {
          window.closeRQLPalette();
        } else {
          window.openRQLPalette();
        }
        return;
      }

      if (e.key === 'Escape' && paletteOpen) {
        e.preventDefault();
        window.closeRQLPalette();
        return;
      }

      if (e.key === '/' && !paletteOpen) {
        var tag = (e.target && e.target.tagName) ? e.target.tagName.toLowerCase() : '';
        if (tag !== 'input' && tag !== 'textarea') {
          e.preventDefault();
          window.openRQLPalette();
        }
      }
    });

    document.querySelectorAll('[data-open-palette]').forEach(function(el) {
      el.addEventListener('click', function(e) {
        e.preventDefault();
        window.openRQLPalette();
      });
    });
  }


  // 13. Deep-Link Target Highlighting & Category Auto-Switching
  function handleDeepLinkFocus() {
    var hash = window.location.hash;
    if (!hash || hash.length < 2) return;
    var targetId = hash.substring(1);
    var el = document.getElementById(targetId);
    if (!el) return;

    // If on store page and element has category, auto-switch store tab!
    var cat = el.getAttribute('data-category');
    if (cat && typeof window.switchStoreTab === 'function') {
      window.switchStoreTab(cat);
    }

    setTimeout(function() {
      el.scrollIntoView({ behavior: 'smooth', block: 'center' });
      el.classList.add('rql-highlight-target');
      setTimeout(function() {
        el.classList.remove('rql-highlight-target');
      }, 6000);
    }, 250);
  }

  // window.addEventListener('hashchange', handleDeepLinkFocus); -> DISABLED: no involuntary scroll jumping

  // Self-Executing DOM Initialization
  function boot() {
    // Pure rock-solid stability - NO scroll hijacking, NO 3D wobbling, NO magnetic drifting
    initLenis(); // Active: Lenis hardware-accelerated momentum scroll
    // init3DTiltCards(); -> DISABLED: no annoying wobbling cards
    // initMagneticButtons(); -> DISABLED: buttons stay strictly in place
    // initStaggeredReveals(); -> DISABLED: zero layout shifts
    initOdometers();
    initScrollProgress();
    initDiscountCodeCopy();
    initCommandPalette();
    // handleDeepLinkFocus(); -> DISABLED: no involuntary auto-scrolling
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
