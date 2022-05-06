# -*- coding: utf-8 -*-
from odoo import models, fields, _

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

    @api.model
    def create(self, vals):
    # Heredar función create y agregar secuencia
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('bim')
        result = super(BimBim, self).create(vals)
   