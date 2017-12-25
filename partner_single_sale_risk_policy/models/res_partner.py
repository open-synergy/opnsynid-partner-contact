# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api
from openerp.tools.translate import _
from openerp.exceptions import Warning as UserError


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.multi
    def _compute_single_sale_policy(self):
        single_sale_order = 0.0
        criteria = [
            ("user_ids.id", "in", [self.env.user.id]),
        ]
        policy = self.env["partner.risk_limit_policy"].search(
            criteria, limit=1)
        if len(policy) == 1:
            single_sale_order = policy.single_sale_order_limit

        for partner in self:
            partner.single_sale_order_limit_policy = single_sale_order

    single_sale_order_limit_policy = fields.Float(
        string="Single Sale Order Limit Policy",
        compute="_compute_single_sale_policy",
        store=False,
    )

    @api.constrains(
        "single_sale_order_limit_policy", "risk_single_sale_order_limit",
    )
    def _check_single_sale_limit_policy(self):
        for partner in self:
            if partner.single_sale_order_limit_policy and \
                    partner.single_sale_order_limit_policy < \
                    partner.risk_single_sale_order_limit:
                raise UserError(_("Unauthorized single sale order amount"))
