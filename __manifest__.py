{
    'name': 'Permissões Balcão - Módulo Fiscal Brasileiro',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Permissões específicas para ocultar campos fiscais do módulo l10n_br_fiscal.',
    'depends': ['sale', 'l10n_br_fiscal', 'l10n_br_sale', 'account'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/product_view.xml',
    ],
}
