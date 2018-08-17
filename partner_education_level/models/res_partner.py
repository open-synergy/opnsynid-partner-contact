# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from openerp import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    formal_education_level_id = fields.Many2one(
        string="Latest Formal Level Education",
        comodel_name="partner.formal_education_level",
    )
