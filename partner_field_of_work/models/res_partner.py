# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from openerp import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    field_of_work_id = fields.Many2one(
        string="Field of Work",
        comodel_name="partner.field_of_work",
    )
