from odoo import models,fields,api,_
from odoo.exceptions import ValidationError,UserError
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



class PracticeInheritance(models.Model):
    _inherit = 'sale.order'

    test = fields.Char(string="Test")


class PracticeInheritance(models.Model):
    _inherit = 'sale.order'

    test = fields.Char(string="Test")




#Pepar question ans
class PeparQuestions(models.Model):
    _inherit = 'hr.employee'

    employee_code = fields.Char(string="Employee Code")


    #first question ans
    @api.constrains('work_email')
    def check_email(self):
        for rec in self:
            if not rec.work_email.endswith('@gmail.com'):
                raise ValidationError("email must end with @gmail.com")

    #2nd question ans
    def create(self,vals):
        vals['employee_code'] = self.env['ir.sequence'].next_by_code('hr.employee')
        return super().create(vals)


class ProductShow(models.Model):
        _inherit = 'product.product'


        def showwarning(self):
            for rec in self:
                print(self.qty_available)
                if rec.qty_available < 5:
                    raise UserError('Quanltity is less than 5')



class AccountMoveInherit(models.Model):
    _inherit = 'account.move'


    def create(self,vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('account.move')
        return super().create(vals)

























