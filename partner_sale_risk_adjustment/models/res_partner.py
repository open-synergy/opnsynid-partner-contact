# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.multi
    @api.depends(
        "risk_adjustment_ids",
    )
    def _compute_sale_risk_adjustment(self):
        for partner in self:
            risk_sale_order_adjustment = 0.0
            for adj in partner.risk_adjustment_ids.filtered(
                    lambda r: r.state == "done"):
                risk_sale_order_adjustment += adj.risk_sale_order
            partner.risk_sale_order_adjustment = \
                risk_sale_order_adjustment

    @api.multi
    @api.depends(
        "sale_order_ids", "sale_order_ids.invoice_pending_amount",
        "child_ids.sale_order_ids",
        "child_ids.sale_order_ids.invoice_pending_amount",
        "risk_adjustment_ids", "risk_adjustment_ids.state",
    )
    def _compute_risk_sale_order(self):
        _super = super(ResPartner, self)
        _super._compute_risk_sale_order()
        for partner in self:
            partner.risk_sale_order += \
                partner.risk_sale_order_adjustment

    risk_sale_order_adjustment = fields.Float(
        string="Sale Order Adjustment",
        compute="_compute_sale_risk_adjustment",
        store=False,
        readonly=True,
    )
    risk_sale_order = fields.Float(
        compute="_compute_risk_sale_order",
    )
