# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 17:28:47 2019

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

cds_tickers = ['US CDS EUR SR 5Y D14 Corp','GERMAN CDS USD SR 5Y D14 Corp', 'UK CDS USD SR 5Y D14 Corp', 'JGB CDS USD SR 5Y D14 Corp',
               'CHINAGOV CDS USD SR 5Y D14 Corp','TURKEY CDS USD SR 5Y D14 Corp','MEX CDS USD SR 5Y D14 Corp',
               'BRAZIL CDS USD SR 5Y D14 Corp', 'RUSSIA CDS USD SR 5Y D14 Corp','REPSOU CDS USD SR 5Y D14 Corp']

cds = con.bdh(cds_tickers, 'PX LAST', firstday, today)

cds_int = cds.interpolate(method='linear')



cds_int_w = cds_int.groupby(pd.Grouper(freq ='W')).last()

cds_int_w_delta = cds_int_w.pct_change()
cds_int_w_delta =cds_int_w_delta[cds_int_w_delta.index>=start]


cds_int_w.columns = [i[0] for i in cds_int_w.columns]
cds_int_w = cds_int_w[cds_tickers]

cds_int_w =cds_int_w[cds_int_w.index>=start]



cds_int_w.columns = ['9-1_US', '9-1_GER','9-1_UK','9-1_JP','9-1_CH','9-1_TR','9-1_MX','9-1_BR','9-1_RU','9-1_SA']

cds_int_w_delta.columns = ['9-2_US', '9-2_GER','9-2_UK','9-2_JP','9-2_CH','9-2_TR','9-2_MX','9-2_BR','9-2_RU','9-2_SA']


cds_int_w.to_excel ('C:/Users/sb0538/Desktop/15022020/excels/9-1_cds.xlsx') 
cds_int_w_delta.to_excel ('C:/Users/sb0538/Desktop/15022020/excels/9-2_cdsdelta.xlsx') 