# -*- coding: utf-8 -*-
# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ResPartnerRelatedPartyRelation(models.Model):
    _name = "res.partner.related_party"
    _description = "Partner Related Party"

    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
        required=True,
    )
    relationship_type_id = fields.Many2one(
        string="Relationship Type",
        comodel_name="res.partner.related_party_relationship_type",
        required=True,
    )
    transaction_type_id = fields.Many2one(
        string="Transaction Type",
        comodel_name="res.partner.related_party_transaction_type",
        required=True,
    )
