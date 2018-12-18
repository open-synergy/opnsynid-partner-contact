# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class Skill(models.Model):
    _name = "hr.skill_level"
    _description = "Skill Level"
    _order = "sequence desc"

    name = fields.Char(
        string="Level",
        required=True,
    )
    sequence = fields.Integer(
        string="Sequence",
        default=5,
        required=True,
    )
    description = fields.Text(
        string="Description",
    )
    skill_id = fields.Many2one(
        string="Skill",
        comodel_name="hr.skill",
        required=True,
        ondelete="cascade",
    )
