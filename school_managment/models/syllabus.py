from odoo import models,fields,api
from datetime import date


class Syllabus(models.Model):
    _name="syllabus.model"
    _description="view syllabus"

    syllabus_file = fields.Binary(string="Syllabus PDF", required=True, attachment=True)
    std = fields.Selection([('11','11th std'),('12','12th std')])
    department_id = fields.Many2one('department.model',string="Department",ondelete="cascade")
    student_id = fields.Many2one("stulist.model", string="Student")
