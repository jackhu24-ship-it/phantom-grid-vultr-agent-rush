#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHANToM GRID :: Drawer 01 Specs Audit Test
Asserts complete presence and purity of Four Diagrams and One Table (Rule 57/58),
White Paper, and Official Requirements for Vultr Agent Rush Hackathon.
"""
import os
import unittest

class TestSpecsAudit(unittest.TestCase):
    def setUp(self):
        self.specs_dir = os.path.dirname(os.path.abspath(__file__))

    def test_specs_files_exist(self):
        expected_files = [
            "01_Official_Rules_and_Requirements.md",
            "WHITE_PAPER_VULTR_AGENT_RUSH.md",
            "01_system_topology.mmd",
            "02_sequence_flow.mmd",
            "03_state_machine.mmd",
            "04_security_boundary.mmd",
            "table1_resource_defense_matrix.csv"
        ]
        for fname in expected_files:
            fpath = os.path.join(self.specs_dir, fname)
            self.assertTrue(os.path.exists(fpath), f"Missing required spec file: {fname}")
            self.assertGreater(os.path.getsize(fpath), 0, f"Spec file is empty: {fname}")

    def test_mmd_purity(self):
        mmd_files = [
            "01_system_topology.mmd",
            "02_sequence_flow.mmd",
            "03_state_machine.mmd",
            "04_security_boundary.mmd"
        ]
        for fname in mmd_files:
            fpath = os.path.join(self.specs_dir, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertNotIn("```", content, f"MMD file must be pure code without markdown fences: {fname}")
            self.assertFalse(content.strip().startswith("#"), f"MMD file must not have markdown headers: {fname}")

    def test_table1_csv_content(self):
        csv_path = os.path.join(self.specs_dir, "table1_resource_defense_matrix.csv")
        with open(csv_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
        self.assertGreaterEqual(len(lines), 5, "Resource defense matrix must contain header and metric rows")
        self.assertTrue(lines[0].startswith("metric_id,"), "CSV header must start with metric_id")

    def test_white_paper_contents(self):
        wp_path = os.path.join(self.specs_dir, "WHITE_PAPER_VULTR_AGENT_RUSH.md")
        with open(wp_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("https://api.vultrinference.com/v1", content)
        self.assertIn("ASIL-D", content)
        self.assertIn("0.00 MB", content)

if __name__ == "__main__":
    unittest.main()
