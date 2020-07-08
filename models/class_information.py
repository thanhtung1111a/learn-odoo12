from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Class_Infor(models.Model):
    _name = 'class.information'
    _description = 'Class Information'

    @api.constrains('monitor')
    def check_monitor(self):
        for _class in self:
            if _class.monitor==_class.vice_monitor:
                raise ValidationError(
                    'Moniter and Vice Moniter must different!')
        return True
    name = fields.Char('Name', required=True)
    class_id = fields.Char('Class ID')
    school_year=fields.Integer('School Year')
    date_start=fields.Date(string='Date Start')
    date_end=fields.Date(string='Date End')
    homeroom_teacher=fields.Many2one('teacher.information',string='Homeroom Teacher')
    monitor=fields.Many2one('student.information',string='Monitor')
    vice_monitor=fields.Many2one('student.information',string='Vice Monitor')

   