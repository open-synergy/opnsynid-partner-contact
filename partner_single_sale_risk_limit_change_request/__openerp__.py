# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Partner Single Sale Risk Limit Change Request",
    "version": "8.0.1.0.0",
    "category": "Partner",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "auto_install": True,
    "depends": [
        "partner_single_sale_risk",
        "partner_financial_risk_limit_change_request",
    ],
    "data": [
        "views/partner_risk_limit_change_request_views.xml",
    ],
}
