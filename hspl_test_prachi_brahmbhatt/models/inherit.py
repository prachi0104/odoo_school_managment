from odoo import models, fields,api
from datetime import datetime
from odoo.exceptions import UserError
from datetime import timedelta

class InheritedExample(models.Model):
    _inherit = 'res.partner'

    is_a_member = fields.Boolean(string="is Member")
    filter_based_on_so = fields.Boolean(string="filter_based_on_so")
    membership_levels = fields.Many2one('membership.level',string="membership_level")

class InheritedsaleorderExample(models.Model):
    _inherit = 'sale.order'

    def create(self):
        today_date = datetime.today()
        for i in self:
            if self.order_date < today_date:
                raise UserError("Date should be greater than today!!")

         # fields.Date.context_today(self) + timedelta(days=5)

    def _get_default_date(self):
        validity_date = fields.Date.context_today(self) + timedelta(days=5)
        return validity_date






