from odoo import models, fields

class CustomNama(models.Model):
    _name = 'custom.nama'
    _description = 'Custom Module'

    request_vendor = fields.Many2one('res.partner', string='Request Vendor')
    no_kontrak = fields.Char(string='No Kontrak')
    with_po = fields.Boolean(string='With PO')

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    custom_nama_ids = fields.One2many('custom.nama', 'purchase_order_id', string='Custom Nama')
