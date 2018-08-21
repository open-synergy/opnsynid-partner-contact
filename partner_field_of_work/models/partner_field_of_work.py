# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class PartnerFieldOfWork(models.Model):
    _name = "partner.field_of_work"
    _description = "Field of Work"

    name = fields.Char(
        string="Field of Work",
        required=True,
    )
    code = fields.Char(
        string="Code",
    )
    note = fields.Text(
        string="Note",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
