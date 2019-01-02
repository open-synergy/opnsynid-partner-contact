# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from openerp import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    father_id = fields.Many2one(
        string="Father",
        comodel_name="res.partner",
        domain=[
            ("is_company", "=", False),
            ("parent_id", "=", False),
            ("gender", "=", "male"),

        ],
    )
    mother_id = fields.Many2one(
        string="Mother",
        comodel_name="res.partner",
        domain=[
            ("is_company", "=", False),
            ("parent_id", "=", False),
            ("gender", "=", "female"),
        ],
    )
    spouse_id = fields.Many2one(
        string="Spouse",
        comodel_name="res.partner",
        domain=[
            ("is_company", "=", False),
            ("parent_id", "=", False),
        ],
    )
    guardian_id = fields.Many2one(
        string="Guardian",
        comodel_name="res.partner",
        domain=[
            ("is_company", "=", False),
            ("parent_id", "=", False),
        ],
    )
