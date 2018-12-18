# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import tools
from openerp import models, fields

LANGUAGE_RATING = [
    ("0", "0 - No Proficiency"),
    ("0+", "0+ - Memorized Proficiency"),
    ("1", "1 - Elementary Proficiency"),
    ("1+", "1+ - Elementary Proficiency, Plus"),
    ("2", "2 - Limited Working Proficiency"),
    ("2+", "2+ - Limited Working Proficiency, Plus"),
    ("3", "3 - General Professional Proficiency"),
    ("3+", "3+ - General Professional Proficiency, Plus"),
    ("4", "4 - Advance Professional Proficiency"),
    ("4+", "4+ - Advance Professional Proficiency, Plus"),
    ("5", "5 - Funcionally Native Proficiency"),
]


class PartnerLanguange(models.Model):
    _name = "partner.language"

    name = fields.Selection(
        selection=tools.scan_languages(),
        string="Language",
        required=True
    )
    description = fields.Char(
        string="Description",
        size=64,
        required=False
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner",
        required=True
    )
    read_rating = fields.Selection(
        string="Reading",
        selection=LANGUAGE_RATING,
        required=True,
        default="0",
    )
    write_rating = fields.Selection(
        string="Writing",
        selection=LANGUAGE_RATING,
        required=True,
        default="0",
    )
    speak_rating = fields.Selection(
        string="Speaking",
        selection=LANGUAGE_RATING,
        required=True,
        default="0",
    )
    listen_rating = fields.Selection(
        string="Listening",
        selection=LANGUAGE_RATING,
        required=True,
        default="0",
    )
