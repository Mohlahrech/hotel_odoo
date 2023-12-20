from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.tools.translate import _
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError


class Ceti(models.Model):
    _name = 'od_ceti2.formations'

    name = fields.Char('Reference',readonly=True, default=lambda self: self.env['ir.sequence'].
                       next_by_code('od_ceti2.formations') or _('New'))
    ref = fields.Char(string="Titre de la formation", required= True)
    client_name = fields.Many2one('res.partner', string='Client')
    start_date = fields.Date(string='Date de debut', default=fields.Date.context_today)

    end_date = fields.Date(string='Date de fin', compute='_compute_end_date', store=True)
    duration = fields.Integer(string='Durée de la formation (jours)')

    formateur = fields.Many2one('res.partner', string='Formateur',ondelete='set null')
    number_of_seats = fields.Integer(string='Nombre de participants Prévu',min=1)
    participants = fields.Many2many('res.partner', 'formation_res_partner','formation_id','participant_id', string='Participants')
    bc = fields.Many2many('purchase.order', 'formation_purchase_order', 'poformation_id', 'pot_id',
                                    string='Achats')
    places_vides = fields.Integer(string='Places disponibles',compute='_compute_places_vides')
    active = fields.Boolean(default='True')
    _sql_constraints = [('name_unique', 'UNIQUE(name)', 'La ref de la formation doit etre unique')]
    days_difference = fields.Integer(compute='compute_days_difference', string='Days Difference' )
    nombre_participants= fields.Integer(string="nombre de participants",compute='_get_participants_count', store=True)
    color = fields.Integer(string="Color")
    stage_id = fields.Many2one('formation.stage', string='Stage',
                               default=lambda self: self.env[
                                   'formation.stage'].search(
                                   [('name', '=', 'Nouveau')], limit=1).id,
                               tracking=True,
                               group_expand='_read_group_stage_ids')

    kanban_state = fields.Selection([
        ('normal', 'Ready'),
        ('done', 'In Progress'),
        ('blocked', 'Blocked'), ], default='normal')


    tags = fields.Many2many('formation.tag')
    place = fields.Char('Lieu de la formation')

    @api.model_create_multi
    def create(self, vals_list):
        return super(Ceti, self).create(vals_list)

    def write(self, vals):
        result = super(Ceti, self).write(vals)
        return result


    @api.depends('participants')
    def _get_participants_count(self):
        for r in self:
            r.nombre_participants = len(r.participants)

    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
        for record in self:
            if record.start_date and record.duration > 0:
                duration = timedelta(days=record.duration)
                record.end_date = record.start_date + duration
            else:
                record.end_date = False


    def compute_days_difference(self):
        for record in self:
            if record.start_date:
                today_date = datetime.now().date()
                days_difference = (today_date - record.start_date).days
                record.days_difference = days_difference
            else:
                record.days_difference = 0

    @api.depends('participants','number_of_seats')
    def _compute_places_vides(self):
         for formation in self:
             formation.places_vides = formation.number_of_seats-len(formation.participants)

    @api.constrains('formateur','participants','number_of_seats')
    def check_formateur_participant(self):
        for record in self:
            if record.formateur.id in record.participants.ids:
                raise ValidationError(_("Le formateur ne peux pas etre le participant"))
            if self.number_of_seats < len(self.participants):
                raise ValidationError(_("Le nombre de participants ne peux pas dépasser la capacité de la formation"))
            if self.number_of_seats < 1:
                raise ValidationError(_("Le nombre de participants toléré ne peux pas etre inferieur a 1"))

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        """
        return the stages to stage_ids
        """
        stage_ids = self.env['formation.stage'].search([])
        return stage_ids


    def default_stage_id(self):
        # Search your stage
        return self.env['formation.stage'].search(
            [('name', '=', 'Nouveau')], limit=1).id

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        """
        return the stages to stage_ids
        """
        stage_ids = self.env['formation.stage'].search([])
        return stage_ids



class HelpdeskTags(models.Model):
    _name = 'formation.tag'
    _description = 'formation Tags'

    name = fields.Char(string='Tag')
