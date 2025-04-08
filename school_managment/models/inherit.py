from odoo import models,fields,api,_
from odoo.exceptions import ValidationError
from datetime import timedelta
from datetime import date


class AccountMove(models.Model):
    _inherit = 'sale.order'

    teacher_id = fields.Many2one("teacher.model",string="teacher")
    is_teacher = fields.Boolean(string="Is_teacher")



class Customer(models.Model):
    _inherit = 'res.partner'

    company_type = fields.Selection(selection_add=[('personal','Personal')])



class ResultEdit(models.Model):
    _inherit = 'result.model'

    result_id = fields.Many2one('result.model')
    checking_faculty = fields.Char(string="Checking faculty")








