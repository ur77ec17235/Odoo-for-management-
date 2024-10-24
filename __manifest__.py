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
    'author': 'Your Name',
    'website': 'https://www.yourwebsite.com',
    
    # Dependencies
    'depends': ['base', 'mail'],
    
    # Data files to load
    'data': [
        'security/medical_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/menu.xml',
    ],
    
    'demo': [
        'demo/demo_data.xml',
    ],
    
    'application': True,
    'installable': True,
    'auto_install': False,
    'sequence': 1,
}
