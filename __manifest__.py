{
    'name': 'Medical Records Demo',
    'version': '1.0',
    'category': 'Healthcare',
    'summary': 'Basic Medical Records Management System',
    'description': """
        Demo Medical Records Management System includes:
        - Patient Management
        - Medical History Tracking
        - Doctor Records
    """,
    'author': 'HONGVIET',
    'website': 'https://www.yourwebsite.com',
    
    # Dependencies
    'depends': ['base', 'mail'],
    
    # Data files to load
    'data': [
        'security/medical_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/menu.xml',
        'views/hospital_room_view.xml',
        'views/hospital_bed_view.xml',
        'views/patient_admission_view.xml',
        'security/ir.model.access.csv',
    ],
    
    'demo': [
        'demo/demo_data.xml',
    ],
    
    'application': True,
    'installable': True,
    'auto_install': False,
    'sequence': 1,
}
