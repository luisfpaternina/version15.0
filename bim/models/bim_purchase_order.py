# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import datetime, date
import logging


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    project_id = fields.Many2one(
        'bim.bim',
        string="BIM Project")
