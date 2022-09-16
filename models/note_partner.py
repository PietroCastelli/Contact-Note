
from odoo import fields, models,api

class NotePartner(models.Model):
    _inherit = ["note.note"]
    partner_id = fields.Many2one('res.partner', string='Partner', ondelete='cascade')

