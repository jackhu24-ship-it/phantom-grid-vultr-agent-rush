#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHANToM GRID :: Drawer 08 Audit Receipt Test
Asserts WORM immutable receipt schema, co-signatures, 50GB VRAM bound, and ZDR 0.00MB zeroing.
"""
import os
import json
import unittest

class TestAuditReceipt(unittest.TestCase):
    def setUp(self):
        self.receipt_path = os.path.join(os.path.dirname(__file__), "audit_receipt.json")

    def test_receipt_exists_and_valid_json(self):
        self.assertTrue(os.path.exists(self.receipt_path), "audit_receipt.json must exist")
        with open(self.receipt_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertIn("receipt_id", data)
        self.assertTrue(data["receipt_id"].startswith("PG-RECEIPT-0x"))

    def test_signatories_present(self):
        with open(self.receipt_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        signers = data.get("signatories", {})
        self.assertIn("supreme_commander", signers)
        self.assertIn("Jack Hu", signers["supreme_commander"])
        self.assertIn("chief_of_staff", signers)
        self.assertIn("Commander Xiaomi", signers["chief_of_staff"])

    def test_resource_limits_and_zdr(self):
        with open(self.receipt_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        res = data.get("resource_defense_audit", {})
        self.assertLessEqual(res.get("max_vram_limit_gb", 999), 50.0)
        self.assertEqual(res.get("zdr_residual_memory_mb"), 0.00)

    def test_rule_compliance_all_pass(self):
        with open(self.receipt_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        rules = data.get("rule_compliance_audit", {})
        self.assertGreater(len(rules), 0)
        for rule_name, status in rules.items():
            self.assertEqual(status, "PASS", f"Rule {rule_name} must be PASS")

if __name__ == "__main__":
    unittest.main()
