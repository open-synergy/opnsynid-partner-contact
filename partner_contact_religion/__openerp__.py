# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Contact Religion",
    "version": "8.0.1.1.0",
    "category": "Partner",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "partner_contact_personal_information_page",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/partner_religion_views.xml",
        "views/res_partner_views.xml",
    ],
}
