# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Partner Skills",
    "version": "8.0.1.1.1",
    "category": "Partner",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["hr_skill"],
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_views.xml",
        "views/hr_skill_views.xml",
    ],
}
