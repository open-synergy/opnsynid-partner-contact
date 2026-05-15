import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo11-addons-open-synergy-opnsynid-partner-contact",
    description="Meta package for open-synergy-opnsynid-partner-contact Odoo addons",
    version=version,
    install_requires=[
        'odoo11-addon-partner_company_legal_name',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 11.0',
    ]
)
