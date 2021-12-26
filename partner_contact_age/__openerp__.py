# -*- coding: utf-8 -*-
# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author/

{
    "name": "Partner Contact Age",
    "version": "8.0.1.0.0",
    "category": "Partner",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "website": "https://simetri-sinergi.id",
    "license": "AGPL-3",
    "depends": [
        "partner_contact_birthdate",
    ],
    "data": [
        "data/res_partner_age_cron.xml",
        "views/res_partner_views.xml",
    ],
    "installable": True,
}
