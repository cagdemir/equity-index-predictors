# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 18:24:23 2019

@author: Administrator
"""

import pdblp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
from datetime import date

plt.style.use('seaborn')

#con = pdblp.BCon(debug=True, port=8194, timeout=5000)
con = pdblp.BCon(debug=False, port=8194, timeout=50000)
con.start()
index_tickers = ['NYA Index', 'SPX Index', 'CCMP Index','NDX Index','CDAX Index' ,'DAX Index', 
            'ASX Index','UKX Index', 'TPX Index','NKY Index', 'SHCOMP Index' , 
           'SZCOMP Index','XUTUM Index','XU100 Index',  'MEXBOL Index', 
           'IBOV Index', 'IMOEX Index' , 'JALSH Index']

start = '20040101'
today = date.today().strftime('%Y%m%d')
firstday = '19991230'

ohlc_tickers = ['OPEN','HIGH','LOW', 'LAST']

prices_open = con.bdh(index_tickers, 'PX OPEN',firstday, today)
prices_open.columns = [i[0] for i in prices_open.columns]
prices_open_int = prices_open.interpolate(method='linear')[index_tickers]
prices_open_w = prices_open_int.groupby(pd.Grouper(freq='W')).first()

prices_high = con.bdh(index_tickers, 'PX HIGH',firstday, today) 
prices_high.columns = [i[0] for i in prices_high.columns]
prices_high_int = prices_high.interpolate(method='linear')[index_tickers]
prices_high_w = prices_high_int.groupby(pd.Grouper(freq='W')).max()

prices_low  = con.bdh(index_tickers, 'PX LOW',firstday, today)
prices_low.columns = [i[0] for i in prices_low.columns]
prices_low_int = prices_low.interpolate(method='linear')[index_tickers]
prices_low_w = prices_low_int.groupby(pd.Grouper(freq='W')).min()

prices_close  = con.bdh(index_tickers, 'PX LAST',firstday, today)
prices_close.columns = [i[0] for i in prices_close.columns]
prices_close_int = prices_close.interpolate(method='linear')[index_tickers]
prices_close_w = prices_close_int.groupby(pd.Grouper(freq='W')).last()

returns_open = prices_open_w / prices_close_w.shift(1) - 1
returns_high = prices_high_w / prices_close_w.shift(1) - 1
returns_low = prices_low_w / prices_close_w.shift(1) - 1
returns_close = prices_close_w / prices_close_w.shift(1) - 1

returns_fromClose_ohlc =  pd.concat([returns_open, returns_high, returns_low, returns_close],axis=1)
returns_fromClose_ohlc.columns =  [('-').join(i) for i in zip(returns_fromClose_ohlc.columns,np.repeat(ohlc_tickers,len(index_tickers)))]

returns_fromClose_ohlc = returns_fromClose_ohlc[returns_fromClose_ohlc.index>=start]

target = returns_fromClose_ohlc.shift(-1)

target.to_excel('C:/Users/sb0538/Desktop/15022020/excels/0_ohlc.xlsx') 