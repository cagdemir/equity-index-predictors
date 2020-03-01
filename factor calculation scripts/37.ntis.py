# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 18:12:59 2019

@author: Administrator
"""


import pdblp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import date

plt.style.use('seaborn')

#con = pdblp.BCon(debug=True, port=8194, timeout=5000)
con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()



index_tickers = ['NYA Index', 'SPX Index', 'CCMP Index','NDX Index','CDAX Index' ,'DAX Index', 
            'ASX Index','UKX Index', 'TPX Index','NKY Index', 'SHCOMP Index' , 
           'SZCOMP Index','XUTUM Index','XU100 Index',  'MEXBOL Index', 
           'IBOV Index', 'IMOEX Index' , 'JALSH Index']


start = '20040101'
today = date.today().strftime('%Y%m%d')
firstday = '19991230'

window_short = 13 
window_medium = 26
window_long = 52



prices_close  = con.bdh(index_tickers, 'PX LAST',firstday, today)
prices_close.columns = [i[0] for i in prices_close.columns]
prices_close = prices_close[index_tickers]
prices_close_int = prices_close.interpolate(method='linear')
prices_close_w = prices_close_int.groupby(pd.Grouper(freq='W')).last()

returns_close_short = prices_close_w.pct_change(window_short)
returns_close_medium = prices_close_w.pct_change(window_medium)
returns_close_long = prices_close_w.pct_change(window_long)

#####################

mcap =con.bdh(index_tickers,['CUR MKT CAP'],firstday, today)

#mcap = mcap[mcap.index>=start]

#mcap_int = mcap.interpolate(method='linear')
mcap_w = mcap.groupby(pd.Grouper(freq='B')).last().groupby(pd.Grouper(freq='W')).last()

mcap_w.columns = [i[0] for i in mcap_w.columns]
mcap_w = mcap_w[index_tickers]

mcap_w_delta_short = mcap_w.pct_change(window_short)
mcap_w_delta_medium = mcap_w.pct_change(window_medium)
mcap_w_delta_long = mcap_w.pct_change(window_long)


ntis_short = mcap_w_delta_short - returns_close_short
ntis_medium = mcap_w_delta_medium - returns_close_medium
ntis_long = mcap_w_delta_long - returns_close_long

var_no = '37'

ntis_short.columns = [var_no+'-1_'+i for i in ntis_short.columns]
ntis_medium.columns = [var_no+'-2_'+i for i in ntis_medium.columns]
ntis_long.columns = [var_no+'-3_'+i for i in ntis_long.columns]


ntis_short = ntis_short[ntis_short.index>=start]
ntis_medium = ntis_medium[ntis_medium.index>=start]
ntis_long = ntis_long[ntis_long.index>=start]


ntis_short = ntis_short.replace(np.nan,0.001)
ntis_medium = ntis_medium.replace(np.nan,0.001)
ntis_long = ntis_long.replace(np.nan,0.001)



ntis_short.to_excel('C:/Users/sb0538/Desktop/15022020/excels/37-1_ntisshort.xlsx')
ntis_medium.to_excel('C:/Users/sb0538/Desktop/15022020/excels/37-2_ntismedium.xlsx')
ntis_long.to_excel('C:/Users/sb0538/Desktop/15022020/excels/37-3_ntislong.xlsx')
                

