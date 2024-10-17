{
    'name': 'TechCare',
    'version': '1.0',
    'summary': 'Connecting Medical Specialists with the Community',
    'category': 'Medical',
    'author': 'Hasan Ajweh',
    'depends': ['base', 'mail', 'calendar'],
    'data': [
        'security/ir.model.access.csv',       # Security access
        'security/techcare_security.xml',     # Security groups
        'views/techcare_views.xml',
    ],
    'installable': True,
    'application': True,
}
