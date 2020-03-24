# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import fields, models


class ResPartnerBank(models.Model):
    _inherit = "res.partner.bank"

    active = fields.Boolean(
        string="Active",
        default=True,
    )
