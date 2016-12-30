# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Partner's Management Application",
    "version": "8.0.1.0.1",
    "summary": "Base module to manage partner",
    "category": "Partner",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "application": True,
    "depends": [
        "base",
    ],
    "data": [
        "security/res_groups.xml",
        "views/res_partner_view.xml",
    ],
}
