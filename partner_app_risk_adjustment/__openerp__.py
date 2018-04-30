# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Partner Management Application - Risk Adjustment Extension",
    "version": "8.0.1.0.0",
    "category": "Partner",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "auto_install": True,
    "depends": [
        "partner_app_partner_risk",
        "partner_financial_risk_adjustment",
    ],
    "data": [
        "views/partner_risk_config_setting_views.xml",
        "views/res_partner_view.xml",
    ],
}
