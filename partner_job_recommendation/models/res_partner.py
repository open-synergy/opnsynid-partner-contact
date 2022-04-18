# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from openerp import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    job_recommendation_ids = fields.Many2many(
        string="Job Recommendations",
        comodel_name="res.partner",
        relation="rel_partner_job_recommendation",
        column1="partner_id",
        column2="job_recommendation_id",
        domain=[
            ("is_company", "=", False),
        ],
    )
