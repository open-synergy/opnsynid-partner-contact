# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class PartnerCurriculum(models.Model):
    _name = "partner.curriculum"
    _description = "Partner's Curriculum"
    _inherit = "ir.needaction_mixin"

    name = fields.Char(
        string="Name",
        required=True
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner",
        required=True,
        domain="[('is_company', '=', False)]"
    )
    start_date = fields.Date(
        string="Start date"
    )
    end_date = fields.Date(
        string="End date"
    )
    description = fields.Text(
        string="Description"
    )
    partner_address_id = fields.Many2one(
        comodel_name="res.partner",
        string="Address",
        help="Employer, School, University, "
             "Certification Authority"
    )
    location = fields.Char(
        string="Location",
        help="Location"
    )
    expire = fields.Boolean(
        string="Expire",
        help="Expire",
        default=True
    )
