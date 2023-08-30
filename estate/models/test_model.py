# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields,models


class TestModel(models.Model):
    _name = 'test.model'
    _description = "Test model"
    
    name = fields.Char(string='Test Name')
    code = fields.Char(string='Test Code')
    price = fields.Float(string='Test Price')
    is_available = fields.Boolean(string='Is Available')
