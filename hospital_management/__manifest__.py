{
    'name': 'Hospital Management',
    'version': '1.1',
    'summary': 'Hospital Management',
    'sequence': -100,
    'description': """Hospital Management""",
    'website': 'https://www.odoo.com,
    'license': 'AGPL-3',
    'depends': ['base','sale','product','mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'wizard/create_appointment_views.xml',
        'views/patient.xml',
        'views/kids.xml',
        'views/patient_gender_view.xml',
        'views/appointment.xml',
        'views/sale.xml',
        'views/sale_product.xml',
        'views/doctor.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
