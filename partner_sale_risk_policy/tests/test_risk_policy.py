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
            "sale_order_limit": 1.0,
            "unset_sale_order_limit": True,
        })
        self.policy1._compute_user()
        self.policy2 = self.env["partner.risk_limit_policy"].create({
            "name": "Policy 2",
            "sequence": 2,
        })

        return result

    def test_initial_policy(self):
        self.assertTrue(self.partner.unset_sale_order_limit_policy)

    def test_partner_failed_zero_sale_order_limit(self):
        self.policy1.write({
            "sale_order_limit": 1.0,
            "unset_sale_order_limit": False,
        })
        with self.assertRaises(except_orm) as cm:
            self.partner.write({
                "risk_sale_order_limit": 0.0,
            })
        err_msg = "Error while validating constraint\n\n%s" % \
            "Unauthorized to sale order limit amount"
        self.assertEqual(
            cm.exception.value,
            tools.ustr(err_msg)
        )

    def test_partner_failed_sale_order_limit(self):
        self.policy1.write({
            "sale_order_limit": 100.00,
            "unset_sale_order_limit": True,
        })
        with self.assertRaises(except_orm) as cm:
            self.partner.write({
                "risk_sale_order_limit": 200.00,
            })
        err_msg = "Error while validating constraint\n\n%s" % \
            "Unauthorized sale order amount"
        self.assertEqual(
            cm.exception.value,
            tools.ustr(err_msg)
        )
        self.assertEqual(
            self.partner.sale_order_limit_policy,
            100.00
        )

    def test_partner_success_sale_order_limit(self):
        self.policy1.write({
            "sale_order_limit": 200.00,
            "unset_sale_order_limit": True,
        })
        self.partner.write({
            "sale_order_limit_policy": 200.00,
        })
        self.assertEqual(
            self.partner.sale_order_limit_policy,
            200.00
        )
