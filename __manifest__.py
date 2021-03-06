# -*- coding: utf-8 -*-
{
    'name': " Juan Luis Gomez Garcia",

    'summary': """
        Aplicacion para almacenar y gestionar la formacion de los empleados""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Juan Luis Gomez Garcia",
    'website': "http://www.juguetesreunidos.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Generic Modules',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
