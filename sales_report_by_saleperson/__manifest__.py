# -*- coding: utf-8 -*-
##############################################################################

##############################################################################

{
    'name': 'Sales Report By Sale Person',
    'category': 'sale',
    'version': '10.0.0.6',
    'summary': 'This module provides Sales Report By Sales person.',
    'website': ' ',
    'author': 'Crystal Technology Bangladesh Ltd.',
    'license': 'AGPL-3',
    'description': '''This module provides Sales Report By Sale Person.
                      '''
                   ,
    'depends': ['base', 'sale'],
    'data': [
        'wizard/sale_wzd_view.xml',
        'wizard/sale_collection_wzd_view.xml',
        'wizard/sale_saleperson_wzd_view.xml',
        'wizard/sale_saleperson_wzd_view.xml',
        'wizard/sale_productcate_wzd_view.xml',
        'wizard/bill_collection_wzd_view.xml',
        'wizard/product_category_wizard_view.xml',
        'report/menu_report.xml',
        'report/category_wise_report.xml',
        'report/saleperson_report_view.xml',
        'report/sale_collection_report_view.xml',
        'report/sale_saleperson_report_view.xml',
        'report/sale_productcate_report_view.xml',
        'report/sale_productcate_report_view.xml',
        'report/bill_collection_report_view.xml',
        'report/category_wise_report_view.xml',
    ],
    'auto_install': False,
    'installable': True,
    'application': False,
}
