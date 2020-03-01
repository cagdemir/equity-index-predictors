# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 18:23:05 2019

@author: Administrator
"""

import pdblp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')

#con = pdblp.BCon(debug=True, port=8194, timeout=5000)
con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()

from datetime import date


start = '20040101'
today = date.today().strftime('%Y%m%d')
firstday = '19991230'

currency_tickers = ['EUR Curncy','GBP Curncy','JPY Curncy','CNY Curncy','TRY Curncy','MXN Curncy','BRL Curncy','RUB Curncy','ZAR Curncy']


cur_variable_open = ['eur_o','gbp_o','jpy_o' ,'cny_o',
                        'try_o', 'mxn_o', 'brl_o','rub_o', 'zar_o']

cur_variable_close = ['eur_c','gbp_c','jpy_c' ,'cny_c',
                        'try_c', 'mxn_c', 'brl_c','rub_c', 'zar_c']

cur_variable_high = ['eur_h','gbp_h','jpy_h' ,'cny_h',
                        'try_h', 'mxn_h', 'brl_h','rub_h', 'zar_h']

cur_variable_low = ['eur_l','gbp_l','jpy_l' ,'cny_l',
                        'try_l', 'mxn_l', 'brl_l','rub_l', 'zar_l']

currency_open = con.bdh(currency_tickers, 'PX OPEN', firstday, today)
currency_open.columns =  [i[0] for i in currency_open.columns]
currency_open = currency_open[currency_tickers]
currency_open.columns = cur_variable_open
currency_open_int = currency_open.interpolate(method='linear')
currency_open_int_w = currency_open_int.groupby(pd.Grouper(freq='W')).first()

currency_high = con.bdh(currency_tickers, 'PX HIGH', firstday, today)
currency_high.columns =  [i[0] for i in currency_high.columns]
currency_high = currency_high[currency_tickers]
currency_high.columns = cur_variable_open
currency_high_int = currency_high.interpolate(method='linear')
currency_high_int_w = currency_high_int.groupby(pd.Grouper(freq='W')).max()

currency_low = con.bdh(currency_tickers, 'PX LOW', firstday, today)
currency_low.columns =  [i[0] for i in currency_low.columns]
currency_low = currency_low[currency_tickers]
currency_low.columns = cur_variable_open
currency_low_int = currency_low.interpolate(method='linear')
currency_low_int_w = currency_low_int.groupby(pd.Grouper(freq='W')).min()

currency_close = con.bdh(currency_tickers, 'PX LAST', firstday, today)
currency_close.columns =  [i[0] for i in currency_close.columns]
currency_close = currency_close[currency_tickers]
currency_close.columns = cur_variable_open
currency_close_int = currency_close.interpolate(method='linear')
currency_close_int_w = currency_close_int.groupby(pd.Grouper(freq='W')).last()

########### RETURNS OHLC from Close 

returns_open = currency_open_int_w / currency_close_int_w.shift(1) - 1
returns_high = currency_high_int_w / currency_close_int_w.shift(1) - 1
returns_high.columns = cur_variable_high 
returns_low = currency_low_int_w / currency_close_int_w.shift(1) - 1
returns_low.columns = cur_variable_low
returns_close= currency_close_int_w / currency_close_int_w.shift(1) - 1
returns_high.columns = cur_variable_close

returns_ohlc = pd.concat([returns_open, returns_high, returns_low, returns_close], axis =1 )

cur_tickers_variables = ['EUR','GBP','JPY','CNY','TRY','MXN','BRL','RUB','ZAR']


cur_ohlc_tickers1 = ['extra5-1_O','extra5-1_H','extra5-1_L', 'extra5-1_C']
returns_ohlc.columns =  [('_').join(i) for i in zip(np.repeat(cur_ohlc_tickers1,len(cur_tickers_variables)),returns_ohlc.columns)]

returns_ohlc = returns_ohlc[returns_ohlc.index>=start]
returns_ohlc.to_excel('C:/Users/sb0538/Desktop/15022020/excels/extra5-1_returncurrencyclose.xlsx') 


##################################
currency_prices = pd.concat([currency_open_int_w , currency_high_int_w , currency_low_int_w , currency_close_int_w], axis=1)
currency_prices_delta = currency_prices.pct_change()
currency_prices_delta = currency_prices_delta[currency_prices_delta.index>=start]


currency_prices_delta.to_excel('C:/Users/sb0538/Desktop/15022020/excels/extra5-2_currencydelta.xlsx') 

