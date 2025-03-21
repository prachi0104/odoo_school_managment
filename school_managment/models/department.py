from enum import unique

from odoo import models,fields,api,_
from datetime import date


class Department(models.Model):
    _name = "department.model"
    _description = "Department"

    name = fields.Char(string="Department Name", required=True,unique=True)
    list_of_subjects=fields.Html(sanitize=False)


    @api.returns('self',lambda value: value.id)
    def copy(self,default=None):
        if default is None:
            default = {}
        if not default.get('name'):
            default['name'] = self.name + "(copy)"
        return super(Department,self).copy(default)


    _sql_constraints = [
        ('unique_department_name', 'UNIQUE(name)',
         'Department Name must be unique for each department.')
    ]