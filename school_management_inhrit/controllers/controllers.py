# -*- coding: utf-8 -*-
# from odoo import http


# class SchoolManagementInhrit(http.Controller):
#     @http.route('/school_management_inhrit/school_management_inhrit', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/school_management_inhrit/school_management_inhrit/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('school_management_inhrit.listing', {
#             'root': '/school_management_inhrit/school_management_inhrit',
#             'objects': http.request.env['school_management_inhrit.school_management_inhrit'].search([]),
#         })

#     @http.route('/school_management_inhrit/school_management_inhrit/objects/<model("school_management_inhrit.school_management_inhrit"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('school_management_inhrit.object', {
#             'object': obj
#         })

