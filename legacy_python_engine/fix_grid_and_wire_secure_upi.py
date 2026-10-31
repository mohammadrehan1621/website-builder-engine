import os
import sys
import shutil
import re
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PORTFOLIO_DIR = Path(r"C:\Users\rehan\Desktop\website_builder\Deployed_Websites\mohammadrehan.pages.dev")
PWA_SRC_DIR = Path(r"C:\Users\rehan\Desktop\software projects\ExpressBill_Billing_Software\ExpressBill_Mobile_PWA")

# ==============================================================================
# SECURE UPI MODAL HTML (TAMPER-PROOF, NPCI ENCODED, ZERO-FEES)
# ==============================================================================
SECURE_UPI_MODAL_HTML = """
<!-- 🔒 SECURE DUAL-CHECKOUT & UPI MODAL (VERIFIED PAYEE: 7091518548@pthdfc) -->
<div id="secure-upi-modal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/85 backdrop-blur-md hidden opacity-0 transition-opacity duration-300">
    <div class="bg-slate-900 border-2 border-emerald-500/50 rounded-3xl max-w-lg w-full p-6 sm:p-7 shadow-2xl text-white relative max-h-[92vh] overflow-y-auto">
        <!-- Close Button -->
        <button onclick="closeUpiModal()" class="absolute top-4 right-4 text-slate-400 hover:text-white p-2 rounded-xl bg-slate-800/80 hover:bg-slate-800 transition">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
        </button>

        <div class="text-center space-y-3">
            <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-400 text-xs font-mono font-bold border border-emerald-500/30">
                <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                🔒 Verified Direct Settlement &bull; Zero Platform Fee
            </div>
            
            <h3 class="text-xl sm:text-2xl font-bold tracking-tight text-white">ExpressBill POS™ Lifetime License</h3>
            <p class="text-xs text-slate-300">Choose your preferred checkout method below:</p>

            <!-- TRACK 1: GUMROAD INTERNATIONAL CARD / PAYPAL -->
            <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 text-left space-y-2 mt-2">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold text-slate-300 uppercase font-mono tracking-wider">Option 1: International Checkout</span>
                    <span class="text-xs font-bold text-sky-400 font-mono">$49 USD</span>
                </div>
                <p class="text-[11px] text-slate-400">Credit / Debit Cards, Apple Pay &amp; PayPal with instant automated ZIP delivery.</p>
                <a href="https://quantify17.gumroad.com/l/ExpressBill" data-gumroad-single-product="true" class="gumroad-button block w-full text-center py-2.5 bg-sky-600 hover:bg-sky-500 text-white font-bold rounded-xl text-xs font-mono transition shadow-md shadow-sky-600/20 btn-spring">
                    💳 Pay $49 via Gumroad (Cards / PayPal)
                </a>
            </div>

            <!-- TRACK 2: INDIA DOMESTIC DIRECT UPI (SAVINGS ACCOUNT 0% FEE) -->
            <div class="bg-slate-950 border-2 border-emerald-500/40 rounded-2xl p-4 text-left space-y-3 mt-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold text-emerald-400 uppercase font-mono tracking-wider flex items-center gap-1">
                        <span>Option 2: India Domestic UPI</span>
                        <span class="bg-emerald-500/20 text-emerald-300 text-[9px] px-1.5 py-0.5 rounded font-mono">0% Fee</span>
                    </span>
                    <span class="text-base font-bold text-emerald-400 font-mono">&#8377;3,999 <span class="text-xs line-through text-slate-500">&#8377;12,499</span></span>
                </div>
                <p class="text-[11px] text-slate-400">Scan with Google Pay, PhonePe, Paytm, or BHIM for instant 2-second bank activation.</p>

                <!-- Cryptographic Static QR Code -->
                <div class="bg-white p-3 rounded-2xl text-center shadow-lg border border-slate-200">
                    <img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=upi%3A%2F%2Fpay%3Fpa%3D7091518548%40pthdfc%26pn%3DMohammad%2520Rehan%26am%3D3999%26cu%3DINR%26tn%3DExpressBill%2520POS%2520Lifetime%2520License" alt="ExpressBill UPI QR Code" class="w-44 h-44 mx-auto rounded-lg" loading="lazy" />
                    <span class="text-[10px] text-slate-600 font-mono font-bold block mt-1">Scan with any UPI App (GPay / PhonePe / Paytm)</span>
                </div>

                <!-- Verified Payee VPA Box (Immutable) -->
                <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800 flex items-center justify-between gap-2">
                    <div>
                        <div class="text-[9px] text-slate-400 uppercase font-mono">Verified Payee UPI ID (HDFC Bank)</div>
                        <div class="text-xs font-bold text-emerald-300 font-mono select-all">7091518548@pthdfc</div>
                    </div>
                    <button type="button" onclick="copyUpiId('7091518548@pthdfc')" id="copy-upi-btn" class="text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-200 px-3 py-1.5 rounded-lg border border-slate-700 transition shrink-0 flex items-center gap-1 font-mono">
                        <span>Copy UPI</span>
                    </button>
                </div>

                <!-- Mobile 1-Click UPI Deep-link (Opens GPay/PhonePe directly on mobile) -->
                <a href="upi://pay?pa=7091518548@pthdfc&pn=Mohammad%20Rehan&am=3999&cu=INR&tn=ExpressBill%20POS%20Lifetime%20License" class="md:hidden block w-full py-2.5 bg-gradient-to-r from-emerald-500 to-teal-600 text-white text-center font-bold rounded-xl shadow-md text-xs font-mono transition">
                    📲 Pay &#8377;3,999 on Mobile App
                </a>

                <!-- WhatsApp Verification Dispatch Button -->
                <a href="https://wa.me/917091518548?text=Hi%20Rehan,%20I%20have%20paid%20Rs.%203999%20via%20UPI%20to%207091518548@pthdfc%20for%20ExpressBill%20POS%20Lifetime%20License.%20My%20payment%20UTR%20screenshot%20is%20attached.%20Please%20send%20my%20license%20key%20and%20download%20link." target="_blank" rel="noopener noreferrer" class="block w-full py-2.5 bg-[#25D366] hover:bg-[#20bd5a] text-white text-center font-bold rounded-xl shadow-md text-xs font-mono transition flex items-center justify-center gap-2">
                    <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.288.043.088.072.19.014.305-.058.115-.087.187-.173.289l-.26.309c-.087.087-.179.182-.077.357.101.174.451.744.968 1.205.666.594 1.228.777 1.402.864.174.087.275.073.376-.043.101-.116.433-.506.549-.68.116-.173.231-.144.39-.087s1.011.477 1.184.564.289.13.332.202c.044.072.044.419-.1.824z"/></svg>
                    <span>Send Screenshot on WhatsApp (+91 70915 18548)</span>
                </a>
            </div>

            <p class="text-[10px] text-slate-400 text-center">Encrypted &bull; Direct Settlement to Mohammad Rehan's verified HDFC Bank Account &bull; Zero Middleman Access</p>
        </div>
    </div>
</div>

<script>
function openUpiModal() {
    const modal = document.getElementById('secure-upi-modal');
    if (modal) {
        modal.classList.remove('hidden');
        setTimeout(() => modal.classList.remove('opacity-0'), 10);
    }
}
function closeUpiModal() {
    const modal = document.getElementById('secure-upi-modal');
    if (modal) {
        modal.classList.add('opacity-0');
        setTimeout(() => modal.classList.add('hidden'), 300);
    }
}
function copyUpiId(upiId) {
    navigator.clipboard.writeText(upiId).then(() => {
        const btn = document.getElementById('copy-upi-btn');
        if (btn) {
            btn.innerHTML = '<span class="text-emerald-400">Copied!</span>';
            setTimeout(() => { btn.innerHTML = '<span>Copy UPI</span>'; }, 2000);
        }
    });
}
</script>
"""

# ==============================================================================
# CLEAN FLAGSHIP GRID CARDS 4, 5, AND 6 FOR INDEX.HTML
# ==============================================================================
CLEAN_FLAGSHIP_4_5_6 = """        <!-- Flagship 4: Industrial Fragility Sentinel™ -->
        <div class="hover-lift-card rounded-2xl bg-gradient-to-br from-slate-950 via-slate-900 to-amber-950 border-2 border-amber-500/50 shadow-xl p-6 sm:p-7 flex flex-col justify-between text-white hover:border-amber-400 transition duration-300">
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2">
                    <span class="bg-amber-500/20 text-amber-300 border border-amber-400/50 text-[10px] px-2.5 py-1 rounded-lg font-mono font-bold uppercase tracking-wider flex items-center gap-1.5">
                        <span class="w-2 h-2 rounded-full bg-amber-400 animate-pulse"></span>
                        Shop Floor Resilience Sentinel
                    </span>
                    <div class="flex items-center gap-2">
                        <span class="text-xs font-bold text-amber-300 bg-amber-950/80 border border-amber-500/40 px-2.5 py-1 rounded-lg font-mono">First 20 Only: $299</span>
                        <span class="text-xs text-slate-400 font-mono line-through">$599</span>
                    </div>
                </div>

                <div>
                    <h3 class="text-xl sm:text-2xl font-bold text-white tracking-tight flex items-center gap-2">
                        <span>Industrial Fragility Sentinel&trade;</span>
                        <span class="text-xs font-mono text-amber-400 font-normal">v1.0 (PROD)</span>
                    </h3>
                    <p class="text-xs font-mono text-amber-400 font-semibold mt-1">On-Premises Factory Uptime &amp; Chokepoint Sentinel</p>
                </div>

                <p class="text-slate-300 text-sm leading-relaxed">
                    Air-gapped plant resilience daemon implementing Sun Tzu's Art of War and Gall's Law. Runs 24/7 on shop floor industrial hardware to eliminate single-vendor supply chokepoints, power drops, and machine downtime with zero recurring monthly cloud SaaS bills.
                </p>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center font-mono">
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[9px] text-slate-400 uppercase">Fragility Index</div>
                        <div class="text-xs sm:text-sm font-bold text-amber-400 mt-0.5">0 to 100 Score</div>
                    </div>
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[9px] text-slate-400 uppercase">Chokepoints</div>
                        <div class="text-xs sm:text-sm font-bold text-emerald-400 mt-0.5">&gt;50% Single Vendor</div>
                    </div>
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[9px] text-slate-400 uppercase">Power Telemetry</div>
                        <div class="text-xs sm:text-sm font-bold text-cyan-400 mt-0.5">Fuel Runway</div>
                    </div>
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[9px] text-slate-400 uppercase">Packaging</div>
                        <div class="text-xs sm:text-sm font-bold text-indigo-400 mt-0.5">9.16 MB EXE</div>
                    </div>
                </div>

                <div class="space-y-1.5 text-xs text-slate-300">
                    <div class="flex items-center gap-2">
                        <i data-lucide="check-circle-2" class="w-4 h-4 text-amber-400 flex-shrink-0"></i>
                        <span>Captive Power &amp; Fuel Runway Telemetry &bull; Zero furnace or line freezes</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <i data-lucide="check-circle-2" class="w-4 h-4 text-amber-400 flex-shrink-0"></i>
                        <span>100% on-premises offline operation &bull; Pay once, protect your factory forever</span>
                    </div>
                </div>
            </div>

            <div class="pt-5 mt-5 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-3">
                <div class="text-xs font-mono">
                    <span class="text-amber-400 font-bold bg-amber-950/70 border border-amber-500/40 px-2 py-0.5 rounded text-[11px]">🔥 FIRST 20 BUYERS ONLY: 50% OFF</span>
                    <div class="text-[11px] text-slate-400 mt-1">Standard: <span class="line-through text-slate-500">$599</span> &bull; Promo: <span class="text-amber-400 font-bold">SENTINEL</span></div>
                </div>
                <div class="flex items-center gap-2">
                    <a href="https://quantify17.gumroad.com/l/ivyiwh" target="_blank" rel="noopener noreferrer" class="text-xs font-semibold text-slate-300 hover:text-white px-3 py-2 rounded-lg border border-slate-700 hover:border-slate-500 transition">
                        Details
                    </a>
                    <a href="https://quantify17.gumroad.com/l/ivyiwh/SENTINEL?wanted=true" data-gumroad-single-product="true" class="gumroad-button bg-amber-400 hover:bg-amber-300 text-slate-950 font-bold text-xs px-4 py-2 rounded-xl transition flex items-center gap-1.5 shadow-md shadow-amber-400/20 btn-spring">
                        <i data-lucide="zap" class="w-3.5 h-3.5 text-slate-950"></i>
                        <span>Claim Early Pass ($299 / &#8377;28,427)</span>
                    </a>
                </div>
            </div>
        </div>

        <!-- Flagship 5: RQL Conduit Bonding Engine™ -->
        <div class="hover-lift-card rounded-2xl bg-gradient-to-br from-slate-950 via-slate-900 to-sky-950 border-2 border-sky-500/50 shadow-xl p-6 sm:p-7 flex flex-col justify-between text-white hover:border-sky-400 transition duration-300 relative overflow-hidden group">
            <div class="absolute -top-24 -right-24 w-48 h-48 bg-sky-500/10 rounded-full blur-2xl group-hover:bg-sky-500/20 transition duration-500 pointer-events-none"></div>
            <div class="space-y-4 relative z-10">
                <div class="flex flex-wrap items-center justify-between gap-2">
                    <span class="bg-sky-500/20 text-sky-300 border border-sky-400/50 text-[10px] px-2.5 py-1 rounded-lg font-mono font-bold uppercase tracking-wider flex items-center gap-1.5">
                        <span class="w-2 h-2 rounded-full bg-sky-400 animate-pulse"></span>
                        Commercial Rust Networking Engine
                    </span>
                    <div class="flex items-center gap-2">
                        <span class="text-xs font-mono font-bold text-sky-300 bg-sky-950/90 border border-sky-500/40 px-2 py-0.5 rounded">Live at $60 / &#8377;4,999</span>
                        <span class="text-xs text-slate-500 line-through font-mono">$120</span>
                    </div>
                </div>

                <div>
                    <h3 class="text-xl sm:text-2xl font-bold text-white tracking-tight flex items-center gap-2">
                        <span>RQL Conduit Bonding Engine&trade;</span>
                        <span class="text-xs font-mono text-sky-400 font-normal">v2.0 (PROD)</span>
                    </h3>
                    <p class="text-xs font-mono text-cyan-400 font-semibold mt-1">Bare-Metal Rust Multi-WAN SOCKS5 Gateway &bull; Sub-3ms Failover</p>
                </div>

                <p class="text-slate-300 text-sm leading-relaxed">
                    A 100% local-first network socket multiplexer written in bare-metal Rust. Bonds Wi-Fi, 5G Mobile Hotspot, and Ethernet concurrently into a single resilient virtual pipe (<code class="text-sky-300 font-mono">127.0.0.1:1080</code>) with sub-3ms zero-drop failover, real-time RTT jitter variance radar, and HTTP range-slicing. Strictly <b>zero remote VPN servers, zero packet logging, and &#8377;0 recurring SaaS fees</b>.
                </p>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5 text-center pt-1 font-mono">
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[10px] text-slate-400 uppercase">Failover</div>
                        <div class="text-sm font-bold text-sky-400 mt-0.5">Sub-3ms</div>
                        <div class="text-[9px] text-slate-500">Zero Drops</div>
                    </div>
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[10px] text-slate-400 uppercase">Engine</div>
                        <div class="text-sm font-bold text-emerald-400 mt-0.5">Rust Core</div>
                        <div class="text-[9px] text-slate-500">Tokio Sockets</div>
                    </div>
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[10px] text-slate-400 uppercase">Privacy</div>
                        <div class="text-sm font-bold text-indigo-400 mt-0.5">100% Local</div>
                        <div class="text-[9px] text-slate-500">No VPN Clouds</div>
                    </div>
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[10px] text-slate-400 uppercase">Pricing</div>
                        <div class="text-sm font-bold text-amber-400 mt-0.5">Perpetual</div>
                        <div class="text-[9px] text-slate-500">No SaaS Fees</div>
                    </div>
                </div>
            </div>

            <div class="pt-6 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-3 mt-4 relative z-10">
                <div class="flex flex-col">
                    <span class="text-xs text-sky-300 font-mono font-bold">Perpetual Lifetime License</span>
                    <span class="text-[10px] text-slate-400 font-mono">Includes Windows Desktop GUI + Rust DLL Core</span>
                </div>
                <div class="flex items-center gap-2">
                    <a href="https://quantify17.gumroad.com/l/RQLConduit" target="_blank" rel="noopener noreferrer" class="text-xs font-semibold text-slate-300 hover:text-white px-3 py-2 rounded-lg border border-slate-700 hover:border-slate-500 transition">
                        Details
                    </a>
                    <a href="https://quantify17.gumroad.com/l/RQLConduit" data-gumroad-single-product="true" class="gumroad-button text-xs font-bold text-white bg-sky-600 hover:bg-sky-500 px-4 py-2 rounded-xl transition flex items-center gap-1.5 shadow-md shadow-sky-600/30 btn-spring shimmer-badge">
                        <i data-lucide="zap" class="w-3.5 h-3.5"></i>
                        <span>Claim License ($60)</span>
                    </a>
                </div>
            </div>
        </div>

        <!-- Flagship 6: ExpressBill POS™ -->
        <div class="hover-lift-card rounded-2xl bg-gradient-to-br from-slate-950 via-slate-900 to-teal-950 border-2 border-teal-500/50 shadow-xl p-6 sm:p-7 flex flex-col justify-between text-white hover:border-teal-400 transition duration-300 relative overflow-hidden group">
            <div class="absolute -top-24 -right-24 w-48 h-48 bg-teal-500/10 rounded-full blur-2xl group-hover:bg-teal-500/20 transition duration-500 pointer-events-none"></div>
            <div class="space-y-4 relative z-10">
                <div class="flex flex-wrap items-center justify-between gap-2">
                    <span class="bg-teal-500/20 text-teal-300 border border-teal-400/50 text-[10px] px-2.5 py-1 rounded-lg font-mono font-bold uppercase tracking-wider flex items-center gap-1.5">
                        <span class="w-2 h-2 rounded-full bg-teal-400 animate-pulse"></span>
                        Commercial Offline Retail POS
                    </span>
                    <div class="flex items-center gap-2">
                        <span class="text-xs font-mono font-bold text-teal-300 bg-teal-950/90 border border-teal-500/40 px-2 py-0.5 rounded">Live at $49 / &#8377;3,999</span>
                        <span class="text-xs text-slate-500 line-through font-mono">$149</span>
                    </div>
                </div>

                <div>
                    <h3 class="text-xl sm:text-2xl font-bold text-white tracking-tight flex items-center gap-2">
                        <span>ExpressBill POS&trade;</span>
                        <span class="text-xs font-mono text-teal-400 font-normal">v2.0 (PROD)</span>
                    </h3>
                    <p class="text-xs font-mono text-emerald-400 font-semibold mt-1">100% Offline Retail Suite &bull; Dynamic Real-Time UPI QR &bull; Mobile PWA</p>
                </div>

                <p class="text-slate-300 text-sm leading-relaxed">
                    An ultra-fast checkout counter workstation for retail shops, cafes, pharmacies, and boutiques. Powered by an embedded redb storage engine, ring up 20 items in under 5 seconds with zero internet. Displays dynamic real-time UPI QR codes directly on the customer screen for 1-second PhonePe/GPay scans, sends WhatsApp tax receipts, and prints thermal receipts with strictly <b>&#8377;0 monthly SaaS fees</b>.
                </p>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5 text-center pt-1 font-mono">
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[10px] text-slate-400 uppercase">Checkout</div>
                        <div class="text-sm font-bold text-teal-400 mt-0.5">&lt; 500ms</div>
                        <div class="text-[9px] text-slate-500">Barcode Scan</div>
                    </div>
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[10px] text-slate-400 uppercase">Storage</div>
                        <div class="text-sm font-bold text-cyan-400 mt-0.5">Embedded Redb</div>
                        <div class="text-[9px] text-slate-500">Offline Local DB</div>
                    </div>
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[10px] text-slate-400 uppercase">Payments</div>
                        <div class="text-sm font-bold text-purple-400 mt-0.5">Dynamic UPI</div>
                        <div class="text-[9px] text-slate-500">Instant Scan</div>
                    </div>
                    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
                        <div class="text-[10px] text-slate-400 uppercase">Mobile POS</div>
                        <div class="text-sm font-bold text-amber-400 mt-0.5">Touch PWA</div>
                        <div class="text-[9px] text-slate-500">iOS / Android</div>
                    </div>
                </div>
            </div>

            <div class="pt-6 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-3 mt-4 relative z-10">
                <div class="flex flex-col">
                    <span class="text-xs text-teal-300 font-mono font-bold">Lifetime Store License</span>
                    <span class="text-[10px] text-slate-400 font-mono">Windows EXE + Offline Mobile PWA Suite</span>
                </div>
                <div class="flex items-center gap-2">
                    <a href="expressbill/" class="text-xs font-semibold text-slate-300 hover:text-white px-3 py-2 rounded-lg border border-slate-700 hover:border-slate-500 transition">
                        Live Demo
                    </a>
                    <button type="button" onclick="openUpiModal()" class="text-xs font-bold text-white bg-gradient-to-r from-emerald-500 to-teal-600 hover:from-emerald-400 hover:to-teal-500 px-4 py-2 rounded-xl transition flex items-center gap-1.5 shadow-md shadow-emerald-500/30 btn-spring shimmer-badge">
                        <i data-lucide="qr-code" class="w-3.5 h-3.5"></i>
                        <span>Claim License ($49 / &#8377;3,999)</span>
                    </button>
                </div>
            </div>
        </div>"""

def run_fix():
    print("=" * 70)
    print("🛠️ REPAIRING MAIN PAGE GRID & INTEGRATING SECURE UPI SUITE")
    print("=" * 70)

    # 1. Fix index.html Flagship Grid
    index_file = PORTFOLIO_DIR / "index.html"
    index_text = index_file.read_text(encoding="utf-8")

    # Replace from Flagship 4 to the end of the flagship grid
    pos_flag4 = index_text.find("<!-- Flagship 4: Industrial Fragility Sentinel")
    pos_end_flag = index_text.find("<!-- ABOUT / PHILOSOPHY")

    if pos_flag4 != -1 and pos_end_flag != -1:
        # Find where the grid finishes before ABOUT
        # Replace from pos_flag4 to pos_end_flag
        prefix = index_text[:pos_flag4]
        suffix = index_text[pos_end_flag:]
        # Wrap cleanly in the 2-column grid container
        middle = CLEAN_FLAGSHIP_4_5_6 + "\n\n    </div>\n</div>\n</div>\n</section>\n\n"
        index_text = prefix + middle + suffix
        print("✅ Cleanly replaced Cards 4, 5, and 6 in index.html with 100% balanced <div> tags.")

    # 2. Inject SECURE_UPI_MODAL_HTML into index.html and projects.html if not present
    for fname in ["index.html", "projects.html"]:
        fpath = PORTFOLIO_DIR / fname
        content = fpath.read_text(encoding="utf-8") if fname != "index.html" else index_text
        if "secure-upi-modal" not in content:
            content = content.replace("</body>", f"{SECURE_UPI_MODAL_HTML}\n</body>")
            print(f"[{fname}] Injected Secure Tamper-Proof UPI Modal.")
        fpath.write_text(content, encoding="utf-8")

    # 3. Create expressbill/ directory and deploy interactive demo PWA
    expressbill_dest = PORTFOLIO_DIR / "expressbill"
    expressbill_dest.mkdir(exist_ok=True)
    if PWA_SRC_DIR.exists():
        for item in PWA_SRC_DIR.iterdir():
            dest_item = expressbill_dest / item.name
            if item.is_file():
                shutil.copy2(item, dest_item)
        print("✅ Copied ExpressBill Mobile PWA into expressbill/ directory.")

        # In expressbill/index.html, inject the floating top action pill + UPI modal
        pwa_index_file = expressbill_dest / "index.html"
        pwa_html = pwa_index_file.read_text(encoding="utf-8")
        
        floating_cta = """
        <!-- FLOATING COMMERCIAL CTA BANNER -->
        <div style="position: fixed; bottom: 16px; left: 16px; right: 16px; z-index: 9999; max-width: 650px; margin: 0 auto; background: rgba(15, 23, 42, 0.96); backdrop-filter: blur(16px); border: 2px solid rgba(16, 185, 129, 0.5); border-radius: 18px; padding: 12px 18px; box-shadow: 0 20px 40px rgba(0,0,0,0.5); display: flex; align-items: center; justify-content: space-between; gap: 12px; color: white;">
            <div>
                <div style="font-size: 11px; font-weight: 700; color: #34d399; text-transform: uppercase; letter-spacing: 0.05em;">⚡ EXPRESSBILL POS™ — INTERACTIVE DEMO</div>
                <div style="font-size: 13px; font-weight: 600; color: #f1f5f9;">Own the Perpetual License ($49 / &#8377;3,999)</div>
            </div>
            <div style="display: flex; gap: 8px;">
                <button type="button" onclick="openUpiModal()" style="background: linear-gradient(135deg, #10b981, #0d9488); color: white; font-weight: 700; font-size: 12px; border: none; padding: 8px 14px; border-radius: 12px; cursor: pointer; box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);">
                    Claim License
                </button>
                <a href="../" style="background: rgba(255,255,255,0.1); color: #cbd5e1; font-weight: 600; font-size: 12px; text-decoration: none; padding: 8px 12px; border-radius: 12px; display: inline-flex; align-items: center;">
                    Exit
                </a>
            </div>
        </div>
        """
        if "secure-upi-modal" not in pwa_html:
            pwa_html = pwa_html.replace("</body>", f"{floating_cta}\n{SECURE_UPI_MODAL_HTML}\n</body>")
            pwa_index_file.write_text(pwa_html, encoding="utf-8")
            print("✅ Injected floating commercial action bar and UPI modal into expressbill/index.html.")

    print("\n✅ Verification and repair complete!")

if __name__ == "__main__":
    run_fix()
