
from odoo import models, fields, api
from odoo.exceptions import  ValidationError

class pedido(models.Model):

    _name = 'odoo_basico.pedido'
    _description = 'exemplo pedido'
    _sql_constraints = [('nomeUnico','unique(name)','O identificador do pedido debe ser único')]
    _order = 'name desc'

    name = fields.Char(required=True, size=20, string="Identificador de pedido:")
    persoa_id = fields.Many2one('res.partner', ondelete='set null', domain="[('visible','=','True')]", index=True,
                                string="Persoa")

    # Os campos One2many Non se almacenan na BD
    lineapedido_ids = fields.One2many("odoo_basico.lineapedido", 'pedido_id')

    def actualizadorSexo(self):
        informacion_ids = self.env['odoo_basico.informacion'].search([('autorizado', '=', False)])
        for rexistro in informacion_ids:
            self.env['odoo_basico.informacion']._cambia_campo_sexo(rexistro)

    def creaRexistroInformacion(self):
        creado_id = self.env['odoo_basico.informacion'].create({'name': 'Creado dende pedido'})
        creado_id.descripcion =  "Creado dende o modelo pedido"
        creado_id.autorizado = False

    def actualizadorHoraTimezone(self):
        informacion_ids = self.env['odoo_basico.informacion'].search([])
        for rexistro in informacion_ids:
            self.env['odoo_basico.informacion'].actualiza_hora_timezone_usuario(rexistro)