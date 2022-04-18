# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models
from openerp.exceptions import Warning as UserError
from openerp.tools.translate import _


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.multi
    def _compute_sale_policy(self):
        sale_order = 0.0
        unset_sale_order = False

        criteria = [
            ("user_ids.id", "in", [self.env.user.id]),
        ]
        policy = self.env["partner.risk_limit_policy"].search(criteria, limit=1)
        if len(policy) == 1:
            sale_order = policy.sale_order_limit
            unset_sale_order = policy.unset_sale_order_limit

        for partner in self:
            partner.sale_order_limit_policy = sale_order
            partner.unset_sale_order_limit_policy = unset_sale_order

    sale_order_limit_policy = fields.Float(
        string="Sale Order Limit Policy",
        compute="_compute_sale_policy",
        store=False,
    )
    unset_sale_order_limit_policy = fields.Boolean(
        string="Unset Sale Order Limit Policy",
        compute="_compute_sale_policy",
        store=False,
    )

    @api.model
    def _update_limit_check_context(self, values):
        _super = super(ResPartner, self)
        ctx = _super._update_limit_check_context(values)
        for field in iter(values):
            if field == "risk_sale_order_limit":
                ctx.update({"check_sale_order_limit": True})
        return ctx

    @api.constrains(
        "risk_sale_order_limit",
    )
    def _check_sale_limit_policy(self):
        for partner in self:
            if (
                partner.sale_order_limit_policy
                and partner.sale_order_limit_policy < partner.risk_sale_order_limit
                and partner.risk_sale_order_limit > 0
                and self.env.context.get("check_sale_order_limit", False)
            ):
                raise UserError(_("Unauthorized sale order amount"))

            if (
                not partner.unset_sale_order_limit_policy
                and partner.risk_sale_order_limit <= 0.0
                and self.env.context.get("check_sale_order_limit", False)
            ):
                raise UserError(_("Unauthorized to sale order limit amount"))
