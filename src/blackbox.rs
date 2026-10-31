// ============================================================================
// REHAN QUANT LAB™ — OFFLINE FLIGHT RECORDER (THE NUCLEUS / BLACK BOX)
// "Zero Cloud Sockets • Air-Gapped Ring Buffer • Immutable Ash Journaling"
// Founder & Principal Systems Architect: Mohammad Rehan
// ============================================================================

use std::fs::{self, OpenOptions};
use std::io::Write;
use std::path::{Path, PathBuf};
use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};
use sha2::{Digest, Sha256};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct FlightFrame {
    pub epoch_timestamp: i64,
    pub iso_time: String,
    pub node_id: String,
    pub vector_action: String,
    pub phase: String, // "CW_FORWARD" | "ACW_REVERSE" | "NUCLEUS_AUDIT"
    pub payload_hash: String,
    pub execution_micros: u64,
    pub status: String,
    pub message: String,
}

pub struct OfflineFlightRecorder {
    wal_path: PathBuf,
    app_data_path: Option<PathBuf>,
}

impl OfflineFlightRecorder {
    pub fn new() -> Self {
        let local_wal = PathBuf::from("flight_recorder.wal");
        
        let app_data = std::env::var("LOCALAPPDATA").ok().map(|base| {
            let p = PathBuf::from(base).join("Rehan_Quant_Lab").join("website_builder");
            let _ = fs::create_dir_all(&p);
            p.join("flight_recorder.wal")
        });

        Self {
            wal_path: local_wal,
            app_data_path: app_data,
        }
    }

    pub fn record(
        &self,
        node_id: &str,
        phase: &str,
        action: &str,
        payload_bytes: &[u8],
        duration_micros: u64,
        status: &str,
        message: &str,
    ) -> FlightFrame {
        let now: DateTime<Utc> = Utc::now();
        let mut hasher = Sha256::new();
        hasher.update(payload_bytes);
        let hash = format!("{:x}", hasher.finalize());

        let frame = FlightFrame {
            epoch_timestamp: now.timestamp_millis(),
            iso_time: now.to_rfc3339(),
            node_id: node_id.to_string(),
            vector_action: action.to_string(),
            phase: phase.to_string(),
            payload_hash: hash,
            execution_micros: duration_micros,
            status: status.to_string(),
            message: message.to_string(),
        };

        if let Ok(line) = serde_json::to_string(&frame) {
            self.append_line(&line);
        }

        frame
    }

    fn append_line(&self, line: &str) {
        let line_with_nl = format!("{}\n", line);

        if let Ok(mut file) = OpenOptions::new().create(true).append(true).open(&self.wal_path) {
            let _ = file.write_all(line_with_nl.as_bytes());
        }

        if let Some(ref ad_path) = self.app_data_path {
            if let Ok(mut file) = OpenOptions::new().create(true).append(true).open(ad_path) {
                let _ = file.write_all(line_with_nl.as_bytes());
            }
        }
    }

    pub fn export_diagnostic_snapshot(&self, out_path: &Path) -> std::io::Result<usize> {
        if !self.wal_path.exists() {
            fs::write(out_path, b"RQL_FLIGHT_RECORDER: EMPTY_LOG_INITIALIZED\n")?;
            return Ok(1);
        }

        let content = fs::read_to_string(&self.wal_path)?;
        let lines: Vec<&str> = content.lines().collect();
        let tail_lines = if lines.len() > 100 {
            &lines[lines.len() - 100..]
        } else {
            &lines[..]
        };

        let mut out = String::new();
        out.push_str("====================================================================\n");
        out.push_str("REHAN QUANT LAB™ — AIR-GAPPED DIAGNOSTIC SNAPSHOT (BLACK BOX EXPORT)\n");
        out.push_str("Zero Cloud Sockets • Pure Offline Telemetry • Sovereign Invariant\n");
        out.push_str("====================================================================\n");
        out.push_str(&format!("Generated: {}\n", Utc::now().to_rfc3339()));
        out.push_str(&format!("Total Frame Records in WAL: {}\n", lines.len()));
        out.push_str("--------------------------------------------------------------------\n");
        for line in tail_lines {
            out.push_str(line);
            out.push('\n');
        }
        out.push_str("====================================================================\n");

        fs::write(out_path, out.as_bytes())?;
        Ok(tail_lines.len())
    }

    pub fn get_recent_frames(&self, count: usize) -> Vec<FlightFrame> {
        if !self.wal_path.exists() {
            return Vec::new();
        }

        if let Ok(content) = fs::read_to_string(&self.wal_path) {
            let mut frames: Vec<FlightFrame> = content
                .lines()
                .filter_map(|l| serde_json::from_str::<FlightFrame>(l).ok())
                .collect();
            let start = frames.len().saturating_sub(count);
            frames.split_off(start)
        } else {
            Vec::new()
        }
    }
}
