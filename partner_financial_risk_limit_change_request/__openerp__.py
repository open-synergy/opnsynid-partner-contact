# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Partner Financial Risk Limit Change Request",
    "version": "8.0.1.2.0",
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
        "views/partner_risk_limit_change_request_views.xml",
        "views/res_company_views.xml",
        "views/res_partner_views.xml",
    ],
}
