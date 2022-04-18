# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class PartnerRiskLimitPolicy(models.Model):
    _inherit = "partner.risk_limit_policy"

    single_sale_order_limit = fields.Float(
        string="Single Sale Order Limit",
        default=0.0,
        track_visibility="onchange",
    )
    unset_single_sale_order_limit = fields.Boolean(
        string="Unset Single Sale Order Limit",
    )
