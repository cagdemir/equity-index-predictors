# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:31:15 2019

@author: Administrator
"""

import pdblp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()

from datetime import date


start = '20040101'
today = date.today().strftime('%Y%m%d')
firstday = '19991230'

#for Germany we used Eurozone money supply ECMSM1, 

m1_tickers = ['M1 Index' ,'ECMSM1 Index' , 
            'A23 VWYT  Index', 'JMNSM1SA Index', 'CNMSM1 Index' , 
           'TUNMM1 Index', 'MXMSM1 Index', 'BZMS1 Index', 
           'RMSNM1 Index','SAMYM1 Index']

ms = con.bdh(m1_tickers, ['PX LAST' ], firstday, today)



idx_sent = pd.date_range(start=firstday, end=today, freq='D')

ms_sent = pd.DataFrame(columns=ms.columns,index=idx_sent)
ms_sent.update(ms)

ms_ff = ms_sent.astype(float).ffill()

delta_ms = ms_ff.pct_change()[ms_sent.notnull()]

delta_ms_w = delta_ms.groupby(pd.Grouper(freq='W')).last()

delta_ms_w_last = delta_ms_w.ffill()


delta_ms_w_last.columns = [i[0] for i in delta_ms_w_last.columns]

delta_ms_w_last =delta_ms_w_last[m1_tickers]


delta_ms_w_last = delta_ms_w_last[delta_ms_w_last.index>=start]

delta_ms_w_last.columns = ['30_US', '30_GER','30_UK','30_JP','30_CH', '30_TR','30_MX','30_BR','30_RU','30_SA']

delta_ms_w_last.to_excel('C:/Users/sb0538/Desktop/15022020/excels/30_moneysupplygrowth.xlsx') 





