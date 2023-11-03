# -*- encoding: utf-8 -*-

# Custom HR Module by Augusto Calado

# 17h23

from odoo import models, fields

class HrEmployeeExtension(models.Model):

    _inherit  = 'hr.employee'

    setor     = fields.Many2one('hr.department', string='Setor')
    cbo       = fields.Integer(string="CBO")
    esocial   = fields.Integer(string="eSocial")
