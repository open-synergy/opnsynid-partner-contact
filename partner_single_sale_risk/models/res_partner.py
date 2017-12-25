# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    risk_single_sale_order_limit = fields.Float(
        string="Limit Single Sale Order",
        help="Set 0 if it is not locked",
    )
