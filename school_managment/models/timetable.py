from odoo import fields,models


class Timetable(models.Model):
    _name = "timetable.model"
    _description = "Student time table"

    timetable_html=fields.Html(sanitize=False,readonly=True)