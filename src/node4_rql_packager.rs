// ============================================================================
// REHAN QUANT LAB™ — NODE 4: RQL PACKAGER (PURE RUST NVME FASTENER)
// "The Silicon Fastener — 100% Pure Rust Assembly at NVMe Bus Speed (>1 GB/s)"
// Founder & Principal Systems Architect: Mohammad Rehan
// ============================================================================

use std::fs::{self, File};
use std::io::Write;
use std::path::{Path, PathBuf};
use chrono::Utc;
use serde::{Deserialize, Serialize};
use sha2::{Digest, Sha256};
use zip::write::SimpleFileOptions;
use zip::ZipWriter;

use crate::seo::SeoEngine;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ManifestFileRecord {
    pub path: String,
    pub size_bytes: u64,
    pub sha256_hash: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct WebsiteReleaseManifest {
    pub project_name: String,
    pub generated_at: String,
    pub total_files: usize,
    pub total_size_bytes: u64,
    pub bundle_sha256: String,
    pub files: Vec<ManifestFileRecord>,
}

pub struct RqlPackagerEngine;

impl RqlPackagerEngine {
    /// 🔄 CW: High-Speed NVMe Packaging with Automatic SEO Panopticon Synchronization
    pub fn package_directory(
        source_dir: &Path,
        zip_output_path: &Path,
        manifest_output_path: &Path,
        project_name: &str,
    ) -> std::io::Result<WebsiteReleaseManifest> {
        Self::package_directory_with_domain(source_dir, zip_output_path, manifest_output_path, project_name, "rehanquantlab.com")
    }

    /// 🔄 CW: High-Speed NVMe Packaging with explicit Domain SEO binding
    pub fn package_directory_with_domain(
        source_dir: &Path,
        zip_output_path: &Path,
        manifest_output_path: &Path,
        project_name: &str,
        domain: &str,
    ) -> std::io::Result<WebsiteReleaseManifest> {
        // 1. Invariant: Auto-enrich all pages with Schema.org JSON-LD structured data
        let _ = crate::schema::SchemaEngine::enrich_directory_with_schemas(source_dir, domain);

        // 2. Invariant: Auto-generate/update sitemap.xml, robots.txt, and SEO report before packaging
        let _ = SeoEngine::execute_panopticon_suite(source_dir, domain);

        let zip_file = File::create(zip_output_path)?;
        let mut zip_writer = ZipWriter::new(zip_file);
        let options = SimpleFileOptions::default()
            .compression_method(zip::CompressionMethod::Deflated)
            .unix_permissions(0o755);

        let mut manifest_records = Vec::new();
        let mut total_bytes = 0u64;

        let mut file_list = Vec::new();
        Self::collect_files_recursive(source_dir, source_dir, &mut file_list)?;

        // Sort files for deterministic, bit-exact reproducible archives
        file_list.sort_by(|a, b| a.0.cmp(&b.0));

        for (rel_path_str, abs_path) in file_list {
            let bytes = fs::read(&abs_path)?;
            let file_len = bytes.len() as u64;
            total_bytes += file_len;

            // Compute SHA-256
            let mut hasher = Sha256::new();
            hasher.update(&bytes);
            let sha = format!("{:x}", hasher.finalize());

            manifest_records.push(ManifestFileRecord {
                path: rel_path_str.clone(),
                size_bytes: file_len,
                sha256_hash: sha,
            });

            // Write into zip
            zip_writer.start_file(&rel_path_str, options)?;
            zip_writer.write_all(&bytes)?;
        }

        zip_writer.finish()?;

        // Compute SHA-256 of the resulting ZIP
        let zip_bytes = fs::read(zip_output_path)?;
        let mut zip_hasher = Sha256::new();
        zip_hasher.update(&zip_bytes);
        let bundle_sha = format!("{:x}", zip_hasher.finalize());

        let manifest = WebsiteReleaseManifest {
            project_name: project_name.to_string(),
            generated_at: Utc::now().to_rfc3339(),
            total_files: manifest_records.len(),
            total_size_bytes: total_bytes,
            bundle_sha256: bundle_sha,
            files: manifest_records,
        };

        let manifest_json = serde_json::to_string_pretty(&manifest)?;
        fs::write(manifest_output_path, manifest_json.as_bytes())?;

        Ok(manifest)
    }

    /// 🔁 ACW: Reverse Manifest Verification
    /// Reads the compiled archive/directory and verifies byte-for-byte fidelity against manifest.
    pub fn verify_manifest_integrity(
        source_dir: &Path,
        manifest_path: &Path,
    ) -> std::io::Result<(bool, Vec<String>)> {
        if !manifest_path.exists() {
            return Ok((false, vec!["Manifest file does not exist on disk".to_string()]));
        }

        let manifest_str = fs::read_to_string(manifest_path)?;
        let manifest: WebsiteReleaseManifest = serde_json::from_str(&manifest_str)?;

        let mut errors = Vec::new();

        for record in manifest.files {
            let file_path = source_dir.join(&record.path);
            if !file_path.exists() {
                errors.push(format!("Missing file declared in manifest: {}", record.path));
                continue;
            }

            let bytes = fs::read(&file_path)?;
            if bytes.len() as u64 != record.size_bytes {
                errors.push(format!(
                    "File size mismatch on {}: expected {} bytes, found {}",
                    record.path, record.size_bytes, bytes.len()
                ));
                continue;
            }

            let mut hasher = Sha256::new();
            hasher.update(&bytes);
            let current_hash = format!("{:x}", hasher.finalize());

            if current_hash != record.sha256_hash {
                errors.push(format!(
                    "SHA-256 hash drift on {}: expected {}, found {}",
                    record.path, record.sha256_hash, current_hash
                ));
            }
        }

        let is_intact = errors.is_empty();
        Ok((is_intact, errors))
    }

    fn collect_files_recursive(
        root: &Path,
        current: &Path,
        file_list: &mut Vec<(String, PathBuf)>,
    ) -> std::io::Result<()> {
        if current.is_dir() {
            for entry in fs::read_dir(current)? {
                let entry = entry?;
                let path = entry.path();
                let fname = path.file_name().unwrap_or_default().to_string_lossy();

                // Skip output bundle, git directory, and manifest itself to prevent circular hashing
                if fname == "website_bundle.zip" 
                    || fname == "RQL_WEBSITE_MANIFEST.json" 
                    || fname == ".git" 
                    || fname == ".wrangler" 
                    || fname.ends_with(".tmp") {
                    continue;
                }

                if path.is_dir() {
                    Self::collect_files_recursive(root, &path, file_list)?;
                } else if path.is_file() {
                    let rel = path.strip_prefix(root).map_err(|e| {
                        std::io::Error::new(std::io::ErrorKind::Other, e.to_string())
                    })?;
                    let rel_str = rel.to_string_lossy().replace('\\', "/");
                    file_list.push((rel_str, path));
                }
            }
        }
        Ok(())
    }
}
