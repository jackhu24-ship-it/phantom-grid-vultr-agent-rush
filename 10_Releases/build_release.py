#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHANToM GRID :: Release Packager for Vultr Agent Rush Hackathon
Office 3 Commander Xiao-Ma & Office 1 Pioneer Xiao-Ke
"""
import os
import sys
import json
import zipfile
import hashlib

def compute_sha256(filepath: str) -> str:
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()

def build_package():
    releases_dir = os.path.dirname(os.path.abspath(__file__))
    tourney_dir = os.path.abspath(os.path.join(releases_dir, ".."))
    archive_path = os.path.join(releases_dir, "phantom_grid_vultr_release_v1.0.0.zip")
    manifest_path = os.path.join(releases_dir, "RELEASE_MANIFEST.json")

    drawers = [
        "01_Specs",
        "02_SourceCode",
        "03_CoverImage_16x9",
        "04_Slides_PDF",
        "05_DemoVideo_1440P",
        "06_Deploy_and_Sandbox",
        "07_SubmissionPackage",
        "08_AuditReceipts",
        "09_ChaosReports",
        "10_Releases"
    ]

    print(f">> Packaging release archive: {archive_path}")
    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        # Add root manifests
        for root_file in ["README.md", "match_manifest.yaml"]:
            fp = os.path.join(tourney_dir, root_file)
            if os.path.exists(fp):
                zipf.write(fp, arcname=root_file)

        # Add drawers
        for drawer in drawers:
            drawer_dir = os.path.join(tourney_dir, drawer)
            if not os.path.exists(drawer_dir):
                continue
            for root, dirs, files in os.walk(drawer_dir):
                dirs[:] = [d for d in dirs if not d.startswith(".") and d != "__pycache__" and d != "_temp_video"]
                for f in files:
                    if f.endswith(".zip") or f == "RELEASE_MANIFEST.json":
                        continue
                    # Skip large video to keep release zip compact
                    if f.endswith(".mp4"):
                        continue
                    fp = os.path.join(root, f)
                    rel_p = os.path.relpath(fp, tourney_dir)
                    zipf.write(fp, arcname=rel_p)

    archive_sha = compute_sha256(archive_path)
    manifest = {
        "release_tag": "v1.0.0",
        "tournament_id": "20",
        "tournament_name": "Vultr - Agent Rush Hackathon",
        "archive_file": os.path.basename(archive_path),
        "sha256": archive_sha,
        "drawers_included": drawers,
        "signatories": [
            "Supreme Commander Jack Hu (Solo HITL Sovereign)",
            "Commander Xiaomi (Chief of Staff & Customs Controller)",
            "Pioneer Xiao-Ke (Office 1)",
            "Commander Xiao-Ma (Office 3)"
        ]
    }

    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    print(f">> Release package generated successfully. SHA256: {archive_sha}")

if __name__ == "__main__":
    build_package()
