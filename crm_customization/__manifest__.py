# -*- coding: utf-8 -*-
{
    'name': "CRM Customization",
    'summary': """ This is a module created for custom the CRM module in Odoo v16. """,
    'author': "Daniela Rivera Feria",
    'website': " ",
    'application': True,
    'category': 'sales',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['crm'],

    # always loaded
    'data': ['views/res_partner_views.xml'],

    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'auto_install': False
}
