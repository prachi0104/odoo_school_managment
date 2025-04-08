from odoo import models,fields,api,_
from odoo.exceptions import ValidationError


#inherits model for inheriting existing model in our model and add extra fields or functionality
class InheritsModel(models.Model):
    _name='inherits'
    _description = "inherits"

    _inherits = {'teacher.model': 'teacher_id'}
    teacher_id = fields.Many2one("teacher.model", string="Partner", required=True, ondelete="cascade")
    gender = fields.Char(string="Gender")
