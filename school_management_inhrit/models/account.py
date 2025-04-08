from odoo import fields,models


class AccountMove(models.Model):
    _inherit = 'account.move'


    student_id= fields.Many2one('student.model',string="Student")