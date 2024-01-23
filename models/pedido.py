
from odoo import models, fields, api
from odoo.exceptions import  ValidationError

class pedido(models.Model):

    _name = 'odoo_basico.pedido'
    _description = 'exemplo pedido'

    name = fields.Char(required=True, size=20, string="Nome:")
    descripcion = fields.Text(string="A descripción:")

    # Os campos One2many Non se almacenan na BD
    lineapedido_ids = fields.One2many("odoo_basico.lineapedido", 'pedido_id')