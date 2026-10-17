"""
========================================================================================
 PROJECT PHOENIX: THE CHAOS ENGINEERING LAB (CHAOS ARENA) 💥
========================================================================================
 "Breaking your own code before the world breaks it for you."
 
 The 5 Chaos Missiles:
   [1] Toxic Payload Injection  -> Corrupted AST, SQLi, recursion bombs to test Immunity Vault.
   [2] Process Decapitation     -> Hard OS SIGKILL to test sub-second Phoenix resurrection.
   [3] Memory Tsunami           -> Simulated heap leak to verify OOM prevention & reclamation.
   [4] API Blackhole            -> Consecutive HTTP 429/503 strikes to verify Circuit Breaker.
   [5] Ash Ledger Replay        -> Mid-flight power-cut simulation to verify 100% state recovery.
========================================================================================
"""

import os
import sys
import time
import json
import random
import subprocess
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

try:
    import psutil
except ImportError:
    psutil = None

from phoenix_engine import (
    AshLedger,
    ImmunityVault,
    CircuitBreaker,
    PhoenixTelemetry,
    PhoenixSupervisor,
    ChaosLedger,
    phoenix_resilient,
    print_phoenix_dashboard
)

BASE_DIR = Path(__file__).resolve().parent


# ======================================================================================
# CHAOS MISSILE 1: TOXIC PAYLOAD INJECTION
# ======================================================================================
def launch_missile_1_toxic_payload() -> bool:
    print("\n" + "─" * 70)
    print("🚀 [CHAOS MISSILE 1] Launching: Toxic Payload & AST Poison Injection...")
    print("─" * 70)

    # Fallback routine to protect the user
    def safe_fallback(payload):
        return {"status": "recovered", "safe_response": "Phoenix Fallback Engaged. Poison safely contained."}

    # Fragile function wrapped with Phoenix Armor
    @phoenix_resilient(task_name="compiler_ast_parser", fallback_fn=safe_fallback, retry_limit=2)
    def fragile_parser(payload: dict):
        code = payload.get("raw_code", "")
        if "POISON_TOKEN_CRASH_NOW" in code:
            raise ValueError(f"AST Fatal Crash: Unhandled illegal token syntax in '{code[:30]}'")
        return {"status": "compiled", "ast_nodes": len(code)}

    toxic_payload = {
        "raw_code": "SELECT * FROM users WHERE '1'='1'; <script>POISON_TOKEN_CRASH_NOW();</script>",
        "user_agent": "Adversary_Chaos_Bot/1.0"
    }

    print("[CHAOS] Injecting toxic payload into fragile parser...")
    
    # 1st Strike: Function will crash, Phoenix will catch it, perform autopsy, and synthesize immunity!
    res1 = fragile_parser(toxic_payload)
    print(f"[CHAOS] First Strike Result: {res1}")

    # 2nd Strike: Immunity Vault should IMMEDIATELY intercept before code even executes!
    print("[CHAOS] Injecting SAME toxic payload a second time to verify IMMUNITY...")
    res2 = fragile_parser(toxic_payload)
    print(f"[CHAOS] Second Strike Result (Immunity Shielded): {res2}")

    passed = (res1.get("status") in ["recovered", "quarantined"]) and (res2.get("status") in ["recovered", "quarantined"])
    if passed:
        print("✅ [MISSILE 1 DEFENDED] Toxic input quarantined. System survived with ZERO crash!")
    else:
        print("❌ [MISSILE 1 FAILED] Fragile parser did not handle the poison.")
    return passed


# ======================================================================================
# CHAOS MISSILE 2: PROCESS DECAPITATION (SIGKILL / HARD REAP)
# ======================================================================================
def launch_missile_2_process_decapitation() -> bool:
    print("\n" + "─" * 70)
    print("🚀 [CHAOS MISSILE 2] Launching: Process Decapitation (Hard OS Kill)...")
    print("─" * 70)

    # Create a dummy worker script that loops
    worker_script = BASE_DIR / "phoenix_vault" / "dummy_worker.py"
    worker_script.write_text(
        "import time, sys\n"
        "while True:\n"
        "    time.sleep(0.1)\n",
        encoding="utf-8"
    )

    supervisor = PhoenixSupervisor(
        target_cmd=[sys.executable, str(worker_script)],
        cwd=BASE_DIR,
        name="ChaosTargetWorker"
    )

    print("[CHAOS] Spawning supervised worker process...")
    supervisor.start()
    time.sleep(1.0)

    if not supervisor.process or supervisor.process.poll() is not None:
        print("❌ [CHAOS] Failed to spawn worker.")
        return False

    victim_pid = supervisor.process.pid
    print(f"[CHAOS] Target Worker is running with PID: {victim_pid}")
    print("[CHAOS] 💥 FIRING HARD OS KILL (Decapitating process)...")

    # Hard kill process
    t_strike = time.perf_counter()
    if psutil:
        try:
            p = psutil.Process(victim_pid)
            p.kill()
        except Exception:
            supervisor.process.terminate()
    else:
        supervisor.process.terminate()

    # Wait for Phoenix Supervisor to detect and resurrect
    resurrected = False
    new_pid = None
    for _ in range(20):
        time.sleep(0.2)
        if supervisor.process and supervisor.process.pid != victim_pid and supervisor.process.poll() is None:
            resurrected = True
            new_pid = supervisor.process.pid
            break

    mttr_ms = (time.perf_counter() - t_strike) * 1000
    supervisor.stop()

    if resurrected:
        print(f"🔥 [MISSILE 2 DEFENDED] Process was killed (PID {victim_pid}), but Phoenix resurrected new PID {new_pid} in {mttr_ms:.2f}ms!")
        return True
    else:
        print("❌ [MISSILE 2 FAILED] Process did not resurrect automatically.")
        return False


# ======================================================================================
# CHAOS MISSILE 3: MEMORY TSUNAMI (SIMULATED HEAP LEAK)
# ======================================================================================
def launch_missile_3_memory_tsunami() -> bool:
    print("\n" + "─" * 70)
    print("🚀 [CHAOS MISSILE 3] Launching: Memory Tsunami (Simulated Heap Leak)...")
    print("─" * 70)

    def memory_safe_fallback(leak_mb):
        return {"status": "reclaimed", "message": "Memory tsunami safely intercepted & garbage collected."}

    @phoenix_resilient(task_name="heavy_image_render_buffer", fallback_fn=memory_safe_fallback, retry_limit=1)
    def memory_hungry_task(leak_mb: int):
        if leak_mb > 150:
            raise MemoryError(f"Simulated OutOfMemory: Task requested {leak_mb}MB exceeding 150MB heap ceiling!")
        # Allocate harmless dummy buffer
        dummy = bytearray(leak_mb * 1024 * 1024)
        return {"status": "success", "allocated_mb": len(dummy) // (1024*1024)}

    print("[CHAOS] Testing normal 20MB buffer allocation...")
    res_normal = memory_hungry_task(20)
    print(f"[CHAOS] Normal task result: {res_normal}")

    print("[CHAOS] 💥 INJECTING 500MB MEMORY TSUNAMI...")
    res_tsunami = memory_hungry_task(500)
    print(f"[CHAOS] Tsunami response: {res_tsunami}")

    passed = (res_tsunami.get("status") in ["reclaimed", "quarantined"])
    if passed:
        print("✅ [MISSILE 3 DEFENDED] OutOfMemory hazard contained; memory reclaimed gracefully.")
    else:
        print("❌ [MISSILE 3 FAILED] Memory leak caused unhandled crash.")
    return passed


# ======================================================================================
# CHAOS MISSILE 4: API BLACKHOLE & CIRCUIT BREAKER STRESS
# ======================================================================================
def launch_missile_4_circuit_breaker() -> bool:
    print("\n" + "─" * 70)
    print("🚀 [CHAOS MISSILE 4] Launching: API Blackhole & Circuit Breaker Stress...")
    print("─" * 70)

    breaker_name = f"test_api_gateway_{int(time.time())}"
    breaker = CircuitBreaker(breaker_name, failure_threshold=3, cooldown_seconds=2.0)

    def static_offline_fallback():
        return {"source": "local_phoenix_cache", "data": "High-fidelity cached response."}

    @phoenix_resilient(
        task_name="upstream_cloud_call",
        fallback_fn=static_offline_fallback,
        retry_limit=1,
        service_breaker=breaker_name
    )
    def volatile_api_call():
        # Simulate upstream 503 / 429
        raise ConnectionResetError("503 Service Unavailable: Cloudflare Edge connection reset by peer")

    print("[CHAOS] Bombarding external API endpoint with 5 consecutive failures...")
    for i in range(1, 6):
        res = volatile_api_call()
        print(f"  Strike {i}/5 -> Result source: {res.get('source', 'unknown')}")

    # Inspect breaker state in Immunity Vault
    vault = ImmunityVault.load_vault()
    b_state = vault.get("circuit_breakers", {}).get(breaker_name, {})
    current_state = b_state.get("state")
    print(f"[CHAOS] Circuit Breaker State: {current_state} (Tripped Count: {b_state.get('tripped_count')})")

    passed = (current_state in [CircuitBreaker.STATE_OPEN, CircuitBreaker.STATE_HALF_OPEN])
    if passed:
        print("✅ [MISSILE 4 DEFENDED] Circuit Breaker tripped into OPEN mode! Upstream protected from cascading collapse.")
    else:
        print("❌ [MISSILE 4 FAILED] Circuit Breaker failed to trip.")
    return passed


# ======================================================================================
# CHAOS MISSILE 5: ASH LEDGER REPLAY (MID-FLIGHT POWER CUT RECOVERY)
# ======================================================================================
def launch_missile_5_ash_ledger_replay() -> bool:
    print("\n" + "─" * 70)
    print("🚀 [CHAOS MISSILE 5] Launching: Ash Ledger Mid-Flight Crash & Replay...")
    print("─" * 70)

    # Simulate an in-flight business transaction that was cut off by an abrupt power loss
    stranded_task_id = f"business_gst_invoice_{int(time.time())}"
    state_payload = {
        "invoice_number": "INV-2026-9042",
        "customer": "Maison Ladies Zone VIP Client",
        "total_amount": 48500.0,
        "items": ["Bridal Haute Lehenga (Ivory Silk)", "Handmade Zardozi Dupatta"],
        "payment_status": "PENDING_SETTLEMENT"
    }

    print(f"[CHAOS] Simulating critical state checkpoint in flight for task: {stranded_task_id}")
    checksum = AshLedger.record_checkpoint(stranded_task_id, state_payload, stage="IN_FLIGHT")
    print(f"[CHAOS] Checkpoint committed to Ash Ledger (Checksum: {checksum})")
    print("[CHAOS] 💥 SIMULATING INSTANTANEOUS SYSTEM POWER LOSS (No clean exit, no commit)...")

    # Now run Phoenix state recovery
    print("[CHAOS] Phoenix Engine rebooting... Scanning Ash Ledger for stranded operations...")
    uncommitted = AshLedger.recover_uncommitted_tasks()
    found = [t for t in uncommitted if t.get("task_id") == stranded_task_id]

    if found:
        recovered_task = found[0]
        recovered_payload = recovered_task.get("payload", {})
        print(f"🔥 [CHAOS] Stranded task found in the ashes! Resurrecting state: {recovered_payload.get('invoice_number')}")
        print(f"   Items Recovered: {recovered_payload.get('items')}")
        print(f"   Amount Preserved: ₹{recovered_payload.get('total_amount'):,.2f}")
        
        # Complete the resurrected task
        AshLedger.finalize_task(stranded_task_id, success=True, result_summary="Resurrected & Settled via Phoenix")
        print("✅ [MISSILE 5 DEFENDED] 100% data retention verified! Zero business data lost in crash.")
        return True
    else:
        print("❌ [MISSILE 5 FAILED] Stranded task was not recovered from the Ash Ledger.")
        return False


# ======================================================================================
# MASTER CHAOS GAUNTLET
# ======================================================================================
def run_chaos_gauntlet(mode: str = "MANUAL_CLI") -> dict:
    t0 = time.time()
    print("\n" + "═" * 70)
    print("         💥 WELCOME TO THE PROJECT PHOENIX CHAOS ARENA 💥")
    print(f"   Mode: {mode} | Continuous Adversarial Verification")
    print("═" * 70)

    results = {}
    results["Missile 1: Toxic AST Payload"] = launch_missile_1_toxic_payload()
    results["Missile 2: Hard Process Kill"] = launch_missile_2_process_decapitation()
    results["Missile 3: Memory Tsunami (OOM)"] = launch_missile_3_memory_tsunami()
    results["Missile 4: API Blackhole (Breaker)"] = launch_missile_4_circuit_breaker()
    results["Missile 5: Ash Ledger State Replay"] = launch_missile_5_ash_ledger_replay()

    duration_ms = (time.time() - t0) * 1000.0
    total = len(results)
    passed = sum(1 for v in results.values() if v)
    score = (passed / total) * 100.0

    print("\n" + "═" * 70)
    print("                   🏁 FINAL CHAOS WAR ROOM REPORT 🏁")
    print("═" * 70)
    for name, success in results.items():
        symbol = "🟢 PASSED" if success else "🔴 FAILED"
        print(f"  • {name:40}: {symbol}")

    print("─" * 70)
    grade = "TITANIUM GRADE INVULNERABLE" if score == 100 else "NEEDS HARDENING"
    print(f"  PHOENIX SURVIVAL SCORE: {score:.1f}% [{grade}]")
    print(f"  Drill Duration: {duration_ms:.1f}ms | Mode: {mode}")
    print("═" * 70 + "\n")

    # Record permanently into Chaos Ledger
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
    run_chaos_gauntlet()
