# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Partner Risk Configuration Policy",
    "version": "8.0.4.1.2",
    "category": "Partner",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "partner_financial_risk",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/partner_risk_limit_policy_views.xml",
        "views/res_partner_views.xml",
    ],
}
