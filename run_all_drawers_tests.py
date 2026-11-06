#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHANToM GRID :: Competition 20 All-Drawers Gate-Before-Ship Test Runner
Executes audit test suites across all 10 standard drawers.
"""
import os
import sys
import unittest

def run_all_tests():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    test_files = [
        os.path.join(root_dir, "01_Specs", "test_specs_audit.py"),
        os.path.join(root_dir, "02_SourceCode", "test_source_code.py"),
        os.path.join(root_dir, "03_CoverImage_16x9", "test_cover_image.py"),
        os.path.join(root_dir, "04_Slides_PDF", "test_slides_pdf_audit.py"),
        os.path.join(root_dir, "05_DemoVideo_1440P", "test_video_1440p_audit.py"),
        os.path.join(root_dir, "06_Deploy_and_Sandbox", "test_deploy_sandbox.py"),
        os.path.join(root_dir, "07_SubmissionPackage", "test_submission_package.py"),
        os.path.join(root_dir, "08_AuditReceipts", "test_audit_receipt.py"),
        os.path.join(root_dir, "09_ChaosReports", "test_chaos_stress.py"),
        os.path.join(root_dir, "10_Releases", "test_releases_audit.py"),
        os.path.join(root_dir, "10_Releases", "test_closure.py"),
    ]

    print("=" * 70)
    print("PHANToM GRID :: Competition 20 Full Gate-Before-Ship Suite")
    print("=" * 70)

    total_tests = 0
    total_failures = 0
    total_errors = 0

    loader = unittest.TestLoader()

    for test_file in test_files:
        print(f"\n[RUNNING] Suite: {os.path.relpath(test_file, root_dir)}")
        test_dir = os.path.dirname(test_file)
        test_name = os.path.basename(test_file)
        suite = loader.discover(start_dir=test_dir, pattern=test_name)
        runner = unittest.TextTestRunner(verbosity=1)
        result = runner.run(suite)

        total_tests += result.testsRun
        total_failures += len(result.failures)
        total_errors += len(result.errors)

    print("\n" + "=" * 70)
    print(f"TOTAL TESTS RUN: {total_tests}")
    print(f"FAILURES: {total_failures} | ERRORS: {total_errors}")
    if total_failures == 0 and total_errors == 0:
        print("[RESULT] 100% ALL GREEN PASS! [PASS: GATE CLEARED]")
        print("=" * 70)
        return 0
    else:
        print("[RESULT] GATE FAILED! [FAIL: GATE BLOCKED]")
        print("=" * 70)
        return 1

if __name__ == "__main__":
    sys.exit(run_all_tests())
