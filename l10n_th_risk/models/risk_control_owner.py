# -*- coding: utf-8 -*-
from openerp import models, fields


class risk_control_owner(models.Model):
    _name = 'risk.control.owner'
    _description = 'risk_control_owner'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _order = "write_date desc"

    # @api.model
    # def create(self, values):
    #     """Override default Odoo create function and extend."""
    #     # Do your custom logic here
    #     return super(nstda_new, self).create(values)

    # @api.multi
    # def write(self, values):
    #     """Override default Odoo write function and extend."""
    #     # Do your custom logic here
    #     return super(nstda_new, self).write(values)

    # @api.multi
    # def unlink(self, values):
    #     """Override default Odoo unlink function and extend."""
    #     return super(nstda_new, self).unlink()

    # @api.multi
    # def copy(self, default=None):
    #     """Override default Odoo unlink function and extend."""
    #     default = default or {}
    #     return super(nstda_new, self).copy(default)

    risk_ids = fields.Many2one('risk')
    control_owner_ids = fields.Selection([('1', 'Division'), ('2', 'Employee')],
                                         string="Control Owner", default='1')
    division_ids = fields.Many2one('res.groups', string="Division",
                                   track_visibility='onchange')
    employee_ids = fields.Many2one('res.users', string="Employee",
                                   track_visibility='onchange')
    control_owner_display = fields.Char(string="Control Owner")
