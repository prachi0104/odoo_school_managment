from odoo import fields,models,api
from datetime import datetime, timedelta
from odoo.exceptions import UserError


class Result(models.Model):
    _name = "result.model"
    _description = "generate student result"


    name = fields.Many2one('stulist.model',string="Student name")
    roll_no = fields.Char(string="Roll No")
    std = fields.Integer(string="Standard")
    acadmic_year = fields.Char(string="A-Y")
    physics = fields.Integer(string="Physics")
    chemistry = fields.Integer(string="Chemistry")
    biology = fields.Integer(string="Biology")
    mathematics = fields.Integer(string="Mathematics")
    computer = fields.Integer(string="Computer")
    total_marks = fields.Integer(string="Total Marks")
    total_obtain = fields.Integer(string="Total Obtain",compute='_compute_total_obtain_marks')
    percentage = fields.Float(string="Percentage",compute='_compute_percentage')
    result = fields.Char(string="Result",compute='_compute_result')


    @api.onchange('name')
    def onchange_name(self):
        self.roll_no = self.name.enrollment
        self.std = self.name.std
        self.total_obtain = self.physics + self.chemistry + self.biology + self.mathematics + self.computer
        # self.total_marks = self.physics + self.chemistry + self.biology + self.mathematics + self.computer


    @api.depends('physics','chemistry','biology','mathematics','computer')
    def _compute_total_obtain_marks(self):
        for rec in self:
            if rec.physics and rec.chemistry and rec.mathematics and rec.mathematics and rec.computer:
                rec.total_obtain = rec.physics + rec.chemistry + rec.mathematics + rec.mathematics + rec.computer
            else:
                rec.total_obtain = 0


    @api.depends('total_obtain','total_marks')
    def _compute_percentage(self):
        for rec in self:
            if rec.total_obtain: #and rec.total_marks:
                rec.percentage = rec.total_obtain/5
            else:
                rec.percentage = 0


    @api.depends('physics','chemistry','biology','mathematics','computer')
    def _compute_result(self):
        for rec in self:
            if rec.physics > 33 and rec.chemistry > 33 and rec.mathematics > 33 and rec.mathematics > 33 and rec.computer > 33:
                rec.result = "Qualified"
            else:
                rec.result = "Not Qualified"

    def action_print_pdf(self):
        self.ensure_one()
        return self.env.ref('school_managment.student_result').report_action(self.id)






