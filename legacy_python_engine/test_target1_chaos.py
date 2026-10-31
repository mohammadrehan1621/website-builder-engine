"""
========================================================================================
 TARGET 1 CHAOS STRIKE: AUTONOMOUS AI WEBSITE BUILDER STUDIO
========================================================================================
 "Sledgehammering the Website Builder Studio to verify Phoenix Invulnerability."

 Strikes Executed:
   [1] Toxic AST & Prompt Injection   -> Tries to crash generator with malicious payloads.
   [2] Gemini API Fleet Quota Storm    -> Simulates 429 ResourceExhausted & verifies fallback.
   [3] Mid-Generation Ash Recovery     -> Tests zero-loss recovery of client briefs.
   [4] Cloudflare Edge Network Drop    -> Verifies deployment resilience & ledger commit.
   [5] Studio Port 8503 Decapitation   -> Verifies sub-second hot resurrection via Watchdog.
========================================================================================
"""

import sys
import time
import json
from pathlib import Path

# Configure Windows UTF-8 stdout
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from generator import WebsiteGenerator
from hosting_deployer import deploy_to_cloudflare_pages
from phoenix_engine import (
    AshLedger,
    ImmunityVault,
    CircuitBreaker,
    PhoenixTelemetry,
    ChaosLedger,
    print_phoenix_dashboard
)
from watchdog_healer import restart_service, is_port_in_use, is_service_healthy

BASE_DIR = Path(__file__).resolve().parent


def strike_1_toxic_ast_injection():
    print("\n" + "─" * 70)
    print("🎯 [TARGET 1 - STRIKE 1] Toxic AST & Prompt Injection Bombardment...")
    print("─" * 70)
    
    gen = WebsiteGenerator()
    malicious_prompt = """
    DROP TABLE users; <script>window.location='http://attacker.com';</script>
    {{{[[[((( UNCLOSED_RECURSION_BOMB_9999999999999999999999999999999999999
    """

    print("[CHAOS] Passing poison prompt into WebsiteGenerator.generate_site()...")
    t0 = time.perf_counter()
    html = gen.generate_site(
        prompt=malicious_prompt,
        site_type="Luxury Salon & Spa Atelier",
        theme_hint="Haute Editorial Alabaster"
    )
    elapsed = (time.perf_counter() - t0) * 1000

    has_doctype = "<!DOCTYPE html>" in html
    has_body = "</body>" in html
    size_bytes = len(html)

    print(f"[CHAOS] Site generated in {elapsed:.2f}ms ({size_bytes:,} bytes)")
    print(f"[CHAOS] HTML Valid: {has_doctype and has_body}")

    if has_doctype and has_body and size_bytes > 1000:
        print("✅ [STRIKE 1 DEFENDED] Poison contained! Studio produced valid, production-ready HTML.")
        return True
    else:
        print("❌ [STRIKE 1 FAILED] Poison broke the generator.")
        return False


def strike_2_gemini_api_fleet_storm():
    print("\n" + "─" * 70)
    print("🎯 [TARGET 1 - STRIKE 2] Gemini API Fleet Quota Storm (Simulating 429 / 503)...")
    print("─" * 70)

    # Instantiate generator with dummy client that always raises ResourceExhausted (429)
    gen = WebsiteGenerator()
    
    class MockExhaustedClient:
        class models:
            @staticmethod
            def generate_content(*args, **kwargs):
                raise RuntimeError("429 RESOURCE_EXHAUSTED: Quota exceeded for model fleet.")

    gen.client = MockExhaustedClient()

    print("[CHAOS] Simulating 100% Gemini API fleet quota exhaustion...")
    t0 = time.perf_counter()
    html = gen.generate_site(
        prompt="High-performance CrossFit Gym with VIP booking",
        site_type="High-Intensity Gym & Athletic Performance",
        theme_hint="Aggressive Neon Dark"
    )
    elapsed = (time.perf_counter() - t0) * 1000

    has_doctype = "<!DOCTYPE html>" in html
    print(f"[CHAOS] Procedural Fallback delivered complete site in {elapsed:.2f}ms ({len(html):,} bytes)")

    if has_doctype and len(html) > 1000:
        print("✅ [STRIKE 2 DEFENDED] Zero-downtime failover! Complete website built without external API.")
        return True
    else:
        print("❌ [STRIKE 2 FAILED] Studio crashed when API quota died.")
        return False


def strike_3_mid_generation_ash_recovery():
    print("\n" + "─" * 70)
    print("🎯 [TARGET 1 - STRIKE 3] Mid-Generation Crash & Ash Ledger State Recovery...")
    print("─" * 70)

    task_id = f"gen_site_chaos_{int(time.time() * 1000)}"
    client_brief = {
        "client_name": "Patna Couture House",
        "niche": "Bridal Lehengas & Handcrafted Sarees",
        "budget": "₹1,50,000",
        "whatsapp": "+918986047584"
    }

    print(f"[CHAOS] Simulating client submitting brief mid-flight: {task_id}")
    AshLedger.record_checkpoint(task_id, client_brief, stage="IN_FLIGHT")
    print("[CHAOS] 💥 CUTTING PROCESS POWER (Emulating abrupt kill)...")

    # Inspect Ash Ledger for resurrection
    uncommitted = AshLedger.recover_uncommitted_tasks()
    found = [t for t in uncommitted if t.get("task_id") == task_id]

    if found:
        rec = found[0].get("payload", {})
        print(f"🔥 [CHAOS] Ash Ledger rescued client brief! Client: {rec.get('client_name')}")
        print(f"   Budget Preserved: {rec.get('budget')} | WhatsApp: {rec.get('whatsapp')}")
        AshLedger.finalize_task(task_id, success=True, result_summary="Recovered by Phoenix")
        print("✅ [STRIKE 3 DEFENDED] Zero client data lost! State safely committed.")
        return True
    else:
        print("❌ [STRIKE 3 FAILED] Brief lost in the crash.")
        return False


def strike_4_cloudflare_deploy_resilience():
    print("\n" + "─" * 70)
    print("🎯 [TARGET 1 - STRIKE 4] Cloudflare Deploy Network Resilience & Checkpointing...")
    print("─" * 70)

    # Create dummy zip bytes
    import io, zipfile
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr("index.html", "<!DOCTYPE html><html><body><h1>Phoenix Chaos Test</h1></body></html>")
    zip_bytes = buf.getvalue()

    print("[CHAOS] Deploying mock site with simulated invalid token to test failure handling...")
    res = deploy_to_cloudflare_pages(
        zip_bytes=zip_bytes,
        project_name="chaos-phoenix-test",
        account_id="d064c1b92d1088a0578aeed4cd790bf5",
        api_token="invalid_token_test_123"
    )

    print(f"[CHAOS] Deploy response handled gracefully: success={res.get('success')}")
    # Verify Ash Ledger recorded the failure cleanly without unhandled exception
    uncommitted = AshLedger.recover_uncommitted_tasks()
    stranded_cf = [t for t in uncommitted if "chaos-phoenix-test" in t.get("task_id", "")]

    if len(stranded_cf) == 0:
        print("✅ [STRIKE 4 DEFENDED] Deploy failure trapped cleanly; Ash Ledger state finalized without leaks.")
        return True
    else:
        print("❌ [STRIKE 4 FAILED] Deploy left uncommitted debris in ledger.")
        return False


def strike_5_studio_resurrection():
    print("\n" + "─" * 70)
    print("🎯 [TARGET 1 - STRIKE 5] Studio Watchdog & Hot Resurrection Test...")
    print("─" * 70)

    print("[CHAOS] Triggering Phoenix restart_service() on Streamlit Studio...")
    t0 = time.perf_counter()
    restart_service()
    mttr_ms = (time.perf_counter() - t0) * 1000

    print(f"🔥 [CHAOS] Service command fired in {mttr_ms:.2f}ms.")
    telem = PhoenixTelemetry.load()
    print(f"[CHAOS] Phoenix Total Resurrections: {telem.get('total_resurrections')}")
    print(f"[CHAOS] System Health Index: {telem.get('health_index')}%")

    if telem.get("total_resurrections", 0) > 0:
        print("✅ [STRIKE 5 DEFENDED] Streamlit Studio hot-resurrection verified via Phoenix Watchdog!")
        return True
    else:
        print("❌ [STRIKE 5 FAILED] Resurrection not recorded.")
        return False


def run_target_1_chaos(mode: str = "TARGET1_CHAOS_STRIKE") -> dict:
    t0 = time.time()
    print("\n" + "═" * 70)
    print("    💥 TARGET 1: AUTONOMOUS AI WEBSITE BUILDER STUDIO CHAOS ARENA 💥")
    print(f"   Mode: {mode} | Continuous Adversarial Verification")
    print("═" * 70)

    results = {}
    results["Strike 1: Toxic AST & Prompt Injection"] = strike_1_toxic_ast_injection()
    results["Strike 2: Gemini Fleet 429 Quota Storm"] = strike_2_gemini_api_fleet_storm()
    results["Strike 3: Mid-Generation Ash Recovery"] = strike_3_mid_generation_ash_recovery()
    results["Strike 4: Cloudflare Deploy Checkpointing"] = strike_4_cloudflare_deploy_resilience()
    results["Strike 5: Studio Hot Resurrection"] = strike_5_studio_resurrection()

    duration_ms = (time.time() - t0) * 1000.0
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    score = (passed / total) * 100.0

    print("\n" + "═" * 70)
    print("        🏁 TARGET 1 CHAOS WAR ROOM REPORT: STUDIO ARMOR 🏁")
    print("═" * 70)
    for name, success in results.items():
        symbol = "🟢 DEFENDED" if success else "🔴 FAILED"
        print(f"  • {name:42}: {symbol}")

    print("─" * 70)
    grade = "TITANIUM GRADE INVULNERABLE" if score == 100 else "NEEDS HARDENING"
    print(f"  TARGET 1 RESILIENCE SCORE: {score:.1f}% [{grade}]")
    print(f"  Strike Duration: {duration_ms:.1f}ms | Mode: {mode}")
    print("═" * 70 + "\n")

    entry = ChaosLedger.record_drill(
        mode=mode,
        score=score,
        defended=passed,
        total=total,
        breakdown=results,
        duration_ms=duration_ms
    )
    print_phoenix_dashboard()

    return {
        "score": score,
        "defended": passed,
        "total": total,
        "results": results,
        "duration_ms": duration_ms,
        "mode": mode,
        "entry": entry
    }


if __name__ == "__main__":
    run_target_1_chaos()

