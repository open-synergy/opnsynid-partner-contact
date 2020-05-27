# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ResCompany(models.Model):
    _name = "res.company"
    _inherit = "res.company"

    res_partner_confirm_grp_ids = fields.Many2many(
        string="Allow To Confirm Partner",
        comodel_name="res.groups",
        relation="rel_company_2_res_partner_confirm",
        column1="company_id",
        column2="group_id",
    )
    res_partner_valid_grp_ids = fields.Many2many(
        string="Allow To Validate Partner",
        comodel_name="res.groups",
        relation="rel_company_2_res_partner_valid",
        column1="company_id",
        column2="group_id",
    )
    res_partner_restart_grp_ids = fields.Many2many(
        string="Allow To Restart Partner",
        comodel_name="res.groups",
        relation="rel_company_2_res_partner_restart",
        column1="company_id",
        column2="group_id",
    )
    # Customer and Supplier
    res_partner_mark_customer_grp_ids = fields.Many2many(
        string="Allow To Mark As Customer",
        comodel_name="res.groups",
        relation="rel_company_2_res_partner_mark_customer",
        column1="company_id",
        column2="group_id",
    )
    res_partner_unmark_customer_grp_ids = fields.Many2many(
        string="Allow To Un Mark As Customer",
        comodel_name="res.groups",
        relation="rel_company_2_res_partner_unmark_customer",
        column1="company_id",
        column2="group_id",
    )
    res_partner_mark_supplier_grp_ids = fields.Many2many(
        string="Allow To Mark As Supplier",
        comodel_name="res.groups",
        relation="rel_company_2_res_partner_mark_supplier",
        column1="company_id",
        column2="group_id",
    )
    res_partner_unmark_supplier_grp_ids = fields.Many2many(
        string="Allow To Un Mark As Supplier",
        comodel_name="res.groups",
        relation="rel_company_2_res_partner_unmark_supplier",
        column1="company_id",
        column2="group_id",
    )
