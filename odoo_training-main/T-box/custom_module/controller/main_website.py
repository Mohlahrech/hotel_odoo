from odoo import http
from odoo.http import request
from odoo.exceptions import AccessError, MissingError
import base64

class Sale(http.Controller):
	#type ="http" , "json" , auth="public",'users','none'

	@http.route('/my_sale_details',type="http",auth="public",website=True)
	def get_sale_orders(self, **kwargs):
		sale_details = request.env['sale.order'].sudo().search([])

		#return {'my_details':sale_details}

		return request.render('custom_module.sale_details_page',{'my_details':sale_details})


	@http.route('/new_application_request',type="http",auth="public",website=True)
	def redirect_to_request(self):
		return request.render('custom_module.registration_form_page')


	@http.route('/new_request_submit',type="http",auth="public",website=True,csrf=True)
	def request_submit(self, **kwargs):
		student_name = kwargs.get('st_name')
		Attachments = request.env['ir.attachment']
		file = kwargs.get('attachment1')

		stu = request.env['student.student'].sudo().create({
			'name':student_name,
			'amount':900,
			'is_student':True

			})

		attachment = file.read() 
		attachment_id = Attachments.sudo().create({
			'name':stu.name,
			'res_name': stu.name,
			'type': 'binary',   
			'res_model': 'student.student',
			'res_id':stu.id,
			'datas': base64.b64encode(attachment),
		})



		#sale_details = request.env['student.student'].sudo().search([('id','=',stu)])
		#return request.render('custom_module.sale_details_page',{'my_details':sale_details})