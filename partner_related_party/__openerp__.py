# -*- coding: utf-8 -*-
# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author/

{
    "name": "Partner Related Party",
    "version": "8.0.1.0.0",
    "category": "Partner",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "website": "https://simetri-sinergi.id",
    "license": "AGPL-3",
    "depends": [
        "partner_app",
    ],
    "data": [
        "security/ir.model.access.csv",
        "menu.xml",
        "views/res_partner_views.xml",
        "views/res_partner_related_party_relationship_type_views.xml",
        "views/res_partner_related_party_transaction_type_views.xml",
    ],
    "installable": True,
}
