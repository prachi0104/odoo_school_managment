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
    user_id = fields.Many2one('res.users', string="User", ondelete="cascade")


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
    @api.model_create_multi
    def create(self, vals_list):
        admissions = super(HostelAdmission, self).create(vals_list)
        for vals, admission in zip(vals_list, admissions):
            if vals.get('state') == 'allocated' and vals.get('room_type'):
                room = self.env['hostel.room'].browse(vals['room_type'])
                if room:
                    room.occupied += 1
                    room.available = room.total_room - room.occupied
        return admissions


#what functionality should happen during update or write which reflactes in hostel.room model
    def write(self, vals):
        for rec in self:
            old_state = rec.state
            new_state = vals.get('state', old_state)
            room = rec.room_type

            if room and old_state != new_state:
                # Handle transition logic
                if old_state == 'allocated' and new_state == 'deallocated':
                    room.occupied = max(0, room.occupied - 1)
                elif old_state == 'deallocated' and new_state == 'allocated':
                    room.occupied += 1

                # Recalculate available
                room.available = room.total_room - room.occupied

        return super(HostelAdmission, self).write(vals)

    def action_print_student_pdf(self):
        self.ensure_one()
        return self.env.ref('school_managment.student_hostel_receipt').report_action(self.id)


 #cron method to change state from allocated to deallocate written in cron file
    # @api.model
    # def update_meeting_state(self):
    #     meetings = self.search([('state', '=', 'allocated')])
    #     for meeting in meetings:
    #         meeting.write({'state': 'deallocated'})
    #     return True

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




# sent mail show in chatter box
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










