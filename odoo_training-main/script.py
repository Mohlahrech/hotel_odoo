


import odoorpc

odoo = odoorpc.ODOO('172.0.0.1', port=8069)

print(odoo.db.list())

odoo.login('docker_test', 'admin', 'admin')

order_ids = odoo.env['account.move'].search([('id','=',31)])
print(order_ids)
order_ids = odoo.env['account.move'].browse(order_ids)

print(order_ids)
for so in order_ids:
    so.write({'partner_id':28})
    
    
    
