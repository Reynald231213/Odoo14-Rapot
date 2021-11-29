# -*- coding: utf-8 -*-
# from odoo import http


# class Rapot(http.Controller):
#     @http.route('/rapot/rapot/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rapot/rapot/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rapot.listing', {
#             'root': '/rapot/rapot',
#             'objects': http.request.env['rapot.rapot'].search([]),
#         })

#     @http.route('/rapot/rapot/objects/<model("rapot.rapot"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rapot.object', {
#             'object': obj
#         })
