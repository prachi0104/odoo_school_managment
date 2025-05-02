from odoo import models,fields,api


class ProductReview(models.Model):
    _name='product.review'
    _description = "provide product review"

    product_id= fields.Many2one('product.product',string="product")
    rating = fields.Selection(selection=[('1', '1star'), ('2', '2star'),  ('3', '3star')] )
    review_text = fields.Text()
    partner_id = fields.Many2one('res.partner',string="Partner_id")

