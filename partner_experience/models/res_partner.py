# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from openerp import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    academic_ids = fields.One2many(
        comodel_name="partner.academic",
        inverse_name="partner_id",
        string="Academic experiences",
        help="Academic experiences"
    )
    certification_ids = fields.One2many(
        comodel_name="partner.certification",
        inverse_name="partner_id",
        string="Certifications",
        help="Certifications"
    )
    experience_ids = fields.One2many(
        comodel_name="partner.experience",
        inverse_name="partner_id",
        string="Professional Experiences",
        help="Professional Experiences"
    )
