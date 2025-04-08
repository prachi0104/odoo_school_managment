from odoo import fields,models


class StudentModel(models.Model):
    _name = 'student.model'
    _description = 'student model'


    name = fields.Char(string="Provide student name")



