# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import fields, models


class ResPartnerBankTypeField(models.Model):
    _inherit = "res.partner.bank.type.field"

    active = fields.Boolean(
        string="Active",
        default=True,
    )
