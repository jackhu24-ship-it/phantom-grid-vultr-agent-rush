#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHANToM GRID :: Drawer 06 Deployment and Sandbox Audit Test
Asserts Vultr cloud-init automation, deployment manager, and air-gapped sandbox network configurations.
"""
import os
import sys
import unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from vultr_deploy import VultrDeploymentManager, VULTR_SERVERLESS_URL

class TestDeploySandboxAudit(unittest.TestCase):
    def setUp(self):
        self.mgr = VultrDeploymentManager()
        self.script_path = os.path.join(current_dir, "vultr_cloud_init.sh")

    def test_cloud_init_script_exists_and_valid(self):
        self.assertTrue(os.path.exists(self.script_path), "vultr_cloud_init.sh must exist")
        self.assertGreater(os.path.getsize(self.script_path), 500)
        with open(self.script_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("docker network create --internal", content, "Script must create internal airgapped network")
        self.assertIn("https://api.vultrinference.com/v1/chat/completions", content)
        self.assertIn("ufw", content)

    def test_vultr_serverless_connectivity_schema(self):
        res = self.mgr.verify_serverless_connectivity(mock=True)
        self.assertEqual(res["status"], "CONNECTED")
        self.assertEqual(res["endpoint"], VULTR_SERVERLESS_URL)
        self.assertIn("llama-3.3-70b-instruct", res["models_available"])

    def test_sandbox_runtime_limits(self):
        runtime = self.mgr.verify_sandbox_runtime()
        self.assertEqual(runtime["network_isolation"], "AIR_GAPPED")
        self.assertEqual(runtime["status"], "PASS")
        self.assertTrue(runtime["read_only_rootfs"])

if __name__ == "__main__":
    unittest.main()
