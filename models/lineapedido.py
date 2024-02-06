
from odoo import models, fields, api
from odoo.exceptions import  ValidationError

class lineapedido(models.Model):

    _name = 'odoo_basico.lineapedido'
    _description = 'exemplo lineapedido'
    _order = "name desc"

    name = fields.Char(required=True, size=20, string="Nome:")
    descripcion = fields.Text(string="Descripcion da linea de pedido")
    # Os campos Many2one crean un campo na BD
    pedido_id = fields.Many2one('odoo_basico.pedido',
                                ondelete="cascade", required=True)