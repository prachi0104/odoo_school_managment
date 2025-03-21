from odoo import fields,models


class SaleOrder(models.Model):
    _inherit = "sale.order"


    confirm_user_id = fields.Many2one('res.users',string="Confirmed User")

    def action_confirm(self):
        print("success")
        super(SaleOrder,self).action_confirm()
        self.confirm_user_id = self.env.user.id




