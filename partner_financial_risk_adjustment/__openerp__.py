# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Partner Financial Risk Adjustment",
    "version": "8.0.1.1.0",
    "category": "Partner",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "partner_financial_risk",
    ],
    "data": [
        "data/ir_sequence_data.xml",
        "security/ir.model.access.csv",
        "views/res_company_views.xml",
        "views/partner_risk_adjustment_views.xml",
        "views/res_partner_views.xml",
    ],
}
