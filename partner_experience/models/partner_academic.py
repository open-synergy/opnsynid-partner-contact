# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class PartnerAcademic(models.Model):
    _name = "partner.academic"
    _inherit = "partner.curriculum"

    diploma = fields.Char(
        string="Diploma",
        translate=True
    )
    study_field = fields.Char(
        string="Field of study",
        translate=True
    )
    activities = fields.Text(
        string="Activities and associations",
        translate=True
    )
