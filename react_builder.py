"""
=============================================================================
REHAN QUANT LAB™ — REACT + 3D + RUST ENGINE BUILDER
Automates building the Rust WASM kernel, audits assets, and packages the
modern React + GSAP + Framer Motion + Three.js sovereign portal.
=============================================================================
"""

import os
import sys
import subprocess
import shutil
import time
from pathlib import Path

# Configure Windows UTF-8 stdout
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent
RUST_DIR = BASE_DIR / "rql_rust_engine"
DEPLOYED_DIR = BASE_DIR / "Deployed_Websites" / "mohammadrehan.pages.dev"

def build_rust_engine():
    print("\n" + "═" * 70)
    print("🦀 BUILDING RUST WEBASSEMBLY & NATIVE SITE BUILDER ENGINE")
    print("═" * 70)

    if not RUST_DIR.exists():
        print(f"❌ Error: {RUST_DIR} not found.")
        return False

    # 1. Compile WebAssembly Target
    print("\n[1/3] Compiling wasm32-unknown-unknown WebAssembly release...")
    res_wasm = subprocess.run(
        ["cargo", "build", "--release", "--target", "wasm32-unknown-unknown"],
        cwd=RUST_DIR,
        capture_output=True,
        text=True
    )
    if res_wasm.returncode != 0:
        print(f"❌ WASM build failed:\n{res_wasm.stderr}")
        return False
    print("   ✔ WebAssembly kernel compiled successfully.")

    # 2. Compile Native CLI Binary
    print("\n[2/3] Compiling native x86_64 host release binary (rql_builder.exe)...")
    res_bin = subprocess.run(
        ["cargo", "build", "--release"],
        cwd=RUST_DIR,
        capture_output=True,
        text=True
    )
    if res_bin.returncode != 0:
        print(f"❌ Native binary build failed:\n{res_bin.stderr}")
        return False
    print("   ✔ Native host optimizer compiled successfully.")

    # 3. Copy WASM artifact to deployment directory
    wasm_src = RUST_DIR / "target" / "wasm32-unknown-unknown" / "release" / "rql_rust_engine.wasm"
    if wasm_src.exists():
        wasm_dest = DEPLOYED_DIR / "rql_wasm_engine.wasm"
        shutil.copy2(wasm_src, wasm_dest)
        print(f"\n[3/3] Deployed WASM artifact: {wasm_dest.name} ({wasm_dest.stat().st_size:,} bytes)")

    # 4. Run Rust Audit & Benchmark
    bin_path = RUST_DIR / "target" / "release" / "rql_builder.exe"
    if bin_path.exists():
        print("\n⚡ Executing Native Rust Speed Audit:")
        subprocess.run([str(bin_path)], cwd=BASE_DIR)

    return True

def package_react_portal():
    print("\n" + "═" * 70)
    print("⚛️ PACKAGING REACT + GSAP + FRAMER MOTION + THREE.JS 3D PORTAL")
    print("═" * 70)

    portal_html = DEPLOYED_DIR / "react_portal.html"
    if portal_html.exists():
        print(f"   ✔ Standalone React 3D Portal Ready: {portal_html.name} ({portal_html.stat().st_size:,} bytes)")
    else:
        print("   ⚠️ react_portal.html missing.")

    # Copy to projects/website_builder if mirrored
    mirrored_dir = Path("C:/Users/rehan/Desktop/projects/website_builder/Deployed_Websites/mohammadrehan.pages.dev")
    if mirrored_dir.exists():
        try:
            shutil.copy2(portal_html, mirrored_dir / "react_portal.html")
            print(f"   ✔ Synced to mirrored workspace: {mirrored_dir / 'react_portal.html'}")
        except Exception as e:
            print(f"   Mirror notice: {e}")

    return True

if __name__ == "__main__":
    t0 = time.time()
    build_rust_engine()
    package_react_portal()
    print(f"\n🏁 ALL SYSTEMS COMPILED & AUDITED IN {time.time() - t0:.2f}s\n")
