# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
        Manage Academy""",

    'description': """
        Manage Academy
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/open_academy_groups.xml',
        'security/open_academy_session_security.xml',
        'wizard/course_session_register_attendee_views.xml',
        'views/open_academy_course_views.xml',
        'views/open_academy_course_session_views.xml',
        'views/open_academy_partner_inherit_views.xml',
        'report/open_academy_session_reports.xml',
        # 'data/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
