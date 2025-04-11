from odoo import fields,models,api
from datetime import datetime, timedelta
from odoo.exceptions import UserError,ValidationError
import base64
import tempfile
from pdf2image import convert_from_bytes

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
    image=fields.Image("image")
    parents_phone = fields.Char(string="Pnone")
    progress= fields.Integer(string="Growth",compute='_compute_progress')




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

    @api.depends('percentage')
    def _compute_progress(self):
        for rec in self:
            if rec.percentage <= 25:
                rec.progress = 25
            elif rec.percentage <= 50:
                rec.progress = 50
            elif  rec.percentage <= 75:
                rec.progress = 75
            else:
                rec.progress = 100


    #whatsapp interation
    def action_shar_whatsapp(self):
        if not self.parents_phone:
            raise ValidationError("Missing phone number in form")

        msg = 'student name is *%s*,roll number is *%s*, *percentage* of student is: *%s* ,collect full result from school' % (self.name.name,self.roll_no, self.percentage )
        whatsapp_api_url = 'https://web.whatsapp.com/send?phone=%s&text=%s' % (self.parents_phone, msg)
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': whatsapp_api_url
        }














