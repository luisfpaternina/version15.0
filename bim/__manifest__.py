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
        'security/security.xml',
        'security/ir.model.access.csv',   
        'views/bim.xml',
        'views/bim_categ.xml',
        'reports/report_license_plates.xml',
              
    ],
    
    "images": [
        #'static/description/school.png'
    ],
    

    "application": False,
    "installable": True,
    "auto_install": False,

}
