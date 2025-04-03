from odoo import models,fields


class StudentAdmi(models.TransientModel):
    _name = 'student.wizard'
    _description = 'Student Wizard'

    ctop = fields.Integer(string='Charges To Pay')
    student_state = fields.Selection([('allocated', 'Allocated'), ('deallocated', 'Deallocated')],
                             string="Status", default='deallocated', required=True, tracking=True)
    room_type = fields.Many2one('hostel.room', string="room type", tracking=True)
    hostel_admission_ids = fields.Many2many('hostel.admission', string="Hostel Admission")

    def action_apply_charges(self):
        if self.hostel_admission_ids:
            for record in self.hostel_admission_ids:
                record.write({
                    'charges_to_pay': self.ctop,
                    'state':self.student_state,
                    'room_type':self.room_type
                })



