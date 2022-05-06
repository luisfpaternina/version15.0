# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import logging

class BimCateg(models.Model):

    _name = "bim.categ"
    _inherit = 'mail.thread'
    _description = "BIM categ"

    name = fields.Char(
        string='Name',
        tracking=True)
