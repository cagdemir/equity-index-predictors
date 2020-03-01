# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:03:06 2019

@author: Administrator
"""

import pdblp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns

plt.style.use('seaborn')

#con = pdblp.BCon(debug=True, port=8194, timeout=5000)
con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()
index_tickers = ['NYA Index', 'SPX Index', 'CCMP Index' ,'CDAX Index' , 
            'ASX Index', 'TPX Index', 'SHCOMP Index' , 
           'SZCOMP Index', 'XUTUM Index', 'MEXBOL Index', 
           'IBOV Index', 'IMOEX Index' , 'JALSH Index']

from datetime import date


start = '2004-1-1'
today = date.today().strftime('%Y%m%d')
firstday = '19991230'

window_long = 52
window_short = 13


ohlc_tickers = ['OPEN','HIGH','LOW', 'LAST']

prices_open = con.bdh(index_tickers, 'PX OPEN',firstday , today)
prices_open.columns = [i[0] for i in prices_open.columns]
prices_open_int = prices_open.interpolate(method='linear')[index_tickers]
prices_open_w = prices_open_int.groupby(pd.Grouper(freq='W')).first()

prices_high = con.bdh(index_tickers, 'PX HIGH',firstday , today) 
prices_high.columns = [i[0] for i in prices_high.columns]
prices_high_int = prices_high.interpolate(method='linear')[index_tickers]
prices_high_w = prices_high_int.groupby(pd.Grouper(freq='W')).max()

prices_low  = con.bdh(index_tickers, 'PX LOW',firstday , today)
prices_low.columns = [i[0] for i in prices_low.columns]
prices_low_int = prices_low.interpolate(method='linear')[index_tickers]
prices_low_w = prices_low_int.groupby(pd.Grouper(freq='W')).min()

prices_close  = con.bdh(index_tickers, 'PX LAST',firstday , today)
prices_close.columns = [i[0] for i in prices_close.columns]
prices_close_int = prices_close.interpolate(method='linear')[index_tickers]
prices_close_w = prices_close_int.groupby(pd.Grouper(freq='W')).last()

returns_open = prices_open_w / prices_close_w.shift(1) - 1
returns_high = prices_high_w / prices_close_w.shift(1) - 1
returns_low = prices_low_w / prices_close_w.shift(1) - 1
returns_close = prices_close_w / prices_close_w.shift(1) - 1

returns_fromClose_ohlc =  pd.concat([returns_open, returns_high, returns_low, returns_close],axis=1)
returns_fromClose_ohlc.columns =  [('_').join(i) for i in zip(returns_fromClose_ohlc.columns,np.repeat(ohlc_tickers,len(index_tickers)))]


std_fromClose_ohlc_long = returns_fromClose_ohlc.rolling(window_long).std()[returns_fromClose_ohlc.index>=start]
std_fromClose_ohlc_long.columns = ['23-2_'+i for i in std_fromClose_ohlc_long.columns]
#std_fromClose_ohlc_long.columns = ['23_1_US_NY','23_1_US_SPX','23_1_US_CCMP','23_1_DE','23_1_UK','23_1_JP','23_1_CH_SH','23_1_SZ','23_1_TR',
#                                   '23_1_MX','23_1_BR','23_1_RU','23_1_ZA']


mean_fromClose_ohlc_long = returns_fromClose_ohlc.rolling(window_long).mean()[returns_fromClose_ohlc.index>=start]
mean_fromClose_ohlc_long.columns = ['23-1_'+i for i in mean_fromClose_ohlc_long.columns]


std_fromClose_ohlc_short= returns_fromClose_ohlc.rolling(window_short).std()[returns_fromClose_ohlc.index>=start]
std_fromClose_ohlc_short.columns = ['23-4_'+i for i in std_fromClose_ohlc_short.columns]

mean_fromClose_ohlc_short= returns_fromClose_ohlc.rolling(window_short).mean()[returns_fromClose_ohlc.index>=start]
mean_fromClose_ohlc_short.columns = ['23-3_'+i for i in mean_fromClose_ohlc_short.columns]

#std_fromClose_ohlc_short.columns = ['23_2_US_NY','23_2_US_SPX','23_2_US_CCMP','23_2_DE','23_2_UK','23_2_JP','23_2_CH_SH','23_2_SZ','23_2_TR',
#                                   '23_2_MX','23_2_BR','23_2_RU','23_2_ZA']
##############################################################################

prices_ohlc = pd.concat([prices_open_w, prices_high_w, prices_low_w, prices_close_w],axis=1)
prices_ohlc.columns =  [('_').join(i) for i in zip(prices_ohlc.columns,np.repeat(ohlc_tickers,len(index_tickers)))]


std_delta_ohlc_long = prices_ohlc.pct_change().rolling(window_long).std()
mean_delta_ohlc_long = prices_ohlc.pct_change().rolling(window_long).mean()

std_ohlc_long = std_delta_ohlc_long[std_delta_ohlc_long.index>=start]
std_ohlc_long.columns = ['23-6_'+i for i in std_ohlc_long.columns]

mean_ohlc_long = mean_delta_ohlc_long[mean_delta_ohlc_long.index>=start]
mean_ohlc_long.columns = ['23-5_'+i for i in mean_ohlc_long.columns]

#std_ohlc_long.columns = ['23_3_US_NY','23_3_US_SPX','23_3_US_CCMP','23_3_DE','23_3_UK','23_3_JP','23_3_CH_SH','23_3_SZ','23_3_TR',
#                                   '23_3_MX','23_3_BR','23_3_RU','23_3_ZA']


std_delta_ohlc_short = prices_ohlc.pct_change().rolling(window_short).std()
mean_delta_ohlc_short = prices_ohlc.pct_change().rolling(window_short).mean()

std_ohlc_short = std_delta_ohlc_short[std_delta_ohlc_short.index>=start]
std_ohlc_short.columns = ['23-8_'+i for i in std_ohlc_short.columns]

mean_ohlc_short = mean_delta_ohlc_short[mean_delta_ohlc_short.index>=start]
mean_ohlc_short.columns = ['23-7_'+i for i in mean_ohlc_short.columns]

#std_ohlc_short.columns = ['23_4_US_NY','23_4_US_SPX','23_4_US_CCMP','23_4_DE','23_4_UK','23_4_JP','23_4_CH_SH','23_4_SZ','23_4_TR',
#                                   '23_4_MX','23_4_BR','23_4_RU','23_4_ZA']


mean_fromClose_ohlc_long.to_excel('C:/Users/sb0538/Desktop/15022020/excels/23-1_rvolmeanfromCloseohlclong.xlsx') 

std_fromClose_ohlc_long.to_excel('C:/Users/sb0538/Desktop/15022020/excels/23-2_rvolstdfromcloseohlclong.xlsx') 

mean_fromClose_ohlc_short.to_excel('C:/Users/sb0538/Desktop/15022020/excels/23-3_rvolmeanfromcloseohlcshort.xlsx')

std_fromClose_ohlc_short.to_excel('C:/Users/sb0538/Desktop/15022020/excels/23-4_rvolstdfromcloseohlcshort.xlsx')

mean_ohlc_long.to_excel('C:/Users/sb0538/Desktop/15022020/excels/23-5_rvolmeanohlcdeltalong.xlsx')

std_ohlc_long.to_excel('C:/Users/sb0538/Desktop/15022020/excels/23-6_rvolstdohlcdeltalong.xlsx')

mean_ohlc_short.to_excel('C:/Users/sb0538/Desktop/15022020/excels/23-7_rvolmeanohlcdeltashort.xlsx')

std_ohlc_short.to_excel('C:/Users/sb0538/Desktop/15022020/excels/23-8_rvolstdohlcdeltashort.xlsx')





