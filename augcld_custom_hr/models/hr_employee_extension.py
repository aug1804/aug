# -*- encoding: utf-8 -*-

# Custom HR Module by Augusto Calado

from odoo import models, fields

class HrEmployeeExtension(models.Model):

    _inherit  = 'hr.employee'

    setor     = fields.Many2one('hr.department', string='Setor')
    cbo       = fields.Integer(string="CBO")
    esocial   = fields.Integer(string="eSocial")
