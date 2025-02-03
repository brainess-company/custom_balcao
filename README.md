# Permissões Balcão - Módulo Fiscal Brasileiro

Este módulo personalizado foi criado para adicionar o grupo de segurança **"Balcão"** ao Odoo 14, com foco em controle de permissões fiscais. O objetivo principal é ocultar campos fiscais do cadastro de produtos para evitar interferências indesejadas por vendedores do balcão.

## Funcionalidades
- Oculta campos fiscais importantes, como CFOP, CST e NCM, para os usuários do grupo "Balcão".
- Permite que os usuários do grupo editem outros dados do produto, sem visualizar informações fiscais.

## Estrutura do Módulo
```
custom_balcao/
├── __init__.py
├── __manifest__.py
├── security/
│   └── ir.model.access.csv
├── security/
│   └── security.xml
└── views/
    └── product_view.xml
```

## Instalação
1. Copie a pasta `custom_balcao` para o diretório de addons do seu Odoo.
2. Ative o modo de desenvolvedor no Odoo.
3. Instale o módulo "Permissões Balcão".

## Configuração
1. Navegue para **Configurações > Usuários e Empresas > Usuários**.
2. Selecione o usuário desejado.
3. Adicione o grupo **"Balcão"**.

A partir desse momento, os campos fiscais serão automaticamente ocultos para os usuários desse grupo.

## Ideia Futura
Uma próxima evolução deste módulo é ocultar o menu que se abre ao clicar em um item na **Sale Order**. Este é um atributo criado pelo módulo **l10n_br_sale**, que futuramente será configurado para não estar acessível aos usuários do grupo "Balcão".

