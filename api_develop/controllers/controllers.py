# -*- coding: utf-8 -*-
from email import header
import json
import math
import logging
# from urllib import request
import requests
import werkzeug.wrappers
import functools
from odoo.http import request

from odoo import api, http, _, exceptions
# from odoo.addons.project_api_models.common import invalid_response, valid_response
from odoo.exceptions import AccessDenied, AccessError

_logger = logging.getLogger(__name__)




class ApiDevelop(http.Controller):
     @http.route('/api_develop', website=True, auth='public', csrf=False, type='json', methods=['GET','POST'])
     def object(self, **params):
        contacts = http.request.env['res.partner'].sudo().search([])
        # getdata = {key: params.get(key) for key in params if params.get(key)}
        contact_list = []
        for contact in contacts:
            contact_list.append({
                'id':contact.id,
                'name':contact.name,
                'email': contact.email,
                'is_company': contact.is_company,
                'state_id': contact.state_id,
                })
        # contacts.write({'name':params['name']})
        return contact_list

class ApiDevelop(http.Controller):
     @http.route('/ListUser', website=True, auth='public', csrf=False, type='json', methods=['POST'])
     def object(self, **params):
        Users = http.request.env['res.users'].sudo().search([])
        # getdata = {key: params.get(key) for key in params if params.get(key)}
        user_list = []
        for user in Users:
            user_list.append({
                'id':user.id,
                'login':user.login,
                'password': user.password,
                })
        # contacts.write({'name':params['name']})
        return user_list



class ApiCheck(http.Controller):
    @http.route('/ApiCheck', website=False, auth='public', csrf=False, type='json', methods=['POST'])
    def object(self, **kw):
        PurchaseOrder = http.request.env['purchase.order'].sudo().search([('state', '=', 'draft')])
        arraypurchase= []
        for v in PurchaseOrder:
            arraypurchase.append({
                'name' : v.name,
                'code' : v.state
            })
        return arraypurchase


class ApiInvoice(http.Controller):
    @http.route('/ApiInvoice', website=False, auth='public', csrf=False, type='json', methods=['POST'])
    def object(self, **params):
        InvoiceList = http.request.env['account.move'].sudo().search([('state', '=', params['state'])])
        arrayinvoice = []
        for v in InvoiceList:
            arrayinvoice.append({
                'name' : v.name,
                'state' : v.state,
                'date' : v.date,
                'amount' : v.amount_total
            })
        return arrayinvoice

class ApiPurchaseList(http.Controller):
    @http.route('/ApiPurchaseList', website=False, auth='public', csrf=False, type='json', methods=['POST'])
    def object(self, **params):
        InvoiceList = http.request.env['account.move'].sudo().search([('state', '=', params['state'])])
        arrayinvoice = []
        for v in InvoiceList:
            arrayinvoice.append({
                'name' : v.name,
                'state' : v.state,
                'date' : v.date,
                'amount' : v.amount_total
            })
        return arrayinvoice

class CreateContact(http.Controller):
    @http.route('/CreateContact', website=False, auth='public', csrf=False, type='json', methods=['POST'])
    def object(self, **params):
        # getdata = {key: params.get(key) for key in params if params.get(key)}
        data = [(params['input'])]
        name = data[0]['name']
        # data_contact = {
        #     "name" : data.name,
        #     "create_date" : data.create_date,
        #     "display_name" : data.display_name,
        #     "lang" : data.lang,
        #     "active" : data.active,
        #     "type" : data.type,
        #     "street" : data.street,
        #     "street2" : data.street2,
        #     "city" : data.city,
        #     "email" : data.email,
        #     "mobile" : data.mobile,
        #     "is_company" : data.is_company,
        #     "commercial_company_id" : data.commercial_company_id,
        #     "create_uid" : data.create_uid,
        #     "message_bounce" : data.message_bounce,
        #     "picking_warn" : data.picking_warn,
        #     "invoice_warn" : data.invoice_warn,
        #     "supplier_rank" : data.supplier_rank,
        #     "customer_rank" : data.customer_rank,
        #     "purchase_warn" : data.purchase_warn,
        #     "l10n_id_pkp" : data.l10n_id_pkp,
        #     "sale_warn" : data.sale_warn,
        # }
        
        data_contact = {
            "name" : data[0]['name'],
            "create_date" : data[0]['create_date'],
            "display_name" : data[0]['display_name'],
            "street" : data[0]['street'],
            "street2" : data[0]['street2'],
            "city" : data[0]['city'],
            "email" : data[0]['email'],
            "mobile" : data[0]['mobile'],
        }
        
        input_contact = http.request.env['res.partner'].sudo().create(data_contact)
        
        status = {
            'status' : 200,
            'message' : 'succes'
        }
        return status

#api list vendor

class ListVendor(http.Controller):
     @http.route('/ListVendor', website=True, auth='public', csrf=False, type='json', methods=['GET','POST'])
     def object(self, **params):
        vendor = http.request.env['res.partner'].sudo().search([])
        # getdata = {key: params.get(key) for key in params if params.get(key)}
        list_vendor = []
        for contact in vendor:
            list_vendor.append({
                'id':contact.id,
                'name':contact.name,
                })
        # contacts.write({'name':params['name']})
        return list_vendor

#api untuk buat purchase order
class CreatePurchase(http.Controller):
    @http.route('/CreatePurchase', website=False, auth='public', csrf=False, type='json', methods=['POST'])
    def object(self, **params):
        # getdata = {key: params.get(key) for key in params if params.get(key)}
        data = [(params['input'])]
        name = data[0]['name']
        
        data_purchase = {
            "name" : data[0]['name'],
            "create_date" : data[0]['create_date'],
            "display_name" : data[0]['display_name'],
            "street" : data[0]['street'],
            "street2" : data[0]['street2'],
            "city" : data[0]['city'],
            "email" : data[0]['email'],
            "mobile" : data[0]['mobile'],
        }
        
        # input_contact = http.request.env['res.partner'].sudo().create(data_contact)
        
        # status = {
        #     'status' : 200,
        #     'message' : 'succes'
        # }
        return status
    
    #api list product

class ListProduct(http.Controller):
     @http.route('/ListProduct', website=True, auth='public', csrf=False, type='json', methods=['GET','POST'])
     def object(self, **params):
        product = http.request.env['product.template'].sudo().search([])
        # getdata = {key: params.get(key) for key in params if params.get(key)}
        list_product = []
        for v in product:
            list_product.append({
                'id':v.id,
                'name':v.name,
                })
        # contacts.write({'name':params['name']})
        return list_product
    
class ListPurchaseReq(http.Controller):
    @http.route('/ListPurchaseReq', website=True, auth='public', csrf=False, type='json', methods=['POST'])
    def object(self, **params):
        request = http.request.env['purchase.request'].sudo().search([('name','=',params['name'])])
        # requested = []
        # for vr in request:
        #     requested.append(
        #          vr.requested_by
        #     )
        # viewUser = http.request.env['res.users'].sudo().search([('id', '=', requested)])
        # vuser = []
        # for vu in viewUser:
        #     vuser.append({
        #         'id' : vu.id,
        #         'login' : vu.login  
        #     })
        return request
    
    
    #get list employe
    @http.route('/   ', website=True, auth='public', csrf=False, type='json', methods=['POST'])
    def object(self):
        listEmploye = http.request.env['hr.employee'].sudo().search([])
        list = []
        for v in listEmploye:
            list.append({
                'name' : v.name,
                'gender' : v.gender,
                'birthday' : v.birthday,
                'phone' : v.mobile_phone,
                'email' : v.work_email,
            })
        return list

# class AccessToken(http.Controller):
#     @http.route('/web/session/authenticate', type='json', auth="none")
#     def authenticate(self, db, login, password, base_location=None):
#     request.session.authenticate(db, login, password)
#     return request.env['ir.http'].session_info()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def object(self, **kw):
    #     PurchaseOrder = http.request.env['account.move'].sudo().search([('state', '=', 'draft')])
    #     arraypurchase= []
    #     for v in PurchaseOrder:
    #         arraypurchase.append({
    #             'name' : v.name,
    #             'code' : v.state
    #         })
    #     return arraypurchase
      
        
 #@http.route[]'/api_develop', auth='public')
     #def hello(self, **kw):
     #return "hello word"
    #return http.request.render('api_develop.listing')
#     @http.route('/api_develop/api_develop/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('api_develop.listing', {
#             'root': '/api_develop/api_develop',
#             'objects': http.request.env['api_develop.api_develop'].search([]),
#         })

#     @http.route('/api_develop/api_develop/objects/<model("api_develop.api_develop"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('api_develop.object', {
#             'object': obj
#         })
