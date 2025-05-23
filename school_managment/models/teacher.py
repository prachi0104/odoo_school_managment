from odoo import models,fields,api
from datetime import date

class teacher(models.Model):
    _name='teacher.model'
    _description='teacher model'
    _inherit = ['mail.thread']
    _order = 'sequence,id'

    sequence = fields.Integer(string="Sequence")
    name=fields.Char("Name",required=True)
    age = fields.Integer(string="Age", compute='_compute_age',store=True)
    dob= fields.Date(string="DOB", help="Date of Birth") #required=True
    department_id = fields.Many2one("department.model", string="Department", ondelete="set null")
    salary=fields.Integer()
    qualification=fields.Char("Qualification") #required=True
    address=fields.Text(string='Address')
    star_ids=fields.One2many('stulist.model','teacher_id',string='Star Students')
    phone = fields.Char(string="Pnone")
    email = fields.Char(string="Email")
    
    # Compute total number of students
    student_count = fields.Integer(string="Student Count", compute="_compute_student_count")
    task_id = fields.One2many('school.task', 'assign_to', string= "Assigned Task")

    @api.depends('star_ids')
    def _compute_student_count(self):
        for record in self:
            record.student_count = len(record.star_ids)



    # Action for Smart Button
    def action_open_students(self):
        return {
            'name': 'Students',
            'type': 'ir.actions.act_window',
            'res_model': 'stulist.model',
            'view_mode': 'list,form',
            'domain': [('teacher_id', '=', self.id)],
            'context': {'default_teacher_id': self.id},
        }


    @api.depends('dob') #using this decorator it will reflect age in the form view it self without this it will reflact age after saving
    def _compute_age(self):
        for rec in self:
         today=date.today()
         if rec.dob:
                rec.age = today.year - rec.dob.year
         else:
                rec.age = 0



