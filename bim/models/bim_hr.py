# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import datetime, date
import logging


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    project_id = fields.Many2one(
        'bim.bim',
        string="BIM Project")
    wage_bim = fields.Float(
        'BIM Salary')
    total_hours_week = fields.Float(
        compute='compute_total_hours_week')
    hour_cost = fields.Float(
        string='Hour Cost')
    bim_resource_id = fields.Many2one(
        'product.product',
        domain="[('type','=','service')]")

    def compute_total_hours_week(self):
        for record in self:
            total = 0
            for line in record.resource_calendar_id.attendance_ids:
                total += line.hour_to - line.hour_from
            record.total_hours_week = total
