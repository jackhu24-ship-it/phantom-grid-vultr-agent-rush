#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHANToM GRID :: Drawer 10 Releases Audit Test
Asserts release package zip existence, valid SHA-256 in RELEASE_MANIFEST.json, and inclusion of all 10 drawers.
"""
import os
import json
import hashlib
import unittest

def compute_sha256(filepath: str) -> str:
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()

class TestReleasesAudit(unittest.TestCase):
    def setUp(self):
        self.releases_dir = os.path.dirname(__file__)
        self.manifest_path = os.path.join(self.releases_dir, "RELEASE_MANIFEST.json")
        self.archive_path = os.path.join(self.releases_dir, "phantom_grid_vultr_release_v1.0.0.zip")

    def test_archive_and_manifest_exist(self):
        self.assertTrue(os.path.exists(self.archive_path), "Release archive must exist")
        self.assertTrue(os.path.exists(self.manifest_path), "Release manifest must exist")
        self.assertGreater(os.path.getsize(self.archive_path), 1000, "Release archive must not be empty")

    def test_manifest_checksum_integrity(self):
        with open(self.manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)

        declared_sha = manifest.get("sha256")
        actual_sha = compute_sha256(self.archive_path)
        self.assertEqual(declared_sha, actual_sha, "Manifest SHA-256 must match actual archive digest")

    def test_manifest_metadata(self):
        with open(self.manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)

        self.assertEqual(len(manifest.get("drawers_included", [])), 10)
        self.assertIn("Supreme Commander Jack Hu", " ".join(manifest.get("signatories", [])))

if __name__ == "__main__":
    unittest.main()
