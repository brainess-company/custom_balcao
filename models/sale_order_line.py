from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    has_balcao_permission = fields.Boolean(
        string="Permissão Balcão",
        compute="_compute_has_balcao_permission",
        store=True
    )

    @api.depends('user_id.has_balcao_permission')
    def _compute_has_balcao_permission(self):
        for order in self:
            # Recupera a permissão do usuário atual vinculado ao pedido
            order.has_balcao_permission = order.user_id.has_balcao_permission if order.user_id else False
