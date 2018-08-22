# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class PartnerExperience(models.Model):
    _name = "partner.experience"
    _inherit = "partner.curriculum"

    category = fields.Selection(
        selection=[
            ("professional", "Professional"),
            ("academic", "Academic"),
            ("certification", "Certification")
        ],
        string="Category",
        required=True,
        default="professional",
        help="Category"
    )
    job_id = fields.Many2one(
        string="Position",
        comodel_name="res.partner.job_position",
        )
    job_level_id = fields.Many2one(
        string="Job Level",
        comodel_name="partner.job_level",
        )
