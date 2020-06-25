# -*- coding: utf-8 -*-
from openerp import models, fields


class risk(models.Model):
    _name = 'risk'
    _description = 'risk'
    _rec_name = 'name'
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
    # 1.Risk ID
    name = fields.Char(string="Risk ID", track_visibility='onchange')
    title = fields.Char(string="Title", track_visibility='onchange')
    detail = fields.Text(string="Detail", track_visibility='onchange')
    owner_ids = fields.Many2one('res.users', string="Owner",
                                track_visibility='onchange')
    asst_owner_ids = fields.One2many('risk.assist.owner', 'risk_ids',
                                     string="Asst. Owner",
                                     track_visibility='onchange')
    # 6. Risk Rating“Before” Mitigation
    likelihood_before = fields.Char(string="Likelihood",
                                    track_visibility='onchange')
    impact_before = fields.Char(string="Impact", track_visibility='onchange')
    residual_before = fields.Char(string="Residual Risk Rating",
                                  track_visibility='onchange')
    date_before = fields.Date(string="Date", track_visibility='onchange')
    # 8. Risk Rating “After” Mitigation
    # Plan
    likelihood_after = fields.Char(string="Likelihood",
                                   track_visibility='onchange')
    impact_after = fields.Char(string="Impact", track_visibility='onchange')
    residual_after = fields.Char(string="Residual Risk Rating",
                                 track_visibility='onchange')
    date_after = fields.Date(string="Date", track_visibility='onchange')
    # Result
    likelihood_result = fields.Char(string="Likelihood",
                                    track_visibility='onchange')
    impact_result = fields.Char(string="Impact", track_visibility='onchange')
    residual_result = fields.Char(string="Residual Risk Rating",
                                  track_visibility='onchange')
    date_result = fields.Date(string="Date", track_visibility='onchange')
    causes_ids = fields.One2many('risk.causes', 'risk_ids',
                                 string="Causes",
                                 track_visibility='onchange')
    impacts_ids = fields.One2many('risk.impacts', 'risk_ids',
                                  string="Impacts",
                                  track_visibility='onchange')
    preventative_ids = fields.One2many('risk.preventative', 'risk_ids',
                                       string="Existing Controls (Preventative)",
                                       track_visibility='onchange')
