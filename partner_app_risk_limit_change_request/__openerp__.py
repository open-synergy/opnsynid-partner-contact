# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Partner App - Risk Limit Change Request Extension",
    "version": "8.0.2.0.0",
    "category": "Partner",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "auto_install": True,
    "depends": [
        "partner_app_partner_risk",
        "partner_financial_risk_limit_change_request",
    ],
    "data": [
        "views/partner_risk_config_setting_views.xml",
        "views/res_partner_view.xml",
    ],
}
