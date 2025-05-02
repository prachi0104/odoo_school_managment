from odoo import models,fields,api,_
from odoo.exceptions import ValidationError


#inherits model for inheriting existing model in our model and add extra fields or functionality
class InheritsModel(models.Model):
    _name='inherits'
    _description = "inherits"

    _inherits = {'teacher.model': 'teacher_id'}
    teacher_id = fields.Many2one("teacher.model", string="Partner", required=True, ondelete="cascade")
    gender = fields.Char(string="Gender")



class inheritsPractice(models.Model):
    _name = "saleinherits"
    _description = "inheritsPractice"

    _inherits = {"sale.order":"sale_order_id"}
    sale_order_id = fields.Many2one("sale.order",string="orders",required=True,ondelete="cascade")
    papigudiya = fields.Char(string="Papi_gudiya")
    email_id = fields.Char(string="Porvide Email")



    def action_sent_email_sale(self):
        template = self.env.ref('school_managment.sale_order_template_send')
        for rec in self:
            template.send_mail(rec.id, force_send=True)
            message = "Email Sent Successfully!"
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'target': 'new',
                'params': {

                    'type': 'success',
                    'message': message,
                    'next': {'type': 'ir.actions.act_window_close'},
                }}

    @api.constrains('email_id')
    def check_email(self):
        for rec in self:
            if not rec.email_id.endswith('@gmail.com'):
                raise ValidationError("email must end with @gmail.com")






