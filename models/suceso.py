from odoo import fields, models, api




class suceso(models.Model):
    _name = 'odoo_basico.suceso'
    _descripcion = 'Modulo suceso'

    name = fields.Char(required=True, size=20, string="Suceso")
    descripcion = fields.Text(string="A Descripción do Suceso")  # string é a etiqueta do campo
    nivel = fields.Selection([('Baixo', 'Baixo'), ('Medio', 'Medio'), ('Alto', 'Alto')], string='Nivel')
