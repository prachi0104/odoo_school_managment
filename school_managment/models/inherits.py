from odoo import models,fields,api,_
from odoo.exceptions import ValidationError
from datetime import timedelta
from datetime import date

class InheritsModel(models.Model):
    _name='inherits'
    #_inherit = "teacher.model"
    # _inherits={'res.partner':'partner_id'}
    # partner_id=fields.Many2one("res.partner",string="Partner",required="true",ondelete="casecade")
    _inherits = {'teacher.model': 'teacher_id'}
    teacher_id = fields.Many2one("teacher.model", string="Partner", required="true", ondelete="casecade")
    gender = fields.Char(string="Gender")


    def action_open_students(self):
        print("success.....")
        return super().action_open_students()


