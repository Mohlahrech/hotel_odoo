# -*- coding: utf-8 -*-
{
    'name': "od_ceti2",

    'summary': """
        crée par moh""",

    'description': """
        crée par moh
    """,

    'author': "CETI_MOH",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts','mail','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/views.xml',
        'data/formation_sequence.xml',
        'data/formation_stage.xml',

    ],

    'installable': True
}
