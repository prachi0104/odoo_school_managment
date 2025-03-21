from odoo import fields,models
from datetime import date
from datetime import timedelta

class SceduleExam(models.Model):
    _name="sceduleexam.model"
    _description="scedule exam"

    std=fields.Many2one("stulist.model",string="Standard")
    department_id=fields.Many2one("department.model",string="Department")
    date=fields.Date(string="Exam date", required=True, help="Date of Birth",default=lambda self: self._get_default_date())
    timetable=fields.Html(sanitize=False)


    def _get_default_date(self):
        return fields.Date.context_today(self) + timedelta(days=30)
