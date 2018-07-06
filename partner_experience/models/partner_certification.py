# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class PartnerCertification(models.Model):
    _name = "partner.certification"
    _inherit = "partner.curriculum"

    certification = fields.Char(
        string="Certification Number",
        help="Certification Number"
    )
