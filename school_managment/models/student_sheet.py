from odoo import models,fields,api,_
from odoo.exceptions import UserError,ValidationError
from datetime import date, timedelta
from dateutil import relativedelta


class Stulist(models.Model):
    _name="stulist.model"
    _description="student list"

    name=fields.Char("Name",required=True)
    enrollment=fields.Char("Enrol")
    std=fields.Integer(string="Standerd")
    age=fields.Integer(string="Age",compute='_compute_age',inverse='_inverse_compute_age', store="True")
    date_of_birth=fields.Date(string="Date of birth")
    department_id = fields.Many2one("department.model", string="Department", ondelete="set null")
    total_marks=fields.Integer(compute='_compute_total_marks')
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')] )
    fees_status=fields.Char(string="Status")
    teacher_id=fields.Many2one('teacher.model',string="Class_teacher")
    guide_ids=fields.Many2many('teacher.model',string="Guides")
    image=fields.Image("image")
    track_attan=fields.One2many("attandence.model","stulist_id",string="Track History")
    stu_syllabus=fields.One2many("syllabus.model","student_id",string="Syllabus")
    ptm_ids = fields.One2many('parentsteachermeeting.model', 'name', string="PTM Records")
    record_status= fields.Char("Record Status")
    student_hostel = fields.One2many("hostel.admission", "name", string="Student hostel detail")
    fees_due_date = fields.Date(string="fees_due_date", default=lambda self: self._get_default_date())
    result_ids = fields.One2many('result.model', 'name', string="Results")
    is_paid = fields.Boolean(string="Paid or Not",compute="_compute_fees_Paid_or_not")
    user_id = fields.Many2one('res.users', string="User", ondelete="cascade")

    @api.depends('result_ids.total_obtain')
    def _compute_total_marks(self):
        for record in self:
            total_marks = sum(result.total_obtain for result in record.result_ids)
            record.total_marks = total_marks

    def _get_default_date(self):
        default_date = fields.Date.context_today(self) + timedelta(days=2)
        print(default_date)
        return default_date


    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > fields.date.today():
                raise ValidationError(_("The Entered Date Of birth is not accapteble"))


    def create(self,vals):
        print(vals)
        vals['enrollment'] = self.env['ir.sequence'].next_by_code('stulist.model')
        if 'total_marks' in vals and not vals['total_marks'] >=150:
            raise UserError('Students total marks  should be greate than 300 and name starts with h')
        return super().create(vals)


    def write(self, vals):
        print(vals)
        vals['record_status'] = "Edited Record"
        return super(Stulist, self).write(vals)


    def action_open_student_list(self):
        return { 
            'type':'ir.actions.act_window',
            'name':'Student_list',
            'res_model':'stulist.model',
            'view_mode':'list,form',
            'target':'current'
        }
    
    @api.depends('date_of_birth') #using this decorator it will reflect age in the form view it self without this it will reflact age after saving  
    def _compute_age(self):
        for rec in self:
         today=date.today()
         if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
         else:
                rec.age = 0

    @api.depends('age')
    def _inverse_compute_age(self):#to make age field editable
        today = date.today()
        for rec in self:
            rec.date_of_birth = today - relativedelta.relativedelta(years=rec.age)


    @api.depends('fees_status')
    def _compute_fees_Paid_or_not(self):
        for rec in self:
            if rec.fees_status == 'Unpaid':
                rec.is_paid = False
            else:
                rec.is_paid = True


#nameget and search function
    def name_get(self):
        """Customize the display name of records."""
        result = []
        for rec in self:
            display_name = '%s - %s' % (rec.enrollment, rec.name)
            result.append((rec.id, display_name))
        print(result)
        return result

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        """Enable search by enrollment or name in dropdowns."""
        if args is None:
            args = []
        domain = args + ['|', ('enrollment', operator, name), ('name', operator, name)]
        records = self.search(domain, limit=limit)
        return records.name_get()

















    






    

   
