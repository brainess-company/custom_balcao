from odoo import models, fields, api

class ResUsers(models.Model):
    _inherit = 'res.users'

    has_balcao_permission = fields.Boolean(
        compute='_compute_has_balcao_permission',
        string="Permissão Balcão"
    )

    @api.depends('groups_id')
    def _compute_has_balcao_permission(self):
        balcão_group = self.env.ref('custom_balcao.group_balcao', raise_if_not_found=False)
        for user in self:
            user.has_balcao_permission = balcão_group in user.groups_id if balcão_group else False
