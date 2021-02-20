# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Partner Management Application - sale",
    "version": "8.0.1.0.0",
    "category": "Partner",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "auto_install": True,
    "depends": [
        "partner_app",
        "sale",
    ],
    "data": [
        "views/res_partner_view.xml",
    ],
}
