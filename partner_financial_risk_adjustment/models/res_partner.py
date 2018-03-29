# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.multi
    @api.depends(
        "risk_adjustment_ids",
    )
    def _compute_risk_adjustment(self):
        for partner in self:
            risk_invoice_draft_adjustment = \
                risk_invoice_open_adjustment = \
                risk_invoice_unpaid_adjustment = \
                risk_account_amount_adjustment = \
                0.0
            for adj in partner.risk_adjustment_ids.filtered(
                    lambda r: r.state == "done"):
                risk_invoice_draft_adjustment += adj.risk_invoice_draft
                risk_invoice_open_adjustment += adj.risk_invoice_open
                risk_invoice_unpaid_adjustment += adj.risk_invoice_unpaid
                risk_account_amount_adjustment += adj.risk_account_amount
            partner.risk_invoice_draft_adjustment = \
                risk_invoice_draft_adjustment
            partner.risk_invoice_open_adjustment = \
                risk_invoice_open_adjustment
            partner.risk_invoice_unpaid_adjustment = \
                risk_invoice_unpaid_adjustment
            partner.risk_account_amount_adjustment = \
                risk_account_amount_adjustment

    @api.multi
    @api.depends(
        "invoice_ids", "invoice_ids.state",
        "invoice_ids.amount_total", "invoice_ids.residual",
        "invoice_ids.company_id.invoice_unpaid_margin",
        "risk_adjustment_ids", "risk_adjustment_ids.state",
    )
    def _compute_risk_invoice(self):
        _super = super(ResPartner, self)
        _super._compute_risk_invoice()
        for partner in self:
            partner.risk_invoice_draft += \
                partner.risk_invoice_draft_adjustment
            partner.risk_invoice_open += \
                partner.risk_invoice_open_adjustment
            partner.risk_invoice_unpaid += \
                partner.risk_invoice_unpaid_adjustment

    @api.multi
    @api.depends(
        "credit", "risk_invoice_open", "risk_invoice_unpaid",
    )
    def _compute_risk_account_amount(self):
        _super = super(ResPartner, self)
        _super._compute_risk_account_amount()
        for partner in self:
            partner.risk_account_amount += \
                partner.risk_account_amount_adjustment

    risk_adjustment_ids = fields.One2many(
        string="Risk Adjustments",
        comodel_name="partner.risk_adjustment",
        inverse_name="partner_id",
    )
    risk_invoice_draft_adjustment = fields.Float(
        string="Draft Invoice Adjustment",
        compute="_compute_risk_adjustment",
        store=False,
        readonly=True,
    )
    risk_invoice_open_adjustment = fields.Float(
        string="Open Invoice Adjustment",
        compute="_compute_risk_adjustment",
        store=False,
        readonly=True,
    )
    risk_invoice_unpaid_adjustment = fields.Float(
        string="Unpaid Invoice Adjustment",
        compute="_compute_risk_adjustment",
        store=False,
        readonly=True,
    )
    risk_account_amount_adjustment = fields.Float(
        string="Other Account Adjustment",
        compute="_compute_risk_adjustment",
        store=False,
        readonly=True,
    )
    risk_invoice_draft = fields.Float(
        compute="_compute_risk_invoice",
    )
    risk_invoice_open = fields.Float(
        compute="_compute_risk_invoice",
    )
    risk_invoice_unpaid = fields.Float(
        compute="_compute_risk_invoice",
    )
    risk_account_amount = fields.Float(
        compute="_compute_risk_account_amount",
    )
