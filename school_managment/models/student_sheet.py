from odoo import models,fields,api,_
from odoo.exceptions import UserError,ValidationError
from datetime import date, timedelta


class Stulist(models.Model):
    _name="stulist.model"
    _description="student list"


    name=fields.Char("Name",required=True)
    enrollment=fields.Char("Enrol")
    std=fields.Integer(string="Standerd")
    age=fields.Integer(string="Age",compute='_compute_age',store="True")
    date_of_birth=fields.Date(string="Date of birth")
    department_id = fields.Many2one("department.model", string="Department", ondelete="set null")
    total_marks=fields.Integer()
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
    fees_due_date=fields.Date(string="Fees Due Date")


    def create(sef,vals):
      vals['fees_due_date']= date.tody + timedelta(3)


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

    # @api.model_create_multi #at this point of time their is no diffrence between  @api.model_create_multi and normal @api.model just see for passing variable vals or vals_list
    # def create(self,vals_list):
    #     print(vals_list)
    #     for vals in vals_list:
    #         print(vals)
    #         vals['enrollment'] = self.env['ir.sequence'].next_by_code('stulist.model')
    #         if 'total_marks' in vals and not vals['total_marks'] >= 150:
    #             raise UserError('Students total marks should be greater than 150 and name starts with h')
    #     return super().create(vals_list)

    def write(self, vals):
        print(vals)
        print(self.name)
        vals['record_status'] = "Edited Record"
            # for record in self:
            #     if not record.name.startswith('#'):
            #         vals['name'] = '#' + record.name
        return super(Stulist, self).write(vals)


    def action_open_student_list(self):
        return { 
            'type':'ir.actions.act_window',
            'name':'Student_list',
            'res_model':'stulist.model',
            'view_mode':'list',
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




    






    

   
