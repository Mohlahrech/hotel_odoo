# -*- coding: utf-8 -*-

from odoo import models


class PosOrder(models.Model):
    _inherit = "pos.order"

    def get_alert_call(self):
        return 'success ......'
