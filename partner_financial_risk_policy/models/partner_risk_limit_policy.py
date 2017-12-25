# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class PartnerRiskLimitPolicy(models.Model):
    _name = "partner.risk_limit_policy"
    _description = "Partner Risk Limit Policy"
    _order = "sequence"

    @api.multi
    @api.depends(
        "group_ids", "group_ids.users",
    )
    def _compute_user(self):
        for policy in self:
            users = self.env["res.users"]
            for group in policy.group_ids:
                users += group.users
            policy.user_ids = users

    name = fields.Char(
        string="Ownership Type",
        required=True,
    )
    notes = fields.Text(
        string="Notes"
    )
    active = fields.Boolean(
        string="Active",
        default=True
    )
    sequence = fields.Integer(
        string="Sequence",
        default=5,
    )
    group_ids = fields.Many2many(
        string="Groups",
        comodel_name="res.groups",
        relation="rel_group_partner_risk_policy",
        column1="policy_id",
        column2="group_id",
    )
    user_ids = fields.Many2many(
        string="Users",
        comodel_name="res.users",
        relation="rel_user_partner_risk_policy",
        column1="policy_id",
        column2="user_id",
        compute="_compute_user",
        store=True,
    )
    total_risk_limit = fields.Float(
        string="Total Risk Limit",
        default=0.0,
    )
    invoice_draft_limit = fields.Float(
        string="Draft Invoice Limit",
        default=0.0,
    )
    invoice_open_limit = fields.Float(
        string="Open Invoice Limit",
        default=0.0,
    )
    invoice_unpaid_limit = fields.Float(
        string="Unpaid Invoice Limit",
        default=0.0,
    )
    account_amount_limit = fields.Float(
        string="Other Account Amount Limit",
        default=0.0,
    )
