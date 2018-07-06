# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Partner Experiences",
    "version": "8.0.1.0.0",
    "category": "Partner",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_experience"
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/partner_security.xml",
        "views/res_partner_views.xml",
        "views/partner_academic_view.xml",
        "views/partner_experience_view.xml",
        "views/partner_certification_view.xml",
    ],
}
