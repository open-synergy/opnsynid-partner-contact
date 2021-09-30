# -*- coding: utf-8 -*-
# Copyright 2021 PT Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    related_party_ids = fields.One2many(
        comodel_name="res.partner.related_party",
        inverse_name="partner_id",
        string="Partner Related Party",
    )
