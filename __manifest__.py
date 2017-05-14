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
        'web',
        'website',
    ],
    'data': [
        'xml/website_menus.xml',
        'xml/website_templates.xml',
        'xml/views.xml',
        'xml/pages/homepage.xml',
        'xml/assets.xml',
    ],
    'installable': True,
    'application': True,
    'qweb': [],
}
