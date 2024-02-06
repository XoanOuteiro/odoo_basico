
from odoo import models, fields, api
from odoo.exceptions import  ValidationError

class pedido(models.Model):

    _name = 'odoo_basico.pedido'
    _description = 'exemplo pedido'
    _sql_constraints = [('nomeUnico','unique(name)','O identificador do pedido debe ser único')]
    _order = 'name desc'

    name = fields.Char(required=True, size=20, string="Identificador de pedido:")

    # Os campos One2many Non se almacenan na BD
    lineapedido_ids = fields.One2many("odoo_basico.lineapedido", 'pedido_id')