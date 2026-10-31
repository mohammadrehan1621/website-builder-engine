import os
import sys
import time
import socket
import subprocess
import threading
import requests
from pathlib import Path
from dotenv import load_dotenv

try:
    from phoenix_engine import PhoenixTelemetry, AshLedger, ChaosLedger
    HAS_PHOENIX = True
except ImportError:
    HAS_PHOENIX = False

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")
load_dotenv()

LOGS_DIR = BASE_DIR / "logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)
WATCHDOG_LOG = LOGS_DIR / "watchdog_healing.log"

PORT = 8503
PING_URL = f"http://127.0.0.1:{PORT}"
CHECK_INTERVAL_SECONDS = 8

def log(msg: str):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] [WATCHDOG] {msg}\n"
    print(entry.strip())
    try:
        with open(WATCHDOG_LOG, "a", encoding="utf-8") as f:
            f.write(entry)
    except Exception:
        pass

def is_port_in_use(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("127.0.0.1", port)) == 0

def is_service_healthy() -> bool:
    try:
        r = requests.get(PING_URL, timeout=4)
        return r.status_code == 200
    except Exception:
        return False

def kill_port_occupant(port: int):
    try:
        # Use PowerShell to safely find and terminate process on port 8503
        cmd = f"Get-NetTCPConnection -LocalPort {port} -ErrorAction SilentlyContinue | ForEach-Object {{ Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }}"
        subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True, timeout=10)
        time.sleep(2)
    except Exception as e:
        log(f"Error terminating port occupant: {e}")

def restart_service():
    t_start = time.perf_counter()
    log(f"Project Phoenix Triggered: Service on port {PORT} unresponsive or stopped. Restoring...")
    kill_port_occupant(PORT)
    
    app_path = BASE_DIR / "streamlit_app.py"
    if not app_path.exists():
        log(f"Error: {app_path} not found.")
        return

    # Start Streamlit in detached background process
    cmd = [
        sys.executable, "-m", "streamlit", "run",
        str(app_path),
        "--server.port", str(PORT),
        "--server.headless", "true"
    ]
    
    try:
        if sys.platform == "win32":
            subprocess.Popen(
                cmd,
                cwd=str(BASE_DIR),
                creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        else:
            subprocess.Popen(cmd, cwd=str(BASE_DIR), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        mttr_ms = (time.perf_counter() - t_start) * 1000
        log(f"🔥 Phoenix resurrected Streamlit Studio on port {PORT} in {mttr_ms:.2f}ms.")
        
        if HAS_PHOENIX:
            PhoenixTelemetry.record_resurrection(mttr_ms, cause="Studio_Port_Unresponsive")
            uncommitted = AshLedger.recover_uncommitted_tasks()
            if uncommitted:
                log(f"🛡️ Phoenix Ash Ledger: Found {len(uncommitted)} stranded tasks. Ready for recovery.")
            threading.Thread(target=run_background_chaos_audit, args=("WATCHDOG_POST_RESURRECTION",), daemon=True).start()
    except Exception as e:
        log(f"Failed to restart service: {e}")

def run_background_chaos_audit(mode: str = "WATCHDOG_AUTO_AUDIT"):
    """
    Executes an autonomous background Chaos Drill to verify resilience
    and archives findings directly into the permanent Chaos Ledger.
    """
    try:
        import chaos_lab
        log(f"⚔️ [CHAOS SENTINEL] Initiating autonomous drill [{mode}]...")
        audit = chaos_lab.run_chaos_gauntlet(mode=mode)
        score = audit.get("score", 0.0)
        grade = "TITANIUM_GRADE" if score >= 100 else "NEEDS_ATTENTION"
        dur = audit.get("duration_ms", 0.0)
        log(f"🛡️ [CHAOS SENTINEL] Audit Complete: {score:.1f}% [{grade}] in {dur:.1f}ms (Defended {audit.get('defended')}/{audit.get('total')})")
    except Exception as e:
        log(f"⚠️ [CHAOS SENTINEL] Background audit exception: {e}")

def probe_gemini_models():
    """Periodically tests model fleet availability and updates health state."""
    try:
        from self_healing import SelfHealingSentinel
        from google import genai
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not api_key:
            return
        
        client = genai.Client(api_key=api_key)
        test_fleet = ["gemini-3.5-flash", "gemini-3.6-flash", "gemini-3.5-flash-lite"]
        for m in test_fleet:
            try:
                client.models.generate_content(model=m, contents="ping")
                SelfHealingSentinel.record_model_status(m, success=True)
            except Exception as e:
                SelfHealingSentinel.record_model_status(m, success=False, error_msg=str(e)[:100])
    except Exception:
        pass

def probe_edge_sites():
    """Periodically verifies edge availability of production deployed platforms."""
    sites = [
        ("Mohammad Rehan Portfolio", "https://mohammadrehan.pages.dev"),
        ("Maison Ladies Zone", "https://ladieszone.pages.dev")
    ]
    for name, url in sites:
        try:
            r = requests.get(url, timeout=6)
            if r.status_code == 200:
                log(f"🌐 [EDGE SENTINEL] {name} ({url}) -> HTTP 200 OK")
            else:
                log(f"⚠️ [EDGE SENTINEL] {name} ({url}) returned status {r.status_code}")
        except Exception as e:
            log(f"⚠️ [EDGE SENTINEL] Anomaly checking {name}: {e}")

def run_watchdog():
    log(f"Self-Healing Watchdog Engine Active. Monitoring port {PORT}...")
    log(f"⚔️ Phoenix Chaos Sentinel ARMED 24/7. Continuous audits active.")

    # Run boot sentinel verification drill in background
    threading.Thread(target=run_background_chaos_audit, args=("WATCHDOG_BOOT_SENTINEL",), daemon=True).start()

    consecutive_failures = 0
    last_probe_time = 0
    last_edge_probe_time = 0
    last_chaos_audit_time = time.time()

    while True:
        try:
            if not is_service_healthy():
                consecutive_failures += 1
                log(f"Health check failed (attempt {consecutive_failures}/2)")
                if consecutive_failures >= 2:
                    restart_service()
                    consecutive_failures = 0
                    time.sleep(10)
            else:
                consecutive_failures = 0

            now = time.time()

            # Probe Gemini models every 3 minutes
            if now - last_probe_time > 180:
                probe_gemini_models()
                last_probe_time = now

            # Probe production edge sites every 5 minutes (300 seconds)
            if now - last_edge_probe_time > 300:
                threading.Thread(target=probe_edge_sites, daemon=True).start()
                last_edge_probe_time = now

            # Continuous Chaos Sentinel Audit every 1 hour (3600 seconds)
            if now - last_chaos_audit_time > 3600:
                threading.Thread(target=run_background_chaos_audit, args=("WATCHDOG_HOURLY_AUTO",), daemon=True).start()
                last_chaos_audit_time = now

        except Exception as e:
            log(f"Watchdog loop anomaly: {e}")

        time.sleep(CHECK_INTERVAL_SECONDS)

if __name__ == "__main__":
    run_watchdog()
