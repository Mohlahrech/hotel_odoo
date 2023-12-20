# -*- coding: utf-8 -*-
{
    "name": " OWL POS",
    "summary": "Eman Khalifa",
    "website": "",
    "category": "point_of_sale",
    "version": "15.0.1",
    "depends": ["base", "point_of_sale","web","pos_discount","sale_management"],
    'data': [
        'views/sales_order_view.xml',

    ],

    'assets': {

    'web.assets_qweb':[
        'owl_pos/static/src/xml/pos_product_button_view.xml' ,
        'owl_pos/static/src/xml/pos_payment_button_view.xml' ,
        'owl_pos/static/src/xml/pos_top_button_view.xml' ,
        'owl_pos/static/src/xml/PartnerOrderSummary.xml' ,
        'owl_pos/static/src/xml/pos_ticket_lines.xml',
        'owl_pos/static/src/xml/pos_ticket.xml',
        'owl_pos/static/src/xml/receipt_types.xml',
        'owl_pos/static/src/xml/keypad_custom.xml',
        'owl_pos/static/src/xml/pos_tree.xml'
       
    ],

    'web.assets_backend': [

        'owl_pos/static/src/js/pos_payment_button.js',
        'owl_pos/static/src/js/pos_top_button.js',
        'owl_pos/static/src/js/pos_product_screen_button.js',
        'owl_pos/static/src/js/pos_extra_extend.js',
        'owl_pos/static/src/js/partnerorder.js',
        'owl_pos/static/src/js/pos_receipt_type.js',
        'owl_pos/static/src/js/keypad_mode.js',
        'owl_pos/static/src/js/hide_archive.js',
        'owl_pos/static/src/js/hide_edit.js',
        'owl_pos/static/src/js/rpc_call.js',
        
    
    ],
       


    },

}



