from odoo import models,fields,api



class LayoutDraft(models.Model):
    _name = "layout.draft"
    _description = "layout draft"


    name= fields.Char(string="Name")
    address = fields.Text()
    qualification =fields.Html(string="Qualification")
    project_list = fields.Html(sanitize=False)
    year_of_passing = fields.Char(string="Year of passing")
    email = fields.Char(string="Email")
    experience = fields.Html(string="Experience")
    hobbies = fields.Html(string="Hobbies")


    def action_open_layout_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Layout Wizard',
            'res_model': 'layout.draft.wizard',
            'view_mode': 'form',
            'target': 'new',  # Opens in a popup
            'context': {
            'active_id': self.id,  # 👈 This is important
        },
        }

