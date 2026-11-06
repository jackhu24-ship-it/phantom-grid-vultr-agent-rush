#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHANToM GRID :: Drawer 09 Chaos Stress Audit Test
Simulates chaos stress cycles verifying 50GB circuit breaker, malformed task resilience, and ZDR 0.00MB purge.
"""
import os
import sys
import unittest

src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "02_SourceCode"))
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from containment.sandbox_runner import SandboxSupervisor
from runner import TrackARunner

class TestChaosStress(unittest.TestCase):
    def setUp(self):
        self.supervisor = SandboxSupervisor(timeout_sec=5)
        self.runner = TrackARunner()

    def test_circuit_breaker_resilience(self):
        """Simulates memory check under extreme simulated load."""
        self.assertTrue(self.runner.check_vram_fuse())
        # Force breaker trip
        self.runner.simulated_ram_gb = 55.0
        self.assertFalse(self.runner.check_vram_fuse())
        self.assertEqual(self.runner.state, "CIRCUIT_BREAKER_TRIGGERED")
        # Reset
        self.runner.simulated_ram_gb = 2.45
        self.runner.state = "INITIALIZED"
        self.assertTrue(self.runner.check_vram_fuse())

    def test_malformed_and_destructive_chaos_fuzzing(self):
        """Simulates 50 iterations of destructive commands and malicious scripts."""
        fuzz_payloads = [
            "rm -rf / --no-preserve-root",
            "rm -rf *",
            "while true; do echo leak; done",
            ":(){ :|:& };:",
            "chmod -R 777 /",
            "cat /dev/zero > /tmp/large_file",
            "malformed json \x00\xff injection"
        ]
        for i in range(50):
            payload = fuzz_payloads[i % len(fuzz_payloads)]
            res = self.supervisor.execute(payload, run_in_docker=False)
            if "rm -rf" in payload or "while true" in payload or "chmod -R 777 /" in payload or ":(){" in payload:
                self.assertTrue(res.contained, f"Payload must be contained: {payload}")

    def test_zdr_continuous_zeroing(self):
        """Simulates repeated runs verifying ZDR 0.00MB zeroing without leaks."""
        for _ in range(20):
            residue = self.runner.execute_zdr_purge()
            self.assertEqual(residue, 0.00)
            self.assertEqual(self.runner.state, "ZDR_PURGED")

    def test_chaos_report_exists(self):
        report_path = os.path.join(os.path.dirname(__file__), "chaos_test_report.md")
        self.assertTrue(os.path.exists(report_path))
        self.assertGreater(os.path.getsize(report_path), 500)

if __name__ == "__main__":
    unittest.main()
