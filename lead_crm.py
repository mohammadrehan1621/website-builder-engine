import os
import json
import csv
import io
import time
from typing import List, Dict, Any, Optional
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
LEADS_FILE = BASE_DIR / "leads_log.json"

def _ensure_leads_file():
    if not LEADS_FILE.exists():
        initial_data = [
            {
                "id": "lead-sample-01",
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() - 3600 * 24)),
                "name": "Sarah Jenkins",
                "email": "sarah.j@apexretail.co",
                "phone": "+91 98765 43210",
                "budget": "₹25,000",
                "message": "Interested in building a retail inventory software and custom digital showroom for our stores in Patna.",
                "source_page": "contact.html",
                "status": "Qualified"
            },
            {
                "id": "lead-sample-02",
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() - 3600 * 4)),
                "name": "Vikram Malhotra",
                "email": "vikram@finscale.io",
                "phone": "+91 91234 56789",
                "budget": "₹15,000",
                "message": "Saw your portfolio on Cloudflare Pages. Need a high-converting single page landing page for an algorithmic bot launch.",
                "source_page": "index.html",
                "status": "New"
            }
        ]
        try:
            with open(LEADS_FILE, "w", encoding="utf-8") as f:
                json.dump(initial_data, f, indent=2)
        except Exception:
            pass

def get_all_leads() -> List[Dict[str, Any]]:
    """Loads all captured leads from disk."""
    _ensure_leads_file()
    try:
        with open(LEADS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return sorted(data, key=lambda x: x.get("timestamp", ""), reverse=True)
    except Exception:
        return []

def log_new_lead(name: str, email: str, phone: str = "", message: str = "", source_page: str = "index.html", budget: str = "Unspecified") -> Dict[str, Any]:
    """Logs a new incoming client inquiry."""
    _ensure_leads_file()
    leads = get_all_leads()
    new_entry = {
        "id": f"lead-{int(time.time()*1000)}",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "name": name.strip(),
        "email": email.strip(),
        "phone": phone.strip() or "N/A",
        "budget": budget.strip() or "Standard",
        "message": message.strip(),
        "source_page": source_page,
        "status": "New"
    }
    leads.insert(0, new_entry)
    try:
        with open(LEADS_FILE, "w", encoding="utf-8") as f:
            json.dump(leads, f, indent=2)
    except Exception:
        pass
    return new_entry

def export_leads_to_csv() -> str:
    """Exports all leads into CSV string format."""
    leads = get_all_leads()
    if not leads:
        return "ID,Timestamp,Name,Email,Phone,Budget,Message,Source Page,Status\n"

    output = io.StringIO()
    fieldnames = ["id", "timestamp", "name", "email", "phone", "budget", "message", "source_page", "status"]
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    for l in leads:
        writer.writerow({k: l.get(k, "") for k in fieldnames})
    return output.getvalue()

def clear_all_leads():
    """Clears all leads for a fresh slate."""
    try:
        with open(LEADS_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, indent=2)
    except Exception:
        pass
