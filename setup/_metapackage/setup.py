import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-open-synergy-opnsynid-partner-contact",
    description="Meta package for open-synergy-opnsynid-partner-contact Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-partner_contact_emergency_contact',
        'odoo12-addon-partner_contact_language',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 12.0',
    ]
)
