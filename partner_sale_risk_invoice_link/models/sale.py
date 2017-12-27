# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    invoice_amount = fields.Float(
        compute="_compute_invoice_amount",
        store=True,
    )
    invoice_pending_amount = fields.Float(
        compute="_compute_invoice_amount",
        store=True,
    )

    @api.multi
    @api.depends(
        "state",
        "invoice_ids",
        "invoice_ids.amount_total",
        "order_line.invoice_lines.invoice_id.amount_total",
    )
    def _compute_invoice_amount(self):
        AccountInvoice = self.env["account.invoice"]
        for order in self:
            order.invoice_pending_amount = order.amount_total
            invoice_ids = order.order_line.mapped("invoice_lines").mapped(
                "invoice_id").ids
            invoice_ids += order.mapped("invoice_ids").ids
            if order.picking_ids:
                picking_ids = order.picking_ids.ids
                criteria = [
                    ("id", "in", picking_ids),
                    ("invoice_state", "=", "invoiced"),
                ]
                pickings = self.env["stock.picking"].search(criteria)
                if len(pickings) > 0:
                    for picking in pickings:
                        for invoice in picking.invoice_ids:
                            invoice_ids.append(invoice.id)
            if not invoice_ids:
                continue
            amount = AccountInvoice.read_group(
                [("id", "in", invoice_ids),
                 ("type", "in", ["out_invoice", "out_refund"])],
                ["amount_total"],
                []
            )[0]["amount_total"]
            order.invoice_amount = amount
            if order.amount_total > amount:
                order.invoice_pending_amount = order.amount_total - amount
