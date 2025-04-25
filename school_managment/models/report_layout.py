from odoo import models, fields

from odoo import models, fields

class ReportLayout(models.Model):
    _inherit = 'report.layout'

    custom_layout_type = fields.Selection([('light', 'Light'),], string='Custom Layout Type', default='light')



