{
    'name': 'Monivertical Report Customization',
    'category': 'Sales',
    'description': """
Monivertical Report Customization
=================================
- Sale Report Customization
    """,
    'depends': ['web', 'sale_management',  'point_of_sale'],
    'data': [
            # Report
            'report/classic_report_template.xml',
            'report/fency_report_template.xml',
            'report/modern_report_template.xml',
            'report/odoo_std_report_template.xml',
            'report/fxo_custom_report_sale_order.xml',
            'report/saleorder_report_inherit.xml',
            'report/report.xml',
            # views
            'views/res_company_views.xml',
        ],
    'qweb': [],

    'installable': True,
    'application': False,
}