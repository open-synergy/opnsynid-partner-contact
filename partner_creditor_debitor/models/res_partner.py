# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from openerp import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    creditor_ids = fields.Many2many(
        string="Creditors",
        comodel_name="res.partner",
        domain=[
            ("parent_id", "=", False),
        ],
        relation="rel_partner_creditor_debitor",
        column1="debitor_id",
        column2="creditor_id",
    )
    primary_creditor_id = fields.Many2one(
        string="Primary Creditor",
        comodel_name="res.partner",
        domain=[
            ("parent_id", "=", False),
        ],
    )
    debitor_ids = fields.Many2many(
        string="Debitors",
        comodel_name="res.partner",
        domain=[
            ("parent_id", "=", False),
        ],
        relation="rel_partner_creditor_debitor",
        column1="creditor_id",
        column2="debitor_id",
    )
