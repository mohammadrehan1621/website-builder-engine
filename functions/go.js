// ====================================================================
// Rehan Quant Lab - Anycast Dynamic QR Redirect Engine (Cloudflare Edge)
// Low-Density, High-Speed Barcode Forwarder
// ====================================================================

export async function onRequest(context) {
    const url = new URL(context.request.url);
    const params = url.searchParams;

    // Supported query parameters: 'to', 'url', 'target', 'slug', 'q'
    const targetParam = params.get('to') || params.get('url') || params.get('target') || params.get('slug') || params.get('q');
    const coupon = params.get('coupon') || params.get('discount');

    // 31-Suite Product Slugs + Core Hub Routing Map
    const slugMap = {
        // Core Hubs
        'store': 'https://rehanquantlab.com/store',
        'home': 'https://rehanquantlab.com/',
        'contact': 'https://rehanquantlab.com/contact',
        'briefing': 'https://rehanquantlab.com/contact#schedule-briefing',
        'whatsapp': 'https://wa.me/917091518548',
        'experience': 'https://rehanquantlab.com/experience',
        'security': 'https://rehanquantlab.com/security',

        // 31 Pure-Rust Commercial Flagships
        'documentshield': 'https://rehanquantlab.gumroad.com/l/rql-documentshield',
        'whispervault': 'https://rehanquantlab.gumroad.com/l/rql-whispervault',
        'retailpos': 'https://rehanquantlab.gumroad.com/l/rql-retailpos',
        'storechain': 'https://rehanquantlab.gumroad.com/l/rql-storechain',
        'conduit': 'https://rehanquantlab.gumroad.com/l/rql-conduit',
        'hashcheck': 'https://rehanquantlab.gumroad.com/l/rql-hashcheck',
        'qrstudio': 'https://rehanquantlab.gumroad.com/l/rql-qrstudio',
        'textdiff': 'https://rehanquantlab.gumroad.com/l/rql-textdiff',
        'renamer': 'https://rehanquantlab.gumroad.com/l/rql-renamer',
        'tageditor': 'https://rehanquantlab.gumroad.com/l/rql-tageditor',
        'fontviewer': 'https://rehanquantlab.gumroad.com/l/rql-fontviewer',
        'dpdpshield': 'https://rehanquantlab.gumroad.com/l/rql-dpdpshield',
        'pricetag': 'https://rehanquantlab.gumroad.com/l/rql-pricetag',
        'invoicegen': 'https://rehanquantlab.gumroad.com/l/rql-invoicegen',
        'csvformat': 'https://rehanquantlab.gumroad.com/l/rql-csvformat',
        'pdfmerge': 'https://rehanquantlab.gumroad.com/l/rql-pdfmerge',
        'taxledger': 'https://rehanquantlab.gumroad.com/l/rql-taxledger',
        'fileshredder': 'https://rehanquantlab.gumroad.com/l/rql-fileshredder',
        'clipvault': 'https://rehanquantlab.gumroad.com/l/rql-clipvault',
        'imagebatch': 'https://rehanquantlab.gumroad.com/l/rql-imagebatch',
        'audioextract': 'https://rehanquantlab.gumroad.com/l/rql-audioextract',
        'subtitlesync': 'https://rehanquantlab.gumroad.com/l/rql-subtitlesync',
        'spacemap': 'https://rehanquantlab.gumroad.com/l/rql-spacemap',
        'docprotect': 'https://rehanquantlab.gumroad.com/l/rql-docprotect',
        'cashdrawer': 'https://rehanquantlab.gumroad.com/l/rql-cashdrawer',
        'receiptprinter': 'https://rehanquantlab.gumroad.com/l/rql-receiptprinter',
        'clauseforge': 'https://rehanquantlab.gumroad.com/l/rql-clauseforge',
        'archivemaster': 'https://rehanquantlab.gumroad.com/l/rql-archivemaster',
        'socketshield': 'https://rehanquantlab.gumroad.com/l/rql-socketshield',
        'pingpulse': 'https://rehanquantlab.gumroad.com/l/rql-pingpulse',
        'foldersync': 'https://rehanquantlab.gumroad.com/l/rql-foldersync'
    };

    let destination = 'https://rehanquantlab.com/store';

    if (targetParam) {
        const cleanSlug = targetParam.trim().toLowerCase();
        if (slugMap[cleanSlug]) {
            destination = slugMap[cleanSlug];
            if (coupon && destination.includes('gumroad.com')) {
                destination += '/' + encodeURIComponent(coupon) + '?wanted=true';
            }
        } else {
            let decoded = targetParam.trim();
            try {
                decoded = decodeURIComponent(decoded);
            } catch (e) {
                // Keep raw if already decoded
            }

            // Ensure valid protocol
            if (decoded.startsWith('http://') || decoded.startsWith('https://') || decoded.startsWith('upi://') || decoded.startsWith('mailto:') || decoded.startsWith('tel:')) {
                destination = decoded;
            } else if (decoded.includes('.') && !decoded.includes(' ')) {
                destination = 'https://' + decoded;
            }
        }
    }

    return new Response(null, {
        status: 302,
        statusText: "Found",
        headers: {
            "Location": destination,
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0",
            "X-Robots-Tag": "noindex, nofollow",
            "X-Redirected-By": "RQL-Anycast-Edge"
        }
    });
}
