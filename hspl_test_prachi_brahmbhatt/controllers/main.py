from odoo import http
from odoo import models
from odoo.http import request,route


from odoo import http
from odoo import models
from odoo.http import request,route
import logging
_logger = logging.getLogger(__name__)



class Member(http.Controller):


    @http.route('/show_data', type='http', auth='user', website=True)
    def show_data(self, **kw):
        user = request.env.user
        member = request.env['membership.level'].sudo().search([('user_id', '=', user.id)], limit=1)
        return request.render('hspl_test_prachi_brahmbhatt.portal_my_custom_template', {
            'member': member,

        })
