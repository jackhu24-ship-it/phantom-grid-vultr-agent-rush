#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHANToM GRID :: Drawer 04 Slides Audit Test
Asserts HTML slide layout, 16:9 canvas, exact 10 pages in HTML and compiled PDF,
Commander badge isolation, and Anti-Mojibake.
"""
import os
import unittest
import pypdf

class TestSlidesPdfAudit(unittest.TestCase):
    def setUp(self):
        self.slides_dir = os.path.dirname(os.path.abspath(__file__))
        self.html_path = os.path.join(self.slides_dir, "slides.html")
        self.pdf_path = os.path.join(self.slides_dir, "slides.pdf")

    def test_slides_files_exist(self):
        self.assertTrue(os.path.exists(self.html_path), "slides.html must exist")
        self.assertGreater(os.path.getsize(self.html_path), 500, "slides.html must not be empty")
        self.assertTrue(os.path.exists(self.pdf_path), "slides.pdf must exist")
        self.assertGreater(os.path.getsize(self.pdf_path), 10000, "slides.pdf must not be empty")

    def test_exact_10_pages_in_html_and_pdf(self):
        with open(self.html_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("1920px 1080px", content, "Slides must be sized 1920px by 1080px (16:9)")
        slide_count = content.count('class="slide"')
        self.assertEqual(slide_count, 10, f"Slides deck in HTML must have exactly 10 slides, got {slide_count}")

        reader = pypdf.PdfReader(self.pdf_path)
        pdf_pages = len(reader.pages)
        self.assertEqual(pdf_pages, 10, f"Compiled slides.pdf must have exactly 10 pages, got {pdf_pages}")

    def test_commander_badge_isolation(self):
        with open(self.html_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("COMMANDER JACK HU", content, "Slides must contain Commander Jack Hu attribution")

    def test_anti_mojibake(self):
        with open(self.html_path, "r", encoding="utf-8") as f:
            content = f.read()
        mojibake_chars = ["ð", "ï", "â€", "\ufffd"]
        for bad in mojibake_chars:
            self.assertNotIn(bad, content, f"Detected mojibake character: {bad}")

if __name__ == "__main__":
    unittest.main()
