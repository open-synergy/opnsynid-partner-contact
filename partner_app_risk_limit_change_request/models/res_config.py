# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ResConfig(models.TransientModel):
    _inherit = "partner.partner_risk_config_setting"

    partner_risk_limit_change_sequence_id = fields.Many2one(
        string="Partner Risk Limit Change Request Sequence",
        comodel_name="ir.sequence",
        related="company_id.partner_risk_limit_change_sequence_id",
        store=False,
    )
    partner_risk_limit_change_confirm_grp_ids = fields.Many2many(
        string="Allowed To Confirm Partner Risk Limit Change Request",
        comodel_name="res.groups",
        related="company_id.partner_risk_limit_change_confirm_grp_ids",
        store=False,
    )
    partner_risk_limit_change_done_grp_ids = fields.Many2many(
        string="Allowed To Validate Partner Risk Limit Change Request",
        comodel_name="res.groups",
        related="company_id.partner_risk_limit_change_done_grp_ids",
        store=False,
    )
    partner_risk_limit_change_cancel_grp_ids = fields.Many2many(
        string="Allowed To Cancel Partner Risk Limit Change Request",
        comodel_name="res.groups",
        related="company_id.partner_risk_limit_change_cancel_grp_ids",
        store=False,
    )
    partner_risk_limit_change_restart_grp_ids = fields.Many2many(
        string="Allowed To Restart Partner Risk Limit Change Request",
        comodel_name="res.groups",
        related="company_id.partner_risk_limit_change_restart_grp_ids",
        store=False,
    )
