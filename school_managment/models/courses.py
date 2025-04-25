from odoo import fields,models,api



class StudentCourses(models.Model):
    _name = "student.courses"
    _description = "student courses"

    name = fields.Char(string="Course Name", required=True)
    code = fields.Char(string="Course Code", required=True)
    description = fields.Text(string="Description")
    duration = fields.Integer(string="Duration (in hours)")