# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import logging

class BimBim(models.Model):

    _name = "bim.bim"
    _inherit = 'mail.thread'
    _description = "BIM"

    name = fields.Char(
        string='Name',
        required=True,
        tracking=True,
        copy=False,
        default="New")
    photo = fields.Binary(
        string='Photo',
        tracking=True)
    attachment = fields.Binary(
        string="Attachment",
        tracking=True)
    project_name = fields.Char(
        string="Project name")
    partner_id = fields.Many2one(
        'res.partner',
        string="Client")
    address = fields.Char(
        string="Address",
        related="partner_id.street")
    state = fields.Selection([
        ('new','New'),
        ('process','Process'),
        ('finish','Finish')],string="State")
    udn_id = fields.Many2one(
        'bim.udn',
        string="Udn")
    categ_id = fields.Many2many(
        'bim.categ',
        string="Categ")
    color = fields.Integer(
        string='Color Index')
    purchase_ids = fields.Many2many(
        'purchase.order',
        string="Purchases",
        compute="compute_purchase_ids")
    photo1 = fields.Binary(
        string="Photo 1")
    photo2 = fields.Binary(
        string="Photo 2")
    photo3 = fields.Binary(
        string="Photo 3")
    photo4 = fields.Binary(
        string="Photo 4")
    departament_id = fields.Many2one(
        'bim.departaments',
        string="Departament")
    partner_type_id = fields.Many2one(
        'bim.partner.type',
        string="Client type")
    notes = fields.Text(
        string="Notes")
    purchase_count = fields.Integer(
        compute="compute_purchase_count")
    sale_count = fields.Integer()
    active = fields.Boolean(
        string="Active",
        tracking=True,
        default=True)
    analytic_account_id = fields.Many2one(
        'account.analytic.account',
        string="Analytic account")
    employee_count = fields.Integer(
        compute="compute_employee_count")
    documents_count = fields.Integer(
        compute="compute_documents_count")
    date_start = fields.Date(
        string="Date start")


    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('bim') or 'New'
        result = super(BimBim, self).create(vals)
        return result

    def compute_purchase_ids(self):
        for record in self:
            purchases = self.env['purchase.order'].search([('project_id','=',self.id)])
            if purchases:
                record.purchase_ids = purchases.ids
            else:
                record.purchase_ids = False

    def get_purchases(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Purchases',
            'view_mode': 'tree',
            'res_model': 'purchase.order',
            'domain': [('project_id', '=', self.id)],
            'context': "{'create': False}"
        }

    def get_employees(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Employees',
            'view_mode': 'tree',
            'res_model': 'hr.employee',
            'domain': [('project_id', '=', self.id)],
            'context': "{'create': False}"
        }

    def get_documents(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Documents',
            'view_mode': 'tree',
            'res_model': 'bim.documentation',
            'domain': [('project_id', '=', self.id)],
            'context': "{'create': False}"
        }

    def compute_purchase_count(self):
        for record in self:
            record.purchase_count = self.env['purchase.order'].search_count([('project_id', '=', self.id)])

    def compute_sale_count(self):
        for record in self:
            record.sale_count = self.env['sale.order'].search_count([('project_id', '=', self.id)])

    def compute_employee_count(self):
        for record in self:
            record.employee_count = self.env['hr.employee'].search_count([('project_id', '=', self.id)])

    def compute_documents_count(self):
        for record in self:
            record.documents_count = self.env['bim.documentation'].search_count([('project_id', '=', self.id)])
   