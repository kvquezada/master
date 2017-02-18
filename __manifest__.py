# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Keith Iris Photography',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Keith Portfolio',
    'description': """
        Aim to create a website for photography
    """,
    'website': 'https://www.keithiris.com/',
    'depends': [
        'base',
        'website',
    ],
    'data': [
        'security/hr_security.xml',
        'security/ir.model.access.csv',
        'views/hr_views.xml',
        'views/hr_templates.xml',
        'data/hr_data.xml',
    ],
    'installable': True,
    'application': True,
    'qweb': [],
}
