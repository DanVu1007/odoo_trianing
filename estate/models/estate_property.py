# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields,models


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = "Estate Property"
    
    name = fields.Char(string='Test Name')
    code = fields.Char(string='Test Code')
