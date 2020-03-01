# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:05:23 2019

@author: Administrator
"""

import pdblp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()

#indices = ['NYA Index', 'SPX Index', 'CCMP Index' ,'CDAX Index' ,'ASX Index', 'TPX Index', 'SHCOMP Index' , 'SZCOMP Index', 'XUTUM Index', 'MEXBOL Index',  'IBOV Index', 'IMOEX Index' , 'JALSH Index']

#price_earnings_ratio = con.bdh(indices, ['PE RATIO'],'19991231', '20191210')
from datetime import date


start = '20040101'
today = date.today().strftime('%Y%m%d')
firstday = '19991230'


pe_ratio_tickers =['NYA Index', 'SPX Index', 'CCMP Index','NDX Index','CDAX Index' ,'DAX Index', 
            'ASX Index','UKX Index', 'TPX Index','NKY Index', 'SHCOMP Index' , 
           'SZCOMP Index','XUTUM Index','XU100 Index',  'MEXBOL Index', 
           'IBOV Index', 'IMOEX Index' , 'JALSH Index']

pe_ratio = con.bdh(pe_ratio_tickers, 'PE RATIO', firstday ,today)

pe_ratio_int = pe_ratio.interpolate(method='linear')
pe_ratio_int_w = pe_ratio_int.groupby(pd.Grouper(freq='W')).last()

pe_ratio_last = pe_ratio_int_w[pe_ratio_int_w.index>=start] 

pe_ratio_log = np.log(pe_ratio_last+1)

var_no='14'
pe_ratio_log.columns = [i[0] for i in pe_ratio_log.columns]
pe_ratio_log = pe_ratio_log[pe_ratio_tickers]
pe_ratio_log.columns = [var_no+'_'+i for i in pe_ratio_log.columns]


#pe_ratio_log.columns =['14_US_NY','14_US_SPX','14_US_CCMP', '14_DE','14_UK','14_JP','14_CH_SH','14_CH_SZ', '14_TR','14_MX','14_BR','14_RU','14_SA']

pe_ratio_log.to_excel('C:/Users/sb0538/Desktop/15022020/excels/14_peratiolog.xlsx') 

