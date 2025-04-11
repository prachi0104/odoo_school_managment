from odoo import models, fields, api
from datetime import date,datetime


class SchoolTask(models.Model):
        _name = "school.task"
        _description = "assign school task to teacher"
        _inherit = ['mail.thread', 'mail.activity.mixin']


        name = fields.Char(string="Task")
        description = fields.Text()
        assign_to = fields.Many2one('teacher.model',string="Assigned_to")
        due_date = fields.Datetime('Target Date')
        priority = fields.Selection([
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High')
        ], default='medium', string='Priority')

        def create_task_from_email(self, subject, description, teacher_id=None):
            # Ensure teacher_id is valid
            if teacher_id:
                teacher = self.env['teacher.model'].browse(teacher_id)
                if not teacher.exists():
                    raise ValueError(f"Teacher with ID {teacher_id} does not exist.")
                assign_to = teacher
            else:
                assign_to = None

            # Create the task record with the provided subject, description, and assignment
            self.create({
                'name': subject,
                'description': description,
                'assign_to': assign_to.id if assign_to else False,
            })

