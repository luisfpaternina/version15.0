# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import datetime

class BimObject(models.Model):
    _name = 'bim.object'
    _description = "BIM Object"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']
    _rec_name = 'description'

    name = fields.Char(
        string='Name')
    description = fields.Char(
        'Description')
    project_id = fields.Many2one(
        'bim.project',
        string='Project')
