# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 14:57:17 2019

@author: Administrator
"""


import pdblp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')

#con = pdblp.BCon(debug=True, port=8194, timeout=5000)
con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()

from datetime import date


start = '20040101'
today = date.today().strftime('%Y%m%d')
firstday='19991230'


flow_em = con.bdh('EEM US EQUITY', 'FUND FLOW', firstday, today)


flow_us = con.bdh('IVV US EQUITY', 'FUND FLOW', firstday, today)

flow_de = con.bdh ('EWG US EQUITY','FUND FLOW', firstday, today)

flow_uk = con.bdh('EWU US EQUITY','FUND FLOW', firstday, today)

flow_jp = con.bdh('EWJ US EQUITY','FUND FLOW', firstday, today)

flow_cn = con.bdh('FXI US EQUITY','FUND FLOW', firstday, today)

flow_tr = con.bdh('TUR US EQUITY', 'FUND FLOW', firstday, today)

flow_mx = con.bdh('EWW US EQUITY', 'FUND FLOW', firstday, today)

flow_br = con.bdh('EWZ US EQUITY', 'FUND FLOW', firstday, today)

flow_ru = con.bdh('ERUS US EQUITY', 'FUND FLOW', firstday, today)

flow_za = con.bdh('EZA US EQUITY', 'FUND FLOW', firstday, today)


flow = pd.concat([flow_em, flow_us, flow_de, flow_uk, flow_jp, flow_cn, flow_tr, flow_mx, flow_br, flow_ru, flow_za], axis =1 )

flow.columns = [i[0] for i in flow.columns ]


flow_w = flow.groupby(pd.Grouper(freq='W')).sum() 

flow_w.columns = ['extra_7_1_em', 'extra_7_1_us','extra_7_1_de','extra_7_1_uk','extra_7_1_jp','extra_7_1_cn','extra_7_1_tr','extra_7_1_mx','extra_7_1_br','extra_7_1_ru','extra_7_1_za']
#flow_w_delta = flow_w.pct_change()

window=13
flow_w_mom = flow_w.rolling(window).sum()

flow_w_mom.columns = ['extra_7_2_em', 'extra_7_2_us','extra_7_2_de','extra_7_2_uk','extra_7_2_jp','extra_7_2_cn','extra_7_2_tr','extra_7_2_mx','extra_7_2_br','extra_7_2_ru','extra_7_2_za']


flow_w_mom_delta = flow_w_mom.pct_change()
flow_w_mom_delta = flow_w_mom_delta.replace([np.inf,-np.inf,np.nan],0)
flow_w_mom_delta.columns = ['extra_7_3_em', 'extra_7_3_us','extra_7_3_de','extra_7_3_uk','extra_7_3_jp','extra_7_3_cn','extra_7_3_tr','extra_7_3_mx','extra_7_3_br','extra_7_3_ru','extra_7_3_za']

flow_w = flow_w[flow_w.index>=start]
flow_w.to_excel('C:/Users/sb0538/Desktop/15022020/excels/extra7-1_flow.xlsx')

flow_w_mom = flow_w_mom[flow_w_mom.index>=start]
flow_w_mom.to_excel('C:/Users/sb0538/Desktop/15022020/excels/extra7-2_flowmom.xlsx')

flow_w_mom_delta = flow_w_mom_delta[flow_w_mom_delta.index>=start]
flow_w_mom_delta.to_excel('C:/Users/sb0538/Desktop/15022020/excels/extra7-3_flowmomdelta.xlsx')





