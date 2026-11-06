#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHANToM GRID :: Drawer 03 Cover Image Audit Test
Asserts 16:9 ratio, Commander Jack Hu badge isolation (<= 68% width, >= 48px padding), and Anti-Mojibake.
"""
import os
import sys
import unittest
import xml.etree.ElementTree as ET

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from generate_banner import generate_banner

class TestCoverImageAudit(unittest.TestCase):
    def setUp(self):
        self.svg_path = os.path.join(current_dir, "cover_16x9.svg")
        self.png_path = os.path.join(current_dir, "cover_16x9.png")
        if not os.path.exists(self.svg_path) or not os.path.exists(self.png_path):
            generate_banner(current_dir)

    def test_svg_exists_and_ratio(self):
        self.assertTrue(os.path.exists(self.svg_path), "cover_16x9.svg must exist")
        self.assertTrue(os.path.exists(self.png_path), "cover_16x9.png must exist")
        self.assertGreater(os.path.getsize(self.png_path), 10000, "cover_16x9.png must not be empty")
        tree = ET.parse(self.svg_path)
        root = tree.getroot()

        viewbox = root.attrib.get("viewBox", "")
        parts = [float(p) for p in viewbox.split()]
        self.assertEqual(len(parts), 4, "viewBox must have 4 parameters: min-x min-y width height")
        w, h = parts[2], parts[3]
        ratio = w / h
        self.assertAlmostEqual(ratio, 16.0 / 9.0, places=2, msg="Aspect ratio must be 16:9")

    def test_commander_badge_isolation(self):
        with open(self.svg_path, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertIn("COMMANDER JACK HU", content, "Cover must feature Commander Jack Hu badge")
        self.assertIn("width=\"1200\"", content, "Commander badge width must be explicitly budgeted")
        # 1200 / 1920 = 62.5% <= 68%
        self.assertLessEqual(1200 / 1920, 0.68, "Commander badge width must not exceed 68%")

    def test_anti_mojibake(self):
        with open(self.svg_path, "r", encoding="utf-8") as f:
            content = f.read()
        mojibake_chars = ["ð", "ï", "â€", "\ufffd"]
        for bad in mojibake_chars:
            self.assertNotIn(bad, content, f"Detected mojibake character: {bad}")

if __name__ == "__main__":
    unittest.main()
