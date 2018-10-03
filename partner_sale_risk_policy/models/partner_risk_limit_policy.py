# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class PartnerRiskLimitPolicy(models.Model):
    _inherit = "partner.risk_limit_policy"

    sale_order_limit = fields.Float(
        string="Sale Order Limit",
        default=0.0,
        track_visibility="onchange",
    )
    unset_sale_order_limit = fields.Boolean(
        string="Unset Sale Order Limit",
    )
