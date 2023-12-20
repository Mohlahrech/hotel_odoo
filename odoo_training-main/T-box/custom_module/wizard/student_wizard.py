# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError
import io
from odoo.tools.misc import xlwt

try:
    import xlsxwriter
except ImportError:
    _logger.debug("Can not import xlsxwriter`.")
from xlsxwriter.utility import xl_rowcol_to_cell

class StudentRegistration(models.TransientModel):
    _name = 'student.registration.wizard'

    department_id = fields.Many2one('students.departmetns', string="Department")

    def print_report(self):
        data = {'department_id': self.department_id.id }

        return self.env.ref('custom_module.action_student_wizard').report_action([], data=data)

    def print_xls_report(self):
        return self.env.ref('custom_module.action_student_xls_report').report_action(self)

class DoctorReferralXlsx(models.AbstractModel):
    _name = 'report.custom_module.student_xls_report'
    _inherit = 'report.report_xlsx.abstract'

    def create_xlsx_report(self, docids, data):
        
        file_data = io.BytesIO()

        workbook = xlsxwriter.Workbook(file_data, self.get_workbook_options())
       

        self.generate_xlsx_report(workbook, data)

        workbook.close()
        file_data.seek(0)
        return file_data.read(), "xlsx"


    def generate_xlsx_report(self, workbook, data):

        sheet = workbook.add_worksheet('My XLS Report')

        heading_table_format = workbook.add_format({
            'align': 'left',
            'bold': True,
            'border': True,
            'size': 12
        })

        sheet.merge_range(0, 1, 0, 2, 'Column merged')

        sheet.set_column('A:A', 20)

        student_ids = self.env['student.student'].search([])

        row = column = 1
        sheet.write(row, column, "Report : ", heading_table_format)
        
        for st in student_ids:
            row += 1
            sheet.write(row, column, st.name, heading_table_format)

        





       
        








