{
    'name': 'Even Organisation',
    'summary': "Estate Account App",
    'author': "Odoo",

    'depends': ['base'],

    'installable': True,
    'application': True,

    'data': [
        'security/ir.model.access.csv',
        'views/event_type.xml',
        'views/event_org_views.xml',
        
    ],
    'demo':[
        'demo/demo_data.xml',
    ],
}
