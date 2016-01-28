# -*- encoding: utf-8 -*-
#                                                                            #
#   OpenERP Module                                                           #
#   Copyright (C) 2016 Vizthoughts Consultancy ltd. <info@vizthoughts.com>                               #
#                                                                            #
#   This program is free software: you can redistribute it and/or modify     #
#   it under the terms of the GNU Affero General Public License as           #
#   published by the Free Software Foundation, either version 3 of the       #
#   License, or (at your option) any later version.                          #
#                                                                            #
#   This program is distributed in the hope that it will be useful,          #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#   GNU Affero General Public License for more details.                      #
#                                                                            #
#   You should have received a copy of the GNU Affero General Public License #
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.    #
#                                                                            #

{
    'name': "WebSite Event Filter City",
	'summary': 'Filter Events by cities in the frontend/website',
    'version': "8.0.1.0.0",
    'depends': ["base"],
    'author': "sum1201",
	          'Vizthoughts Consultancy Ltd.',
    "category": "website",
    "description": """
    """,
    "depends":['website_event'],
    "data":[
        'views/website_event.xml'
    ],
    "init_xml": [],
    'update_xml': [],
    'demo_xml': [],
    'installable': True,
    'active': True,
    #    'certificate': '',
}
