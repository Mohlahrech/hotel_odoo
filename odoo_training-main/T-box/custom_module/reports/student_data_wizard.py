# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class StudentData(models.AbstractModel):
    _name = 'report.custom_module.report_wizard_form'

    @api.model
    def _get_report_values(self, docids, data=None):        
        department_id = data.get('department_id',[])

        docs = self.env['student.student'].browse([('department_id','=',department_id)])
        #self.env['student.student'].create(
        #self.env['student.student'].search([])
        #self.env['student.student'].unlink(id)
        #self.env['student.student'].write({'name':'new'})

        return {
            'doc_ids' : docids,
            'doc_model': self._name,
            'result': docs,
            'department_id':department_id
           
        }