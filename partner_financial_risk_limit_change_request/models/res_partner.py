# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    risk_limit_change_request_ids = fields.One2many(
        string="Risk Limit Change Requests",
        comodel_name="partner.risk_limit_change_request",
        inverse_name="partner_id",
    )
