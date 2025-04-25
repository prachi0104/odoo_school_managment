from odoo import models, fields,api
from odoo import http
from odoo.http import request

class SchoolDashboard(models.Model):
    _name = 'school.dashboard'
    _description = 'School Management Dashboard'

    total_students = fields.Integer(string="Students", compute="_compute_totals")
    total_teachers = fields.Integer(string="Teachers", compute="_compute_totals")
    total_department = fields.Integer(string="Department", compute="_compute_totals")
    results_ids = fields.One2many('result.model', 'dashboard_id', string='Results')

    def _compute_totals(self):
        self.total_students = self.env['stulist.model'].search_count([])
        self.total_teachers = self.env['teacher.model'].search_count([])
        self.total_department = self.env['department.model'].search_count([])
        self.results_ids = self.env['result.model'].search([])

    @api.model
    def get_singleton_dashboard(self):
        dashboard = self.search([], limit=1)
        if not dashboard:
            dashboard = self.create({})
        return dashboard.id

    def action_refresh_dashboard(self):
        self._compute_totals()




