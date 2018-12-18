# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class Skill(models.Model):
    _inherit = "hr.skill"

    level_ids = fields.One2many(
        string="Rating",
        comodel_name="hr.skill_level",
        inverse_name="skill_id",
    )
