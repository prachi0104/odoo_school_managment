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




        def create_task_from_email(self, subject, description, assign_to=None, priority='medium'):
            """
         Creates a task from the provided email data.
            """
            return self.create({
            'name': subject or 'No Subject',
            'description': description or 'No Description',
            'assign_to': assign_to.id if assign_to else self.env.user.id,
            'priority': priority,
        })
