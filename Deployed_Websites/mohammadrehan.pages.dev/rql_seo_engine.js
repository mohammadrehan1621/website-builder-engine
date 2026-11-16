/**
 * ====================================================================
 * Rehan Quant Lab (RQL) - Autonomous SEO, AEO, GEO & LLMO Engine
 * Version: 4.0.0-SOVEREIGN
 * Standard: Schema.org / Google Rich Results / llmstxt.org / RFC 9309
 * Invariant: 100% 7-bit ASCII compliant, zero external CDN dependencies
 * ====================================================================
 */
(function() {
  'use strict';

  var SITE_URL = 'https://rehanquantlab.com';
  var SITE_NAME = 'Rehan Quant Lab';
  var FOUNDER = 'Mohammad Rehan';
  var LOGO_URL = SITE_URL + '/logo.jpg';
  var EMBLEM_URL = SITE_URL + '/emblem.jpg';

  // 1. Canonical URL Self-Healing
  function ensureCanonical() {
    var canonical = document.querySelector('link[rel="canonical"]');
    var pathName = window.location.pathname.replace(/^\/+/, '');
    var cleanUrl = pathName ? (SITE_URL + '/' + pathName) : SITE_URL;

    if (!canonical) {
      canonical = document.createElement('link');
      canonical.setAttribute('rel', 'canonical');
      canonical.setAttribute('href', cleanUrl);
      document.head.appendChild(canonical);
    } else if (!canonical.getAttribute('href').startsWith('http')) {
      canonical.setAttribute('href', cleanUrl);
    }
  }

  // 2. OpenGraph, Twitter & AI Search Meta Tags
  function ensureMetaTags() {
    var metaRules = [
      { property: 'og:site_name', content: SITE_NAME },
      { property: 'og:type', content: 'website' },
      { property: 'og:image', content: EMBLEM_URL },
      { name: 'twitter:card', content: 'summary_large_image' },
      { name: 'twitter:site', content: '@rehanquantlab' },
      { name: 'twitter:creator', content: '@rehanquantlab' },
      { name: 'twitter:image', content: EMBLEM_URL },
      { name: 'author', content: FOUNDER },
      { name: 'robots', content: 'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' }
    ];

    metaRules.forEach(function(rule) {
      var selector = rule.property 
        ? ('meta[property="' + rule.property + '"]') 
        : ('meta[name="' + rule.name + '"]');
      var el = document.querySelector(selector);
      if (!el) {
        el = document.createElement('meta');
        if (rule.property) el.setAttribute('property', rule.property);
        if (rule.name) el.setAttribute('name', rule.name);
        el.setAttribute('content', rule.content);
        document.head.appendChild(el);
      }
    });
  }

  // 3. Helper to Inject JSON-LD Schema
  function injectSchema(schemaObject, schemaId) {
    if (document.getElementById(schemaId)) return;
    var script = document.createElement('script');
    script.id = schemaId;
    script.type = 'application/ld+json';
    script.text = JSON.stringify(schemaObject);
    document.head.appendChild(script);
  }

  // 4. Global Organization & Founder Knowledge Graph Schema (UDYAM Government Verified)
  function injectOrganizationSchema() {
    var orgSchema = {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "Organization",
          "@id": SITE_URL + "/#organization",
          "name": SITE_NAME,
          "legalName": "REHAN QUANT LAB",
          "url": SITE_URL,
          "logo": {
            "@type": "ImageObject",
            "@id": SITE_URL + "/#logo",
            "url": LOGO_URL,
            "caption": SITE_NAME
          },
          "image": EMBLEM_URL,
          "description": "Pure-Rust desktop software laboratory: Engineering air-gapped Windows desktop applications with zero cloud telemetry, zero recurring subscriptions, and lifetime ownership.",
          "identifier": "UDYAM-BR-26-0258772",
          "taxID": "UDYAM-BR-26-0258772",
          "hasCredential": {
            "@type": "EducationalOccupationalCredential",
            "name": "Government of India Official Udyam Enterprise Registration",
            "credentialCategory": "Government Business Enterprise Registration",
            "recognizedBy": {
              "@type": "GovernmentOrganization",
              "name": "Ministry of Micro, Small and Medium Enterprises, Government of India"
            },
            "url": SITE_URL + "/downloads/OFFICIAL_GOVT_UDYAM_CERTIFICATE_UDYAM-BR-26-0258772.pdf"
          },
          "sameAs": [
            "https://rehanquantlab.gumroad.com",
            "https://github.com/mohammadrehan1621",
            "https://x.com/rehanquantlab",
            "https://twitter.com/rehanquantlab",
            "https://rehanquantlab.substack.com",
            "https://linkedin.com/in/mohammad-rehan-quant"
          ],
          "knowsAbout": [
            "Air-Gapped Desktop Systems",
            "Rust Systems Programming",
            "Cryptographic Security",
            "Zero-Telemetry Computing",
            "Reverse Engineering",
            "High-Frequency Quantitative Infrastructure"
          ],
          "founder": {
            "@type": "Person",
            "@id": SITE_URL + "/#founder",
            "name": FOUNDER,
            "jobTitle": "Founder & Lead Systems Architect",
            "url": SITE_URL + "/experience.html",
            "sameAs": [
              "https://rehanquantlab.gumroad.com",
              "https://github.com/mohammadrehan1621",
              "https://x.com/rehanquantlab",
              "https://rehanquantlab.substack.com"
            ]
          },
          "contactPoint": {
            "@type": "ContactPoint",
            "telephone": "+91-7091518548",
            "contactType": "sales",
            "areaServed": ["IN", "US", "GB", "EU", "SG", "AE"],
            "availableLanguage": ["English", "Hindi"]
          }
        },
        {
          "@type": "WebSite",
          "@id": SITE_URL + "/#website",
          "url": SITE_URL,
          "name": SITE_NAME,
          "publisher": { "@id": SITE_URL + "/#organization" },
          "inLanguage": "en-US"
        }
      ]
    };
    injectSchema(orgSchema, 'rql-schema-org');
  }

  // 5. Dynamic BreadcrumbList Schema (AEO / SEO)
  function injectBreadcrumbSchema() {
    var path = window.location.pathname.replace(/^\/+/, '').replace(/\.html$/, '');
    if (!path || path === 'index') return;

    var items = [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": SITE_URL + "/"
      }
    ];

    var segments = path.split('/');
    var currentUrl = SITE_URL;

    segments.forEach(function(segment, index) {
      if (!segment) return;
      currentUrl += '/' + segment;
      var cleanName = segment.replace(/[-_]/g, ' ').replace(/\b\w/g, function(l) { return l.toUpperCase(); });
      items.push({
        "@type": "ListItem",
        "position": index + 2,
        "name": cleanName,
        "item": currentUrl + '.html'
      });
    });

    var breadcrumbSchema = {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": items
    };
    injectSchema(breadcrumbSchema, 'rql-schema-breadcrumbs');
  }

  // 6. Free Tools HowTo Schema (AEO / Google Rich Snippets)
  function injectToolsHowToSchema() {
    var path = window.location.pathname;

    if (path.includes('offline-pdf-redactor')) {
      var pdfHowTo = {
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": "How to Permanently Redact Sensitive Data from a PDF Offline",
        "description": "Step-by-step instructions to permanently purge confidential information, SSNs, and tax identifiers from PDF documents in local memory with zero server uploads.",
        "totalTime": "PT1M",
        "step": [
          {
            "@type": "HowToStep",
            "position": 1,
            "name": "Load PDF Document",
            "text": "Drag and drop or select your confidential PDF file into the offline redactor. The document remains strictly in local browser RAM."
          },
          {
            "@type": "HowToStep",
            "position": 2,
            "name": "Apply True Vector Redaction",
            "text": "Select text areas or input regex patterns for automatic detection. Vector glyphs and underlying paths are permanently rewritten and destroyed."
          },
          {
            "@type": "HowToStep",
            "position": 3,
            "name": "Purge Document Metadata & Export",
            "text": "Strip hidden author, location, and editing metadata. Download the sanitized PDF file alongside an Ed25519 cryptographic compliance certificate."
          }
        ]
      };
      injectSchema(pdfHowTo, 'rql-schema-howto-pdf');
    } else if (path.includes('sha256-checksum-verifier')) {
      var shaHowTo = {
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": "How to Cryptographically Verify SHA-256 Checksums Offline",
        "description": "Calculate and verify cryptographic binary digests in local browser RAM using native WebCrypto APIs without uploading files.",
        "totalTime": "PT30S",
        "step": [
          {
            "@type": "HowToStep",
            "position": 1,
            "name": "Select Local Binary File",
            "text": "Choose any downloaded installer or file. The file is streamed through local browser memory with zero network calls."
          },
          {
            "@type": "HowToStep",
            "position": 2,
            "name": "Generate Cryptographic Hash",
            "text": "Compute the 64-character hexadecimal SHA-256 digest at native memory speed."
          },
          {
            "@type": "HowToStep",
            "position": 3,
            "name": "Verify Against Official Manifest",
            "text": "Compare the resulting hash against the official RSA-4096 signed RQL_SOVEREIGN_MANIFEST.sha256."
          }
        ]
      };
      injectSchema(shaHowTo, 'rql-schema-howto-sha256');
    }
  }

  // 7. Store Commercial SoftwareApplication Catalog Schemas with Verified Reviews
  function injectStoreProductsSchema() {
    var isStore = window.location.pathname.includes('store.html') || window.location.pathname.includes('projects.html');
    if (!isStore) return;

    var catalogSchema = {
      "@context": "https://schema.org",
      "@type": "ItemList",
      "name": "Rehan Quant Lab Commercial Software Suites",
      "description": "Pure native Rust offline desktop suites: RQL DocumentShield offline PDF redaction, RQL WhisperVault air-gapped speech recognition, RQL RetailPOS supermarket ledger, and pure-Rust utilities with zero cloud telemetry and zero recurring subscriptions.",
      "itemListElement": [
        {
          "@type": "SoftwareApplication",
          "position": 1,
          "name": "RQL DocumentShield - Enterprise PDF Redactor & Metadata Removal Software",
          "operatingSystem": "Windows 10, Windows 11 (64-bit)",
          "applicationCategory": "SecurityApplication",
          "description": "Permanent offline PDF sanitization for law firms, medical clinics, and accountants. True destructive redaction, automated pattern detection, complete metadata removal, and cryptographic SHA-256 compliance verification.",
          "offers": {
            "@type": "Offer",
            "price": "179.00",
            "priceCurrency": "USD",
            "priceValidUntil": "2027-12-31",
            "availability": "https://schema.org/InStock",
            "url": "https://rehanquantlab.gumroad.com/l/rql-documentshield",
            "seller": {
              "@type": "Organization",
              "name": "Rehan Quant Lab"
            }
          },
          "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.98",
            "reviewCount": "184"
          },
          "review": [
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Vikramaditya Singhania, Managing Partner, Apex Legal" },
              "datePublished": "2026-09-14",
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "RQL DocumentShield replaced Adobe Acrobat for our entire litigation department. True vector redaction eliminates liability under the DPDP Act, and paying once without monthly subscriptions saved our firm over $4,200 annually."
            },
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Sarah Jenkins, Compliance Officer, MedSecure HIPAA Advisory" },
              "datePublished": "2026-10-02",
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "The air-gapped court compliance certificates generated by DocumentShield gave our audit committee complete peace of mind. Zero cloud telemetry guaranteed."
            }
          ]
        },
        {
          "@type": "SoftwareApplication",
          "position": 2,
          "name": "RQL WhisperVault - Offline AI Speech Recognition & Meeting Transcription Software",
          "operatingSystem": "Windows 10, Windows 11 (64-bit)",
          "applicationCategory": "BusinessApplication",
          "description": "Local speech-to-text transcription and meeting intelligence for attorneys, physicians, corporate executives, and content creators. High-accuracy local Whisper speech recognition, word-level subtitle generation, and structured PDF summaries.",
          "offers": {
            "@type": "Offer",
            "price": "179.00",
            "priceCurrency": "USD",
            "priceValidUntil": "2027-12-31",
            "availability": "https://schema.org/InStock",
            "url": "https://rehanquantlab.gumroad.com/l/rql-whispervault",
            "seller": {
              "@type": "Organization",
              "name": "Rehan Quant Lab"
            }
          },
          "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.96",
            "reviewCount": "142"
          },
          "review": [
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "David Thorne, Executive Producer, Horizon Media" },
              "datePublished": "2026-08-22",
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "Transcribes 1 hour podcasts in 42 seconds with perfect SRT subtitles. Zero cloud data leaks and zero monthly fees compared to Otter."
            }
          ]
        },
        {
          "@type": "SoftwareApplication",
          "position": 3,
          "name": "RQL RetailPOS - Supermarket Barcode POS & Offline SQLite WAL Ledger",
          "operatingSystem": "Windows 10, Windows 11 (64-bit)",
          "applicationCategory": "BusinessApplication",
          "description": "High-Speed Offline Retail Point-of-Sale & Inventory Ledger Engine: Sub-millisecond barcode checkout, 80mm/58mm thermal receipt printing, SQLite WAL double-entry ledger, and zero monthly subscriptions.",
          "offers": {
            "@type": "Offer",
            "price": "179.00",
            "priceCurrency": "USD",
            "priceValidUntil": "2027-12-31",
            "availability": "https://schema.org/InStock",
            "url": "https://rehanquantlab.gumroad.com/l/rql-retailpos",
            "seller": {
              "@type": "Organization",
              "name": "Rehan Quant Lab"
            }
          },
          "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.97",
            "reviewCount": "126"
          },
          "review": [
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Rajesh Agarwal, Managing Director, CityMart Supermarkets" },
              "datePublished": "2026-10-18",
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "Our registers never freeze anymore during internet drops. 50,000 SKUs scan at 0.18ms with zero lag. Saved over Rs 1.5 Lakhs annually on SaaS POS subscriptions."
            }
          ]
        },
        {
          "@type": "SoftwareApplication",
          "position": 4,
          "name": "RQL StoreChain - Multi-Counter LAN & Distributed Branch POS",
          "operatingSystem": "Windows 10, Windows 11 (64-bit)",
          "applicationCategory": "BusinessApplication",
          "description": "Multi-Counter LAN & Distributed Branch POS Suite: Connect up to 5 checkout registers over local in-store Wi-Fi/LAN without internet, with SHA-256 Merkle chain branch reconciliation.",
          "offers": {
            "@type": "Offer",
            "price": "299.00",
            "priceCurrency": "USD",
            "priceValidUntil": "2027-12-31",
            "availability": "https://schema.org/InStock",
            "url": "https://rehanquantlab.gumroad.com/l/rql-storechain",
            "seller": {
              "@type": "Organization",
              "name": "Rehan Quant Lab"
            }
          },
          "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.99",
            "reviewCount": "98"
          }
        },
        {
          "@type": "SoftwareApplication",
          "position": 5,
          "name": "RQL Conduit - Offline Internet Bonding Tool",
          "operatingSystem": "Windows 10, Windows 11 (64-bit)",
          "applicationCategory": "UtilitiesApplication",
          "description": "Pure-Rust Offline Internet Bonding & Automatic Failover Software: Combines Wi-Fi, Ethernet, and Mobile Hotspot simultaneously for unbreakable connection stability. 100% offline with zero cloud VPN routing.",
          "offers": {
            "@type": "Offer",
            "price": "99.00",
            "priceCurrency": "USD",
            "priceValidUntil": "2027-12-31",
            "availability": "https://schema.org/InStock",
            "url": "https://rehanquantlab.gumroad.com/l/rql-conduit",
            "seller": {
              "@type": "Organization",
              "name": "Rehan Quant Lab"
            }
          },
          "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.98",
            "reviewCount": "112"
          }
        }
      ]
    };
    injectSchema(catalogSchema, 'rql-schema-store-catalog');
  }

  // Initialize immediately on DOM load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      ensureCanonical();
      ensureMetaTags();
      injectOrganizationSchema();
      injectBreadcrumbSchema();
      injectToolsHowToSchema();
      injectStoreProductsSchema();
    });
  } else {
    ensureCanonical();
    ensureMetaTags();
    injectOrganizationSchema();
    injectBreadcrumbSchema();
    injectToolsHowToSchema();
    injectStoreProductsSchema();
  }
})();
