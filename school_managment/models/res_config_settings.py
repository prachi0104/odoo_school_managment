from odoo import models, fields


class school_managment(models.TransientModel):
    _inherit = "res.config.settings"

    cancel_days = fields.Boolean(string="Enable Cancellation")
