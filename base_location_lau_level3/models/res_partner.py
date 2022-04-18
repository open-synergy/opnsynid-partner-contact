# -*- coding: utf-8 -*-
# Copyright 2017 Andhitia Rama
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    lau3_id = fields.Many2one(
        "res.partner.lau", "Local Admin. Unit 3", domain=[("level", "=", 3)]
    )

    @api.multi
    @api.onchange("lau2_id")
    def _onchange_lau2(self):
        for p in self:
            if p.lau3_id and p.lau3_id.parent_id != p.lau2_id:
                p.lau3_id = None
