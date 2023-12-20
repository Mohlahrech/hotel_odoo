# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2022-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
import logging
from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class StageTicket(models.Model):
    _name = 'formation.stage'
    _description = 'Formation Stage'
    _order = 'sequence, id'
    _fold_name = 'fold'

    name = fields.Char('Name')
    active = fields.Boolean(default=True)
    sequence = fields.Integer(default=50)
    closing_stage = fields.Boolean('Closing Stage', default=False)
    cancel_stage = fields.Boolean('Cancel Stage', default=False)
    starting_stage = fields.Boolean('Start Stage', default=False)
    folded = fields.Boolean('Folded in Kanban', default=False)
    template_id = fields.Many2one('mail.template',
                                  domain="[('model', '=', 'od_ceti2.formations')]")
    group_ids = fields.Many2many('res.groups')
    fold = fields.Boolean(string='Fold')

    def unlink(self):
        for rec in self:
            tickets = rec.search([])
            sequence = tickets.mapped('sequence')
            lowest_sequence = tickets.filtered(
                lambda x: x.sequence == min(sequence))
            if self.name == "Draft":
                raise UserError(_("Cannot Delete This Stage"))
            if rec == lowest_sequence:
                raise UserError(_("Cannot Delete '%s'" % (rec.name)))
            else:
                res = super().unlink()
                return res