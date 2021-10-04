from odoo import _, fields, models, api


class CourseSessionRegisterAttendee(models.TransientModel):
    _name = 'course.session.register.attendee'

    name = fields.Char()

    def register_attendee(self):
        pass