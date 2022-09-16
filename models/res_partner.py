
from odoo import fields, models
import logging

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = ["res.partner"]
    notes_count = fields.Integer(string="Note", compute="compute_notes_count")
    note_ids = fields.One2many("note.note", "partner_id", readonly=True)

    def compute_notes_count(self):
        for record in self:
            result = self.env['note.note'].search_count([('partner_id', '=', record.id)])
            record.notes_count = result

    def action_go_to_notes(self):
        action = self.env.ref('note.action_note_note').read()[0]
        action['domain'] = [('id', 'in', self.note_ids.ids)]
        action['context'] = {
            'default_partner_id': self.note_ids.partner_id.id,
            'readonly_partner_id': True,
        }
        return action

