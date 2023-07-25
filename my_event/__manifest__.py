{
    'name': 'Event Organisation',
    'summary': "Estate Account App",
    'category': 'MY event/User',
    'author': "Odoo",

    'depends': ['base'],

    'installable': True,
    'application': True,

    'data': [
        'security/ir.model.access.csv',
        'views/event_services.xml',
        'views/event_type.xml',
        'views/event_venue.xml',
        'views/event_org_views.xml',
    ],
    # 'demo': [
    #     'demo/demo_data.xml',
    # ],
}
