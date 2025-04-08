from odoo import models, fields,api

class HostelRoom(models.Model):
    _name = 'hostel.room'
    _description = 'Hostel Room'
    _rec_name = 'room_type'


    room_type = fields.Selection(selection=[('single', 'Single'), ('shared', 'Shared')])
    total_room = fields.Integer(string="Total room", required=True)
    occupied = fields.Integer(string="Occupied", default=0)
    available = fields.Integer(string="Available", compute="_compute_available", store=True)
    student_hostel = fields.One2many("hostel.admission", "room_type", string="Student hostel detail")




    @api.depends('total_room','occupied')
    def _compute_available(self):
        for room in self:
                room.available = room.total_room - room.occupied


    def action_test(self):
        return {
            'name': 'List of student',
            'type': 'ir.actions.act_window',
            'res_model': 'hostel.admission',
            'view_mode': 'list,form',
           'domain': [('room_type', '=', self.id)],

        }




