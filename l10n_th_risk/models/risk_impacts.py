# -*- coding: utf-8 -*-
from openerp import models, fields


class risk_impacts(models.Model):
    _name = 'risk.impacts'
    _description = 'risk_impacts'
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

    impacts_id = fields.Integer(string="ID", track_visibility='onchange')
    impacts_name = fields.Char(string="Detail", track_visibility='onchange',
                               required=True)
    risk_ids = fields.Many2one('risk')
