/**
 * RQL WAVY RIBBON CANVAS ENGINE (Aceternity WavyBackground Standard)
 * Ultra-performance, multi-harmonic sine ribbon wave generator.
 * 60-144 FPS V-Sync, High-DPI retina calibrated, interactive mouse ripple.
 * 100% 7-bit ASCII clean. Zero external dependencies.
 */
(function() {
  'use strict';

  function initWavyRibbon() {
    var canvas = document.getElementById('rql-wavy-canvas');
    if (!canvas) return;

    var ctx = canvas.getContext('2d');
    if (!ctx) return;

    var width = 0;
    var height = 0;
    var dpr = window.devicePixelRatio || 1;
    var time = 0;
    var mouseX = -1000;
    var mouseY = -1000;
    var targetMouseX = -1000;
    var targetMouseY = -1000;

    var colors = [
      'rgba(16, 185, 129, 0.45)', // Emerald
      'rgba(56, 189, 248, 0.40)', // Sky
      'rgba(129, 140, 248, 0.35)', // Indigo
      'rgba(168, 85, 247, 0.30)', // Violet
      'rgba(20, 184, 166, 0.40)'  // Teal
    ];

    function resize() {
      width = canvas.parentElement ? canvas.parentElement.clientWidth : window.innerWidth;
      height = canvas.parentElement ? canvas.parentElement.clientHeight : window.innerHeight;
      canvas.width = Math.floor(width * dpr);
      canvas.height = Math.floor(height * dpr);
      canvas.style.width = width + 'px';
      canvas.style.height = height + 'px';
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    window.addEventListener('resize', resize, { passive: true });
    resize();

    window.addEventListener('mousemove', function(e) {
      var rect = canvas.getBoundingClientRect();
      targetMouseX = e.clientX - rect.left;
      targetMouseY = e.clientY - rect.top;
    }, { passive: true });

    window.addEventListener('mouseleave', function() {
      targetMouseX = -1000;
      targetMouseY = -1000;
    });

    function drawWave(index, total) {
      var waveColor = colors[index % colors.length];
      var baseFreq = 0.002 + index * 0.0006;
      var speed = 0.015 + index * 0.004;
      var amplitude = 35 + index * 8;
      var yOffset = height * 0.52 + (index - total / 2) * 18;

      ctx.beginPath();
      ctx.lineWidth = 32 - index * 3;
      ctx.strokeStyle = waveColor;
      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';

      var step = 8;
      for (var x = 0; x <= width + step; x += step) {
        // Multi-frequency harmonic wave formula
        var harmonic = Math.sin(x * baseFreq + time * speed) *
                       Math.cos(x * (baseFreq * 0.5) - time * (speed * 0.7));
        var y = yOffset + harmonic * amplitude;

        // Mouse displacement ripple
        var dx = x - mouseX;
        var dy = y - mouseY;
        var dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 180) {
          var push = (1 - dist / 180) * 45;
          y += (dy > 0 ? push : -push);
        }

        if (x === 0) {
          ctx.moveTo(x, y);
        } else {
          ctx.lineTo(x, y);
        }
      }

      ctx.stroke();
    }

    var isVisible = true;
    if ('IntersectionObserver' in window) {
      var observer = new IntersectionObserver(function(entries) {
        isVisible = entries[0].isIntersecting;
      }, { threshold: 0.05 });
      observer.observe(canvas);
    }

    function animate() {
      if (isVisible) {
        time += 1;
        // Smooth mouse lerp
        mouseX += (targetMouseX - mouseX) * 0.08;
        mouseY += (targetMouseY - mouseY) * 0.08;

        ctx.clearRect(0, 0, width, height);

        for (var i = 0; i < colors.length; i++) {
          drawWave(i, colors.length);
        }
      }
      requestAnimationFrame(animate);
    }

    requestAnimationFrame(animate);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initWavyRibbon);
  } else {
    initWavyRibbon();
  }
})();
