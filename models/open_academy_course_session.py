from odoo import _, fields, models, api
from odoo.exceptions import ValidationError


class OpenAcademyCourseSession(models.Model):
    _name = 'open.academy.course.session'
    _description = 'Course Session'

    name = fields.Char()
    start_date = fields.Datetime(default=fields.Date.context_today)
    end_date = fields.Datetime()
    duration = fields.Float()
    number_of_seat = fields.Integer()
    taken_seat = fields.Integer()
    taken_seat_percent = fields.Integer()
    # compute = '_get_percentage'
    active = fields.Boolean(default=True)

    instructor = fields.Many2one('res.partner')
    course = fields.Many2one('open.academy.course')

    attendee_ids = fields.Many2many('res.partner')

    # _sql_constraints = [
    #     ('title_description_differ', 'check()')
    # ]

    # @api.depends('number_of_seat', 'taken_seat')
    # def _get_percentage(self):
    #     for rec in self:
    #         if rec.number_of_seat == 0:
    #             rec.taken_seat_percent = 0
    #         else:
    #             rec.taken_seat_percent = (rec.taken_seat / rec.number_of_seat) * 100

    def print_session(self):
        return self.env.ref('open_academy.open_academy_course_session_report').report_action(self)

    @api.onchange('number_of_seat', 'taken_seat')
    def _onchange_price(self):
        if (self.taken_seat > 0) and (self.taken_seat <= self.number_of_seat):
            self.taken_seat_percent = (self.taken_seat / self.number_of_seat) * 100
        else:
            return {
                'warning': {
                    'title': _("Invalid value"),
                    'message': _("Taken seat must higher than 0 and smaller than Number of seat"),
                }
            }

    @api.constrains('attendee_ids')
    def check_instructor_present(self):
        for rec in self:
            if rec.instructor.ids[0] in rec.attendee_ids.ids:
                raise ValidationError('Instructor can be in their own Session')
