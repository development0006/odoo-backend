##############################################################################
#
#    OpenERP, Open Source Management
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
##############################################################################

{
    'name' : 'Odoo amazing Backend Theme',
    'version' : '0.1',
    'author' : 'Development06',
    "license": 'AGPL-3',

    'category' : 'Tools',
    'description': """
	Odoo 8.0 Amazing Backend theme.
	Features:
		Change Odoo Backend Colors and Change Buttons color and shape.
    """,
    'depends' : ['base'],
    'data':[
        'views.xml',
        ],
    'installable': True
}
