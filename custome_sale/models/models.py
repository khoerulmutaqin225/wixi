# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class custome_sale(models.Model):
#     _name = 'custome_sale.custome_sale'
#     _description = 'custome_sale.custome_sale'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

# -*- coding: utf-8 -*-
# import module default odoo
from odoo import api, fields, models, exceptions, _

# buat class baru
# nama class bebas asalkan extends ke class Model
class sale_order(models.Model):
    # _inherit digunakan jika kita akan mengoveride model yang sudah ada
    # model sale.order terdapat di module sale bawaan Odoo
    # jika model tidak tersedia / belum terinstall akan menyebabkan error
    _inherit = 'sale.order'

    # buat kolom database dengan nama makelar, type data varchar dan wajib diisi
    # type data lainnya akan dijelaskan pada tulisan berikutnya
    makelar = fields.Char("Makelar", required=True)