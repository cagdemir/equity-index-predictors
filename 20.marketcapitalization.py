# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 16:52:39 2019

@author: Administrator
"""

import pdblp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date


start = '20040101'
today = date.today().strftime('%Y%m%d')
firstday = '19991230'

#con = pdblp.BCon(debug=True, port=8194, timeout=5000)
con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()


index_tickers = ['NYA Index', 'SPX Index', 'CCMP Index','NDX Index','CDAX Index' ,'DAX Index', 
            'ASX Index','UKX Index', 'TPX Index','NKY Index', 'SHCOMP Index' , 
           'SZCOMP Index','XUTUM Index','XU100 Index',  'MEXBOL Index', 
           'IBOV Index', 'IMOEX Index' , 'JALSH Index']

mcap =con.bdh(index_tickers,['CUR MKT CAP'],firstday, today)

#mcap = mcap[mcap.index>=start]

#mcap_int = mcap.interpolate(method='linear')
mcap_w = mcap.groupby(pd.Grouper(freq='B')).last().groupby(pd.Grouper(freq='W')).last()
#mcap_w.fillna(method='bfill', inplace=True)

mcap_w_last = mcap_w[mcap_w.index>=start]

mcap_w_last.columns = [i[0] for i in mcap_w_last]
mcap_w_last = mcap_w_last[index_tickers]
var_no='20'
mcap_w_last.columns = [var_no+'_'+i for i in mcap_w_last.columns]


#☻mcap_w_last.columns = ['20_US_NY','20_US_SPX','20_US_CCMP', '20_DE','20_UK','20_JP','20_CH_SH','20_CH_SZ', '20_TR','20_MX','20_BR','20_RU','20_SA']

mcap_w_last.to_excel('C:/Users/sb0538/Desktop/15022020/excels/20_mcap.xlsx') 