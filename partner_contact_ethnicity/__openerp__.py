# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Contact Ethnicity",
    "version": "8.0.1.0.0",
    "category": "Partner",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "partner_contact_personal_information_page",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/partner_ethnicity_views.xml",
        "views/res_partner_views.xml",
    ],
}
