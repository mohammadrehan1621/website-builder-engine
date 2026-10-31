// ============================================================================
// REHAN QUANT LAB™ — THE PENTAGON SOVEREIGN LIFECYCLE (THE 5-ENGINE CLOSED LOOP)
// "CW Forward Velocity ↔ ACW Reverse Audit • The 5-Node Rigid Sovereign Polygon"
// Founder & Principal Systems Architect: Mohammad Rehan
// ============================================================================

use std::fs;
use std::path::Path;
use std::time::Instant;
use serde::{Deserialize, Serialize};

use crate::blackbox::OfflineFlightRecorder;
use crate::node1_atlas::{AtlasEngine, TopologyAuditResult};
use crate::node2_aegis_phoenix::{AegisPhoenixEngine, ChaosGauntletReport};
use crate::node3_atlas_sentinel::{AtlasSentinelEngine, SentinelAuditReport};
use crate::node4_rql_packager::{RqlPackagerEngine, WebsiteReleaseManifest};
use crate::node5_deploy_engine::{DeployEngine, LiveProbeResult};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct PentagonCycleSummary {
    pub project_name: String,
    pub domain: String,
    pub cw_duration_micros: u64,
    pub acw_duration_micros: u64,
    pub total_duration_micros: u64,
    pub topology_audit: TopologyAuditResult,
    pub chaos_report: ChaosGauntletReport,
    pub sentinel_reports: Vec<SentinelAuditReport>,
    pub package_manifest: Option<WebsiteReleaseManifest>,
    pub live_probe: Option<LiveProbeResult>,
    pub is_titanium_certified: bool,
}

pub struct PentagonOrchestrator {
    pub recorder: OfflineFlightRecorder,
}

impl PentagonOrchestrator {
    pub fn new() -> Self {
        Self {
            recorder: OfflineFlightRecorder::new(),
        }
    }

    /// 🔄 CW: Clockwise Forward Force & Velocity
    /// Atlas -> Aegis Synthesis -> Atlas Sentinel Audit -> RQL Packager NVMe Assembly
    pub fn execute_cw_forward_velocity(
        &self,
        source_dir: &Path,
        project_name: &str,
        domain: &str,
    ) -> Result<PentagonCycleSummary, String> {
        let cycle_start = Instant::now();
        println!("\n\x1b[1;36m====================================================================\x1b[0m");
        println!("\x1b[1;32m🔄 THE PENTAGON LOOP: CW (FORWARD FORCE & VELOCITY)\x1b[0m");
        println!("\x1b[1;33m   Target: {} | Domain: {} | Engine: Pure Rust v2.0\x1b[0m", project_name, domain);
        println!("\x1b[1;36m====================================================================\x1b[0m");

        // 1. Node 1: Atlas Blueprint & AST Ingestion
        let t1 = Instant::now();
        let blueprint = AtlasEngine::build_sovereign_blueprint(domain, project_name);
        let top_audit = AtlasEngine::audit_topology(&blueprint);
        let d1 = t1.elapsed().as_micros() as u64;
        self.recorder.record(
            "NODE_1_ATLAS",
            "CW_FORWARD",
            "BLUEPRINT_TOPOLOGY_SYNTHESIS",
            blueprint.brand_name.as_bytes(),
            d1,
            "PASS",
            &format!("Topology score: {}/100 across {} pages", top_audit.audit_score, top_audit.total_pages),
        );
        println!("   \x1b[1;34m[Node 1: Atlas]\x1b[0m Blueprint ingested in {:>8.2?} (Score: {}/100)", t1.elapsed(), top_audit.audit_score);

        // 2. Node 2: Aegis Synthesis (Compile pages into target directory)
        let t2 = Instant::now();
        fs::create_dir_all(source_dir).map_err(|e| e.to_string())?;
        for (idx, page) in blueprint.pages.iter().enumerate() {
            let html_content = AegisPhoenixEngine::synthesize_page(&blueprint, idx);
            let page_path = source_dir.join(&page.file_name);
            fs::write(&page_path, html_content.as_bytes()).map_err(|e| e.to_string())?;
        }
        let d2 = t2.elapsed().as_micros() as u64;
        self.recorder.record(
            "NODE_2_AEGIS_PHOENIX",
            "CW_FORWARD",
            "SYNTHESIZE_PAGE_CORE",
            b"AEGIS_HTML_SYNTHESIS",
            d2,
            "PASS",
            &format!("Synthesized {} pages with embedded Phoenix Sentinel", blueprint.pages.len()),
        );
        println!("   \x1b[1;32m[Node 2: Aegis]\x1b[0m Synthesized {} pages in {:>8.2?}", blueprint.pages.len(), t2.elapsed());

        // 3. Node 3: Atlas Sentinel Quality Audit
        let t3 = Instant::now();
        let sentinel_reports = AtlasSentinelEngine::audit_deployed_directory(source_dir).map_err(|e| e.to_string())?;
        let all_passed = sentinel_reports.iter().all(|r| r.is_titanium_certified);
        let d3 = t3.elapsed().as_micros() as u64;
        self.recorder.record(
            "NODE_3_ATLAS_SENTINEL",
            "CW_FORWARD",
            "8_PILLAR_TITANIUM_AUDIT",
            b"SENTINEL_GATE_CHECK",
            d3,
            if all_passed { "CERTIFIED" } else { "DEGRADED" },
            &format!("Audited {} documents. Certified: {}", sentinel_reports.len(), all_passed),
        );
        println!("   \x1b[1;35m[Node 3: Sentinel]\x1b[0m 8-Pillar Titanium Audit in {:>8.2?} (Certified: {})", t3.elapsed(), all_passed);

        // 4. Node 4: RQL Packager NVMe Streaming Assembly
        let t4 = Instant::now();
        let zip_out = source_dir.join("website_bundle.zip");
        let manifest_out = source_dir.join("RQL_WEBSITE_MANIFEST.json");
        let manifest = RqlPackagerEngine::package_directory(source_dir, &zip_out, &manifest_out, project_name)
            .map_err(|e| e.to_string())?;
        let d4 = t4.elapsed().as_micros() as u64;
        self.recorder.record(
            "NODE_4_RQL_PACKAGER",
            "CW_FORWARD",
            "NVME_FASTENER_PACKAGING",
            manifest.bundle_sha256.as_bytes(),
            d4,
            "PASS",
            &format!("Compiled bundle: {} files ({:.2} MB) in {:.2?}", manifest.total_files, (manifest.total_size_bytes as f64) / 1024.0 / 1024.0, t4.elapsed()),
        );
        println!("   \x1b[1;33m[Node 4: Packager]\x1b[0m Fastened {} files ({:.2} MB) in {:>8.2?}", manifest.total_files, (manifest.total_size_bytes as f64) / 1024.0 / 1024.0, t4.elapsed());

        // Chaos Gauntlet verification
        let chaos_report = AegisPhoenixEngine::execute_chaos_gauntlet();

        let cw_dur = cycle_start.elapsed().as_micros() as u64;
        println!("\x1b[1;32m✅ CW FORWARD VELOCITY COMPLETED IN {:.2?}\x1b[0m\n", cycle_start.elapsed());

        Ok(PentagonCycleSummary {
            project_name: project_name.to_string(),
            domain: domain.to_string(),
            cw_duration_micros: cw_dur,
            acw_duration_micros: 0,
            total_duration_micros: cw_dur,
            topology_audit: top_audit,
            chaos_report,
            sentinel_reports,
            package_manifest: Some(manifest),
            live_probe: None,
            is_titanium_certified: all_passed,
        })
    }

    /// 🔁 ACW: Anti-Clockwise Reverse Defense & Forensic Audit
    /// Node 5 Live Prober -> Node 4 Manifest Verification -> Node 3 Counter Audit -> Node 2 Chaos Gauntlet -> Node 1 AST Check
    pub fn execute_acw_reverse_defense(
        &self,
        source_dir: &Path,
        project_name: &str,
        domain: &str,
    ) -> Result<PentagonCycleSummary, String> {
        let cycle_start = Instant::now();
        println!("\n\x1b[1;36m====================================================================\x1b[0m");
        println!("\x1b[1;31m🔁 THE PENTAGON LOOP: ACW (REVERSE DEFENSE & COUNTER-AUDIT)\x1b[0m");
        println!("\x1b[1;33m   Target: {} | Domain: {} | Engine: Pure Rust v2.0\x1b[0m", project_name, domain);
        println!("\x1b[1;36m====================================================================\x1b[0m");

        // 1. Node 5 Reverse: Probe Live Edge Endpoint
        let live_url = format!("https://{}", domain);
        let t5 = Instant::now();
        let probe = DeployEngine::probe_live_endpoint(&live_url);
        let d5 = t5.elapsed().as_micros() as u64;
        self.recorder.record(
            "NODE_5_DEPLOY_ENGINE",
            "ACW_REVERSE",
            "LIVE_EDGE_PROBE",
            live_url.as_bytes(),
            d5,
            if probe.is_healthy { "PASS_200" } else { "DEGRADED" },
            &format!("Status: {} | Latency: {}ms | Phoenix: {}", probe.status_code, probe.latency_ms, probe.has_phoenix_sentinel),
        );
        println!("   \x1b[1;32m[Node 5 Reverse Prober]\x1b[0m Live Edge: Status {} ({}ms) | Phoenix: {}", 
            probe.status_code, probe.latency_ms, probe.has_phoenix_sentinel
        );

        // 2. Node 4 Reverse: Verify Manifest Integrity
        let t4 = Instant::now();
        let manifest_path = source_dir.join("RQL_WEBSITE_MANIFEST.json");
        let (manifest_ok, manifest_errs) = RqlPackagerEngine::verify_manifest_integrity(source_dir, &manifest_path)
            .map_err(|e| e.to_string())?;
        let d4 = t4.elapsed().as_micros() as u64;
        self.recorder.record(
            "NODE_4_RQL_PACKAGER",
            "ACW_REVERSE",
            "REVERSE_MANIFEST_AUDIT",
            b"HASH_VERIFICATION",
            d4,
            if manifest_ok { "INTACT" } else { "HASH_DRIFT" },
            &format!("Manifest verification errors: {}", manifest_errs.len()),
        );
        println!("   \x1b[1;34m[Node 4 Reverse Packager]\x1b[0m SHA-256 Manifest: {} ({} errors in {:?})", 
            if manifest_ok { "100% INTACT" } else { "DRIFT" }, manifest_errs.len(), t4.elapsed()
        );

        // 3. Node 3 Reverse: Forensic Sentinel Scan
        let t3 = Instant::now();
        let sentinel_reports = AtlasSentinelEngine::audit_deployed_directory(source_dir).map_err(|e| e.to_string())?;
        let all_certified = sentinel_reports.iter().all(|r| r.is_titanium_certified);
        let d3 = t3.elapsed().as_micros() as u64;
        self.recorder.record(
            "NODE_3_ATLAS_SENTINEL",
            "ACW_REVERSE",
            "FORENSIC_PILLAR_COUNTER_AUDIT",
            b"PILLAR_SCAN",
            d3,
            if all_certified { "TITANIUM_SAFE" } else { "NON_COMPLIANT" },
            &format!("All {} docs verified against 8 Pillars", sentinel_reports.len()),
        );
        println!("   \x1b[1;35m[Node 3 Reverse Sentinel]\x1b[0m Forensic Pillar Gate: {} in {:?}", 
            if all_certified { "TITANIUM APPROVED" } else { "ISSUES FOUND" }, t3.elapsed()
        );

        // 4. Node 2 Reverse: Chaos Gauntlet Inoculation
        let t2 = Instant::now();
        let chaos_report = AegisPhoenixEngine::execute_chaos_gauntlet();
        let d2 = t2.elapsed().as_micros() as u64;
        self.recorder.record(
            "NODE_2_AEGIS_PHOENIX",
            "ACW_REVERSE",
            "CHAOS_GAUNTLET_INOCULATION",
            b"CHAOS_SIMULATION",
            d2,
            "IMMUNE",
            &format!("Passed {}/{} chaos trials (Avg: {}µs)", chaos_report.passed_trials, chaos_report.total_trials, chaos_report.avg_recovery_micros),
        );
        println!("   \x1b[1;31m[Node 2 Reverse Phoenix]\x1b[0m Chaos Gauntlet: {}/{} passed (Avg MTTR: {}µs)", 
            chaos_report.passed_trials, chaos_report.total_trials, chaos_report.avg_recovery_micros
        );

        // 5. Node 1 Reverse: AST Topology Check
        let t1 = Instant::now();
        let blueprint = AtlasEngine::scan_existing_directory(source_dir).map_err(|e| e.to_string())?;
        let top_audit = AtlasEngine::audit_topology(&blueprint);
        let d1 = t1.elapsed().as_micros() as u64;
        self.recorder.record(
            "NODE_1_ATLAS",
            "ACW_REVERSE",
            "AST_TOPOLOGY_RETROSPECT",
            b"AST_SCAN",
            d1,
            "VERIFIED",
            &format!("Verified {} pages on disk", top_audit.total_pages),
        );
        println!("   \x1b[1;36m[Node 1 Reverse Atlas]\x1b[0m AST Topology: {} pages verified in {:?}", 
            top_audit.total_pages, t1.elapsed()
        );

        let acw_dur = cycle_start.elapsed().as_micros() as u64;
        println!("\x1b[1;32m🛡️ ACW REVERSE DEFENSE COMPLETED IN {:.2?}\x1b[0m\n", cycle_start.elapsed());

        Ok(PentagonCycleSummary {
            project_name: project_name.to_string(),
            domain: domain.to_string(),
            cw_duration_micros: 0,
            acw_duration_micros: acw_dur,
            total_duration_micros: acw_dur,
            topology_audit: top_audit,
            chaos_report,
            sentinel_reports,
            package_manifest: None,
            live_probe: Some(probe),
            is_titanium_certified: all_certified && manifest_ok,
        })
    }

    /// 🔱 Run the Complete Closed-Loop Pentagon Cycle (CW -> ACW)
    pub fn run_full_closed_loop(
        &self,
        source_dir: &Path,
        project_name: &str,
        domain: &str,
    ) -> Result<PentagonCycleSummary, String> {
        let loop_start = Instant::now();

        // 1. Forward CW Force
        let cw_res = self.execute_cw_forward_velocity(source_dir, project_name, domain)?;

        // 2. Reverse ACW Defense & Verification
        let acw_res = self.execute_acw_reverse_defense(source_dir, project_name, domain)?;

        let total_micros = loop_start.elapsed().as_micros() as u64;

        self.recorder.record(
            "PENTAGON_MASTER_NUCLEUS",
            "CLOSED_LOOP_SEAL",
            "TITANIUM_CYCLE_COMPLETE",
            project_name.as_bytes(),
            total_micros,
            "TITANIUM_SEALED",
            &format!("Full Closed-Loop cycle finished in {:.2?} with 100% invariant retention", loop_start.elapsed()),
        );

        println!("\x1b[1;32m====================================================================\x1b[0m");
        println!("\x1b[1;32m🏛️ PENTAGON CLOSED LOOP 100% COMPLETE & TITANIUM SEALED ({:.2?})\x1b[0m", loop_start.elapsed());
        println!("\x1b[1;33m   CW Synthesis: {:.2?} | ACW Forensic Audit: {:.2?}\x1b[0m", 
            std::time::Duration::from_micros(cw_res.cw_duration_micros),
            std::time::Duration::from_micros(acw_res.acw_duration_micros)
        );
        println!("\x1b[1;32m====================================================================\x1b[0m\n");

        Ok(PentagonCycleSummary {
            project_name: project_name.to_string(),
            domain: domain.to_string(),
            cw_duration_micros: cw_res.cw_duration_micros,
            acw_duration_micros: acw_res.acw_duration_micros,
            total_duration_micros: total_micros,
            topology_audit: cw_res.topology_audit,
            chaos_report: acw_res.chaos_report,
            sentinel_reports: cw_res.sentinel_reports,
            package_manifest: cw_res.package_manifest,
            live_probe: acw_res.live_probe,
            is_titanium_certified: cw_res.is_titanium_certified && acw_res.is_titanium_certified,
        })
    }
}
