{
    "name": "Education Managment",  
    "description": "A simple Teacher-model application",
    "summary": "A sheet for teacher management",
    "version": "0.1.0",
    "category": "Productivity",
    "sequence": -1,
    "author": "prachi_brahmbhatt",
    "depends": [
        "base","sale","mail"
        
        
    ],
    "data": [
        # This file defines user access rules, like who can read, write, create, or delete records in this module.
        "security/ir.model.access.csv",
        #"data/teacher_data.xml",
        "data/mail_template.xml",
        "data/sequence_data.xml",
        "data/cron_test.xml",
        'views/sale_order.xml',
        'views/templates.xml',
        "views/timetable.xml",
         "views/student.xml",
        "views/scedule_exam.xml",
        "views/attandence.xml",
        "views/syllabus.xml",
        "views/pta.xml",
        "views/department.xml",
        "views/res_config_settings_view.xml",
        "views/hostel_room.xml",
        "views/hostel_admission.xml",
        "views/teacher.xml",
        "views/result.xml",
        "views/inherits.xml",
        "wizard/student_admi.xml",
         "report/school_managment_views.xml",
         "report/school_managment_template.xml",





       
        
        
        #This file defines how the Teacher records appear in Odoo (Forms, Lists, Kanban views, etc.)
    ], 

    'assets': {
        'web.assets_backend': [
            'school_managment/static/src/css/style.css',
            'school_managment/static/description/icon.png',
        ],
},
    "installable": True,
    "application": True,
    "license": "LGPL-3"

}