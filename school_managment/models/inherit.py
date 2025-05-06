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



# class PracticeInheritance(models.Model):
#     _inherit = 'sale.order'
#
#     test = fields.Char(string="Test")


#13 ans Qweb Custom Report (7 Marks)
class PracticeInheritance(models.Model):
    _inherit = 'sale.order'

    total_weight = fields.Float(string="Total Weight", compute='_compute_total_weight', store=True)
    test = fields.Char(string="Test")


    def _get_total_weight(self):
        total_weight = 0.0
        for line in self.order_line:
                if line.product_id and line.product_id.weight:
                    total_weight += line.product_uom_qty * line.product_id.weight
        return total_weight


#1 question Add a constraint in the Employee form such that the work_email must end with @yourcompany.com. Raise a validation error if it doesn't.
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


#6th ans Auto Warning on Transfer (5 Mark When confirming a delivery order, show a warning if any product has less than 5 quantity on hand.
class ProductShow(models.Model):
        _inherit = 'product.product'

        def showwarning(self):
            for rec in self:
                print(self.qty_available)
                if rec.qty_available < 5:
                    raise UserError('Quanltity is less than 5')


#7th ans Computed Field - Total Weight (4 Marks)
#In the stock picking model, add a computed field total_weight that sums the weight of all products
#in the picking lines.
class StockPicking(models.Model):
    _inherit = 'stock.picking'

    total_weight = fields.Float(string='Total Weight', compute='_compute_total_weight')

    @api.depends('move_ids_without_package.product_id', 'move_ids_without_package.product_uom_qty')
    def _compute_total_weight(self):
        for picking in self:
            weight = 0.0
            for move in picking.move_ids_without_package:
                weight += move.product_id.weight * move.product_uom_qty
            picking.total_weight = weight





#9 Add Auditor Approval (7 Marks) Add a checkbox auditor_approved in journal entries. Only users from a new group “Account Auditor” should be able to check/uncheck it. Use record rules and access rights.
class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    auditor_approved = fields.Boolean(string="Auditor_approved",groups="school_managment.group_school_teacher")

#8 ans Journal Entry Customization (5 Marks When creating a journal entry, auto-fill the ref field in the format JE/YY/MM/Sequence.
    def create(self,vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('account.move')
        return super().create(vals)






























