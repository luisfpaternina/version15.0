# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import logging

class BimUdn(models.Model):

    _name = "bim.udn"
    _inherit = 'mail.thread'
    _description = "BIM udn"

    name = fields.Char(
        string='Name',
        tracking=True)
