# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class PartnerRiskAdjustment(models.Model):
    _inherit = "partner.risk_adjustment"

    risk_sale_order = fields.Float(
        string="Total Sale Order Adjustment",
        required=True,
        default=0.0,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
