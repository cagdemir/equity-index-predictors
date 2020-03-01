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
today = date.today().strftime('%Y%m%d')
firstday = '19991230'

pe_ratio = con.bdh(index_tickers, ['PE RATIO'], firstday , today)

pe_ratio_int = pe_ratio.interpolate(method='linear')
pe_ratio_int_w = pe_ratio_int.groupby(pd.Grouper(freq='W')).last()

pe_ratio_growth = pe_ratio_int_w.pct_change()

pe_ratio_growth_last = pe_ratio_growth[pe_ratio_growth.index>=start]
 
pe_ratio_growth_last.columns = [i[0] for i in pe_ratio_growth_last]
pe_ratio_growth_last = pe_ratio_growth_last[index_tickers]

var_no='16'
pe_ratio_growth_last.columns = [var_no+'_'+i for i in pe_ratio_growth_last.columns]

#pe_ratio_growth_last.columns = ['16_US_NY','16_US_SPX','16_US_CCMP', '16_DE','16_UK','16_JP','16_CH_SH','16_CH_SZ', '16_TR','16_MX','16_BR','16_RU','16_SA']

pe_ratio_growth_last.to_excel('C:/Users/sb0538/Desktop/15022020/excels/16_peratiogrowth.xlsx') 







