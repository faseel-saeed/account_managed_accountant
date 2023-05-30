# -*- coding: utf-8 -*-
{
    'name': 'Accounts - Managed Accountant',
    'version': '0.1',
    'author': 'Benlever Pvt Ltd',
    'company': 'Benelever Pvt Ltd',
    'website': 'https://www.benlever.com',
    'maintainer': 'Benlever Pvt Ltd',
    'category': 'Accounting/Accounting',
    'sequence': 6,
    'summary': 'Managed Invoice Manager for Accounting Module.',
    'description': """

It gives the more flexibility to define groups who have access to create invoices instead of the default accounting group.
This allows custom groups to ashout from Point of Sales Module without having the full rights of the Accounting.

""",
    'depends': ['account'],
    'data': [
        'views/res_config_settings_views.xml'
    ],
    'installable': True,
    'license': 'LGPL-3',
}
