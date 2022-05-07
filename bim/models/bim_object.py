# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import datetime

class BimObject(models.Model):
    _name = 'bim.object'
    _description = "BIM Object"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']
    _rec_name = 'description'

    name = fields.Char(
        'Code',
        default="New")
    description = fields.Char(
        'Description')
    project_id = fields.Many2one(
        'bim.project',
        string='Project')
    user_id = fields.Many2one(
        'res.users',
        string='Responsable',
        tracking=True,
        default=lambda self: self.env.user)
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        default=lambda self: self.env.company,
        required=True)
    image = fields.Binary(
        string="Image")


    @api.model
    def create(self, vals):
        if vals.get('name', "New") == "New":
            vals['name'] = self.env['ir.sequence'].next_by_code('bim.object') or "New"
        return super(BimObject, self).create(vals)
