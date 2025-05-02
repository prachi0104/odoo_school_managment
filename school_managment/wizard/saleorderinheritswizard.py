from odoo import models, fields, api

class saleorderwizard(models.TransientModel):
    _name= 'saleorderwizard'
    _description = 'saleorderwizard'

    thresold_quantity = fields.Integer(string="thresold_quantity")





