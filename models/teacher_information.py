from odoo import models, fields, api

class Teacher_Infor(models.Model):
    _name = 'teacher.information'
    _description = 'Teacher Information'

    name = fields.Char('Name', required=True)
    id_teacher = fields.Integer('ID Teacher', required=True)
    id_social = fields.Char('ID Social')
    gender=fields.Selection([('male','Male'),
    ('female','Female'),('other','Other')],
    default='male',string='Gender')
    date_birth = fields.Date()
    image = fields.Binary('Cover')
    phone = fields.Char('Phone')
    address = fields.Char('Address')
    note = fields.Text('note')