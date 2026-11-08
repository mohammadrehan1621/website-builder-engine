/**
 * RQL 3D Fluid Particle Wave Engine v1.0
 * Pure Native HTML5 Canvas 3D Perspective Wave (Linear / Stripe Style)
 * Supports 60Hz, 120Hz, 144Hz, 180Hz+ V-Sync with Delta-Time Normalization
 * 100% Self-Hosted &bull; Zero External Dependencies &bull; 100% 7-Bit ASCII
 */
(function() {
    'use strict';

    function initWave() {
        var canvases = document.querySelectorAll('.rql-3d-wave-canvas');
        if (canvases.length === 0) {
            var containers = document.querySelectorAll('.rql-wave-mount, #hero-section, .hero-section, main > section:first-of-type, .legal-hero, .aurora-container');
            var target = containers.length > 0 ? containers[0] : (document.querySelector('.card') ? document.body : null);
            if (target) {
                var canvas = document.createElement('canvas');
                canvas.className = 'rql-3d-wave-canvas';
                canvas.style.position = 'absolute';
                canvas.style.top = '0';
                canvas.style.left = '0';
                canvas.style.width = '100%';
                canvas.style.height = '100%';
                canvas.style.pointerEvents = 'none';
                canvas.style.zIndex = '1';
                canvas.style.opacity = '0.72';
                if (!target.style.position || target.style.position === 'static') {
                    target.style.position = 'relative';
                }
                target.insertBefore(canvas, target.firstChild);
                canvases = [canvas];
            }
        }

        for (var i = 0; i < canvases.length; i++) {
            setupSingleWave(canvases[i]);
        }
    }

    function setupSingleWave(canvas) {
        var ctx = canvas.getContext('2d', { alpha: true });
        if (!ctx) return;

        var width = 0;
        var height = 0;
        var dpr = Math.min(window.devicePixelRatio || 1, 2);

        var COLS = 54;
        var ROWS = 26;
        var SPACING_X = 42;
        var SPACING_Z = 36;
        var FOV = 320;
        var CAMERA_Y = 150;
        var CAMERA_Z = -80;

        var waveTime = 0;
        var lastTimestamp = performance.now();
        var animationFrameId = null;
        var isVisible = true;
        var isTabActive = true;

        var mouseX = -9999;
        var mouseY = -9999;
        var targetMouseX = -9999;
        var targetMouseY = -9999;
        var MOUSE_RADIUS = 180;

        function resize() {
            var rect = canvas.getBoundingClientRect();
            width = rect.width || (canvas.parentElement ? canvas.parentElement.clientWidth : 0) || window.innerWidth;
            height = rect.height || (canvas.parentElement ? canvas.parentElement.clientHeight : 0) || 600;
            dpr = Math.min(window.devicePixelRatio || 1, 2);

            canvas.width = Math.floor(width * dpr);
            canvas.height = Math.floor(height * dpr);
            ctx.scale(dpr, dpr);
        }

        resize();
        window.addEventListener('resize', resize, { passive: true });

        var parent = canvas.parentElement || window;
        parent.addEventListener('mousemove', function(e) {
            var rect = canvas.getBoundingClientRect();
            targetMouseX = e.clientX - rect.left;
            targetMouseY = e.clientY - rect.top;
        }, { passive: true });

        parent.addEventListener('mouseleave', function() {
            targetMouseX = -9999;
            targetMouseY = -9999;
        }, { passive: true });

        parent.addEventListener('touchmove', function(e) {
            if (e.touches && e.touches.length > 0) {
                var rect = canvas.getBoundingClientRect();
                targetMouseX = e.touches[0].clientX - rect.left;
                targetMouseY = e.touches[0].clientY - rect.top;
            }
        }, { passive: true });

        parent.addEventListener('touchend', function() {
            targetMouseX = -9999;
            targetMouseY = -9999;
        }, { passive: true });

        if ('IntersectionObserver' in window) {
            var observer = new IntersectionObserver(function(entries) {
                for (var i = 0; i < entries.length; i++) {
                    isVisible = entries[i].isIntersecting;
                    if (isVisible && isTabActive && !animationFrameId) {
                        lastTimestamp = performance.now();
                        render(lastTimestamp);
                    }
                }
            }, { threshold: 0.05 });
            observer.observe(canvas);
        }

        document.addEventListener('visibilitychange', function() {
            isTabActive = !document.hidden;
            if (isTabActive && isVisible && !animationFrameId) {
                lastTimestamp = performance.now();
                render(lastTimestamp);
            }
        });

        function render(currentTimestamp) {
            if (!isVisible || !isTabActive) {
                animationFrameId = null;
                return;
            }

            animationFrameId = requestAnimationFrame(render);

            var dt = Math.min((currentTimestamp - lastTimestamp) / 1000, 0.1);
            lastTimestamp = currentTimestamp;

            waveTime += dt * 1.35;

            mouseX += (targetMouseX - mouseX) * 0.1;
            mouseY += (targetMouseY - mouseY) * 0.1;

            ctx.clearRect(0, 0, width, height);

            var centerX = width * 0.5;
            var centerY = height * 0.52;
            var gridWidth = (COLS - 1) * SPACING_X;
            var startX = -gridWidth * 0.5;

            var projectedGrid = [];

            for (var r = 0; r < ROWS; r++) {
                projectedGrid[r] = [];
                var z = r * SPACING_Z + 120;
                var depthZ = z - CAMERA_Z;

                if (depthZ <= 10) continue;

                var scale = FOV / depthZ;

                for (var c = 0; c < COLS; c++) {
                    var x = startX + c * SPACING_X;

                    var w1 = Math.sin(c * 0.16 + waveTime * 1.5) * 24;
                    var w2 = Math.cos(r * 0.22 + waveTime * 1.1) * 18;
                    var w3 = Math.sin((c * 0.08 + r * 0.12) + waveTime * 0.9) * 14;
                    var y = w1 + w2 + w3;

                    var projX = centerX + x * scale;
                    var projY = centerY + (y - CAMERA_Y) * scale;

                    if (mouseX > -500) {
                        var dx = projX - mouseX;
                        var dy = projY - mouseY;
                        var dist = Math.sqrt(dx * dx + dy * dy);
                        if (dist < MOUSE_RADIUS) {
                            var force = (1 - dist / MOUSE_RADIUS);
                            var ripple = Math.sin(dist * 0.08 - waveTime * 4.5) * force * 38;
                            y += ripple;
                        }
                    }

                    var finalProjY = centerY + (y - CAMERA_Y) * scale;
                    var depthFactor = (r / ROWS);
                    var alpha = Math.max(0.08, (1 - depthFactor * 0.78) * 0.65);
                    var pointRadius = Math.max(0.8, (2.2 * scale));

                    projectedGrid[r][c] = {
                        x: projX,
                        y: finalProjY,
                        scale: scale,
                        alpha: alpha,
                        radius: pointRadius,
                        elevation: y
                    };
                }
            }

            ctx.lineWidth = 0.75;
            for (var cIdx = 0; cIdx < COLS; cIdx += 2) {
                ctx.beginPath();
                var started = false;
                for (var rIdx = 0; rIdx < ROWS; rIdx++) {
                    var pt = projectedGrid[rIdx] && projectedGrid[rIdx][cIdx];
                    if (!pt || pt.x < -50 || pt.x > width + 50) continue;

                    if (!started) {
                        ctx.moveTo(pt.x, pt.y);
                        started = true;
                    } else {
                        ctx.lineTo(pt.x, pt.y);
                    }
                }
                if (started) {
                    ctx.strokeStyle = 'rgba(99, 102, 241, 0.14)';
                    ctx.stroke();
                }
            }

            for (var rLine = 0; rLine < ROWS; rLine += 2) {
                ctx.beginPath();
                var lineStarted = false;
                var rowPts = projectedGrid[rLine];
                if (!rowPts) continue;

                for (var cLine = 0; cLine < COLS; cLine++) {
                    var linePt = rowPts[cLine];
                    if (!linePt || linePt.x < -50 || linePt.x > width + 50) continue;

                    if (!lineStarted) {
                        ctx.moveTo(linePt.x, linePt.y);
                        lineStarted = true;
                    } else {
                        ctx.lineTo(linePt.x, linePt.y);
                    }
                }
                if (lineStarted) {
                    var dFactor = rLine / ROWS;
                    var lineAlpha = (1 - dFactor) * 0.18;
                    ctx.strokeStyle = 'rgba(16, 185, 129, ' + lineAlpha + ')';
                    ctx.stroke();
                }
            }

            for (var rDot = 0; rDot < ROWS; rDot++) {
                var dotRow = projectedGrid[rDot];
                if (!dotRow) continue;

                for (var cDot = 0; cDot < COLS; cDot++) {
                    var dot = dotRow[cDot];
                    if (!dot || dot.x < -10 || dot.x > width + 10 || dot.y < -10 || dot.y > height + 10) continue;

                    ctx.beginPath();
                    ctx.arc(dot.x, dot.y, dot.radius, 0, Math.PI * 2);

                    if (dot.elevation > 8) {
                        ctx.fillStyle = 'rgba(16, 185, 129, ' + dot.alpha + ')';
                    } else if (dot.elevation < -8) {
                        ctx.fillStyle = 'rgba(99, 102, 241, ' + dot.alpha + ')';
                    } else {
                        ctx.fillStyle = 'rgba(148, 163, 184, ' + (dot.alpha * 0.8) + ')';
                    }
                    ctx.fill();
                }
            }
        }

        animationFrameId = requestAnimationFrame(render);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initWave);
    } else {
        initWave();
    }
})();
