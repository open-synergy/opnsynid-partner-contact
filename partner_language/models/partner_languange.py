# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import tools
from openerp import models, fields


class PartnerLanguange(models.Model):
    _name = "partner.language"

    name = fields.Selection(
        selection=tools.scan_languages(),
        string=u"Language",
        required=True
    )
    description = fields.Char(
        string=u"Description",
        size=64,
        required=True
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string=u"Partner",
        required=True
    )
    can_read = fields.Boolean(
        string=u"Read",
        default=True,
        oldname="read"
    )
    can_write = fields.Boolean(
        string=u"Write",
        default=True,
        oldname="write"
    )
    can_speak = fields.Boolean(
        string=u"Speak",
        default=True,
        oldname="speak"
    )
