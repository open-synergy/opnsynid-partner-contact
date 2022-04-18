# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ResConfig(models.TransientModel):
    _inherit = "partner.partner_risk_config_setting"

    partner_risk_adjustment_sequence_id = fields.Many2one(
        string="Partner Risk Adjustment Sequence",
        comodel_name="ir.sequence",
        related="company_id.partner_risk_adjustment_sequence_id",
        store=False,
    )
    partner_risk_adjustment_confirm_grp_ids = fields.Many2many(
        string="Allowed To Confirm Partner Risk Adjustment",
        comodel_name="res.groups",
        related="company_id.partner_risk_adjustment_confirm_grp_ids",
        store=False,
    )
    partner_risk_adjustment_done_grp_ids = fields.Many2many(
        string="Allowed To Validate Partner Risk Adjustment",
        comodel_name="res.groups",
        related="company_id.partner_risk_adjustment_done_grp_ids",
        store=False,
    )
    partner_risk_adjustment_cancel_grp_ids = fields.Many2many(
        string="Allowed To Cancel Partner Risk Adjustment",
        comodel_name="res.groups",
        related="company_id.partner_risk_adjustment_cancel_grp_ids",
        store=False,
    )
    partner_risk_adjustment_restart_grp_ids = fields.Many2many(
        string="Allowed To Restart Partner Risk Adjustment",
        comodel_name="res.groups",
        related="company_id.partner_risk_adjustment_restart_grp_ids",
        store=False,
    )
