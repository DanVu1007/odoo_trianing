from odoo import models, fields


class AnimalAbstract(models.AbstractModel):
    _name = 'animal.abstract'
    _description = 'Animal Abstract'

    name = fields.Char(
        string='name',
        required=True
    )

    gender = fields.Selection(
        string='gender',
        selection=[('female', 'Female'), ('male', 'Male')]
    )
    
    color = fields.Char(
        string='color',
    )

    age = fields.Integer(
        string='age',
    )
    
    def _sound(self):
        pass

    
