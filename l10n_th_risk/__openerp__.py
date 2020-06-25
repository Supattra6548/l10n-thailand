# -*- coding: utf-8 -*-
{
    # ----------------------- Edit --------------
    'name': "NSTDA-APP :: Risk",		            # ชื่อระบบ Eng
    'summary': "ระบบบริหารจัดการความเสี่ยง",             # ชื่อระบบ Thai
    'website': 'https://o.nstda.or.th/app/rsk',     # เปลี่ยน ตัวย่อ new
    'depends': [
        'base',
        # 'nstdaauth_cas',
        # 'nstdaperm',
        # 'nstdamas',
        'mail',
        # 'nstdaweb_widgethtml',
    ],
    'data': [
        'security/module_data.xml',
        'security/risk_security.xml',
        'security/ir.model.access.csv',
        'views/risk_views.xml',
        'views/risk_assist_owner_views.xml',
        'views/risk_causes_views.xml',
        'views/risk_impacts_views.xml',
        'views/risk_preventative_views.xml',
        'views/risk_control_owner_views.xml',
        'views/risk_std_views.xml',
        'views/risk_menu_item_views.xml',
    ],
    # ----------------------- NOT Edit --------------
    'category': 'NSTDA',
    'author': 'ICT Team',
    'installable': True,
    'auto_install': False,
}
