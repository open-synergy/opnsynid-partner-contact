# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api, _
from openerp.exceptions import Warning as UserError


class ResPartner(models.Model):
    _name = "res.partner"
    _inherit = [
        "res.partner",
        "base.workflow_policy_object",
    ]

    @api.depends(
        "company_id",
    )
    # membuat fungsi untuk field compute -->
    @api.multi
    def _compute_policy(self):
        _super = super(ResPartner, self)
        _super._compute_policy()

    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting For Approval"),
            ("valid", "Valid"),
        ],
        default="draft",
        required=True,
    )
    active = fields.Boolean(
        string="Active",
        readonly=True,
        default=False,
    )
    # Make Fields readonly
    child_ids = fields.One2many(
        comodel_name="res.partner",
        readonly=True,
    )
    # name = fields.Char(
    #     readonly=True,
    #     states={
    #         "draft": [
    #             ("readonly", False),
    #         ],
    #     },
    # )
    # user_id = fields.Many2one(
    #     comodel_name="res.users",
    #     readonly=True,
    #     states={
    #         "draft": [
    #             ("readonly", False),
    #         ],
    #     },
    # )
    # category_id = fields.Many2many(
    #     comodel_name="res.partner.category",
    #     readonly=True,
    #     states={
    #         "draft": [
    #             ("readonly", False),
    #         ],
    #     },
    # )
    # ref = fields.Char(
    #     readonly=True,
    #     states={
    #         "draft": [
    #             ("readonly", False),
    #         ],
    #     },
    # )
    # lang = fields.Selection(
    #     readonly=True,
    #     states={
    #         "draft": [
    #             ("readonly", False),
    #         ],
    #     },
    # )
    # Policy Fields
    confirm_ok = fields.Boolean(
        string="Can Confirm",
        compute="_compute_policy"
    )
    valid_ok = fields.Boolean(
        string="Can Valid",
        compute="_compute_policy"
    )
    restart_ok = fields.Boolean(
        string="Can Restart",
        compute="_compute_policy"
    )
    # Policy Fields untuk customer
    mark_customer_ok = fields.Boolean(
        string="Can Mark As Customer",
        compute="_compute_policy"
    )
    unmark_customer_ok = fields.Boolean(
        string="Can Un Mark As Customer",
        compute="_compute_policy"
    )
    # Policy Fields untuk customer
    mark_supplier_ok = fields.Boolean(
        string="Can Mark As Supplier",
        compute="_compute_policy"
    )
    unmark_supplier_ok = fields.Boolean(
        string="Can Un Mark As Supplier",
        compute="_compute_policy"
    )
    # Log Fields
    confirm_date = fields.Datetime(
        string="Confirm Date",
        readonly=True,
    )
    confirm_user_id = fields.Many2one(
        string="Confirmed By",
        comodel_name="res.users",
        readonly=True,
    )
    valid_date = fields.Datetime(
        string="Valid Date",
        readonly=True,
    )
    valid_user_id = fields.Many2one(
        string="Valid By",
        comodel_name="res.users",
        readonly=True,
    )
    restart_date = fields.Datetime(
        string="Restart Date",
        readonly=True,
    )
    restart_user_id = fields.Many2one(
        string="Restart By",
        comodel_name="res.users",
        readonly=True,
    )

    # fungsi saat menekan tombol confirm - valid restart dilakukan
    # perubahan data state user dan tanggal dengan menjalankan fungsi
    @api.multi
    def action_confirm(self):
        for document in self:
            document.write(document._prepare_confirm_data())

    @api.multi
    def action_valid(self):
        for document in self:
            document.write(document._prepare_valid_data())

    @api.multi
    def action_restart(self):
        for document in self:
            document.write(document._prepare_restart_data())

    # fungsi perubahan data state user dan tanggal -- confirm
    @api.multi
    def _prepare_confirm_data(self):
        self.ensure_one()
        result = {
            "state": "confirm",
            "confirm_date": fields.Datetime.now(),
            "confirm_user_id": self.env.user.id,
            "restart_date": False,
            "restart_user_id": False,
        }
        return result

    # fungsi perubahan data state user dan tanggal -- valid
    @api.multi
    def _prepare_valid_data(self):
        self.ensure_one()
        result = {
            "state": "valid",
            "valid_date": fields.Datetime.now(),
            "valid_user_id": self.env.user.id,
            "active": True,
        }
        return result

    # fungsi perubahan data state user dan tanggal -- restart
    @api.multi
    def _prepare_restart_data(self):
        self.ensure_one()
        result = {
            "state": "draft",
            "restart_date": fields.Datetime.now(),
            "restart_user_id": self.env.user.id,
            "confirm_date": False,
            "confirm_user_id": False,
            "valid_date": False,
            "valid_user_id": False,
            "active": False,
        }
        return result
