##########################################################################################
#
# Ing.Luis Felipe Paternina
# Odoo Dev
#
# lfpaternina93@gmail.com
#
# +573215062353
#
# Bogota,Colombia
#
############################################################################################

{
    'name': 'BIM project',

    "summary": """Information modeling for building.""",

    'version': '15.0.0.0',

    'author': "Luis Felipe Paternina",

    'website': "https://github.com/luisfpaternina",

    'category': 'BIM',

    'depends': [

        'base',
        'stock',
        'sale_management',
        'account_accountant',
        'project',
        'sale_subscription',
        'purchase',
        'hr',
        'contacts',
        'crm',

    ],

    'data': [

        'data/sequences.xml',
        'data/bim.categ.csv',
        'data/bim.udn.csv',
        'data/bim.departaments.csv',
        'data/bim.partner.type.csv',
        'security/security.xml',
        'security/ir.model.access.csv',   
        'views/bim.xml',
        'views/bim_categ.xml',
        'views/bim_udn.xml',
        'views/purchase_order.xml',
        'views/bim_departaments.xml',
        'views/bim_partner_type.xml',
        'views/bim_documentation.xml',
        'reports/report_license_plates.xml',
              
    ],
    
    "images": [
        #'static/description/school.png'
    ],
    

    "application": False,
    "installable": True,
    "auto_install": False,

}
