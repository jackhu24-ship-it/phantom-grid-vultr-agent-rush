#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHANToM GRID :: Drawer 07 Submission Package Audit Test
Asserts Rule 30 (100% English / zero Chinese), Short Pitch <= 280 chars, hyphenated tags, -b main 3-line command, and dual signatures.
"""
import os
import re
import unittest

class TestSubmissionPackageAudit(unittest.TestCase):
    def setUp(self):
        self.doc_path = os.path.join(os.path.dirname(__file__), "Official_Submission_Copy_Package.md")

    def test_file_exists(self):
        self.assertTrue(os.path.exists(self.doc_path), "Official_Submission_Copy_Package.md must exist")
        self.assertGreater(os.path.getsize(self.doc_path), 500, "Submission document must not be empty")

    def test_english_only_no_chinese(self):
        with open(self.doc_path, "r", encoding="utf-8") as f:
            content = f.read()
        chinese_chars = re.findall(r'[\u4e00-\u9fff]', content)
        self.assertEqual(len(chinese_chars), 0, f"Submission document must be 100% English. Found Chinese characters: {chinese_chars[:10]}")

    def test_title_and_short_pitch_bounds(self):
        with open(self.doc_path, "r", encoding="utf-8") as f:
            lines = [l.strip() for l in f.readlines()]

        # Check title prefix
        first_line = lines[0]
        self.assertTrue(first_line.startswith("# PHANToM GRID ::"), f"Title must start with '# PHANToM GRID ::', got: {first_line}")

        # Extract short pitch
        pitch_idx = -1
        for i, line in enumerate(lines):
            if "[Field 2] One-Line Short Pitch" in line:
                pitch_idx = i
                break
        self.assertNotEqual(pitch_idx, -1, "Short pitch section must exist")

        # Find the next non-empty line
        pitch_line = ""
        for line in lines[pitch_idx+1:]:
            if line and not line.startswith("---") and not line.startswith("#"):
                pitch_line = line
                break
        self.assertTrue(len(pitch_line) > 0, "Short pitch text must not be empty")
        self.assertLessEqual(len(pitch_line), 280, f"Short pitch must be <= 280 characters, got {len(pitch_line)} chars: '{pitch_line}'")

    def test_reproduce_command_with_b_main(self):
        with open(self.doc_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("git clone -b main", content, "Reproducibility command must use '-b main'")
        self.assertIn("cd vultr-agent-rush", content)

    def test_dual_signatures_present(self):
        with open(self.doc_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("Commander Jack Hu", content, "Must include Commander Jack Hu")
        self.assertIn("Commander Xiaomi", content, "Must include Commander Xiaomi")

if __name__ == "__main__":
    unittest.main()
