{
    "name": "Education Managment",  
    "description": "A simple Teacher-model application",
    "summary": "A sheet for teacher management",
    "version": "0.1.0",
    "category": "Productivity",
    "sequence": 0,
    "author": "prachi_brahmbhatt",
    "depends": [
        "base","sale"
        
        
    ],
    "data": [
        # This file defines user access rules, like who can read, write, create, or delete records in this module.
        "security/ir.model.access.csv",
        #"data/teacher_data.xml",
        "data/sequence_data.xml",
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
        "views/teacher.xml",



       
        
        
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