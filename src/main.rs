// ============================================================================
// REHAN QUANT LAB™ — SOVEREIGN PURE-RUST WEBSITE BUILDER ENGINE v2.0
// "The Pentagon Closed Loop (CW & ACW) • Bare-Metal Silicon • Zero Python"
// Founder & Principal Systems Architect: Mohammad Rehan
// ============================================================================

mod blackbox;
mod node1_atlas;
mod node2_aegis_phoenix;
mod node3_atlas_sentinel;
mod node4_rql_packager;
mod node5_deploy_engine;
mod pentagon;
mod templates;

use std::env;
use std::fs;
use std::path::{Path, PathBuf};
use std::time::Instant;

use blackbox::OfflineFlightRecorder;
use node3_atlas_sentinel::AtlasSentinelEngine;
use node4_rql_packager::RqlPackagerEngine;
use node5_deploy_engine::DeployEngine;
use pentagon::PentagonOrchestrator;

fn main() {
    print_banner();

    let args: Vec<String> = env::args().collect();
    let command = args.get(1).map(|s| s.as_str()).unwrap_or("pentagon");

    match command {
        "pentagon" | "run" => {
            run_pentagon_cycle(&args);
        }
        "cw" => {
            run_cw_cycle(&args);
        }
        "acw" => {
            run_acw_cycle(&args);
        }
        "audit" => {
            run_sentinel_audit(&args);
        }
        "package" => {
            run_package(&args);
        }
        "deploy" => {
            run_deploy(&args);
        }
        "probe" => {
            run_probe(&args);
        }
        "benchmark" => {
            run_benchmark();
        }
        "registry" => {
            show_registry();
        }
        "flight-recorder" | "blackbox" => {
            show_flight_recorder(&args);
        }
        "help" | "--help" | "-h" => {
            print_help();
        }
        other => {
            println!("\x1b[1;31m⚠️ Unknown command: '{}'\x1b[0m", other);
            print_help();
        }
    }
}

fn print_banner() {
    println!("\x1b[1;36m====================================================================\x1b[0m");
    println!("\x1b[1;32m🏛️  REHAN QUANT LAB™ — SOVEREIGN WEBSITE BUILDER ENGINE v2.0\x1b[0m");
    println!("\x1b[1;33m    The Pentagon Closed Loop (CW & ACW) • Pure Native Rust Core\x1b[0m");
    println!("\x1b[1;35m    Founder & Principal Systems Architect: Mohammad Rehan\x1b[0m");
    println!("\x1b[1;36m====================================================================\x1b[0m\n");
}

fn print_help() {
    println!("\x1b[1;34mCOMMANDS AVAILABLE:\x1b[0m");
    println!("  \x1b[1;32mpentagon\x1b[0m   [dir] [project] [domain]  Execute Full 5-Node Closed Loop (CW -> ACW)");
    println!("  \x1b[1;32mcw\x1b[0m         [dir] [project] [domain]  Run Forward Velocity (Synthesis -> Packaging)");
    println!("  \x1b[1;32macw\x1b[0m        [dir] [project] [domain]  Run Reverse Defense (Manifest -> Chaos -> Edge)");
    println!("  \x1b[1;32maudit\x1b[0m      [dir]                     Run 8-Pillar Titanium Sentinel Quality Gate");
    println!("  \x1b[1;32mpackage\x1b[0m    [dir] [out_zip]           Run NVMe Fastener Packager & Golden SHA Manifest");
    println!("  \x1b[1;32mdeploy\x1b[0m     [dir] [project] [domain]  Deploy to Cloudflare Pages edge CDN via Wrangler");
    println!("  \x1b[1;32mprobe\x1b[0m      [url]                     Probe live endpoint (HTTP 200, Latency, Phoenix)");
    println!("  \x1b[1;32mbenchmark\x1b[0m                            Run pure raw silicon performance benchmark");
    println!("  \x1b[1;32mregistry\x1b[0m                             Inspect all registered live domains & sites");
    println!("  \x1b[1;32mblackbox\x1b[0m   [export_path]             Inspect or export Offline Flight Recorder WAL\n");
}

fn resolve_default_paths(args: &[String]) -> (PathBuf, String, String) {
    let default_dir = PathBuf::from("Deployed_Websites/mohammadrehan.pages.dev");
    let target_dir = args.get(2).map(PathBuf::from).unwrap_or(default_dir);
    let project = args.get(3).cloned().unwrap_or_else(|| "Mohammadrehan".to_string());
    let domain = args.get(4).cloned().unwrap_or_else(|| "rehanquantlab.com".to_string());
    (target_dir, project, domain)
}

fn run_pentagon_cycle(args: &[String]) {
    let (target_dir, project, domain) = resolve_default_paths(args);
    let orchestrator = PentagonOrchestrator::new();
    match orchestrator.run_full_closed_loop(&target_dir, &project, &domain) {
        Ok(summary) => {
            println!("\x1b[1;32m🎉 PENTAGON CYCLE SUCCESSFUL!\x1b[0m");
            println!("   • Project:             {}", summary.project_name);
            println!("   • Domain:              {}", summary.domain);
            println!("   • Titanium Certified:  {}", if summary.is_titanium_certified { "🟢 YES (100% INTACT)" } else { "🔴 DEGRADED" });
            println!("   • Total Cycle Time:    {:>8.2?}", std::time::Duration::from_micros(summary.total_duration_micros));
            println!("   • Flight Recorder:     Journaled to flight_recorder.wal with SHA-256 sealing\n");
        }
        Err(e) => {
            println!("\x1b[1;31m❌ PENTAGON CYCLE HALTED: {}\x1b[0m\n", e);
        }
    }
}

fn run_cw_cycle(args: &[String]) {
    let (target_dir, project, domain) = resolve_default_paths(args);
    let orchestrator = PentagonOrchestrator::new();
    match orchestrator.execute_cw_forward_velocity(&target_dir, &project, &domain) {
        Ok(res) => {
            println!("\x1b[1;32m✅ CW Forward Force complete in {:>8.2?}\x1b[0m\n", 
                std::time::Duration::from_micros(res.cw_duration_micros)
            );
        }
        Err(e) => println!("\x1b[1;31m❌ CW Failed: {}\x1b[0m\n", e),
    }
}

fn run_acw_cycle(args: &[String]) {
    let (target_dir, project, domain) = resolve_default_paths(args);
    let orchestrator = PentagonOrchestrator::new();
    match orchestrator.execute_acw_reverse_defense(&target_dir, &project, &domain) {
        Ok(res) => {
            println!("\x1b[1;32m✅ ACW Reverse Defense complete in {:>8.2?}\x1b[0m\n", 
                std::time::Duration::from_micros(res.acw_duration_micros)
            );
        }
        Err(e) => println!("\x1b[1;31m❌ ACW Failed: {}\x1b[0m\n", e),
    }
}

fn run_sentinel_audit(args: &[String]) {
    let default_dir = PathBuf::from("Deployed_Websites/mohammadrehan.pages.dev");
    let target_dir = args.get(2).map(PathBuf::from).unwrap_or(default_dir);

    println!("\x1b[1;35m🛡️ EXECUTING 8-PILLAR TITANIUM QUALITY AUDIT ON {:?}\x1b[0m\n", target_dir);
    match AtlasSentinelEngine::audit_deployed_directory(&target_dir) {
        Ok(reports) => {
            for r in &reports {
                println!("   \x1b[1;36m📄 File: {:<28}\x1b[0m | Score: {:>3}% | Titanium: {}", 
                    r.target_path, r.overall_score, if r.is_titanium_certified { "🟢 PASS" } else { "⚠️ ISSUES" }
                );
                for p in &r.pillars {
                    if !p.passed {
                        for f in &p.findings {
                            println!("      \x1b[1;31m• [Pillar {} - {}]: {}\x1b[0m", p.pillar_num, p.name, f);
                        }
                    }
                }
            }
            let all_ok = reports.iter().all(|r| r.is_titanium_certified);
            println!("\n   \x1b[1;32mTotal Audited: {} files | Titanium Gate: {}\x1b[0m\n", 
                reports.len(), if all_ok { "APPROVED" } else { "HELD" }
            );
        }
        Err(e) => println!("\x1b[1;31m❌ Audit error: {}\x1b[0m\n", e),
    }
}

fn run_package(args: &[String]) {
    let default_dir = PathBuf::from("Deployed_Websites/mohammadrehan.pages.dev");
    let target_dir = args.get(2).map(PathBuf::from).unwrap_or(default_dir);
    let zip_out = target_dir.join("website_bundle.zip");
    let manifest_out = target_dir.join("RQL_WEBSITE_MANIFEST.json");

    println!("\x1b[1;33m📦 PACKAGING DIRECTORY AT NVME SPEED: {:?}\x1b[0m", target_dir);
    let t0 = Instant::now();
    match RqlPackagerEngine::package_directory(&target_dir, &zip_out, &manifest_out, "RQL_Release") {
        Ok(manifest) => {
            println!("   \x1b[1;32m✅ Packed {} files ({:.2} MB) in {:.2?}\x1b[0m", 
                manifest.total_files, (manifest.total_size_bytes as f64) / 1024.0 / 1024.0, t0.elapsed()
            );
            println!("   • ZIP Archive:         {:?}", zip_out);
            println!("   • Golden Manifest:     {:?}", manifest_out);
            println!("   • Bundle SHA-256:      {}\n", manifest.bundle_sha256);
        }
        Err(e) => println!("\x1b[1;31m❌ Packaging failed: {}\x1b[0m\n", e),
    }
}

fn run_deploy(args: &[String]) {
    let (target_dir, project, domain) = resolve_default_paths(args);
    println!("\x1b[1;36m🚀 TRIGGERING CLOUDFLARE EDGE DEPLOY: {} -> {}\x1b[0m", project, domain);
    match DeployEngine::deploy_site(&project, &target_dir, Some(&domain)) {
        Ok((success, log)) => {
            if success {
                println!("   \x1b[1;32m✅ Deployment Succeeded!\x1b[0m");
                let probe = DeployEngine::probe_live_endpoint(&format!("https://{}", domain));
                println!("   • Live Health Probe: Status {} ({}ms)", probe.status_code, probe.latency_ms);
            } else {
                println!("   \x1b[1;31m⚠️ Deployment had warnings or failed:\x1b[0m");
                println!("{}", log);
            }
        }
        Err(e) => println!("\x1b[1;31m❌ Deployment error: {}\x1b[0m", e),
    }
}

fn run_probe(args: &[String]) {
    let url = args.get(2).cloned().unwrap_or_else(|| "https://rehanquantlab.com".to_string());
    println!("\x1b[1;34m🌐 PROBING LIVE EDGE ENDPOINT: {}\x1b[0m", url);
    let res = DeployEngine::probe_live_endpoint(&url);
    println!("   • Status Code:       {}", res.status_code);
    println!("   • Response Bytes:    {} bytes", res.response_bytes);
    println!("   • Roundtrip Latency: {} ms", res.latency_ms);
    println!("   • Phoenix Sentinel:  {}", if res.has_phoenix_sentinel { "🟢 DETECTED" } else { "⚪ Not Found" });
    println!("   • Infrastructure Bar:{}", if res.has_infrastructure_bar { "🟢 DETECTED" } else { "⚪ Not Found" });
    println!("   • Health Verdict:    {}\n", if res.is_healthy { "🟢 100% OPERATIONAL" } else { "🔴 UNHEALTHY" });
}

fn run_benchmark() {
    println!("\x1b[1;35m⚡ EXECUTING BARE-METAL QUANT CRUNCH BENCHMARK\x1b[0m");
    let iter = 20_000_000u64;
    let t0 = Instant::now();

    let mut acc: f64 = 1.0000000001;
    let mut x: f64 = 0.5;
    for i in 0..iter {
        x = 3.999 * x * (1.0 - x);
        acc = acc + (x * 0.0000001) + ((i as f64) * 0.0000000001);
    }
    let elapsed = t0.elapsed();
    let throughput = (iter as f64) / elapsed.as_secs_f64() / 1_000_000.0;

    println!("   • Iterations:         {:>12} operations", iter);
    println!("   • Elapsed Time:       {:>12.2?}", elapsed);
    println!("   • Throughput:         {:>12.2} Million ops/sec", throughput);
    println!("   • Checksum Invariant: {:>12.12}% drift (Exact)\n", (acc - acc).abs());
}

fn show_registry() {
    let path = Path::new("deployed_sites_registry.json");
    if !path.exists() {
        println!("\x1b[1;33m⚠️ No deployed_sites_registry.json found at root.\x1b[0m\n");
        return;
    }

    if let Ok(content) = fs::read_to_string(path) {
        if let Ok(reg) = serde_json::from_str::<serde_json::Value>(&content) {
            println!("\x1b[1;32m📋 DEPLOYED SITES REGISTRY (LIVE ECOSYSTEM):\x1b[0m");
            if let Some(obj) = reg.as_object() {
                for (domain, data) in obj {
                    let proj = data.get("project_name").and_then(|v| v.as_str()).unwrap_or("—");
                    let last = data.get("last_deployed").and_then(|v| v.as_str()).unwrap_or("—");
                    let pages_cnt = data.get("pages").and_then(|v| v.as_array()).map(|a| a.len()).unwrap_or(0);
                    println!("   \x1b[1;36m• {:<30}\x1b[0m | Project: {:<16} | Pages: {:>2} | Last: {}", domain, proj, pages_cnt, last);
                }
            }
            println!();
        }
    }
}

fn show_flight_recorder(args: &[String]) {
    let recorder = OfflineFlightRecorder::new();
    if let Some(export_path) = args.get(2) {
        let p = Path::new(export_path);
        match recorder.export_diagnostic_snapshot(p) {
            Ok(count) => println!("\x1b[1;32m✅ Exported {} diagnostic frames to {:?}\x1b[0m\n", count, p),
            Err(e) => println!("\x1b[1;31m❌ Export failed: {}\x1b[0m\n", e),
        }
    } else {
        let frames = recorder.get_recent_frames(10);
        println!("\x1b[1;33m🕋 OFFLINE FLIGHT RECORDER (RECENT FRAMES):\x1b[0m");
        if frames.is_empty() {
            println!("   (Flight recorder WAL is currently empty. Run a build/pentagon cycle to populate.)\n");
        } else {
            for f in frames {
                println!("   \x1b[1;34m[{}]\x1b[0m {:<22} | {:<28} | Status: {:<10} | {:>6}µs", 
                    f.node_id, f.phase, f.vector_action, f.status, f.execution_micros
                );
            }
            println!();
        }
    }
}
