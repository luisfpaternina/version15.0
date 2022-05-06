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
        string="Address")

    def create(self):
    # Heredar función create y agregar secuencia
        if self.name == 'New':
            self.name = self.env['ir.sequence'].next_by_code('bim')
        result = super(BimBim, self).create()
   