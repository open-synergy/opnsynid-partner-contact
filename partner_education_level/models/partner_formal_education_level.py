# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class PartnerFormalEducationLevel(models.Model):
    _name = "partner.formal_education_level"
    _description = "Formal Education Level"

    name = fields.Char(
        string="Education Level",
        required=True,
    )
    code = fields.Char(
        string="Code",
    )
    sequence = fields.Integer(
        string="Sequence",
        required=True,
        default=5,
    )
    note = fields.Text(
        string="Note",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
