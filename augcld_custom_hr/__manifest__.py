# -*- coding: utf-8 -*-

# Custom HR Module by Augusto Calado

{
    'name': 'Custom HR Module',
    'summary': 'Adds custom fields to employee form',
    'version': '14.0.0.0.0',
    'category': 'Human Resources',
    'author': 'Augusto Calado',
    'description': """
     Addon para incluir 3 novos campos no cadastro de funcionários:
      - Setor (um campo idêntico ao campo Departamento),
      - CBO (campo numérico) e
      - eSocial (campo numérico)""",
    'depends': ['base','hr'],
    'data': ['views/hr_employee_extension.xml'],
    'installable': True,
}
