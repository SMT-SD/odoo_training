

[
    'name': 'Hotel Management',
    'version': '15.0.1.0.2',
    'summary': 'Hotel Management Application for odoo 15',
    'description': """The module helps you to manage rooms,amenities,services,restaurants.
                      End Users can book rooms and reserve foods from hotel restaurant.""",
    'author': 'SMT',
    'company': 'SMT',
    'maintainer': 'SMT',
    'category': 'Sales',
    'depends': ['sale_management', 'account', 'stock'],
    'data': [
        'views/menus.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/room_reservation.xml',
        'views/hotel_meals.xml',
        'views/hotel_restaurant.xml',
        'views/res_settings.xml',
        'views/hotel_amenity.xml',
        'views/hotel_services.xml',
        'views/room_checkin_in_out.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',


}