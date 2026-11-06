#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHANToM GRID :: Drawer 02 Source Code Audit Test
Asserts sandbox containment against rm -rf and loops, Vultr API integration, 50GB fuse, and ZDR 0.00MB purge.
"""
import os
import sys
import unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from containment.sandbox_runner import SandboxSupervisor
from backend.app import call_vultr_inference, zdr_memory_wipe
from runner import TrackARunner

class TestSourceCodeAudit(unittest.TestCase):
    def setUp(self):
        self.supervisor = SandboxSupervisor(timeout_sec=5)
        self.runner = TrackARunner()

    def test_destructive_rm_rf_contained(self):
        cmd = "rm -rf / --no-preserve-root"
        res = self.supervisor.execute(cmd, run_in_docker=False)
        self.assertTrue(res.contained, "Destructive rm -rf command must be contained")
        self.assertIn("Destructive host command detected", res.stderr)
        self.assertEqual(res.exit_code, 137)

    def test_infinite_loop_contained(self):
        cmd = "while true; do echo 'eating cpu'; done"
        res = self.supervisor.execute(cmd, run_in_docker=False)
        self.assertTrue(res.contained, "Infinite loop must be contained")
        self.assertIn("Infinite loop", res.stderr)
        self.assertEqual(res.exit_code, 124)

    def test_vultr_inference_protocol(self):
        messages = [{"role": "user", "content": "Hello Vultr Serverless Agent"}]
        reply = call_vultr_inference(messages, mock=True)
        self.assertIsInstance(reply, str)
        self.assertGreater(len(reply), 10)

    def test_vram_fuse_circuit_breaker(self):
        self.assertTrue(self.runner.check_vram_fuse())
        # Simulate memory breach > 50GB
        self.runner.simulated_ram_gb = 52.0
        self.assertFalse(self.runner.check_vram_fuse())
        self.assertEqual(self.runner.state, "CIRCUIT_BREAKER_TRIGGERED")

    def test_zdr_zero_residue_purge(self):
        residue = zdr_memory_wipe()
        self.assertEqual(residue, 0.00, "ZDR memory purge must result in 0.00 MB residue")
        runner_res = self.runner.execute_zdr_purge()
        self.assertEqual(runner_res, 0.00)
        self.assertEqual(self.runner.state, "ZDR_PURGED")

    def test_runner_full_lifecycle(self):
        res = self.runner.run_task("rm -rf / malicious attack", mock=True)
        self.assertEqual(res["status"], "CONTAINED")
        self.assertEqual(res["state"], "COMPLETED")
        self.assertEqual(res["zdr_residual_mb"], 0.00)

if __name__ == "__main__":
    unittest.main()
