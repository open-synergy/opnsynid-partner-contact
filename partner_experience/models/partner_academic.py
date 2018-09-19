# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class PartnerAcademic(models.Model):
    _name = "partner.academic"
    _inherit = "partner.curriculum"

    # TODO: Remove
    diploma = fields.Char(
        string="Diploma",
        translate=True
    )
    # TODO: Remove
    study_field = fields.Char(
        string="Field of study",
        translate=True
    )
    education_level_id = fields.Many2one(
        string="Education Level",
        comodel_name="partner.formal_education_level",
        )
    field_of_study_id = fields.Many2one(
        string="Field of Study",
        comodel_name="partner.field_of_study",
        )
    gpa = fields.Float(
        string="Latest GPA",
        )
    activities = fields.Text(
        string="Activities and associations",
        translate=True
    )
