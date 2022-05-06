# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import datetime
from odoo.exceptions import ValidationError
import logging

class BimDocumentation(models.Model):
    _name = 'bim.documentation'
    _description = "Documentation BIM"
    _order = "id desc"
    _rec_name = 'description'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']

    name = fields.Char(
        'Code',
        default="New",
        copy=False)
    description = fields.Char(
        'Description',
        copy=True)
    project_id = fields.Many2one(
        'bim.bim',
        string='Project',
        ondelete="cascade",
        copy=True)
    user_id = fields.Many2one(
        'res.users',
        string='Responsable',
        tracking=True,
        default=lambda self: self.env.user,
        copy=False)
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        default=lambda self: self.env.company,
        required=True,
        copy=False)
    observations = fields.Text(
        'Notes')
    file_name = fields.Char(
        "File Name",
        copy=False)
    file_01 = fields.Binary(
        string='File',
        copy=False)
    image = fields.Binary(
        "Image",
        copy=False)

    def _set_image(self):
        self._set_image_value(self.image)

    @api.model
    def create(self, vals):
        if vals.get('name', "New") == "New":
            vals['name'] = self.env['ir.sequence'].next_by_code('bim.documentation') or "New"
        return super(BimDocumentation, self).create(vals)

    def print_document_notes(self):
        return self.env.ref('bim.notes_report_document').report_action(self)
