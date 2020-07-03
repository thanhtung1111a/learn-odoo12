{
    'name': 'Student Management',
    'description': 'Manage student and point',
    'author': 'Cao Thanh Tung',
    'depends': ['base'],
    'data':
    [
        'security/student_information_security.xml',
        'security/ir.model.access.csv',
        'views/student_infomation_menu.xml',
        'views/student_information_list.xml'
    ],
    'application': True,
}