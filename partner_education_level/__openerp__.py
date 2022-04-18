# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Partner Education Level",
    "version": "8.0.1.5.0",
    "category": "Partner",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/partner_formal_education_level_views.xml",
        "views/partner_field_of_study_views.xml",
        "views/res_partner_views.xml",
    ],
}
