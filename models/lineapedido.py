
from odoo import models, fields, api
from odoo.exceptions import  ValidationError

class lineapedido(models.Model):

    _name = 'odoo_basico.lineapedido'
    _description = 'exemplo lineapedido'

    name = fields.Char(required=True, size=20, string="Nome:")
    # Os campos Many2one crean un campo na BD
    pedido_id = fields.Many2one('odoo_basico.pedido',
                                ondelete="cascade", required=True)