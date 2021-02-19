# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Partner Single Sale Risk Configuration Policy",
    "version": "8.0.2.1.0",
    "category": "Partner",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "partner_financial_risk_policy",
        "partner_single_sale_risk",
    ],
    "data": [
        "views/partner_risk_limit_policy_views.xml",
        "views/res_partner_views.xml",
    ],
}
