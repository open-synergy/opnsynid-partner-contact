# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class PartnerRiskLimitChangeRequest(models.Model):
    _inherit = "partner.risk_limit_change_request"

    risk_single_sale_order = fields.Float(
        string="Single Sale Order Risk",
        required=True,
        default=0.0,
        copy=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )

    @api.multi
    def _prepare_partner_data(self):
        self.ensure_one()
        _super = super(PartnerRiskLimitChangeRequest, self)
        result = _super._prepare_partner_data()
        if self.risk_single_sale_order:
            result.update(
                {"risk_single_sale_order_limit": self.risk_single_sale_order})
        return result
