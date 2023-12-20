# -*- coding: utf-8 -*-

from odoo import fields,models,api
import logging
_logger = logging.getLogger(__name__)
from odoo.addons.custom_module.models import api_integration

class FirstTest(models.Model):
    _name = 'student.student'  #=> first_test
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Text(string="Student name")
    amount  = fields.Float(string="Fees",track_visibility='always')
    is_student = fields.Boolean()
    department_id = fields.Many2one('students.departmetns',string="Department")
    subject_ids = fields.Many2many('students.subjects','students_subject_rel' ,string="SUbjects")
    student_result_ids = fields.One2many('results.results','student_id',string="Results")
    
    age = fields.Integer(string="Age")
    date_birth = fields.Date(string="Date")
    level = fields.Integer(string="Level")
    dep_address = fields.Char(related="department_id.address",editable=True)
    gender = fields.Selection([('male','Male'),('femail','Femail')])
    company_id = fields.Many2one('res.company')
    state = fields.Selection([('draft','Draft'),('confirmed','Confirmed'),('approved','Approved'),('approve2','Approve2'),('cancel','Cancel')],string="Status",default='draft',track_visibility='always')
    note = fields.Text()

    def send_get_request(self):
        url = 'http://user_api:8000/api/users' 
        api = api_integration.APIIntegration()

        res = api.get_users(url)
        _logger.info(">>>>>>>>>>>>>",api)
        self.note = res


    def send_post_request(self):
        url = 'http://user_api:8000/api/user' 
        api = api_integration.APIIntegration()
        body = {
            'name': 'Test user from odoo',
            'email': 'test1@test.com',
            'password':'123'
        }
        res = api.post_users(url,body)
        
        self.note = res




    @api.onchange('amount')
    def set_values_cont(self):
        name = self._context.get('set_name')


    def set_confirm(self):
        self.state = 'confirmed'
        #self.write({'state':'confirmed'})

    def set_approved(self):
        if self.amount > 1000 :
            self.state = 'approve2'
        else:
            self.write({'state':'approved'})

        pro_id = self.env['product.template'].create({
            'name': 'Prod',
            'list_price': 10
            })
        self.department_id.name = 'new name'

        self.write({'state':'approved'})

    def set_rejected(self):
        self.write({'state':'cancel'})

    def reset_draft(self):
        self.write({'state':'draft'})


    def action_create_product(self):
        
        pro_id = self.env['product.template'].create({
            'name': 'new new new',
            'list_price': 30
            })
        _logger.info(":LLLLLLLLLLLLLLLLLLLL",pro_id)

        return pro_id


  
class Departments(models.Model):
    _name = 'students.departmetns'

    name = fields.Char(string="Name")
    address = fields.Char(string="Address")


class Subjects(models.Model):
    _name = 'students.subjects' 

    name = fields.Char(string="Name")


class Results(models.Model):
    _name = 'results.results' 

    student_id = fields.Many2one('student.student')
    result = fields.Float(string="Result")
    subject_id = fields.Many2one('students.subjects')




