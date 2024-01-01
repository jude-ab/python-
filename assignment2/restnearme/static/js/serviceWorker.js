importScripts(
  "https://storage.googleapis.com/workbox-cdn/releases/6.1.5/workbox-sw.js"
);

// Check if Workbox loaded successfully
if (workbox) {
  console.log(`Yay! Workbox is loaded 🎉`);

  // Precache items
  workbox.precaching.precacheAndRoute([]);

  // Cache CSS files with a stale-while-revalidate strategy
  workbox.routing.registerRoute(
    ({ request }) => request.destination === "style",
    new workbox.strategies.StaleWhileRevalidate({
      cacheName: 'css-cache',
      plugins: [
        new workbox.cacheableResponse.CacheableResponsePlugin({
          statuses: [0, 200],
        }),
      ],
    })
  );

  // Cache responses from the Google APIs with a network-first strategy
  workbox.routing.registerRoute(
    ({ url }) => url.origin === 'https://www.googleapis.com',
    new workbox.strategies.NetworkFirst({
      networkTimeoutSeconds: 3,
      cacheName: "api-cache",
      plugins: [
        new workbox.expiration.ExpirationPlugin({
          maxEntries: 50,
          maxAgeSeconds: 60 * 60 * 24, // 1 day
          purgeOnQuotaError: true,
        }),
        new workbox.cacheableResponse.CacheableResponsePlugin({
          statuses: [0, 200],
        }),
      ],
    })
  );

  // Cache image files with a cache-first strategy for 30 days
  workbox.routing.registerRoute(
    ({ request }) => request.destination === "image",
    new workbox.strategies.CacheFirst({
      cacheName: "image-cache",
      plugins: [
        new workbox.expiration.ExpirationPlugin({
          maxEntries: 60,
          maxAgeSeconds: 30 * 24 * 60 * 60, // 30 days
        }),
      ],
    })
  );
} else {
  console.log(`Boo! Workbox didn't load 😬`);
}
