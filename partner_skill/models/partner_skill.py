# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models, api, _
from openerp.exceptions import Warning as UserError


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

    @api.constrains(
        "partner_id",
        "skill_id",
    )
    def _check_no_duplicate_skill(self):
        obj_skill = self.env["partner.skill"]
        for skill in self:
            criteria = [
                ("id", "!=", skill.id),
                ("partner_id", "=", skill.partner_id.id),
                ("skill_id", "=", skill.skill_id.id)
            ]
            result = obj_skill.search_count(criteria)
            if result > 0:
                msg = _("No duplicate skill")
                raise UserError(msg)
