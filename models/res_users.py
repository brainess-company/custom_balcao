from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    has_balcao_permission = fields.Boolean(
        string='Permissão Balcão',
        compute='_compute_has_balcao_permission',
        store=False  # Não precisa armazenar, pois é calculado dinamicamente
    )

    def _compute_has_balcao_permission(self):
        for user in self:
            user.has_balcao_permission = self.env.ref('custom_balcao.group_balcao') in user.groups_id
