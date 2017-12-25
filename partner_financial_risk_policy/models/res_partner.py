# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api
from openerp.tools.translate import _
from openerp.exceptions import Warning as UserError


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.multi
    def _compute_policy(self):
        total_risk = invoice_draft = invoice_open = \
            invoice_unpaid = account_amount = 0.0
        criteria = [
            ("user_ids.id", "in", [self.env.user.id]),
        ]
        policy = self.env["partner.risk_limit_policy"].search(
            criteria, limit=1)
        if len(policy) == 1:
            total_risk = policy.total_risk_limit
            invoice_draft = policy.invoice_draft_limit
            invoice_open = policy.invoice_open_limit
            invoice_unpaid = policy.invoice_unpaid_limit
            account_amount = policy.account_amount_limit

        for partner in self:
            partner.total_risk_limit_policy = total_risk
            partner.invoice_draft_limit_policy = invoice_draft
            partner.invoice_open_limit_policy = invoice_open
            partner.invoice_unpaid_limit_policy = invoice_unpaid
            partner.account_amount_limit_policy = account_amount

    total_risk_limit_policy = fields.Float(
        string="Total Risk Limit Policy",
        compute="_compute_policy",
        store=False,
    )
    invoice_draft_limit_policy = fields.Float(
        string="Invoice Draft Limit Policy",
        compute="_compute_policy",
        store=False,
    )
    invoice_open_limit_policy = fields.Float(
        string="Invoice Open Limit Policy",
        compute="_compute_policy",
        store=False,
    )
    invoice_unpaid_limit_policy = fields.Float(
        string="Invoice Unpaid Limit Policy",
        compute="_compute_policy",
        store=False,
    )
    account_amount_limit_policy = fields.Float(
        string="Other Account Amount Limit Policy",
        compute="_compute_policy",
        store=False,
    )

    @api.constrains(
        "total_risk_limit_policy", "invoice_draft_limit_policy",
        "invoice_open_limit_policy", "invoice_unpaid_limit_policy",
        "account_amount_limit_policy", "credit_limit",
        "risk_invoice_draft_limit", "risk_invoice_open_limit",
        "risk_invoice_unpaid_limit", "risk_account_amount_limit",
    )
    def _check_limit_policy(self):
        for partner in self:
            if partner.total_risk_limit_policy and \
                    partner.total_risk_limit_policy < partner.credit_limit:
                raise UserError(_("Unauthorized credit limit amount"))

            if partner.invoice_draft_limit_policy and \
                    partner.invoice_draft_limit_policy < \
                    partner.risk_invoice_draft_limit:
                raise UserError(_("Unauthorized invoice draft amount"))

            if partner.invoice_open_limit_policy and \
                    partner.invoice_open_limit_policy < \
                    partner.risk_invoice_open_limit:
                raise UserError(_("Unauthorized invoice open amount"))

            if partner.invoice_unpaid_limit_policy and \
                    partner.invoice_unpaid_limit_policy < \
                    partner.risk_invoice_unpaid_limit:
                raise UserError(_("Unauthorized invoice unpaid amount"))

            if partner.account_amount_limit_policy and \
                    partner.account_amount_limit_policy < \
                    partner.risk_account_amount_limit:
                raise UserError(_("Unauthorized other account  amount"))
