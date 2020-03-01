# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 18:00:53 2019

@author: Administrator
"""

import pdblp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()

index_tickers = ['NYA Index', 'SPX Index', 'CCMP Index','NDX Index','CDAX Index' ,'DAX Index', 
            'ASX Index','UKX Index', 'TPX Index','NKY Index', 'SHCOMP Index' , 
           'SZCOMP Index','XUTUM Index','XU100 Index',  'MEXBOL Index', 
           'IBOV Index', 'IMOEX Index' , 'JALSH Index']
from datetime import date

start = '20040101'
firstday = '19990101'
today = date.today().strftime('%Y%m%d')



pe_ratio = con.bdh(index_tickers, 'PE RATIO', firstday, today)

pe_ratio_int = pe_ratio.interpolate(method='linear')
pe_ratio_int_w = pe_ratio_int.groupby(pd.Grouper(freq='W')).last()

#pe_ratio_last = pe_ratio_int_w[pe_ratio_int_w.index>=start] 
#
#pe_ratio_last.columns = [i[0] for i in pe_ratio_last.columns]
#pe_ratio_last= pe_ratio_last[index_tickers]

pe_ratio_smoothed = pe_ratio_int_w.rolling(500, min_periods=100).mean()

var_no='15'
pe_ratio_smoothed_last = pe_ratio_smoothed[pe_ratio_smoothed.index>=start]
pe_ratio_smoothed_last.columns = [i[0] for i in pe_ratio_smoothed_last.columns]
pe_ratio_smoothed_last = pe_ratio_smoothed_last[index_tickers]
pe_ratio_smoothed_last.columns = [var_no+'_'+i for i in pe_ratio_smoothed_last.columns]

# pe_ratio_smoothed_last = pe_ratio_smoothed_last[index_tickers]
#pe_ratio_smoothed_last.columns = ['15_US_NY','15_US_SPX','15_US_CCMP', '15_DE','15_UK','15_JP','15_CH_SH','15_CH_SZ', '15_TR','15_MX','15_BR','15_RU','15_SA']

pe_ratio_smoothed_last.to_excel('C:/Users/sb0538/Desktop/15022020/excels/15_peratiosmoothed.xlsx') 




