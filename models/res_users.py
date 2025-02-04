from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    has_balcao_permission = fields.Boolean(compute='_compute_has_balcao_permission')

    @api.depends_context('uid')
    def _compute_has_balcao_permission(self):
        for order in self:
            user = self.env.user
            # Defina a lógica correta para verificar a permissão
            order.has_balcao_permission = user.has_group('custom_balcao.group_balcao_user')
