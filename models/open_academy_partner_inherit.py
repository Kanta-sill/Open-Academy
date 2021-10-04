from odoo import _, fields, models, api


class OpenAcademyPartnerInherit(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    instructor = fields.Boolean(default=False)
    teacher_level1 = fields.Boolean(default=False)
    teacher_level2 = fields.Boolean(default=False)
    attendee = fields.Boolean(default=False)
