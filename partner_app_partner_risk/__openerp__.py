# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Partner App - Partner Risk Extension",
    "version": "8.0.2.0.0",
    "category": "Partner",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "auto_install": True,
    "depends": [
        "partner_app_account",
        "partner_financial_risk",
    ],
    "data": [
        "menu.xml",
        "views/partner_risk_config_setting_views.xml",
    ],
}
