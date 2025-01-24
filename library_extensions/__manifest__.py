# __manifest__.py
{
    'name': 'Library Extensions',
    'version': '1.0',
    'category': 'Library',
    'author': 'Your Name',
    'website': 'http://yourwebsite.com',
    'depends': ['library'],
    'data': [
        'views/library_book_category_views.xml',
        'views/library_book_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
}
