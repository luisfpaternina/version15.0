# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import datetime, date
import logging


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    project_id = fields.Many2one(
        'bim.bim',
        string="BIM Project")
