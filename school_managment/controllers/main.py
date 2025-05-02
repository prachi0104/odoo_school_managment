from odoo import http
from odoo import models
from odoo.http import request,route
import logging
_logger = logging.getLogger(__name__)



class School(http.Controller):

    @http.route('/', website=True, auth='public')
    def homepage(self):
        return request.render("school_managment.home_page_template_new")

    @http.route('/student', website=True, auth='user',groups="school_managment.group_school_teacher")
    def studentcorner(self, **kw):
         return request.render("school_managment.student_corner",{})

    @http.route('/teacher', website=True,auth='user',groups="school_managment.group_school_teacher")
    def teacher_list(self, **kw):
            teacher_list = request.env['teacher.model'].search([])
            return request.render("school_managment.teacher_temp", {'teacher': teacher_list})

    @http.route('/submit',website=True,auth='public',type='http',csrf=True, methods=["POST"])
    def submit(self,**post):
        name=post.get('name')
        date_of_birth=post.get('date_of_birth')


        student=request.env['stulist.model'].sudo().create({
            'name':name,
            'date_of_birth':date_of_birth
        })

        enrollment_no=student.enrollment
        return request.render("school_managment.student_success",{
            'name': name,
            'enr': enrollment_no,
        })


    @http.route('/student_profile',website=True,auth='user',groups="school_managment.group_school_teacher")
    def student_profile(self):
        students=request.env['stulist.model'].sudo().search([])
        return request.render("school_managment.student_profile_tem",{'students':students})

    @http.route('/student/profile/<int:student_id>', website=True, auth='user')
    def student_profile_detail(self, student_id):
        student = request.env['stulist.model'].sudo().browse(student_id)
        if not student.exists():
            return request.not_found()

        return request.render("school_managment.student_detail_tem", {
            'student': student,
        })

    @http.route('/hostel' , website=True,auth="user",groups="school_managment.group_school_teacher")
    def hostel_inquirey(self):
        hostel=request.env['hostel.room'].sudo().search([])
        student= request.env['stulist.model'].sudo().search([])
        return request.render("school_managment.hostel_tem", {'hostel': hostel, 'rooms': hostel,'student_data':student})

    @http.route('/hostel-submit',website=True,auth="public",csrf=False,methods=["POST"])
    def hostel_submit(self,**post):
        request.env['hostel.admission'].sudo().create({
            'name':post.get('student_name'),
            'room_type': int(post.get('room_type')),
            'admission_date': post.get('admission_date'),
            'per_sem_charge': int(post.get('per_sem_charge')),
            'charges_to_pay': int(post.get('charges_to_pay')),
            'email':post.get('email'),})
        return request.render("school_managment.student_success", {})

    @http.route('/my/custom', type='http', auth='user', website=True)
    def portal_student_custom(self, **kw):
            user = request.env.user
            student = request.env['stulist.model'].sudo().search([('user_id', '=', user.id)], limit=1)
            result= request.env['result.model'].sudo().search([('user_id','=', user.id)],limit=1)
            hostel = request.env['hostel.admission'].sudo().search([('user_id','=',user.id)],limit=1)
            ptm = request.env['parentsteachermeeting.model'].sudo().search([('user_id', '=', user.id)], limit=1)
            return request.render('school_managment.portal_my_custom_template', {
                'student': student,
                'result':result,
                'hostel':hostel,
                'ptm':ptm
            })

    @http.route('/cantin',type='http',auth='public', website=True )
    def cantin_menu(self):
        return request.render("school_managment.canteen_menu_template_new", {})

    @http.route('/courses', website=True, auth='public')
    def student_courses(self):
        courses = request.env['student.courses'].sudo().search([])
        return request.render("school_managment.student_courses_website_template", {'courses': courses})

    @route('/json', type='json', auth='public',methods=['POST'], csrf=False )
    def get_students(self):
        students = request.env['stulist.model'].sudo().search([])
        student_data = [{
            'name': student.name,
            'enrollment': student.enrollment,
            'std': student.std
        } for student in students]
        return student_data

    @http.route('/my/json/endpoint', type='json', auth='user', methods=['POST'], csrf=False)
    def my_json_endpoint(self, **kwargs):
        user = request.env.user
        return {
            'message': f'Hello {user.name}, this is a protected JSON route!',
            'user_id': user.id,
            'email': user.email,
        }

    @http.route('/upload/document', type='http', auth='public', website=True)
    def student_document_upload_form(self, **kw):
        students = request.env['stulist.model'].sudo().search([])
        return request.render('school_managment.student_document_upload_website_new', {'students': students})

    @http.route('/submit_student_document', type='http', auth='public', methods=['POST'], csrf=True, website=True)
    def submit_student_document(self, **post):
        # Get the uploaded file
        uploaded_file = post.get('file')
        file_content = uploaded_file.read() if uploaded_file else False
        file_name = uploaded_file.filename if uploaded_file else False

        request.env['student.document'].sudo().create({
            'name': post.get('name'),
            'upload_date': post.get('upload_date'),
            'student_id': int(post.get('student_id')) if post.get('student_id') else False,
            'file': file_content,
            'file_name': file_name,
            'description': post.get('description'),
        })

        return request.render('school_managment.student_success', {})  # Show a success p

    @http.route('/student_syllabus', type='http', auth='user', website=True)
    def student_syllabus(self, **post):
        student_syllabus = request.env['syllabus.model'].sudo().search([])
        return request.render("school_managment.student_syllabus", {'student_syllabus': student_syllabus})


    @http.route('/student_busroute', type='http', auth='user', website=True)
    def student_busroute(self, **post):
        route = request.env['busroute.model'].sudo().search([])
        return request.render("school_managment.student_busroute_template_new", {'route': route})


    @http.route('/product_review', website=True, auth='public')
    def product_review(self, **kw):
        current_partner = request.env.user.partner_id

        products = request.env['product.review'].sudo().search([('partner_id','=',current_partner.id)])
        stock= request.env['product.product'].sudo().search([])
        partners = request.env['res.partner'].sudo().search([])

        return request.render("school_managment.product_review_template", {'products':products,'stock':stock,'partners':partners})















