# -*- coding: utf-8 -*-
# from odoo import http


# class CustomMifta(http.Controller):
#     @http.route('/custom_mifta/custom_mifta', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_mifta/custom_mifta/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_mifta.listing', {
#             'root': '/custom_mifta/custom_mifta',
#             'objects': http.request.env['custom_mifta.custom_mifta'].search([]),
#         })

#     @http.route('/custom_mifta/custom_mifta/objects/<model("custom_mifta.custom_mifta"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_mifta.object', {
#             'object': obj
#         })
