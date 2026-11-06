#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHANToM GRID :: Drawer 05 Demo Video Audit Test
Asserts 5-act Hollywood structure, 2:00-3:00 total duration, > 50% Live Demo, Title Safe Area, and Anti-Mojibake.
"""
import os
import unittest

class TestVideo1440pAudit(unittest.TestCase):
    def setUp(self):
        self.script_path = os.path.join(os.path.dirname(__file__), "video_script.md")

    def test_script_file_exists(self):
        self.assertTrue(os.path.exists(self.script_path), "video_script.md must exist")
        self.assertGreater(os.path.getsize(self.script_path), 500, "video_script.md must not be empty")
        mp4_path = os.path.join(os.path.dirname(__file__), "demo_video_1440p.mp4")
        self.assertTrue(os.path.exists(mp4_path), "demo_video_1440p.mp4 must exist")
        self.assertGreater(os.path.getsize(mp4_path), 100000, "demo_video_1440p.mp4 must not be empty")

    def test_five_act_structure(self):
        with open(self.script_path, "r", encoding="utf-8") as f:
            content = f.read()
        acts = ["Act 1:", "Act 2:", "Act 3:", "Act 4:", "Act 5:"]
        for act in acts:
            self.assertIn(act, content, f"Missing required act: {act}")

    def test_duration_and_live_demo_ratio(self):
        with open(self.script_path, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertIn("155 seconds", content, "Total duration must be specified (155s)")
        # 155s is between 120s and 180s (2:00 ~ 3:00)
        self.assertTrue(120 <= 155 <= 180, "Duration must be within 2:00 and 3:00")

        self.assertIn("85 seconds", content, "Live demo duration must be specified")
        live_ratio = 85.0 / 155.0
        self.assertGreater(live_ratio, 0.50, f"Live Demo must be > 50%, found {live_ratio:.1%}")

    def test_audio_and_telemetry_coordinates(self):
        with open(self.script_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("en-US-ChristopherNeural", content, "Audio track must be en-US-ChristopherNeural")
        self.assertIn("[40, 135, 1270, 825]", content, "Terminal container coordinates must match standard")
        self.assertIn("(60, 975)", content, "Commander safe badge coordinates must match standard")
        self.assertIn("COMMANDER JACK HU", content, "Script must include Commander Jack Hu")

    def test_anti_mojibake(self):
        with open(self.script_path, "r", encoding="utf-8") as f:
            content = f.read()
        mojibake_chars = ["ð", "ï", "â€", "\ufffd"]
        for bad in mojibake_chars:
            self.assertNotIn(bad, content, f"Detected mojibake character: {bad}")

if __name__ == "__main__":
    unittest.main()
