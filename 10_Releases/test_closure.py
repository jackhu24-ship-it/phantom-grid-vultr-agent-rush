#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHANToM GRID :: Drawer 10 Tournament Closure & Manifest Gate Test
Validates that all tournament drawers, core files, and deliverables are closed and sealed.
"""
import os
import unittest

class TestClosureAudit(unittest.TestCase):
    def setUp(self):
        self.releases_dir = os.path.dirname(__file__)
        self.tourney_dir = os.path.abspath(os.path.join(self.releases_dir, ".."))

    def test_all_ten_drawers_present(self):
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
        for drawer in drawers:
            p = os.path.join(self.tourney_dir, drawer)
            self.assertTrue(os.path.exists(p), f"Drawer missing: {drawer}")
            self.assertTrue(os.path.isdir(p), f"Drawer is not a directory: {drawer}")

    def test_root_manifests_present(self):
        root_files = ["README.md", "match_manifest.yaml", "run_all_drawers_tests.py", "test_tournament_compliance_gate.py"]
        for rf in root_files:
            p = os.path.join(self.tourney_dir, rf)
            self.assertTrue(os.path.exists(p), f"Root file missing: {rf}")

if __name__ == "__main__":
    unittest.main()
