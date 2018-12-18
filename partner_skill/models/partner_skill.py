# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class PartnerSkill(models.Model):
    _name = "partner.skill"
    _description = "Partner Skill"

    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
        required=True,
        ondelete="cascade",
    )
    skill_id = fields.Many2one(
        string="Skill",
        comodel_name="hr.skill",
        required=True,
    )
    level_id = fields.Many2one(
        string="Level",
        comodel_name="hr.skill_level",
        required=True,
    )
