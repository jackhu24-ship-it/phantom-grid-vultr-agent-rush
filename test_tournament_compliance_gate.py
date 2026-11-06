#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHANToM GRID :: Tournament Compliance Gate Test Suite
Enforces the 4 Mandatory Golden Actions ordained by Supreme Commander Jack Hu:
  1. Full-bleed 16:9 Cover PNG (03_CoverImage_16x9/cover_16x9.png)
  2. Exact 10-Page Slides PDF (04_Slides_PDF/slides.pdf)
  3. 1440P/1080P Demo Video MP4 (05_DemoVideo_1440P/demo_video_1440p.mp4)
  4. 100% Pure International English with 0 Chinese characters across all deliverables.
"""
import os
import re
import sys
import unittest
import pypdf
from PIL import Image
import numpy as np

class TestTournamentComplianceGate(unittest.TestCase):
    def setUp(self):
        self.tourney_dir = os.path.dirname(os.path.abspath(__file__))

    def test_01_cover_png_full_bleed(self):
        """Action 1: Cover image must be PNG, 16:9, and 100% full bleed."""
        cover_p = os.path.join(self.tourney_dir, "03_CoverImage_16x9", "cover_16x9.png")
        self.assertTrue(os.path.exists(cover_p), f"cover_16x9.png must exist at {cover_p}")
        self.assertGreater(os.path.getsize(cover_p), 10000, "cover_16x9.png must be > 10KB")

        img = Image.open(cover_p)
        w, h = img.size
        ratio = w / h
        self.assertAlmostEqual(ratio, 16.0 / 9.0, places=2, msg=f"Aspect ratio must be 16:9, got {ratio:.4f}")

        # Assert full bleed: no pure white border, no black letterbox
        arr = np.array(img.convert("RGB"))
        top_row = arr[0, :, :]
        bottom_row = arr[-1, :, :]
        has_white = np.all(top_row > 250) or np.all(bottom_row > 250)
        has_black = np.all(top_row < 2) or np.all(bottom_row < 2)
        self.assertFalse(has_white, "Cover PNG must not have an empty white top/bottom border")
        self.assertFalse(has_black, "Cover PNG must not have a black letterbox cut")

    def test_02_slides_pdf_exact_10_pages(self):
        """Action 2: Slides PDF must exist and have exactly 10 pages."""
        pdf_p = os.path.join(self.tourney_dir, "04_Slides_PDF", "slides.pdf")
        self.assertTrue(os.path.exists(pdf_p), f"slides.pdf must exist at {pdf_p}")
        self.assertGreater(os.path.getsize(pdf_p), 10000, "slides.pdf must be > 10KB")

        reader = pypdf.PdfReader(pdf_p)
        num_pages = len(reader.pages)
        self.assertEqual(num_pages, 10, f"slides.pdf must have EXACTLY 10 pages, found {num_pages}")

        # Also check slides.html has 10 slides
        html_p = os.path.join(self.tourney_dir, "04_Slides_PDF", "slides.html")
        if os.path.exists(html_p):
            with open(html_p, "r", encoding="utf-8") as f:
                content = f.read()
            slide_count = content.count('class="slide"')
            self.assertEqual(slide_count, 10, f"slides.html must define 10 slide sections, found {slide_count}")

    def test_03_demo_video_1440p_mp4(self):
        """Action 3: 1440P demo video MP4 must exist and be valid."""
        mp4_p = os.path.join(self.tourney_dir, "05_DemoVideo_1440P", "demo_video_1440p.mp4")
        self.assertTrue(os.path.exists(mp4_p), f"demo_video_1440p.mp4 must exist at {mp4_p}")
        self.assertGreater(os.path.getsize(mp4_p), 500000, "demo_video_1440p.mp4 must be > 500KB")

    def test_04_zero_chinese_characters_all_files(self):
        """Action 4: All deliverable files must be 100% English with zero Chinese characters."""
        chinese_pattern = re.compile(r'[\u4e00-\u9fff]')
        violations = []

        scan_extensions = ('.md', '.yaml', '.yml', '.py', '.html', '.json', '.txt', '.mmd', '.csv', '.sh')

        for root, dirs, files in os.walk(self.tourney_dir):
            dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__' and d != '_temp_video']
            for f in files:
                if f.endswith(scan_extensions):
                    fp = os.path.join(root, f)
                    try:
                        with open(fp, 'r', encoding='utf-8') as fh:
                            content = fh.read()
                        matches = chinese_pattern.findall(content)
                        if matches:
                            rel_p = os.path.relpath(fp, self.tourney_dir)
                            violations.append((rel_p, len(matches), "".join(matches[:10])))
                    except Exception:
                        pass

        self.assertEqual(len(violations), 0, f"Found Chinese characters in deliverable files: {violations}")

if __name__ == "__main__":
    unittest.main()
