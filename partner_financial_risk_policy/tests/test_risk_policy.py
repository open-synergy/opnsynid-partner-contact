# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase
from openerp.exceptions import except_orm
from openerp import tools


class TestRiskPolicy(TransactionCase):

    def setUp(self, *args, **kwargs):
        result = super(TestRiskPolicy, self).setUp(*args, **kwargs)
        # Data
        self.obj_partner = self.env["res.partner"]
        self.user = self.env.ref("base.user_root")
        self.group1 = self.env["res.groups"].create({
            "name": "Group 1",
            "users": [(6, 0, [self.user.id])]
        })
        self.group2 = self.env["res.groups"].create({
            "name": "Group 2",
        })
        self.partner = self.obj_partner.create({
            "name": "Test 1",
            "customer": True,
        })
        self.policy1 = self.env["partner.risk_limit_policy"].create({
            "name": "Policy 1",
            "sequence": 1,
            "group_ids": [(6, 0, [self.group1.id])],
            "total_risk_limit": 1.0,
            "invoice_draft_limit": 1.0,
            "invoice_open_limit": 1.0,
            "invoice_unpaid_limit": 1.0,
            "account_amount_limit": 1.0,
            "unset_total_risk_limit": True,
            "unset_invoice_draft_limit": True,
            "unset_invoice_open_limit": True,
            "unset_invoice_unpaid_limit": True,
            "unset_account_amount_limit": True,
        })
        self.policy1._compute_user()
        self.policy2 = self.env["partner.risk_limit_policy"].create({
            "name": "Policy 2",
            "sequence": 2,
        })

        return result

    def test_initial_policy(self):
        self.assertTrue(self.partner.unset_total_risk_limit_policy)
        self.assertTrue(self.partner.unset_invoice_draft_limit_policy)
        self.assertTrue(self.partner.unset_invoice_open_limit_policy)
        self.assertTrue(self.partner.unset_invoice_unpaid_limit_policy)
        self.assertTrue(self.partner.unset_account_amount_limit_policy)

    def test_partner_failed_zero_total_risk_limit(self):
        self.policy1.write({
            "total_risk_limit": 1.0,
            "invoice_draft_limit": 1.0,
            "invoice_open_limit": 1.0,
            "invoice_unpaid_limit": 1.0,
            "account_amount_limit": 1.0,
            "unset_total_risk_limit": False,
            "unset_invoice_draft_limit": True,
            "unset_invoice_open_limit": True,
            "unset_invoice_unpaid_limit": True,
            "unset_account_amount_limit": True,
        })
        with self.assertRaises(except_orm) as cm:
            self.partner.write({
                "credit_limit": 0.0,
            })
        err_msg = "Error while validating constraint\n\n%s" % \
            "Unauthorized to unset credit limit amount"
        self.assertEqual(
            cm.exception.value,
            tools.ustr(err_msg)
        )

    def test_partner_failed_zero_invoice_draft_limit(self):
        self.policy1.write({
            "total_risk_limit": 1.0,
            "invoice_draft_limit": 1.0,
            "invoice_open_limit": 1.0,
            "invoice_unpaid_limit": 1.0,
            "account_amount_limit": 1.0,
            "unset_total_risk_limit": True,
            "unset_invoice_draft_limit": False,
            "unset_invoice_open_limit": True,
            "unset_invoice_unpaid_limit": True,
            "unset_account_amount_limit": True,
        })
        with self.assertRaises(except_orm) as cm:
            self.partner.write({
                "credit_limit": 0.0,
                "risk_invoice_draft_limit": 0.0,
            })
        err_msg = "Error while validating constraint\n\n%s" % \
            "Unauthorized to unset invoice draft amount"
        self.assertEqual(
            cm.exception.value,
            tools.ustr(err_msg)
        )
        self.assertTrue(self.partner.unset_total_risk_limit_policy)
        self.assertFalse(self.partner.unset_invoice_draft_limit_policy)
        self.assertTrue(self.partner.unset_invoice_open_limit_policy)
        self.assertTrue(self.partner.unset_invoice_unpaid_limit_policy)
        self.assertTrue(self.partner.unset_account_amount_limit_policy)

    def test_partner_failed_zero_invoice_open_limit(self):
        self.policy1.write({
            "total_risk_limit": 1.0,
            "invoice_draft_limit": 1.0,
            "invoice_open_limit": 1.0,
            "invoice_unpaid_limit": 1.0,
            "account_amount_limit": 1.0,
            "unset_total_risk_limit": True,
            "unset_invoice_draft_limit": True,
            "unset_invoice_open_limit": False,
            "unset_invoice_unpaid_limit": True,
            "unset_account_amount_limit": True,
        })
        with self.assertRaises(except_orm) as cm:
            self.partner.write({
                "credit_limit": 0.0,
                "risk_invoice_draft_limit": 0.0,
                "risk_invoice_open_limit": 0.0,
            })
        err_msg = "Error while validating constraint\n\n%s" % \
            "Unauthorized to unset invoice open amount"
        self.assertEqual(
            cm.exception.value,
            tools.ustr(err_msg)
        )
        self.assertTrue(self.partner.unset_total_risk_limit_policy)
        self.assertTrue(self.partner.unset_invoice_draft_limit_policy)
        self.assertFalse(self.partner.unset_invoice_open_limit_policy)
        self.assertTrue(self.partner.unset_invoice_unpaid_limit_policy)
        self.assertTrue(self.partner.unset_account_amount_limit_policy)

    def test_partner_failed_zero_invoice_unpaid_limit(self):
        self.policy1.write({
            "total_risk_limit": 1.0,
            "invoice_draft_limit": 1.0,
            "invoice_open_limit": 1.0,
            "invoice_unpaid_limit": 1.0,
            "account_amount_limit": 1.0,
            "unset_total_risk_limit": True,
            "unset_invoice_draft_limit": True,
            "unset_invoice_open_limit": True,
            "unset_invoice_unpaid_limit": False,
            "unset_account_amount_limit": True,
        })
        with self.assertRaises(except_orm) as cm:
            self.partner.write({
                "credit_limit": 0.0,
                "risk_invoice_draft_limit": 0.0,
                "risk_invoice_open_limit": 0.0,
                "risk_invoice_unpaid_limit": 0.0,
            })
        err_msg = "Error while validating constraint\n\n%s" % \
            "Unauthorized to unset invoice unpaid amount"
        self.assertEqual(
            cm.exception.value,
            tools.ustr(err_msg)
        )
        self.assertTrue(self.partner.unset_total_risk_limit_policy)
        self.assertTrue(self.partner.unset_invoice_draft_limit_policy)
        self.assertTrue(self.partner.unset_invoice_open_limit_policy)
        self.assertFalse(self.partner.unset_invoice_unpaid_limit_policy)
        self.assertTrue(self.partner.unset_account_amount_limit_policy)

    def test_partner_failed_zero_account_amount_limit(self):
        self.policy1.write({
            "total_risk_limit": 1.0,
            "invoice_draft_limit": 1.0,
            "invoice_open_limit": 1.0,
            "invoice_unpaid_limit": 1.0,
            "account_amount_limit": 1.0,
            "unset_total_risk_limit": True,
            "unset_invoice_draft_limit": True,
            "unset_invoice_open_limit": True,
            "unset_invoice_unpaid_limit": True,
            "unset_account_amount_limit": False,
        })
        with self.assertRaises(except_orm) as cm:
            self.partner.write({
                "credit_limit": 0.0,
                "risk_invoice_draft_limit": 0.0,
                "risk_invoice_open_limit": 0.0,
                "risk_invoice_unpaid_limit": 0.0,
                "risk_account_amount_limit": 0.0,
            })
        err_msg = "Error while validating constraint\n\n%s" % \
            "Unauthorized to unset other account amount"
        self.assertEqual(
            cm.exception.value,
            tools.ustr(err_msg)
        )
        self.assertTrue(self.partner.unset_total_risk_limit_policy)
        self.assertTrue(self.partner.unset_invoice_draft_limit_policy)
        self.assertTrue(self.partner.unset_invoice_open_limit_policy)
        self.assertTrue(self.partner.unset_invoice_unpaid_limit_policy)
        self.assertFalse(self.partner.unset_account_amount_limit_policy)

    def test_partner_failed_total_risk_limit(self):
        self.policy1.write({
            "total_risk_limit": 100.00,
            "invoice_draft_limit": 100.0,
            "invoice_open_limit": 100.0,
            "invoice_unpaid_limit": 100.0,
            "account_amount_limit": 100.0,
            "unset_total_risk_limit": True,
            "unset_invoice_draft_limit": True,
            "unset_invoice_open_limit": True,
            "unset_invoice_unpaid_limit": True,
            "unset_account_amount_limit": True,
        })
        with self.assertRaises(except_orm) as cm:
            self.partner.write({
                "credit_limit": 200.00,
                "risk_invoice_draft_limit": 100.00,
                "risk_invoice_open_limit": 100.00,
                "risk_invoice_unpaid_limit": 100.00,
                "risk_account_amount_limit": 100.0,
            })
        err_msg = "Error while validating constraint\n\n%s" % \
            "Unauthorized credit limit amount"
        self.assertEqual(
            cm.exception.value,
            tools.ustr(err_msg)
        )
        self.assertEqual(
            self.partner.total_risk_limit_policy,
            100.00
        )
        self.assertEqual(
            self.partner.invoice_draft_limit_policy,
            100.00
        )
        self.assertEqual(
            self.partner.invoice_open_limit_policy,
            100.00
        )
        self.assertEqual(
            self.partner.invoice_unpaid_limit_policy,
            100.00
        )
        self.assertEqual(
            self.partner.account_amount_limit_policy,
            100.00
        )

    def test_partner_failed_invoice_draft_limit(self):
        self.policy1.write({
            "total_risk_limit": 200.00,
            "invoice_draft_limit": 100.0,
            "invoice_open_limit": 100.0,
            "invoice_unpaid_limit": 100.0,
            "account_amount_limit": 100.0,
            "unset_total_risk_limit": True,
            "unset_invoice_draft_limit": True,
            "unset_invoice_open_limit": True,
            "unset_invoice_unpaid_limit": True,
            "unset_account_amount_limit": True,
        })
        with self.assertRaises(except_orm) as cm:
            self.partner.write({
                "credit_limit": 200.00,
                "risk_invoice_draft_limit": 200.00,
                "risk_invoice_open_limit": 100.00,
                "risk_invoice_unpaid_limit": 100.00,
                "risk_account_amount_limit": 100.0,
            })
        err_msg = "Error while validating constraint\n\n%s" % \
            "Unauthorized invoice draft amount"
        self.assertEqual(
            cm.exception.value,
            tools.ustr(err_msg)
        )
        self.assertEqual(
            self.partner.total_risk_limit_policy,
            200.00
        )
        self.assertEqual(
            self.partner.invoice_draft_limit_policy,
            100.00
        )
        self.assertEqual(
            self.partner.invoice_open_limit_policy,
            100.00
        )
        self.assertEqual(
            self.partner.invoice_unpaid_limit_policy,
            100.00
        )
        self.assertEqual(
            self.partner.account_amount_limit_policy,
            100.00
        )

    def test_partner_failed_invoice_open_limit(self):
        self.policy1.write({
            "total_risk_limit": 200.00,
            "invoice_draft_limit": 200.0,
            "invoice_open_limit": 100.0,
            "invoice_unpaid_limit": 100.0,
            "account_amount_limit": 100.0,
            "unset_total_risk_limit": True,
            "unset_invoice_draft_limit": True,
            "unset_invoice_open_limit": True,
            "unset_invoice_unpaid_limit": True,
            "unset_account_amount_limit": True,
        })
        with self.assertRaises(except_orm) as cm:
            self.partner.write({
                "credit_limit": 200.00,
                "risk_invoice_draft_limit": 200.00,
                "risk_invoice_open_limit": 200.00,
                "risk_invoice_unpaid_limit": 100.00,
                "risk_account_amount_limit": 100.0,
            })
        err_msg = "Error while validating constraint\n\n%s" % \
            "Unauthorized invoice open amount"
        self.assertEqual(
            cm.exception.value,
            tools.ustr(err_msg)
        )
        self.assertEqual(
            self.partner.total_risk_limit_policy,
            200.00
        )
        self.assertEqual(
            self.partner.invoice_draft_limit_policy,
            200.00
        )
        self.assertEqual(
            self.partner.invoice_open_limit_policy,
            100.00
        )
        self.assertEqual(
            self.partner.invoice_unpaid_limit_policy,
            100.00
        )
        self.assertEqual(
            self.partner.account_amount_limit_policy,
            100.00
        )

    def test_partner_failed_invoice_unpaid_limit(self):
        self.policy1.write({
            "total_risk_limit": 200.00,
            "invoice_draft_limit": 200.0,
            "invoice_open_limit": 200.0,
            "invoice_unpaid_limit": 100.0,
            "account_amount_limit": 100.0,
            "unset_total_risk_limit": True,
            "unset_invoice_draft_limit": True,
            "unset_invoice_open_limit": True,
            "unset_invoice_unpaid_limit": True,
            "unset_account_amount_limit": True,
        })
        with self.assertRaises(except_orm) as cm:
            self.partner.write({
                "credit_limit": 200.00,
                "risk_invoice_draft_limit": 200.00,
                "risk_invoice_open_limit": 200.00,
                "risk_invoice_unpaid_limit": 200.00,
                "risk_account_amount_limit": 100.0,
            })
        err_msg = "Error while validating constraint\n\n%s" % \
            "Unauthorized invoice unpaid amount"
        self.assertEqual(
            cm.exception.value,
            tools.ustr(err_msg)
        )
        self.assertEqual(
            self.partner.total_risk_limit_policy,
            200.00
        )
        self.assertEqual(
            self.partner.invoice_draft_limit_policy,
            200.00
        )
        self.assertEqual(
            self.partner.invoice_open_limit_policy,
            200.00
        )
        self.assertEqual(
            self.partner.invoice_unpaid_limit_policy,
            100.00
        )
        self.assertEqual(
            self.partner.account_amount_limit_policy,
            100.00
        )

    def test_partner_failed_account_amount_limit(self):
        self.policy1.write({
            "total_risk_limit": 200.00,
            "invoice_draft_limit": 200.0,
            "invoice_open_limit": 200.0,
            "invoice_unpaid_limit": 200.0,
            "account_amount_limit": 100.0,
            "unset_total_risk_limit": True,
            "unset_invoice_draft_limit": True,
            "unset_invoice_open_limit": True,
            "unset_invoice_unpaid_limit": True,
            "unset_account_amount_limit": True,
        })
        with self.assertRaises(except_orm) as cm:
            self.partner.write({
                "credit_limit": 200.00,
                "risk_invoice_draft_limit": 200.00,
                "risk_invoice_open_limit": 200.00,
                "risk_invoice_unpaid_limit": 200.00,
                "risk_account_amount_limit": 200.0,
            })
        err_msg = "Error while validating constraint\n\n%s" % \
            "Unauthorized other account amount"
        self.assertEqual(
            cm.exception.value,
            tools.ustr(err_msg)
        )
        self.assertEqual(
            self.partner.total_risk_limit_policy,
            200.00
        )
        self.assertEqual(
            self.partner.invoice_draft_limit_policy,
            200.00
        )
        self.assertEqual(
            self.partner.invoice_open_limit_policy,
            200.00
        )
        self.assertEqual(
            self.partner.invoice_unpaid_limit_policy,
            200.00
        )
        self.assertEqual(
            self.partner.account_amount_limit_policy,
            100.00
        )

    def test_partner_success_all_limit(self):
        self.policy1.write({
            "total_risk_limit": 200.00,
            "invoice_draft_limit": 200.0,
            "invoice_open_limit": 200.0,
            "invoice_unpaid_limit": 200.0,
            "account_amount_limit": 200.0,
            "unset_total_risk_limit": True,
            "unset_invoice_draft_limit": True,
            "unset_invoice_open_limit": True,
            "unset_invoice_unpaid_limit": True,
            "unset_account_amount_limit": True,
        })
        self.partner.write({
            "credit_limit": 200.00,
            "risk_invoice_draft_limit": 200.00,
            "risk_invoice_open_limit": 200.00,
            "risk_invoice_unpaid_limit": 200.00,
            "risk_account_amount_limit": 200.0,
        })
        self.assertEqual(
            self.partner.total_risk_limit_policy,
            200.00
        )
        self.assertEqual(
            self.partner.invoice_draft_limit_policy,
            200.00
        )
        self.assertEqual(
            self.partner.invoice_open_limit_policy,
            200.00
        )
        self.assertEqual(
            self.partner.invoice_unpaid_limit_policy,
            200.00
        )
        self.assertEqual(
            self.partner.account_amount_limit_policy,
            200.00
        )
