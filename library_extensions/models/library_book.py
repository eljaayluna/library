# models/library_book.py
from odoo import models, fields

class LibraryBook(models.Model):
    _inherit = 'library.book'

    author_id = fields.Many2one('res.partner', string='Author', required=True)




