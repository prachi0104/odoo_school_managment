from odoo import models, fields,api

class HostelRoom(models.Model):
    _name = 'membership.level'
    _description = 'member ship level'

    name = fields.Char(string="Name",required=True)
    ranking = fields.Integer(string="Ranking",unique=True)
    display_name = fields.Char(string="Display Name",compute='_compute_display_name',store="True")
    color =  fields.Char(string="Color")
    user_id = fields.Many2one('res.partner', string="user_id")

    @api.depends('ranking', 'name')
    def _compute_display_name(self):
        for i in self:
            i.display_name = f'{i.ranking}  {i.name}'



