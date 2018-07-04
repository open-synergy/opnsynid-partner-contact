# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from openerp import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    skill_ids = fields.Many2many(
        comodel_name="hr.skill",
        relation="skill_partner_rel",
        column1="partner_id",
        column2="skill_id",
        string="Skills",
        domain="[('child_ids', '=', False)]",
    )
