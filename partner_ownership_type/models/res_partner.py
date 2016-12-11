# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    ownership_type_id = fields.Many2one(
        string="Ownership Type",
        comodel_name="partner.ownership_type"
    )
