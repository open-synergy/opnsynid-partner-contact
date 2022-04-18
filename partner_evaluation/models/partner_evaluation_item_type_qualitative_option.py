# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class PartnerEvaluationItemTypeQualitativeOption(models.Model):
    _name = "partner.evaluation_item_type_qualitative_option"
    _description = "Measurement Item Type Qualitative Option"
    _order = "sequence, id"

    name = fields.Char(
        string="Option",
        required=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    type_id = fields.Many2one(
        string="Evaluation Item Type",
        comodel_name="partner.evaluation_item_type",
        required=True,
        ondelete="restrict",
    )
    sequence = fields.Integer(
        string="Sequence",
        default=5,
        required=True,
    )
    quantitative_value = fields.Float(
        string="Quantitative Value",
        required=True,
        default=0.0,
    )
    note = fields.Text(
        string="Note",
    )
