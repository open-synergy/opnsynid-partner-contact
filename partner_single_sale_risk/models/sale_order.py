# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api
from openerp.tools.translate import _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def action_button_confirm(self):
        if not self.env.context.get("bypass_risk", False):
            for order in self:
                partner = order.partner_id.commercial_partner_id
                exception_msg = ""
                if partner.risk_single_sale_order_limit and \
                        (order.amount_total >
                         partner.risk_single_sale_order_limit):
                    exception_msg = _(
                        "This sale order exceeds the single sale order limit")
                if exception_msg:
                    return self.env["partner.risk.exceeded.wiz"].create({
                        "exception_msg": exception_msg,
                        "partner_id": partner.id,
                        "origin_reference": "%s,%s" % (self._model, self.id),
                        "continue_method": "action_button_confirm",
                    }).action_show()
        return super(SaleOrder, self).action_button_confirm()
