import os
import re

site_dir = r"C:\Users\rehan\Desktop\projects\website_builder\Deployed_Websites\mohammadrehan.pages.dev"

files_to_clean = ["index.html", "aegis.html", "projects.html", "experience.html", "contact.html", "legal.html"]

replacements = [
    # General trading terms -> Enterprise systems
    ("Deterministic On-Premises Trading Risk Engine", "Deterministic High-Availability Process Supervisor"),
    ("Deterministic on-premises trading risk engine", "Deterministic high-availability process supervisor"),
    ("trading risk middleware", "high-availability process middleware"),
    ("Trading Risk Middleware", "High-Availability Process Middleware"),
    ("algorithmic trading risk", "distributed systems fault tolerance"),
    ("algorithmic trading engines", "distributed high-performance engines"),
    ("algorithmic trading", "distributed systems engineering"),
    ("algorithmic options execution engines", "high-throughput distributed state engines"),
    ("Systematic Execution Engines", "High-Availability Distributed Systems"),
    ("Systematic options execution", "High-availability process supervision"),
    ("quantitative trading infrastructure", "distributed systems infrastructure"),
    ("quant trading systems", "distributed cloud systems"),
    ("Quantitative Trading Systems Setup", "Enterprise Distributed Systems Architecture"),
    ("Quantitative Systems", "High-Availability Systems"),
    ("Institutional Quantitative Execution", "Enterprise High-Availability Engineering"),
    ("trading alpha, order patterns, and private broker credentials", "system state, operational telemetry, and private enterprise data"),
    ("Cryptographic SHA-256 Trade WAL", "Cryptographic SHA-256 State WAL"),
    ("Every order state transition, execution fill, and cancel", "Every process state transition, task dispatch, and checkpoint"),
    ("power fails mid-trade", "power fails during execution"),
    ("zero orphaned orders", "zero orphaned child processes"),
    ("designated broker API (Zerodha, Interactive Brokers, Dhan, Fyers)", "enterprise microservices and private IPC message queues"),
    ("Supported Broker Ecosystem", "Supported IPC & Microservice Ecosystem"),
    ("Native Broker Connectors", "Native IPC & RPC Connectors"),
    ("Interactive Brokers", "ZeroMQ / gRPC"),
    ("Zerodha Kite", "Unix Domain Sockets"),
    ("Dhan", "Shared Memory (IPC)"),
    ("Fyers", "Named Pipes"),
    ("Zerodha Kite, Interactive Brokers, Dhan & Fyers connectors", "Unix Domain Sockets, gRPC, Named Pipes & Shared Memory IPC"),
    ("RQL AEGIS TRADING RISK MIDDLEWARE", "RQL AEGIS ENTERPRISE PROCESS SUPERVISOR"),
    ("proprietary trading firms, funds, and multi-server institutional quants", "mission-critical enterprise systems, industrial IoT, and distributed infrastructure teams"),
    ("resting orders across all broker wires", "active execution threads across all IPC sockets"),
    ("broker gateways (Kotak Neo Trade API, Binance API, NSE, or BSE)", "third-party APIs, network providers, or cloud gateways"),
    ("Kotak Securities, Binance, etc.", "third-party service providers"),
    ("trading programs", "software systems"),
    ("trading bot", "autonomous daemon"),
    ("Trading Bot", "Autonomous Process Daemon"),
    ("crypto bot", "automation service"),
    ("Crypto Bot", "Automation Service"),
]

for fname in files_to_clean:
    fpath = os.path.join(site_dir, fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    modified = content
    for old, new in replacements:
        modified = modified.replace(old, new)

    if modified != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(modified)
        print(f"Updated {fname}")
    else:
        print(f"No changes needed in {fname}")

print("Clean-up finished successfully!")
