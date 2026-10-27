//! ============================================================================
//! REHAN QUANT LAB™ — RUST QUANTITATIVE & WASM KERNEL v2.0
//! Principal Architect: Mohammad Rehan | Founder @ Rehan Quant Lab
//!
//! Gall's Law & Sovereign Systems Doctrine:
//! "A complex system that works is always found to have evolved from a simple
//!  system that worked. Never build a monster we cannot understand."
//! ============================================================================

#![no_std]

#[panic_handler]
fn panic(_info: &core::panic::PanicInfo) -> ! {
    loop {}
}

/// Returns the engine operational status and genomic generation version.
#[no_mangle]
pub extern "C" fn rql_engine_status() -> u32 {
    0x52514C32 // "RQL2" in hex ASCII
}

/// Computes high-throughput deterministic financial calculations across N iterations.
/// Used to demonstrate pure Rust WebAssembly performance in the React browser client.
#[no_mangle]
pub extern "C" fn rql_benchmark_crunch(iterations: u32) -> f64 {
    let mut accumulator: f64 = 1.0000001;
    let mut x: f64 = 0.5;

    for i in 0..iterations {
        // High-precision non-linear recurrence (chaotic map & polynomial drift)
        x = 3.999 * x * (1.0 - x);
        accumulator = accumulator + (x * 0.000001) + ((i as f64) * 0.000000001);
    }

    accumulator
}

/// Computes procedural 3D vertex wave coordinates for Three.js particle geometry.
#[no_mangle]
pub extern "C" fn rql_compute_wave(x: f32, y: f32, time: f32) -> f32 {
    let freq1 = 1.8;
    let freq2 = 2.4;
    // Approximated sine wave without stdlib
    let angle1 = (x * freq1 + time) * 0.5;
    let angle2 = (y * freq2 + time * 0.8) * 0.5;
    
    // Taylor series approximation for sin(theta) within [-pi, pi]
    let s1 = approx_sin(angle1);
    let s2 = approx_sin(angle2);
    
    (s1 + s2) * 0.5
}

/// Stoikov Orderbook Micro-Price Calculation:
/// MicroPrice = (Q_bid * P_ask + Q_ask * P_bid) / (Q_bid + Q_ask)
#[no_mangle]
pub extern "C" fn rql_stoikov_micro_price(bid_price: f64, ask_price: f64, bid_qty: f64, ask_qty: f64) -> f64 {
    let total_qty = bid_qty + ask_qty;
    if total_qty <= 0.0 {
        return (bid_price + ask_price) * 0.5;
    }
    (bid_qty * ask_price + ask_qty * bid_price) / total_qty
}

/// Non-Newtonian Liquid Diamond Armor Viscosity Damping:
/// Under peacetime conditions (spread <= 0.05%), viscosity = 1.0 (water).
/// During volatility spikes, shear-thickening increases exponentially.
#[no_mangle]
pub extern "C" fn rql_liquid_diamond_viscosity(spread: f64, volatility: f64) -> f64 {
    let base_spread = 0.05;
    if spread <= base_spread {
        return 1.0;
    }
    let spread_excess = spread - base_spread;
    let shear = 1.0 + (spread_excess * 15.0) + (volatility * 2.5);
    if shear > 10.0 {
        10.0
    } else {
        shear
    }
}

/// Black-Scholes Call Option Price Approximation using polynomial standard normal CDF.
#[no_mangle]
pub extern "C" fn rql_black_scholes_call(s: f64, k: f64, t: f64, r: f64, v: f64) -> f64 {
    if t <= 0.0 || v <= 0.0 || s <= 0.0 || k <= 0.0 {
        let diff = s - k;
        return if diff > 0.0 { diff } else { 0.0 };
    }
    
    let sqrt_t = approx_sqrt(t);
    let v_sqrt_t = v * sqrt_t;
    let d1 = (approx_ln(s / k) + (r + 0.5 * v * v) * t) / v_sqrt_t;
    let d2 = d1 - v_sqrt_t;

    let nd1 = normal_cdf(d1);
    let nd2 = normal_cdf(d2);
    let exp_rt = approx_exp(-r * t);

    s * nd1 - k * exp_rt * nd2
}

/// Fast 64-bit state hashing for Phoenix Ash Ledger micro-journaling.
#[no_mangle]
pub extern "C" fn rql_hash_state(mut state: u64, salt: u64) -> u64 {
    state ^= salt;
    state = state.wrapping_mul(0x9E3779B97F4A7C15);
    state ^= state >> 30;
    state = state.wrapping_mul(0xBF58476D1CE4E5B9);
    state ^= state >> 27;
    state = state.wrapping_mul(0x94D049BB133111EB);
    state ^ (state >> 31)
}

// ────────────────────────────────────────────────────────────────────────
// Pure Math Primitives (No standard library required for WASM target)
// ────────────────────────────────────────────────────────────────────────

fn approx_sin(mut x: f32) -> f32 {
    let pi = 3.14159265;
    let two_pi = 6.2831853;
    
    // Wrap to [-pi, pi]
    while x > pi { x -= two_pi; }
    while x < -pi { x += two_pi; }
    
    // Taylor approximation: x - x^3/6 + x^5/120 - x^7/5040
    let x2 = x * x;
    let x3 = x * x2;
    let x5 = x3 * x2;
    let x7 = x5 * x2;
    
    x - (x3 * 0.16666667) + (x5 * 0.00833333) - (x7 * 0.00019841)
}

fn approx_sqrt(x: f64) -> f64 {
    if x <= 0.0 { return 0.0; }
    let mut guess = x * 0.5;
    if guess == 0.0 { guess = 1.0; }
    for _ in 0..8 {
        guess = 0.5 * (guess + x / guess);
    }
    guess
}

fn approx_ln(x: f64) -> f64 {
    if x <= 0.0 { return -999.0; }
    // Halley's rational approximation for ln(x)
    let y = (x - 1.0) / (x + 1.0);
    let y2 = y * y;
    2.0 * y * (1.0 + y2 * (1.0 / 3.0 + y2 * (1.0 / 5.0 + y2 * (1.0 / 7.0))))
}

fn approx_exp(x: f64) -> f64 {
    // 1 + x + x^2/2 + x^3/6 + x^4/24 + x^5/120
    let mut sum = 1.0;
    let mut term = 1.0;
    for i in 1..12 {
        term *= x / (i as f64);
        sum += term;
    }
    sum
}

fn normal_cdf(x: f64) -> f64 {
    // Abramowitz and Stegun approximation (error < 7.5e-8)
    let b1 = 0.319381530;
    let b2 = -0.356563782;
    let b3 = 1.781477937;
    let b4 = -1.821255978;
    let b5 = 1.330274429;
    let p = 0.2316419;

    let abs_x = if x < 0.0 { -x } else { x };
    let t = 1.0 / (1.0 + p * abs_x);
    let poly = t * (b1 + t * (b2 + t * (b3 + t * (b4 + t * b5))));
    let pdf = 0.3989422804014327 * approx_exp(-0.5 * x * x);
    let cdf = 1.0 - pdf * poly;

    if x < 0.0 { 1.0 - cdf } else { cdf }
}
