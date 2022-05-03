# -*- coding: utf-8 -*-
# from odoo import http


# class Formacionfjpalomo(http.Controller):
#     @http.route('/formacionfjpalomo/formacionfjpalomo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/formacionfjpalomo/formacionfjpalomo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('formacionfjpalomo.listing', {
#             'root': '/formacionfjpalomo/formacionfjpalomo',
#             'objects': http.request.env['formacionfjpalomo.formacionfjpalomo'].search([]),
#         })

#     @http.route('/formacionfjpalomo/formacionfjpalomo/objects/<model("formacionfjpalomo.formacionfjpalomo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('formacionfjpalomo.object', {
#             'object': obj
#         })
