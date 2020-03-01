# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 18:19:29 2019

@author: Administrator
"""

import pdblp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')

#con = pdblp.BCon(debug=True, port=8194, timeout=5000)
con = pdblp.BCon(debug=False, port=8194, timeout=6000)
con.start()
index_tickers = ['NYA Index', 'SPX Index', 'CCMP Index','NDX Index','CDAX Index' ,'DAX Index', 
            'ASX Index','UKX Index', 'TPX Index','NKY Index', 'SHCOMP Index' , 
           'SZCOMP Index','XUTUM Index','XU100 Index',  'MEXBOL Index', 
           'IBOV Index', 'IMOEX Index' , 'JALSH Index']
from datetime import date


start = '20040101'
today = date.today().strftime('%Y%m%d')
firstday = '19991230'


prices_open = con.bdh(index_tickers, 'PX OPEN',firstday, today)
prices_open.columns = [i[0] for i in prices_open.columns]
prices_open = prices_open[index_tickers]
prices_open_int = prices_open.interpolate(method='linear')
prices_open_w = prices_open_int.groupby(pd.Grouper(freq='W')).first()

prices_high = con.bdh(index_tickers, 'PX HIGH',firstday, today)
prices_high.columns = [i[0] for i in prices_high.columns]
prices_high = prices_high[index_tickers]
prices_high_int = prices_high.interpolate(method='linear')
prices_high_w = prices_high_int.groupby(pd.Grouper(freq='W')).max()

prices_low  = con.bdh(index_tickers, 'PX LOW',firstday, today)
prices_low.columns = [i[0] for i in prices_low.columns]
prices_low = prices_low[index_tickers]
prices_low_int = prices_low.interpolate(method='linear')
prices_low_w = prices_low_int.groupby(pd.Grouper(freq='W')).min()

prices_close  = con.bdh(index_tickers, 'PX LAST',firstday, today)
prices_close.columns = [i[0] for i in prices_close.columns]
prices_close = prices_close[index_tickers]
prices_close_int = prices_close.interpolate(method='linear')
prices_close_w = prices_close_int.groupby(pd.Grouper(freq='W')).last()


var_no1 = '21-1'


returns_open = prices_open_w / prices_close_w.shift(1) - 1
returns_open.columns = [var_no1+'_'+i+'_OPEN' for i in returns_open.columns]

returns_high = prices_high_w / prices_close_w.shift(1) - 1
returns_high.columns = [var_no1+'_'+i+'_HIGH' for i in returns_high.columns]

returns_low = prices_low_w / prices_close_w.shift(1) - 1
returns_low.columns = [var_no1+'_'+i+'_LOW' for i in returns_low.columns]

returns_close = prices_close_w / prices_close_w.shift(1) - 1
returns_close.columns = [var_no1+'_'+i+'_LAST' for i in returns_close.columns]


returns_fromClose_ohlc =  pd.concat([returns_open, returns_high, returns_low, returns_close],axis=1)


#returns_fromClose_ohlc.columns =  [('_').join(i) for i in zip(np.repeat(ohlc_tickers1,len(index_tickers)),returns_fromClose_ohlc.columns)]

#returns_fromClose_ohlc = returns_fromClose_ohlc[ohlc_tickers]
#returns_fromClose_ohlc.columns = ['21_return_ohlc_US_NY','21_return_ohlc_US_SPX','21_return_ohlc_US_CCMP', '21_return_ohlc_DE','21_return_ohlc_UK','21_return_ohlc_JP','21_return_ohlc_CH_SH','21_return_ohlc_CH_SZ', '21_return_ohlc_TR','21_return_ohlc_MX','21_return_ohlc_BR','21_return_ohlc_RU','21_return_ohlc_SA']

returns_fromClose_ohlc = returns_fromClose_ohlc[returns_fromClose_ohlc.index>=start]


returns_fromClose_ohlc.to_excel('C:/Users/sb0538/Desktop/15022020/excels/21-1_laggedexcessmarketreturnfromclose.xlsx') 
##############################################################################


var_no2 = '21-2'

prices_open_w.columns = [var_no2+'_'+i+'_OPEN' for i in prices_open_w.columns]
prices_high_w.columns = [var_no2+'_'+i+'_HIGH' for i in prices_high_w.columns]
prices_low_w.columns = [var_no2+'_'+i+'_LOW' for i in prices_low_w.columns]
prices_close_w.columns = [var_no2+'_'+i+'_LAST' for i in prices_close_w.columns]


prices_ohlc = pd.concat([prices_open_w, prices_high_w, prices_low_w, prices_close_w],axis=1)

#prices_ohlc.columns =  [('_').join(i) for i in zip(np.repeat(ohlc_tickers2,len(index_tickers)),prices_ohlc.columns)]
#prices_ohlc = prices_ohlc[index_tickers]
#prices_ohlc.columns = ['21_px_ohlc_US_NY','21_px_ohlc_US_SPX','21_px_ohlc_US_CCMP', '21_px_ohlc_DE','21_px_ohlc_UK','21_px_ohlc_JP','21_px_ohlc_CH_SH','21_px_ohlc_CH_SZ', '21_px_ohlc_TR','21_px_ohlc_MX','21_px_ohlc_BR','21_px_ohlc_RU','21_px_ohlc_SA']


delta_ohlc = prices_ohlc.pct_change()

delta_ohlc = delta_ohlc[delta_ohlc.index>=start]

delta_ohlc.to_excel('C:/Users/sb0538/Desktop/15022020/excels/21-2_laggedexcessmarketreturndeltaohlc.xlsx') 


