from odoo import models, fields,api

class HostelRoom(models.Model):
    _name = 'hostel.room'
    _description = 'Hostel Room'

    room_number = fields.Char(string="Room Number", required=True)
    capacity = fields.Integer(string="Room Capacity", required=True)
    occupied = fields.Integer(string="Occupied", default=0)
    available = fields.Integer(string="Available", compute="_compute_available", store=True)

    @api.depends('capacity','occupied')
    def _compute_available(self):
        for room in self:
            room.available = room.capacity - room.occupied

