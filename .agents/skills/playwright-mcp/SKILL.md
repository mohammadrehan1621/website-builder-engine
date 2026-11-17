---
name: playwright-mcp
description: Engineering and operational guide for Microsoft Playwright MCP (@playwright/mcp), enabling browser automation, visual regression verification, zero-wobble stability testing, broken link scanning, and agentic UI validation.
---

# Microsoft Playwright MCP -- Engineering Codex
Developed by Microsoft (`microsoft/playwright-mcp` / `@playwright/mcp`).
Agentic headless browser automation, testing, and UI verification through the Model Context Protocol.

---

## 1. Core Architecture & Available Tools

Playwright MCP gives AI agents full programmatic control over a real Chromium/WebKit/Firefox browser:

| Tool | Action | Primary Verification Use Case |
| :--- | :--- | :--- |
| `browser_navigate` | Loads target URL | Testing production deployments, verifying DNS, and checking HTTP status codes. |
| `browser_screenshot` | Captures viewport or full page | Visual regression audits, checking mobile responsiveness, verifying layout shifts. |
| `browser_click` | Dispatches pointer clicks | Testing CTA buttons, modal triggers, command palette (`Ctrl+K`), and tab navigation. |
| `browser_fill` | Inputs form data | Validating checkout forms, search query inputs, and inquiry dispatch. |
| `browser_evaluate` | Executes JS in page context | Checking console errors, measuring Cumulative Layout Shift (`CLS`), inspecting DOM nodes. |
| `browser_console_logs` | Retrieves browser logs | Detecting uncaught JavaScript exceptions, CSP violations, and 404 resource errors. |

---

## 2. The 6-Point Sovereign Verification Suite

When using Playwright MCP to verify Rehan Quant Lab deployments:

### Check 1: Zero Layout Shifts (CLS = 0.000)
Run in `browser_evaluate`:
```javascript
new Promise((resolve) => {
  let cls = 0;
  new PerformanceObserver((entryList) => {
    for (const entry of entryList.getEntries()) {
      if (!entry.hadRecentInput) cls += entry.value;
    }
    resolve(cls);
  }).observe({ type: 'layout-shift', buffered: true });
  setTimeout(() => resolve(cls), 2000);
});
```
**Standard**: Must strictly equal `0.000`.

### Check 2: Zero Console Errors & CSP Violations
Retrieve logs via `browser_console_logs`:
- Must have 0 uncaught exceptions.
- Must have 0 blocked script or stylesheet violations.

### Check 3: Broken Link & Anchor Audit
Verify that every `<a>` tag on the page contains a valid, clickable `href` attribute:
```javascript
const deadLinks = Array.from(document.querySelectorAll('a')).filter(a => !a.getAttribute('href') || a.getAttribute('href') === '#');
return deadLinks.length;
```
**Standard**: Must equal `0`.

### Check 4: Modal Z-Index & Scroll Lock Audit
1. Click the Command Palette trigger or Schedule Briefing button.
2. Confirm the modal appears with `z-index >= 10000`.
3. Confirm `window.rqlLenis.stop()` was invoked or background scrolling is frozen.
4. Close modal and confirm `window.rqlLenis.start()` resumed smooth scrolling.

### Check 5: Responsive Mobile Viewport Verification
Capture screenshots across three exact dimensions:
1. **Desktop**: 1440 x 900
2. **Tablet**: 768 x 1024
3. **Mobile Phone**: 390 x 844 (iPhone 14)
Verify that category tabs do not truncate, single-line badges do not wrap, and table horizontal scroll indicators are visible.

### Check 6: Air-Gap Zero-Telemetry Sniffing
Monitor network requests during page interaction:
- Verify that **0 outbound network sockets** leave the browser to third-party tracking services (Google Analytics, Facebook Pixel, Mixpanel, etc.).
- Only approved asset CDNs (or 100% self-hosted assets) are allowed.
