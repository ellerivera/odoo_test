# -*- coding: utf-8 -*-
{
    'name': "Website Customization",
    'summary': """ This is a module created for custom the CRM module in Odoo v16. """,
    'author': "Daniela Rivera Feria",
    'website': " ",
    'application': True,
    'category': 'website',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': ['views/menu.xml',
             'views/request_customers_promotions.xml',
             'views/view_customers_promotions.xml',
             ],

    # only loaded in demonstration mode
    'demo': [],

    'assets': {
        'web.assets_frontend': [
            'website_customization/static/src/css/style.css',
        ],

        'web.assets_backend': []
    },

    'installable': True,
    'auto_install': False
}
