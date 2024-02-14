# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class custom_mifta(models.Model):
#     _name = 'custom_mifta.custom_mifta'
#     _description = 'custom_mifta.custom_mifta'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
