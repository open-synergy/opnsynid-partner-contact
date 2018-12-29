# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from openerp import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    ethnicity_id = fields.Many2one(
        string="Ethnicity",
        comodel_name="partner.ethnicity",
    )
