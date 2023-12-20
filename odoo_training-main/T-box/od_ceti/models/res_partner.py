from odoo import models, fields

class Res_Partner(models.Model):
    _inherit = 'res.partner'

    is_formateur = fields.Boolean(string="Formateur", default=False)
    formations_given = fields.One2many("od_ceti2.formations",'formateur', string="Formations données")








