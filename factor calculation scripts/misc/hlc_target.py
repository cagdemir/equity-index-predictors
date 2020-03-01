# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 12:45:02 2019

@author: Administrator
"""


import pdblp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date

plt.style.use('seaborn')

#con = pdblp.BCon(debug=True, port=8194, timeout=5000)
con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()
target_tickers = [ 'XUTUM Index', 'MEXBOL Index', 
           'IBOV Index', 'IMOEX Index' , 'JALSH Index']

start = '20040101'
today = date.today().strftime('%Y%m%d')
firstday = '19991230'

ohlc_tickers = ['HIGH','LOW', 'CLOSE']

prices_high = con.bdh(target_tickers, 'PX HIGH',firstday, today) 
prices_high.columns = [i[0] for i in prices_high.columns]
prices_high_int = prices_high.interpolate(method='linear')[target_tickers]
prices_high_w = prices_high_int.groupby(pd.Grouper(freq='W')).max()

prices_low  = con.bdh(target_tickers, 'PX LOW',firstday, today)
prices_low.columns = [i[0] for i in prices_low.columns]
prices_low_int = prices_low.interpolate(method='linear')[target_tickers]
prices_low_w = prices_low_int.groupby(pd.Grouper(freq='W')).min()

prices_close  = con.bdh(target_tickers, 'PX LAST',firstday, today)
prices_close.columns = [i[0] for i in prices_close.columns]
prices_close_int = prices_close.interpolate(method='linear')[target_tickers]
prices_close_w = prices_close_int.groupby(pd.Grouper(freq='W')).last()


returns_high = prices_high_w / prices_close_w.shift(1) - 1
returns_low = prices_low_w / prices_close_w.shift(1) - 1
returns_close = prices_close_w / prices_close_w.shift(1) - 1

returns_fromClose_hlc =  pd.concat([returns_high, returns_low, returns_close],axis=1)
returns_fromClose_hlc.columns =  [('_').join(i) for i in zip(returns_fromClose_hlc.columns,np.repeat(ohlc_tickers,len(target_tickers)))]

returns_fromClose_hlc = returns_fromClose_hlc[returns_fromClose_hlc.index>=start]

target_hlc = returns_fromClose_hlc.copy()

var_no = 'hltarget'


target_hlc.columns = [var_no+'_'+i for i in target_hlc.columns]

target_hlc.to_excel('C:/Users/sb0538/Desktop/15022020/excels/hlctarget.xlsx') 



