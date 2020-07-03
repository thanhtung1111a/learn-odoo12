from odoo import models, fields, api

class StudentInfo(models.Model):
    _name = 'student.information'
    _description = 'Student Information'

    @api.multi
    @api.depends('gpa')
    def set_classification(self):
        for student in self:
            if student.gpa:
                if student.gpa>=9.5:
                    student.classification='excellent'
                else:
                    if student.gpa>=6.5:
                        student.classification='good'
                    else:
                        if student.gpa>=6:
                            student.classification='average'
                        else:
                            student.classification='poor'
    name = fields.Char('Name', required=True)
    id_student = fields.Integer('ID Student', required=True)
    id_social = fields.Char('ID Social')
    gender=fields.Selection([('male','Male'),
    ('female','Female'),('other','Other')],
    default='male',string='Gender')
    date_birth = fields.Date()
    image = fields.Binary('Cover')
    phone = fields.Char('Phone')
    address = fields.Char('Address')
    gpa = fields.Float('GPA')
    classification=fields.Selection([('excellent','Excellent'),
    ('good','Good'),('average','Average'),('poor','Poor')],
    default='poor',string='Classification',compute='set_classification',store=True)
    note = fields.Text('note')