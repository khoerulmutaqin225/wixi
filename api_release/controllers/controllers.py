# -*- coding: utf-8 -*-
import json
import math
import logging
from re import search
# from urllib import request
import requests
import werkzeug.wrappers
import functools
from odoo.http import request

from odoo import api, http, _, exceptions


#1. get purchase list
class ApiRelease(http.Controller):
    @http.route('/api_release/get_purchase_list/', website=True, auth='public', csrf=False, type='json', methods=['GET'])
    def object(self, **kw):
        list = http.request.env['purchase.request'].sudo().search([])
        purchaseList = []
        for see in list:
            purchaseList.append({
                'id':see.id,
                'name':see.name,
                'date_start': see.date_start,
                'remarks': see.remarks,
                'tanggal_po': see.tanggal_po,
                'company_id': see.company_id,
                'create_uid': see.create_uid,
                'purchase_order_id': see.purchase_order_id,
                })
        return purchaseList
    
#2 & 3 POST purchase request & POST purchase request line    
class PurchaseRequest(http.Controller):
    @http.route('/api_release/post_purchase_request', website=True, auth='public', csrf=False, type='json', methods=['POST'])
    def object(self, **params):
        # data = params.get('productdetail')
        # productdetail = data[0]['productdetail']
        if params:
            purreq = {
                'date_start'            : params.get('date_start'),
                'requested_by'          : params.get('requested_by'),
                'assigned_to'           : params.get('assigned_to'),
                'origin'                : params.get('origin'),
                'company_id'            : params.get('company_id'),
                'state'                 : params.get('state'),
                'picking_type_id'       : params.get('picking_type_id'),
                'create_uid'            : params.get('create_uid'),
                'estimated_arrival_date' : params.get('estimated_arrival_date'),
                'checked_by'            : params.get('checked_by'),
                'final_approve_by_id'   : params.get('final_approve_by_id'),
                'location_dest_id'      : params.get('location_dest_id'),
                'job_id'                : params.get('job_id'),
            }
        getpurreq = request.env['purchase.request'].sudo().create(purreq)
        productdetail = params.get('productdetail')
        purreqline = []
        for pl in productdetail:
            if pl.get('name') != '':
                # purreqline.append({
                purreqline = {
                'product_id'        : pl.get('product_id'),
                'name'              : pl.get('name'),
                'product_uom_id'    : pl.get('product_uom_id'),
                'product_qty'       : pl.get('product_qty'),
                'request_id'        : getpurreq.id,
                'company_id'        : pl.get('company_id'),
                'assigned_to'       : pl.get('assigned_to'),
                'date_start'        : pl.get('date_start'),
                'date_required'     : pl.get('date_required'),
                'request_state'     : pl.get('request_state'),
                'pending_qty_to_receive' : pl.get('pending_qty_to_receive'),
                'create_uid'        : pl.get('create_uid'),
                'checked_by'        : pl.get('checked_by'),
                'state'             : pl.get('state'),
                'location_dest_id'  : pl.get('location_dest_id'),
                'final_approve_by_id' : pl.get('final_approve_by_id'),
                'form_type'         : pl.get('form_type')
                }
                # })
            request.env['purchase.request.line'].sudo().create(purreqline)
        return params
    
    
#4. GET stock picking line (id)
class listStockPickingById(http.Controller):
    @http.route('/api_release/get_list_stok_picking_by_id/', website=True, auth='public', csrf=False, type='json', methods=['GET'])
    def object(self, **params):
        getStockById = http.request.env['stock.picking'].sudo().search([('id','=',params['id'])])
        stockListById = []
        for view in getStockById:
            stockListById.append({
                'id':view.id,
                'name':view.name,
                'origin': view.origin,
                'note': view.note,
                'move_type': view.move_type,
                'state': view.state,
                'second_state': view.second_state,
                'create_date': view.create_date,
                })
        return stockListById
    
    
#5. one purchase request (id)
class onepurchaseById(http.Controller):
    @http.route('/api_release/get_purchase_request_by_id/', website=True, auth='public', csrf=False, type='json', methods=['GET'])
    def object(self, **params):
        getById = http.request.env['purchase.request'].sudo().search([('id','=',params['id'])])
        purchaseListById = []
        for l in getById:
            purchaseListById.append({
                'id':l.id,
                'name':l.name,
                'date_start': l.date_start,
                'remarks': l.remarks,
                'tanggal_po': l.tanggal_po,
                'company_id': l.company_id.id,
                'create_uid': l.create_uid,
                'purchase_order_id': l.purchase_order_id,
                })
        return purchaseListById
    
#6. get list purchase request line
class onepurchaseLineById(http.Controller):
    @http.route('/api_release/get_purchase_line_by_requestid/', website=True, auth='public', csrf=False, type='json', methods=['GET'])
    def object(self, **params):
        getLineById = http.request.env['purchase.request.line'].sudo().search([('request_id.id','=',params['request_id'])])
        purchaseLineById = []
        for v in getLineById:
            purchaseLineById.append({
                'id':v.id,
                'name':v.name,
                'qty_in_progress':v.qty_in_progress,
                'qty_done': v.qty_done,
                'qty_cancelled' : v.qty_cancelled,
                'qty_to_buy' : v.qty_to_buy,
                'product_id' : v.product_id.id,
                'divisi_id' : v.divisi_id.id,
                'merk_barang' : v.merk_barang,
                'model_barang': v.model_barang,
                'nomor_seri' : v.nomor_seri,
                'purchase_order_id' : v.purchase_order_id.id,
                'request_id': v.request_id.id
                })
        return purchaseLineById

    # def object(self, **kw):
    # list = http.request.env['purchase_request'].sudo().search([])
    # purchaseList = []
    #     for l in list:
    #         purchaseList.append({
    #             'id':contact.id,
    #             'name':contact.name,
    #             'email': contact.email,
    #             'is_company': contact.is_company,
    #             'state_id': contact.state_id,
    #             })
    #     return purchaseList

#     @http.route('/api_release/api_release/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('api_release.listing', {
#             'root': '/api_release/api_release',
#             'objects': http.request.env['api_release.api_release'].search([]),
#         })

#     @http.route('/api_release/api_release/objects/<model("api_release.api_release"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('api_release.object', {
#             'object': obj
#         })
