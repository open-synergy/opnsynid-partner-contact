# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    # Accountant Config
    partner_risk_limit_change_sequence_id = fields.Many2one(
        string="Partner Risk Limit Change Request Sequence",
        comodel_name="ir.sequence",
    )
    partner_risk_limit_change_confirm_grp_ids = fields.Many2many(
        string="Allowed To Confirm Partner Risk Limit Change Request",
        comodel_name="res.groups",
        relation="rel_partner_risk_limit_change_allowed_confirm_groups",
        column1="company_id",
        column2="group_id",
    )
    partner_risk_limit_change_done_grp_ids = fields.Many2many(
        string="Allowed To Validate Partner Risk Limit Change Request",
        comodel_name="res.groups",
        relation="rel_partner_risk_limit_change_allowed_done_groups",
        column1="company_id",
        column2="group_id",
    )
    partner_risk_limit_change_cancel_grp_ids = fields.Many2many(
        string="Allowed To Cancel Partner Risk Limit Change Request",
        comodel_name="res.groups",
        relation="rel_partner_risk_limit_change_allowed_cancel_groups",
        column1="company_id",
        column2="group_id",
    )
    partner_risk_limit_change_restart_grp_ids = fields.Many2many(
        string="Allowed To Restart Partner Risk Limit Change Request",
        comodel_name="res.groups",
        relation="rel_partner_risk_limit_change_allowed_restart_groups",
        column1="company_id",
        column2="group_id",
    )

    @api.model
    def _get_partner_risk_limit_change_button_policy_map(self):
        return [
            ("confirm_ok", "partner_risk_limit_change_confirm_grp_ids"),
            ("done_ok", "partner_risk_limit_change_done_grp_ids"),
            ("cancel_ok", "partner_risk_limit_change_cancel_grp_ids"),
            ("restart_ok", "partner_risk_limit_change_restart_grp_ids"),
        ]

    @api.multi
    def _get_partner_risk_limit_change_button_policy(self, policy_field):
        self.ensure_one()
        result = False
        button_group_ids = []
        user = self.env.user
        group_ids = user.groups_id.ids

        button_group_ids += getattr(self, policy_field).ids

        if not button_group_ids:
            result = True
        else:
            if set(button_group_ids) & set(group_ids):
                result = True
        return result
