from odoo import models, fields, api

class saleorderwizard(models.TransientModel):
    _name= 'saleorderwizard'
    _description = 'saleorderwizard'

    thresold_quantity = fields.Integer(string="thresold_quantity")

    def generate_report(self):
        domain = [('qty_available', '<', self.thresold_quantity)]
        return {
            'name': 'Low Stock Products',
            'type': 'ir.actions.act_window',
            'res_model': 'product.product',
            'view_mode': 'list,form',
            'domain': domain,
            'context': self.env.context,
        }





