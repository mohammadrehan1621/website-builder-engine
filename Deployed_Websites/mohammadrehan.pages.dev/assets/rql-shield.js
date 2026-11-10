/**
 * ====================================================================
 * 🛡️ REHAN QUANT LAB™ — UNIVERSAL ROUTE & BUTTON OBFUSCATION SHIELD
 * ====================================================================
 * Client-Side Route Hydration Engine
 * Blinds automated web scrapers, crawler spiders, and contact harvesters.
 * Zero plaintext emails, zero plaintext WhatsApp numbers, zero plaintext
 * affiliate routes in the static HTML DOM.
 * 
 * Invoked instantaneously in local RAM upon verified human interaction.
 * ====================================================================
 */
(function () {
  'use strict';

  // Institutional Named Route Registry (Base64 Encoded in Static Memory)
  var ROUTE_VAULT = {
    'vip-onboard': 'aHR0cHM6Ly93YS5tZS85MTcwOTE1MTg1NDg=',
    'founder-mail': 'bWFpbHRvOmZvdW5kZXJAcmVoYW5xdWFudGxhYi5jb20=',
    'support-mail': 'bWFpbHRvOnJlaGFucXVhbnRsYWJAZ21haWwuY29t',
    'privacy-mail': 'bWFpbHRvOnByaXZhY3lAcmVoYW5xdWFudGxhYi5jb20=',
    'contact-mail': 'bWFpbHRvOmNvbnRhY3RAcmVoYW5xdWFudGxhYi5jb20=',
    'gumroad-store': 'aHR0cHM6Ly9xdWFudGlmeTE3Lmd1bXJvYWQuY29t',
    'gumroad-affiliates': 'aHR0cHM6Ly9xdWFudGlmeTE3Lmd1bXJvYWQuY29tL2FmZmlsaWF0ZXM=',
    'gumroad-pricetag': 'aHR0cHM6Ly9xdWFudGlmeTE3Lmd1bXJvYWQuY29tL2wvcnFsLXByaWNldGFn',
    'gumroad-dpdpshield': 'aHR0cHM6Ly9xdWFudGlmeTE3Lmd1bXJvYWQuY29tL2wvcnFsLWRwZHBzaGllbGQ=',
    'gumroad-documentshield': 'aHR0cHM6Ly9xdWFudGlmeTE3Lmd1bXJvYWQuY29tL2wvcnFsLWRvY3VtZW50c2hpZWxk',
    'gumroad-whispervault': 'aHR0cHM6Ly9xdWFudGlmeTE3Lmd1bXJvYWQuY29tL2wvcnFsLXdoaXNwZXJ2YXVsdA==',
    'gumroad-retailpos': 'aHR0cHM6Ly9xdWFudGlmeTE3Lmd1bXJvYWQuY29tL2wvcnFsLXJldGFpbHBvcw==',
    'gumroad-storechain': 'aHR0cHM6Ly9xdWFudGlmeTE3Lmd1bXJvYWQuY29tL2wvcnFsLXN0b3JlY2hhaW4=',
    'gumroad-conduit': 'aHR0cHM6Ly9xdWFudGlmeTE3Lmd1bXJvYWQuY29tL2wvcnFsLWNvbmR1aXQ=',
    'gumroad-hashcheck': 'aHR0cHM6Ly9xdWFudGlmeTE3Lmd1bXJvYWQuY29tL2wvcnFsLWhhc2hjaGVjaw==',
    'gumroad-qrstudio': 'aHR0cHM6Ly9xdWFudGlmeTE3Lmd1bXJvYWQuY29tL2wvcnFsLXFyc3R1ZGlv',
    'gumroad-textdiff': 'aHR0cHM6Ly9xdWFudGlmeTE3Lmd1bXJvYWQuY29tL2wvcnFsLXRleHRkaWZm',
    'gumroad-renamer': 'aHR0cHM6Ly9xdWFudGlmeTE3Lmd1bXJvYWQuY29tL2wvcnFsLXJlbmFtZXI=',
    'gumroad-tageditor': 'aHR0cHM6Ly9xdWFudGlmeTE3Lmd1bXJvYWQuY29tL2wvcnFsLXRhZ2VkaXRvcg==',
    'gumroad-fontviewer': 'aHR0cHM6Ly9xdWFudGlmeTE3Lmd1bXJvYWQuY29tL2wvcnFsLWZvbnR2aWV3ZXI=',
    'gumroad-pdfmerge': 'aHR0cHM6Ly9xdWFudGlmeTE3Lmd1bXJvYWQuY29tL2wvcnFsLXBkZm1lcmdl',
    'gumroad-taxledger': 'aHR0cHM6Ly9xdWFudGlmeTE3Lmd1bXJvYWQuY29tL2wvcnFsLXRheGxlZGdlcg==',
    'gumroad-fileshredder': 'aHR0cHM6Ly9xdWFudGlmeTE3Lmd1bXJvYWQuY29tL2wvcnFsLWZpbGVzaHJlZGRlcg==',
    'gumroad-clipvault': 'aHR0cHM6Ly9xdWFudGlmeTE3Lmd1bXJvYWQuY29tL2wvcnFsLWNsaXB2YXVsdA==',
    'gumroad-imagebatch': 'aHR0cHM6Ly9xdWFudGlmeTE3Lmd1bXJvYWQuY29tL2wvcnFsLWltYWdlYmF0Y2g='
  };

  function hydrateString(b64) {
    try {
      return decodeURIComponent(escape(window.atob(b64)));
    } catch (e) {
      try {
        return window.atob(b64);
      } catch (err) {
        return null;
      }
    }
  }

  function dispatchAction(el) {
    if (!el) return;
    var targetUrl = null;

    if (el.dataset.obf) {
      targetUrl = hydrateString(el.dataset.obf);
    } else if (el.dataset.route && ROUTE_VAULT[el.dataset.route]) {
      targetUrl = hydrateString(ROUTE_VAULT[el.dataset.route]);
    }

    if (!targetUrl) return;

    if (targetUrl.indexOf('mailto:') === 0) {
      window.location.href = targetUrl;
    } else {
      window.open(targetUrl, '_blank', 'noopener,noreferrer');
    }
  }

  // Delegated click listener (captures all dynamic & static elements)
  document.addEventListener('click', function (e) {
    var trigger = e.target.closest('[data-route], [data-obf]');
    if (!trigger) return;

    e.preventDefault();
    e.stopPropagation();
    dispatchAction(trigger);
  }, true);

  // Keyboard accessibility (Enter & Space trigger click)
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') {
      var trigger = e.target.closest('[data-route], [data-obf]');
      if (!trigger) return;

      e.preventDefault();
      e.stopPropagation();
      dispatchAction(trigger);
    }
  }, true);

  // Hydrate DOM on load for accessibility & styling
  function secureElements() {
    var nodes = document.querySelectorAll('[data-route], [data-obf]');
    for (var i = 0; i < nodes.length; i++) {
      var node = nodes[i];
      if (!node.getAttribute('role')) {
        node.setAttribute('role', 'button');
      }
      if (!node.hasAttribute('tabindex')) {
        node.setAttribute('tabindex', '0');
      }
      node.style.cursor = 'pointer';
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', secureElements);
  } else {
    secureElements();
  }
})();
