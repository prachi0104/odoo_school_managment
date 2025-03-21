from odoo import models,fields,api
from datetime import date


class Attandence(models.Model):
    _name="attandence.model"
    _description="mark attandence"

    stulist_id = fields.Many2one('stulist.model',string="student")
    date = fields.Date(string="Date of Attandence")
    status = fields.Selection([('present','Present'),('absent','Absent')])


    def create(self,vals):
        vals['date']= date.today()
        return super().create(vals)

    




