# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    journal_entry_group_id = fields.Many2many('res.groups',
                                      string='Journal Entry Groups',
                                      related='company_id.journal_entry_group_id',
                                      readonly=False)

