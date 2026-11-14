// RQL Service Worker v6.0 (Auto-Purge Old Caches & Network-First)
const CACHE_NAME = 'rql-desktop-v10.5';
const ASSETS_TO_CACHE = [
  '/manifest.json',
  '/emblem.webp',
  '/favicon.svg',
  '/og_preview.png',
  '/assets/rql-wave.js'
];

self.addEventListener('install', (event) => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS_TO_CACHE))
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            return caches.delete(key);
          }
        })
      )
    ).then(() => self.clients.claim())
  );
});

// Network-First with Cache Fallback
self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;
  const fetchReq = (event.request.mode === 'navigate' || (event.request.headers.get('accept') || '').includes('text/html'))
    ? new Request(event.request, { cache: 'no-store' })
    : event.request;
  event.respondWith(
    fetch(fetchReq)
      .then((networkResponse) => {
        if (networkResponse && networkResponse.status === 200) {
          const responseToCache = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, responseToCache);
          });
        }
        return networkResponse;
      })
      .catch(() => caches.match(event.request))
  );
});
