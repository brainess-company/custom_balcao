from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    has_balcao_permission = fields.Boolean(
        string="Permissão Balcão",
        compute="_compute_has_balcao_permission",
        store=True
    )

    @api.depends('order_id.user_id.has_balcao_permission')
    def _compute_has_balcao_permission(self):
        for order_line in self:
            # Acessa o campo 'user_id' a partir de 'order_id' e calcula 'has_balcao_permission'
            order_line.has_balcao_permission = order_line.order_id.user_id.has_balcao_permission if order_line.order_id.user_id else False
