/**
 * RQL ACETERNITY 3D CARD TILT ENGINE
 * Mathematical perspective tilt tracking cursor velocity with depth layering.
 * 100% 7-bit ASCII clean. Zero external dependencies.
 */
(function() {
  'use strict';

  function init3DTilt() {
    // Disable on touch devices to avoid interference with scrolling
    if ('ontouchstart' in window || navigator.maxTouchPoints > 0) return;

    var cards = document.querySelectorAll('.aside-window-frame, .aceternity-3d-card, .conwest-card, .zagato-card');

    cards.forEach(function(card) {
      // Ensure parent has perspective
      if (!card.parentElement.classList.contains('aceternity-3d-wrap')) {
        card.parentElement.classList.add('aceternity-3d-wrap');
      }
      card.classList.add('aceternity-3d-card');

      var rect = null;

      function onMouseEnter() {
        rect = card.getBoundingClientRect();
      }

      function onMouseMove(e) {
        if (!rect) rect = card.getBoundingClientRect();
        var x = (e.clientX - rect.left - rect.width / 2) / (rect.width / 2);
        var y = (e.clientY - rect.top - rect.height / 2) / (rect.height / 2);

        // Max tilt angles: 8 degrees X/Y
        var tiltX = -(y * 8).toFixed(2);
        var tiltY = (x * 8).toFixed(2);

        card.style.transform = 'perspective(1200px) rotateX(' + tiltX + 'deg) rotateY(' + tiltY + 'deg) scale3d(1.01, 1.01, 1.01)';
      }

      function onMouseLeave() {
        card.style.transform = 'perspective(1200px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
        rect = null;
      }

      card.addEventListener('mouseenter', onMouseEnter, { passive: true });
      card.addEventListener('mousemove', onMouseMove, { passive: true });
      card.addEventListener('mouseleave', onMouseLeave, { passive: true });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init3DTilt);
  } else {
    init3DTilt();
  }
})();
