# -*- coding: utf-8 -*-

from odoo import models, fields, api

class catalogo(models.Model):
    _name = 'formacionjgg.catalogo'
    _description = 'Datos de los cursos'
    _sql_constraints =[('name_uniq','unique(name)',"Este curso ya existe")]

    name = fields.Char('Nombre del curso',required=True)
    duration = fields.Integer('Duracion',required=True,default=48)
    name_trainer = fields.Many2one('formacionjgg.datoproveedores',string='Nombre del proveedor')
    start_date = fields.Date('Fecha de inicio',default=fields.datetime.now())
    description = fields.Text('Descripcion')
    

class datoproveedores(models.Model):
    _name = 'formacionjgg.datoproveedores'
    _description = 'Datos de los proveedores'
    _sql_constraints =[('name_uniq2','unique(name_company)',"Este formador ya existe")]
    _sql_constraints =[('name_value','unique(name_supplier)',"Este proveedor ya existe")]

    name_company = fields.Char('Nombre de la empresa',required=True)
    name_supplier = fields.Char('Nombre del proveedor',required=True)
    name_trainer = fields.Many2one('formacionjgg.datoempleados',string='Nombre del formador')
    
class acciones(models.Model):
    _name = 'formacionjgg.acciones'
    _description = 'Datos de las acciones'
    _sql_constraints =[('name_uniq3','unique(name_action)',"Esta accion ya existe")]

    name_action = fields.Char('Id de la accion',required=True)
    name_course = fields.Many2one('formacionjgg.catalogo',string='Nombre del curso',required=True)
    name_trainer = fields.Many2one('formacionjgg.datosempleados',string='Nombre del formador')
    names_employees = fields.Many2many('hr.employee',string='Participantes')
    number_sessions = fields.Integer('Numero de sesiones')

class datosempleados(models.Model):
    _name = 'formacionjgg.datosempleados'
    _description = 'Datos de los formadores'
    _sql_constraints = [('name_value3', 'unique(name_trainer)', "Este etrenador ya existe")]

    name_trainer = fields.Char('Nombre del formador',required=True)
    specialty = fields.Char('Especialidad')
    


