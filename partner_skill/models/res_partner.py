# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from openerp import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    skill_ids = fields.One2many(
        comodel_name="partner.skill",
        string="Skill",
        inverse_name="partner_id",
    )
