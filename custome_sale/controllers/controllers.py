# -*- coding: utf-8 -*-
# from odoo import http


# class CustomeSale(http.Controller):
#     @http.route('/custome_sale/custome_sale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custome_sale/custome_sale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custome_sale.listing', {
#             'root': '/custome_sale/custome_sale',
#             'objects': http.request.env['custome_sale.custome_sale'].search([]),
#         })

#     @http.route('/custome_sale/custome_sale/objects/<model("custome_sale.custome_sale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custome_sale.object', {
#             'object': obj
#         })
