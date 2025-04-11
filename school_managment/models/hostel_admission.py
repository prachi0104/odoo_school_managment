from odoo import fields,models,api
from odoo.exceptions import UserError
from odoo.tools import html2plaintext


class HostelAdmission(models.Model):
    _name = "hostel.admission"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "hostel admission form"


    name = fields.Many2one('stulist.model',string="Student Name", tracking=True)
    admission_date = fields.Date(string="Date of Admission", default=lambda self: self._get_default_date(),tracking=True)
    room_type = fields.Many2one('hostel.room',string="room type",tracking=True)
    per_sem_charge = fields.Integer(tracking=True)
    charges_to_pay =fields.Integer(string="Charges To Pay",tracking=True)
    state = fields.Selection([('allocated', 'Allocated'), ('deallocated', 'Deallocated')],
                         string="Status",default='deallocated', required=True,tracking=True)
    email = fields.Char(string="Email", size=100, help="Email address",tracking=True)


# Show notification when room allocation happens
    def action_allocate_room(self):
        for rec in self:
            rec.state = 'allocated'
            message = "Student Room allocation done to",self.name.name
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'target': 'new',
                'params': {

                    'type': 'success',
                    'message': message,
                    'next': {'type': 'ir.actions.act_window_close'},
                }}


#Show notification when room deallocation happens
    def action_deallocate_room(self):
        for rec in self:
            rec.state = 'deallocated'
            message = "Student Room Deallocation done"
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'target': 'new',
                'params': {

                    'type': 'success',
                    'message': message,
                    'next': {'type': 'ir.actions.act_window_close'},
                }}


#What happen when somneone try to delete record
    @api.ondelete(at_uninstall=False)
    def check_allocation(self):
        for rec in self:
            if rec.state == 'allocated':
                raise UserError("You can't delete record with state allocated")


#To get default date in date field
    def _get_default_date(self):
       return fields.Date.context_today(self)


# when we create new record it will change parametr value in hotel_room model
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


#what functionality should happen during update or write which reflactes in hostel.room model
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


    def action_print_student_pdf(self):
        self.ensure_one()
        return self.env.ref('school_managment.student_hostel_receipt').report_action(self.id)


 #cron method to change state from allocated to deallocate written in cron file
    @api.model
    def update_meeting_state(self):
        meetings = self.search([('state', '=', 'allocated')])
        for meeting in meetings:
            meeting.write({'state': 'deallocated'})
        return True

    def action_open_url(self):
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': 'https://www.odoo.com/documentation/18.0/',
        }


#for functionality check for mapped,sorted,filtered
    def test_recordset(self):
        for rec in self:
            students = self.env['stulist.model'].search([])
            print("partners ...",students.mapped('name'))
            print("sorted partners ...", students.sorted(lambda o:o.name))
            print("filtered partners ...", students.filtered(lambda o: o.fees_status == 'Paid'))




#sent mail show in chatter box
    def action_sent_email(self):
        self.ensure_one()
        template = self.env.ref(
            "school_managment.hostel_receipt", raise_if_not_found=False
        )
        ctx = {
            "default_model": "hostel.admission",
            "default_res_ids": [self.id],
            "default_use_template": bool(template),
            "default_template_id": template.id if template else False,
            "default_composition_mode": "comment",
            "force_email": True,
        }
        return {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "mail.compose.message",
            "target": "new",
            "context": ctx,
        }










