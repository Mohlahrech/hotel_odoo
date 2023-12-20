{
    'name': 'Test Customizations',
    'summary': """Test Customizations""",
    'version': '15.1.1.0.1',
    'description': """Test Customizations""",

    'category': 'tool',
    'depends': ['base_setup','product','account','website','report_xlsx',"sale", "sale_management"],

    'data': [
        'security/ir.model.access.csv',
        'security/groups_students.xml',
        'reports/student_registration_form.xml',
        'reports/actions_student_wizard.xml',
        'reports/analysis_report.xml',
        'views/students_process.xml',
        'wizard/student_wizard_view.xml',
        'views/product_inherit.xml',
        'views/controller_views.xml',
        'views/website_app_view.xml'
  
    ],

    'installable': True,
    'auto_install': False,

}
