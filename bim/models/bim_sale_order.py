# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime, date
import base64
import logging


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    project_id = fields.Many2one('bim.project', 'Project', tracking=True)
    budget_id = fields.Many2one('bim.budget', 'Budjet', ondelete="restrict")
    concept_id = fields.Many2one('bim.concepts', 'Concept', ondelete="restrict")

    def _prepare_invoice(self):
        values = super()._prepare_invoice()
        values.update({
            'project_id': self.project_id.id or False,
            'budget_id': self.budget_id.id or False,
            'concept_id': self.concept_id.id or False,
        })
        return values

    def _create_invoices(self, grouped=False, final=False, date=None):
        moves = super()._create_invoices(grouped,final,date)
        for move in moves:
            if move.project_id and move.project_id.analytic_id:
                for line in move.invoice_line_ids:
                    line.analytic_account_id = move.project_id.analytic_id.id
        return moves

    def action_confirm(self):
        confirmation = super().action_confirm()
        for picking in self.picking_ids:
            if not picking.bim_project_id and self.project_id:
                picking.bim_project_id = self.project_id.id
            if not picking.bim_budget_id and self.budget_id:
                picking.bim_budget_id = self.budget_id.id
            if not picking.bim_concept_id and self.concept_id:
                picking.bim_concept_id = self.concept_id.id
        return confirmation
