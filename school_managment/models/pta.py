from odoo import models,fields,api,_
from odoo.exceptions import ValidationError
from datetime import timedelta
from datetime import date

class Parentsteachermeeting(models.Model):
    _name='parentsteachermeeting.model'
    _description='parentsteachermeeting model'



    name=fields.Many2one('stulist.model',string="Student Name")
    depratment_name=fields.Many2one('department.model',string="Student Depratment")
    date_of_ptm=fields.Date(string="Date of Meeting",default=lambda self: self._get_default_date())
    parents_email=fields.Char(string="Email", size=100, help="Email address")
    point_of_discussion=fields.Text(string="Your Text Field", required=False,default="Regarding Result Discussion")
    state=fields.Selection([('draft','Draft'),('sceduled','sceduled'),('done','Done'),('cancel','Cancel')] ,default='draft',string="Status",required=True)
    enrollment = fields.Char("Enrol")

    @api.onchange('name','depratment_name')
    def onchange_name(self):
        self.enrollment = self.name.enrollment
        self.depratment_name=self.name.department_id
        self.state="sceduled"

    def _get_default_date(self):
        return fields.Date.context_today(self) + timedelta(days=2)


    def unlink(self):
        for i in self:
            if i.state == 'done':
                raise ValidationError("You can not delete this record with done status")
        return super().unlink()


    



