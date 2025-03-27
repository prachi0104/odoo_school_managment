from odoo import fields,models,api
from odoo.exceptions import UserError


class HostelAdmission(models.Model):
    _name = "hostel.admission"
    _description = "hostel admission form"


    name = fields.Many2one('stulist.model',string="Student Name")
    admission_date = fields.Date(string="Date of Admission", default=lambda self: self._get_default_date())
    room_type = fields.Many2one('hostel.room',string="room type")
    per_sem_charge = fields.Integer()
    state = fields.Selection([('allocated', 'Allocated'), ('deallocated', 'Deallocated')],
                         string="Status",default='deallocated', required=True)



    def action_allocate_room(self):
        for rec in self:
            rec.state = 'allocated'

    def action_deallocate_room(self):
        for rec in self:
            rec.state = 'deallocated'

    @api.ondelete(at_uninstall=False)
    def check_allocation(self):
        for rec in self:
            if rec.state == 'allocated':
                raise UserError("You can't delete record with state allocated")


    def _get_default_date(self):
       return fields.Date.context_today(self)

    # @api.model
    def create(self, vals):
        # Create the admission record first

        admission = super(HostelAdmission, self).create(vals)
        print(admission) #data which is enterd by user

        if 'state' in vals and 'room_type' in vals:
            room = self.env['hostel.room'].browse(vals['room_type'])  # Get the room record
            print(room) #id of the room according to enterd by use for shared id is 12 and for single id is 11

            if room:

                if vals['state'] == 'allocated':
                    room.occupied += 1  # Increase occupied rooms
                    room.available = room.total_room - room.occupied  # Update available rooms
                elif vals['state'] == 'deallocated':
                    room.occupied -= 1  # Decrease occupied rooms
                    room.available = room.total_room - room.occupied  # Update available rooms

        return admission

    def write(self, vals):
        # Ensure room_type is in the vals before updating
        if 'state' in vals and self.room_type:
            room = self.room_type  # Directly get the room from self

            if room:
                if vals['state'] == 'allocated': # To avoid multiple increments
                    room.occupied += 1  # Increase occupied rooms
                    room.available = room.total_room - room.occupied  # Update available rooms
                elif vals['state'] == 'deallocated':  # To avoid multiple decrements
                    room.occupied -= 1  # Decrease occupied rooms
                    room.available = room.total_room - room.occupied  # Update available rooms

        return super(HostelAdmission, self).write(vals)


    def action_print_pdf(self):
        self.ensure_one()
        return self.env.ref('school_managment.student_hostel_receipt').report_action(self.id)




