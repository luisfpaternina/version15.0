# -*- coding: utf-8 -*-
from odoo import models, fields, _

class BimBim(models.Model):

    _name = "bim.bim"
    _inherit = 'mail.thread'
    _description = "BIM"

    name = fields.Char(
        string='Name',
        required=True,
        tracking=True)
    photo = fields.Binary(
        string='Photo',
        tracking=True)
    attachment = fields.Binary(
        string="Attachment",
        tracking=True)
   