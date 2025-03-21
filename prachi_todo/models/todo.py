from odoo import models,fields

class todo(models.Model):
    _name='prachi.todo'
    _description="prachi todo"

    name = fields.Char("Name", required=True)
    done = fields.Boolean()
