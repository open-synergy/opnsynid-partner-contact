# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api
from openerp.exceptions import Warning as UserError
from openerp.tools.translate import _


class PartnerRiskAdjustment(models.Model):
    _name = "partner.risk_adjustment"
    _inherit = ["mail.thread"]
    _description = "Partner Risk Adjustment"

    @api.model
    def _default_company_id(self):
        return self.env.user.company_id.id

    name = fields.Char(
        string="# Risk Adjustment",
        required=True,
        default="/",
        copy=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        required=True,
        default=lambda self: self._default_company_id(),
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    partner_id = fields.Many2one(
        string="Customer",
        comodel_name="res.partner",
        required=True,
        domain=[
            ("customer", "=", True),
        ],
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    risk_invoice_draft = fields.Float(
        string="Total Draft Invoice Adjustment",
        required=True,
        default=0.0,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    risk_invoice_open = fields.Float(
        string="Total Open Invoice Adjustment",
        required=True,
        default=0.0,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    risk_invoice_unpaid = fields.Float(
        string="Total Unpaid Invoice Adjustment",
        required=True,
        default=0.0,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    risk_account_amount = fields.Float(
        string="Total Account Amount Adjustment",
        required=True,
        default=0.0,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    reason = fields.Text(
        string="Reason",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting for Approval"),
            ("done", "Done"),
            ("cancel", "Cancelled"),
        ],
        default="draft",
        required=True,
        readonly=True,
        copy=False,
    )
    confirmed_date = fields.Datetime(
        string="Confirmation Date",
        readonly=True,
        copy=False,
    )
    confirmed_user_id = fields.Many2one(
        string="Confirmation By",
        comodel_name="res.users",
        readonly=True,
        copy=False,
    )
    done_date = fields.Datetime(
        string="Approval Date",
        readonly=True,
        copy=False,
    )
    done_user_id = fields.Many2one(
        string="Approval By",
        comodel_name="res.users",
        readonly=True,
        copy=False,
    )
    cancelled_date = fields.Datetime(
        string="Cancellation Date",
        readonly=True,
        copy=False,
    )
    cancelled_user_id = fields.Many2one(
        string="Cancellation By",
        comodel_name="res.users",
        readonly=True,
        copy=False,
    )

    @api.multi
    def action_confirm(self):
        for adjustment in self:
            data = adjustment._prepare_confirm_data()
            adjustment.write(data)

    @api.multi
    def action_done(self):
        for adjustment in self:
            data = adjustment._prepare_done_data()
            adjustment.write(data)

    @api.multi
    def action_cancel(self):
        for adjustment in self:
            data = adjustment._prepare_cancel_data()
            adjustment.write(data)

    @api.multi
    def action_reset(self):
        for adjustment in self:
            data = adjustment._prepare_reset_data()
            adjustment.write(data)

    @api.multi
    def _prepare_confirm_data(self):
        self.ensure_one()
        data = {
            "state": "confirm",
            "confirmed_date": fields.Datetime.now(),
            "confirmed_user_id": self.env.user.id,
        }
        return data

    @api.multi
    def _prepare_done_data(self):
        self.ensure_one()
        data = {
            "state": "done",
            "done_date": fields.Datetime.now(),
            "done_user_id": self.env.user.id,
        }
        return data

    @api.multi
    def _prepare_cancel_data(self):
        self.ensure_one()
        data = {
            "state": "cancel",
            "cancel_date": fields.Datetime.now(),
            "cancel_user_id": self.env.user.id,
        }
        return data

    @api.multi
    def _prepare_reset_data(self):
        self.ensure_one()
        data = {
            "state": "draft",
            "confirmed_date": False,
            "confirmed_user_id": False,
            "done_date": False,
            "done_user_id": False,
            "cancel_date": False,
            "cancel_user_id": False,
        }
        return data

    @api.model
    def _prepare_create_data(self, values):
        name = values.get("name", False)
        if name == "/" or not name:
            values["name"] = self._create_sequence()

        return values

    @api.model
    def _create_sequence(self):
        sequence_id = self._get_sequence()
        sequence = self.env["ir.sequence"].\
            next_by_id(sequence_id)
        return sequence

    @api.model
    def _get_sequence(self):
        result = self.env.ref(
            "partner_financial_risk_adjustment.sequence_risk_adjustment")
        return result.id

    @api.model
    def create(self, values):
        values = self._prepare_create_data(values)
        _super = super(PartnerRiskAdjustment, self)
        return _super.create(values)

    @api.multi
    def unlink(self):
        strWarning = _("You can only delete data on draft state")
        for adj in self:
            if adj.state != "draft":
                if not self.env.context.get("force_unlink", False):
                    raise UserError(strWarning)
        _super = super(PartnerRiskAdjustment, self)
        _super.unlink()
