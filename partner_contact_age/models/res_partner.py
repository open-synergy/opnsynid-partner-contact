# -*- coding: utf-8 -*-
# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import date, datetime

from dateutil.relativedelta import relativedelta
from openerp import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.multi
    @api.depends(
        "birthdate_date",
    )
    def _compute_age(self):
        for document in self:
            if document.birthdate_date:
                today = date.today()
                dob = datetime.strptime(document.birthdate_date, "%Y-%m-%d")
                document.age_year = relativedelta(today, dob).years
                document.age_month = relativedelta(today, dob).months
                document.age_day = relativedelta(today, dob).days

    age_year = fields.Integer(
        string="Age Year",
        compute="_compute_age",
        store=True,
    )
    age_month = fields.Integer(
        string="Age Month",
        compute="_compute_age",
        store=True,
    )
    age_day = fields.Integer(
        string="Age Days",
        compute="_compute_age",
        store=True,
    )

    @api.model
    def cron_update_age(self):
        criteria = [
            "&",
            ("is_company", "=", False),
            ("birthdate_date", "!=", False),
        ]
        partner_ids = self.search(criteria)
        for partner in partner_ids:
            partner._compute_age()
