# -*- coding: utf-8 -*-
{
    'name': "create_invoice_db",

    'summary': """
        It create invoice on button click on other db """,

    'description': """
        It create invoice on button click on other db through odoo api
        First you have to go to Setting > Configuration > DB Credentials 
        Enter the credentials 
        Now got to Accouting > Customer Invoice > 
        Open any Invoice and Click on Update DB You will get the required Result
    """,

    'author': "Ehtisham Faisal",
    'website': "http://www.oxenlab.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account_accountant'],

    # always loaded
    'data': [
        'templates.xml',
        'config.xml',
    ],
}