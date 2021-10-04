from odoo import _, fields, models, api


class OpenAcademyCourse(models.Model):
    _name = 'open.academy.course'
    _description = 'Academy Course'
    _rec_name = 'title'

    title = fields.Char(require=True)
    description = fields.Text()
    state = fields.Selection(selection=[
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ], default='active')

    manager = fields.Many2one('res.users')
    manager_state = fields.Boolean(compute='_get_manager_status')
    session_ids = fields.One2many('open.academy.course.session', 'course')

    test = fields.Char(compute='get_title')

    _sql_constraints = [
        ('title_description_differ', 'check(title != description)', 'Title must be differ from Description'),
        ('unique_title', 'unique(title)', 'Title must be unique')
    ]

    def get_title(self):
        self.test = '1'
        self.env.cr.execute("""
        SELECT title, description
        FROM open_academy_course
        WHERE state = %(state)s
        """, {'state': 'active'})
        # ['active']
        # {'state': 'active'}
        # print(self.env.cr.dictfetchall())
        return

    @api.model
    def create(self, vals_list):
        if vals_list['title']:
            vals_list['title'] = '_' + vals_list['title']
        rec = super(OpenAcademyCourse, self).create(vals_list)
        return rec

    def copy(self, default=None):
        self.ensure_one()
        vals = self.with_context(active_test=False).copy_data(default)[0]
        if vals['title']:
            vals['title'] = 'Copy of ' + vals['title']
        # To avoid to create a translation in the lang of the user, copy_translation will do it
        new = self.with_context(lang=None).create(vals)
        self.with_context(from_copy_translation=True).copy_translations(new, excluded=default or ())
        return new

    @api.depends('manager')
    def _get_manager_status(self):
        self.manager_state = False
        if self.manager:
            self.manager_state = True

    def action_confirm(self):
        pass
