# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class Skill(models.Model):
    _inherit = "hr.skill"

    partner_ids = fields.Many2many(
        comodel_name="res.partner",
        relation="skill_partner_rel",
        column1="skill_id",
        column2="partner_id",
        string="Partner(s)"
    )
