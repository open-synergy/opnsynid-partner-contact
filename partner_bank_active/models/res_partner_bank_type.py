# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import fields, models


class ResPartnerBankType(models.Model):
    _inherit = "res.partner.bank.type"

    active = fields.Boolean(
        string="Active",
        default=True,
    )
