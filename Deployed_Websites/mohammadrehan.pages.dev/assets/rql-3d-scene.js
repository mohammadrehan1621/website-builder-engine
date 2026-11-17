/**
 * RQL Sovereign 3D Interactive Geometry Engine
 * Zero external libraries - Pure HTML5 Canvas 3D Perspective Projection
 * Supports High-DPI (Retina), 60-144Hz V-Sync, Mouse Tracking & Drag Inertia
 * 100% 7-bit ASCII Compliant
 */
(function() {
  'use strict';

  function initRQL3DScene() {
    var canvas = document.getElementById('rql-3d-canvas');
    if (!canvas) return;

    var ctx = canvas.getContext('2d');
    if (!ctx) return;

    var width = 0;
    var height = 0;
    var dpr = Math.min(window.devicePixelRatio || 1, 2);

    var mouse = { x: 0, y: 0, targetX: 0, targetY: 0, isDown: false, lastX: 0, lastY: 0 };
    var rotX = 0.2;
    var rotY = -0.4;
    var velRotX = 0;
    var velRotY = 0;
    var time = 0;
    var isVisible = true;

    // Resize Handler
    function resize() {
      var rect = canvas.getBoundingClientRect();
      width = rect.width;
      height = rect.height;
      canvas.width = Math.floor(width * dpr);
      canvas.height = Math.floor(height * dpr);
    }
    window.addEventListener('resize', resize, { passive: true });
    resize();

    // Mouse & Touch Interaction
    window.addEventListener('mousemove', function(e) {
      var rect = canvas.getBoundingClientRect();
      var nx = (e.clientX - (rect.left + rect.width / 2)) / (rect.width / 2);
      var ny = (e.clientY - (rect.top + rect.height / 2)) / (rect.height / 2);
      mouse.targetX = nx;
      mouse.targetY = ny;

      if (mouse.isDown) {
        var dx = e.clientX - mouse.lastX;
        var dy = e.clientY - mouse.lastY;
        velRotY += dx * 0.005;
        velRotX -= dy * 0.005;
        mouse.lastX = e.clientX;
        mouse.lastY = e.clientY;
      }
    }, { passive: true });

    canvas.addEventListener('mousedown', function(e) {
      mouse.isDown = true;
      mouse.lastX = e.clientX;
      mouse.lastY = e.clientY;
    });

    window.addEventListener('mouseup', function() {
      mouse.isDown = false;
    });

    // Touch support
    canvas.addEventListener('touchstart', function(e) {
      if (e.touches.length === 1) {
        mouse.isDown = true;
        mouse.lastX = e.touches[0].clientX;
        mouse.lastY = e.touches[0].clientY;
      }
    }, { passive: true });

    window.addEventListener('touchmove', function(e) {
      if (mouse.isDown && e.touches.length === 1) {
        var dx = e.touches[0].clientX - mouse.lastX;
        var dy = e.touches[0].clientY - mouse.lastY;
        velRotY += dx * 0.008;
        velRotX -= dy * 0.008;
        mouse.lastX = e.touches[0].clientX;
        mouse.lastY = e.touches[0].clientY;
      }
    }, { passive: true });

    window.addEventListener('touchend', function() {
      mouse.isDown = false;
    });

    // Visibility Observer to save battery
    if ('IntersectionObserver' in window) {
      var observer = new IntersectionObserver(function(entries) {
        isVisible = entries[0].isIntersecting;
      }, { threshold: 0.05 });
      observer.observe(canvas);
    }

    // 3D Math Helper
    function rotatePoint(p, rx, ry, rz) {
      var x = p[0], y = p[1], z = p[2];
      // Y-axis rotation
      var cosY = Math.cos(ry), sinY = Math.sin(ry);
      var x1 = x * cosY + z * sinY;
      var z1 = -x * sinY + z * cosY;
      // X-axis rotation
      var cosX = Math.cos(rx), sinX = Math.sin(rx);
      var y2 = y * cosX - z1 * sinX;
      var z2 = y * sinX + z1 * cosX;
      // Z-axis rotation
      var cosZ = Math.cos(rz), sinZ = Math.sin(rz);
      var x3 = x1 * cosZ - y2 * sinZ;
      var y3 = x1 * sinZ + y2 * cosZ;
      return [x3, y3, z2];
    }

    function project(p, fov, cx, cy) {
      var dist = 420;
      var z = p[2] + dist;
      if (z <= 10) z = 10;
      var scale = fov / z;
      return [p[0] * scale + cx, p[1] * scale + cy, p[2]];
    }

    // Create 3D Meshes
    // 1. Central Forensic Beveled Cube
    function createCube(s) {
      var v = [
        [-s, -s, -s], [s, -s, -s], [s, s, -s], [-s, s, -s],
        [-s, -s,  s], [s, -s,  s], [s, s,  s], [-s, s,  s]
      ];
      var f = [
        [0, 1, 2, 3], // Front
        [5, 4, 7, 6], // Back
        [4, 0, 3, 7], // Left
        [1, 5, 6, 2], // Right
        [4, 5, 1, 0], // Top
        [3, 2, 6, 7]  // Bottom
      ];
      return { vertices: v, faces: f, color: [16, 185, 129] }; // Emerald
    }

    // 2. Octahedron (Diamond)
    function createOctahedron(s) {
      var v = [
        [0, -s * 1.3, 0], [0, s * 1.3, 0],
        [-s, 0, -s], [s, 0, -s], [s, 0, s], [-s, 0, s]
      ];
      var f = [
        [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 2],
        [1, 3, 2], [1, 4, 3], [1, 5, 4], [1, 2, 5]
      ];
      return { vertices: v, faces: f, color: [6, 182, 212] }; // Cyan
    }

    // 3. Cylinder
    function createCylinder(r, h, seg) {
      var v = [];
      var f = [];
      for (var i = 0; i < seg; i++) {
        var theta = (i / seg) * Math.PI * 2;
        var x = Math.cos(theta) * r;
        var z = Math.sin(theta) * r;
        v.push([x, -h / 2, z]); // Top circle
        v.push([x, h / 2, z]);  // Bottom circle
      }
      for (var j = 0; j < seg; j++) {
        var n = (j + 1) % seg;
        f.push([j * 2, n * 2, n * 2 + 1, j * 2 + 1]);
      }
      return { vertices: v, faces: f, color: [99, 102, 241] }; // Indigo
    }

    // 4. Torus / Ring
    function createTorus(R, r, segR, segr) {
      var v = [];
      var f = [];
      for (var i = 0; i < segR; i++) {
        var u = (i / segR) * Math.PI * 2;
        for (var j = 0; j < segr; j++) {
          var w = (j / segr) * Math.PI * 2;
          var x = (R + r * Math.cos(w)) * Math.cos(u);
          var y = (R + r * Math.cos(w)) * Math.sin(u);
          var z = r * Math.sin(w);
          v.push([x, y, z]);
        }
      }
      for (var a = 0; a < segR; a++) {
        var nextA = (a + 1) % segR;
        for (var b = 0; b < segr; b++) {
          var nextB = (b + 1) % segr;
          var i1 = a * segr + b;
          var i2 = nextA * segr + b;
          var i3 = nextA * segr + nextB;
          var i4 = a * segr + nextB;
          f.push([i1, i2, i3, i4]);
        }
      }
      return { vertices: v, faces: f, color: [244, 63, 94] }; // Rose
    }

    var objects = [
      { mesh: createCube(65), pos: [0, 0, 0], rot: [0, 0, 0], spin: [0.008, 0.012, 0.005], floatOffset: 0, scale: 1 },
      { mesh: createOctahedron(38), pos: [-160, -70, -20], rot: [0.3, 0.2, 0.1], spin: [0.015, -0.01, 0.007], floatOffset: 1.5, scale: 0.9 },
      { mesh: createCylinder(26, 60, 10), pos: [170, -60, -40], rot: [0.8, 0.4, 0], spin: [-0.009, 0.014, 0.01], floatOffset: 3.0, scale: 0.85 },
      { mesh: createTorus(45, 14, 14, 7), pos: [-140, 90, -50], rot: [1.2, 0.5, 0], spin: [0.012, 0.015, -0.008], floatOffset: 4.2, scale: 0.8 },
      { mesh: createOctahedron(32), pos: [150, 85, -30], rot: [-0.4, 0.6, 0.2], spin: [-0.012, -0.014, 0.01], floatOffset: 2.1, scale: 0.8 }
    ];

    // Light direction vector (normalized)
    var light = [0.577, -0.577, 0.577];

    function render() {
      if (!isVisible) {
        requestAnimationFrame(render);
        return;
      }

      time += 0.02;

      // Mouse smoothing
      mouse.x += (mouse.targetX - mouse.x) * 0.08;
      mouse.y += (mouse.targetY - mouse.y) * 0.08;

      // Velocity damping
      velRotX *= 0.92;
      velRotY *= 0.92;
      rotX += velRotX;
      rotY += velRotY;

      ctx.save();
      ctx.scale(dpr, dpr);
      ctx.clearRect(0, 0, width, height);

      var cx = width / 2;
      var cy = height / 2;
      var fov = Math.min(width, height) * 0.95;

      var baseRotX = rotX + mouse.y * 0.35;
      var baseRotY = rotY + mouse.x * 0.45;

      // Collect all faces across all objects for correct global depth sorting
      var allFaces = [];

      for (var o = 0; o < objects.length; o++) {
        var obj = objects[o];
        obj.rot[0] += obj.spin[0];
        obj.rot[1] += obj.spin[1];
        obj.rot[2] += obj.spin[2];

        // Float bobbing
        var floatY = Math.sin(time + obj.floatOffset) * 12;
        var objPos = [obj.pos[0], obj.pos[1] + floatY, obj.pos[2]];

        // Transform vertices
        var transV = [];
        var projV = [];

        for (var vi = 0; vi < obj.mesh.vertices.length; vi++) {
          var v = obj.mesh.vertices[vi];
          // Local rotation & scale
          var sv = [v[0] * obj.scale, v[1] * obj.scale, v[2] * obj.scale];
          var rv = rotatePoint(sv, obj.rot[0], obj.rot[1], obj.rot[2]);
          // Local offset
          var worldV = [rv[0] + objPos[0], rv[1] + objPos[1], rv[2] + objPos[2]];
          // Scene global rotation based on mouse
          var camV = rotatePoint(worldV, baseRotX, baseRotY, 0);
          transV.push(camV);
          projV.push(project(camV, fov, cx, cy));
        }

        // Process faces
        for (var fi = 0; fi < obj.mesh.faces.length; fi++) {
          var face = obj.mesh.faces[fi];
          var p0 = transV[face[0]];
          var p1 = transV[face[1]];
          var p2 = transV[face[2]];

          // Face normal calculation
          var ax = p1[0] - p0[0], ay = p1[1] - p0[1], az = p1[2] - p0[2];
          var bx = p2[0] - p0[0], by = p2[1] - p0[1], bz = p2[2] - p0[2];
          var nx = ay * bz - az * by;
          var ny = az * bx - ax * bz;
          var nz = ax * by - ay * bx;
          var len = Math.sqrt(nx * nx + ny * ny + nz * nz);

          if (len > 0.0001) {
            nx /= len; ny /= len; nz /= len;
          }

          // Backface culling: only render faces pointing towards camera (nz < 0 in our coordinate system)
          if (nz < 0.05) {
            var avgZ = 0;
            for (var k = 0; k < face.length; k++) {
              avgZ += transV[face[k]][2];
            }
            avgZ /= face.length;

            // Dot product with light
            var dot = Math.max(0.12, (nx * light[0] + ny * light[1] + nz * light[2]));
            // Specular highlight boost
            var spec = Math.pow(dot, 4) * 0.45;

            allFaces.push({
              points: face.map(function(idx) { return projV[idx]; }),
              avgZ: avgZ,
              color: obj.mesh.color,
              dot: dot,
              spec: spec
            });
          }
        }
      }

      // Depth sort faces (Painter's algorithm: farthest z first)
      allFaces.sort(function(a, b) { return b.avgZ - a.avgZ; });

      // Draw faces
      for (var i = 0; i < allFaces.length; i++) {
        var f = allFaces[i];
        var c = f.color;
        var r = Math.min(255, Math.floor(c[0] * f.dot + 255 * f.spec));
        var g = Math.min(255, Math.floor(c[1] * f.dot + 255 * f.spec));
        var b = Math.min(255, Math.floor(c[2] * f.dot + 255 * f.spec));
        var alpha = 0.88;

        ctx.beginPath();
        ctx.moveTo(f.points[0][0], f.points[0][1]);
        for (var p = 1; p < f.points.length; p++) {
          ctx.lineTo(f.points[p][0], f.points[p][1]);
        }
        ctx.closePath();

        // Shaded face fill
        ctx.fillStyle = 'rgba(' + r + ',' + g + ',' + b + ',' + alpha + ')';
        ctx.fill();

        // Hairline metallic edge
        ctx.strokeStyle = 'rgba(255, 255, 255, ' + (0.15 + f.spec * 0.4) + ')';
        ctx.lineWidth = 1;
        ctx.stroke();
      }

      ctx.restore();
      requestAnimationFrame(render);
    }

    requestAnimationFrame(render);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initRQL3DScene);
  } else {
    initRQL3DScene();
  }
})();
