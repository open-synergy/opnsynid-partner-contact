# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models
from openerp.exceptions import Warning as UserError
from openerp.tools.translate import _


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.multi
    def _compute_policy(self):
        total_risk = (
            invoice_draft
        ) = invoice_open = invoice_unpaid = account_amount = 0.0
        unset_total_risk = (
            unset_invoice_open
        ) = unset_invoice_draft = unset_invoice_unpaid = unset_account_amount = False
        criteria = [
            ("user_ids.id", "in", [self.env.user.id]),
        ]
        policy = self.env["partner.risk_limit_policy"].search(criteria, limit=1)
        if len(policy) == 1:
            total_risk = policy.total_risk_limit
            invoice_draft = policy.invoice_draft_limit
            invoice_open = policy.invoice_open_limit
            invoice_unpaid = policy.invoice_unpaid_limit
            account_amount = policy.account_amount_limit
            unset_total_risk = policy.unset_total_risk_limit
            unset_invoice_draft = policy.unset_invoice_draft_limit
            unset_invoice_open = policy.unset_invoice_open_limit
            unset_invoice_unpaid = policy.unset_invoice_unpaid_limit
            unset_account_amount = policy.unset_account_amount_limit

        for partner in self:
            partner.total_risk_limit_policy = total_risk
            partner.invoice_draft_limit_policy = invoice_draft
            partner.invoice_open_limit_policy = invoice_open
            partner.invoice_unpaid_limit_policy = invoice_unpaid
            partner.account_amount_limit_policy = account_amount
            partner.unset_total_risk_limit_policy = unset_total_risk
            partner.unset_invoice_draft_limit_policy = unset_invoice_draft
            partner.unset_invoice_open_limit_policy = unset_invoice_open
            partner.unset_invoice_unpaid_limit_policy = unset_invoice_unpaid
            partner.unset_account_amount_limit_policy = unset_account_amount

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
    unset_total_risk_limit_policy = fields.Boolean(
        string="Unset Total Risk Limit Policy",
        compute="_compute_policy",
        store=False,
    )
    unset_invoice_draft_limit_policy = fields.Boolean(
        string="Unset Invoice Draft Limit Policy",
        compute="_compute_policy",
        store=False,
    )
    unset_invoice_open_limit_policy = fields.Boolean(
        string="Unset Invoice Open Limit Policy",
        compute="_compute_policy",
        store=False,
    )
    unset_invoice_unpaid_limit_policy = fields.Boolean(
        string="Unset Invoice Unpaid Limit Policy",
        compute="_compute_policy",
        store=False,
    )
    unset_account_amount_limit_policy = fields.Boolean(
        string="Unset Other Account Amount Limit Policy",
        compute="_compute_policy",
        store=False,
    )

    def _commercial_fields(self, cr, uid, context=None):
        res = super(ResPartner, self)._commercial_fields(cr, uid, context=None)
        res.remove("credit_limit")
        return res

    @api.multi
    def write(self, values):
        ctx = self._update_limit_check_context(values)
        _super = super(ResPartner, self.with_context(ctx))
        return _super.write(values)

    @api.model
    def create(self, values):
        ctx = self._update_limit_check_context(values)
        _super = super(ResPartner, self.with_context(ctx))
        return _super.create(values)

    @api.model
    def _update_limit_check_context(self, values):
        ctx = self.env.context.copy()
        for field in iter(values):
            if field == "credit_limit":
                ctx.update({"check_credit_limit": True})
            elif field == "risk_invoice_draft_limit":
                ctx.update({"check_invoice_draft_limit": True})
            elif field == "risk_invoice_open_limit":
                ctx.update({"check_invoice_open_limit": True})
            elif field == "risk_invoice_unpaid_limit":
                ctx.update({"check_invoice_unpaid_limit": True})
            elif field == "risk_account_amount_limit":
                ctx.update({"check_account_amount_limit": True})
        return ctx

    @api.constrains(
        "credit_limit",
        "risk_invoice_draft_limit",
        "risk_invoice_open_limit",
        "risk_invoice_unpaid_limit",
        "risk_account_amount_limit",
    )
    def _check_limit_policy(self):
        for partner in self:
            if (
                partner.total_risk_limit_policy
                and partner.total_risk_limit_policy < partner.credit_limit
                and partner.credit_limit > 0.0
                and self.env.context.get("check_credit_limit", False)
            ):
                raise UserError(_("Unauthorized credit limit amount"))

            if (
                partner.invoice_draft_limit_policy
                and partner.invoice_draft_limit_policy
                < partner.risk_invoice_draft_limit
                and partner.risk_invoice_draft_limit > 0.0
                and self.env.context.get("check_invoice_draft_limit", False)
            ):
                raise UserError(_("Unauthorized invoice draft amount"))

            if (
                partner.invoice_open_limit_policy
                and partner.invoice_open_limit_policy < partner.risk_invoice_open_limit
                and partner.risk_invoice_open_limit > 0.0
                and self.env.context.get("check_invoice_open_limit", False)
            ):
                raise UserError(_("Unauthorized invoice open amount"))

            if (
                partner.invoice_unpaid_limit_policy
                and partner.invoice_unpaid_limit_policy
                < partner.risk_invoice_unpaid_limit
                and partner.risk_invoice_unpaid_limit > 0.0
                and self.env.context.get("check_invoice_unpaid_limit", False)
            ):
                raise UserError(_("Unauthorized invoice unpaid amount"))

            if (
                partner.account_amount_limit_policy
                and partner.account_amount_limit_policy
                < partner.risk_account_amount_limit
                and partner.risk_account_amount_limit > 0.0
                and self.env.context.get("check_account_amount_limit", False)
            ):
                raise UserError(_("Unauthorized other account amount"))

            if (
                not partner.unset_total_risk_limit_policy
                and partner.credit_limit <= 0.0
                and self.env.context.get("check_credit_limit", False)
            ):
                raise UserError(_("Unauthorized to unset credit limit amount"))

            if (
                not partner.unset_invoice_draft_limit_policy
                and partner.risk_invoice_draft_limit <= 0.0
                and self.env.context.get("check_invoice_draft_limit", False)
            ):
                err_msg = _("Unauthorized to unset invoice draft amount")
                raise UserError(err_msg)

            if (
                not partner.unset_invoice_open_limit_policy
                and partner.risk_invoice_open_limit <= 0.0
                and self.env.context.get("check_invoice_open_limit", False)
            ):
                err_msg = _("Unauthorized to unset invoice open amount")
                raise UserError(err_msg)

            if (
                not partner.unset_invoice_unpaid_limit_policy
                and partner.risk_invoice_unpaid_limit <= 0.0
                and self.env.context.get("check_invoice_unpaid_limit", False)
            ):
                err_msg = _("Unauthorized to unset invoice unpaid amount")
                raise UserError(err_msg)

            if (
                not partner.unset_account_amount_limit_policy
                and partner.risk_account_amount_limit <= 0.0
                and self.env.context.get("check_account_amount_limit", False)
            ):
                err_msg = _("Unauthorized to unset other account amount")
                raise UserError(err_msg)
