# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class PartnerFieldOfStudy(models.Model):
    _name = "partner.field_of_study"
    _description = "Field of Study"

    name = fields.Char(
        string="Field of Study",
        required=True,
    )
    code = fields.Char(
        string="Code",
    )
    parent_id = fields.Many2one(
        string="Parent",
        comodel_name="partner.field_of_study",
    )
    note = fields.Text(
        string="Note",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
