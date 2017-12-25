# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api
from openerp.tools.translate import _
from openerp.exceptions import Warning as UserError


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.multi
    def _compute_sale_policy(self):
        sale_order = 0.0
        criteria = [
            ("user_ids.id", "in", [self.env.user.id]),
        ]
        policy = self.env["partner.risk_limit_policy"].search(
            criteria, limit=1)
        if len(policy) == 1:
            sale_order = policy.sale_order_limit

        for partner in self:
            partner.sale_order_limit_policy = sale_order

    sale_order_limit_policy = fields.Float(
        string="Sale Order Limit Policy",
        compute="_compute_sale_policy",
        store=False,
    )

    @api.constrains(
        "sale_order_limit_policy", "risk_sale_order_limit",
    )
    def _check_sale_limit_policy(self):
        for partner in self:
            if partner.sale_order_limit_policy and \
                    partner.sale_order_limit_policy < \
                    partner.risk_sale_order_limit:
                raise UserError(_("Unauthorized sale order amount"))
