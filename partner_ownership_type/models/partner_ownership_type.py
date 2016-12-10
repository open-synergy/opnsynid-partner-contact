# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class PartnerOwnershipType(models.Model):
    _name = "partner.ownership_type"
    _description = "Partner Ownership Type"

    name = fields.Char(
        string="Ownership Type",
        required=True,
    )
    notes = fields.Text(
        string="Notes"
    )
    active = fields.Boolean(
        string="Active"
    )
