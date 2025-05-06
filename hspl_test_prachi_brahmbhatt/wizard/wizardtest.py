from odoo import models, fields, api

class purchasorderwizard(models.TransientModel):
    _name= 'purchasorderwizard'
    _description = 'wizard'

    vendors = fields.Many2many('res.partner',string="Select Vendors")

    # def generate_report(self):
    #     domain = [('qty_available', '=', self.vendors)]
    #     return {
    #         'name': 'Low Stock Products',
    #         'type': 'ir.actions.act_window',
    #         'res_model': 'product.product',
    #         'view_mode': 'list,form',
    #         'domain': domain,
    #         'context': self.env.context,
    #     }





