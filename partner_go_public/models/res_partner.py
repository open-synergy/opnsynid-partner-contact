# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields
from openerp.tools.translate import _


class res_partner(models.Model):
    _inherit = "res.partner"

    go_public = fields.Boolean(
        string=_("Go Public"),
        required=False,
        translate=False,
        readonly=False
    )
