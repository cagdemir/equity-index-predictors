# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 12:44:02 2019

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
index_tickers = [ 'XUTUM Index', 'MEXBOL Index', 
           'IBOV Index', 'IMOEX Index' , 'JALSH Index']

start = '20040101'
today = date.today().strftime('%Y%m%d')
firstday = '19991230'

ohlc_tickers = ['HIGH','LOW']

#prices_open = con.bdh(index_tickers, 'PX OPEN',firstday, today)
#prices_open.columns = [i[0] for i in prices_open.columns]
#prices_open_int = prices_open.interpolate(method='linear')[index_tickers]
#prices_open_w = prices_open_int.groupby(pd.Grouper(freq='W')).first()

idx_high = con.bdh(index_tickers, 'PX HIGH',firstday, today) 
idx_high.columns = [i[0] for i in idx_high.columns]
idx_high_int = idx_high.interpolate(method='linear')[index_tickers]
idx_high_w = idx_high_int.groupby(pd.Grouper(freq='W')).idxmax()
idx_high_w = idx_high_w[idx_high_w.index>=start]

idx_low  = con.bdh(index_tickers, 'PX LOW',firstday, today)
idx_low.columns = [i[0] for i in idx_low.columns]
idx_low_int = idx_low.interpolate(method='linear')[index_tickers]
idx_low_w = idx_low_int.groupby(pd.Grouper(freq='W')).idxmin()
idx_low_w = idx_low_w[idx_low_w.index>=start]


#returns_fromClose_ohlc = returns_fromClose_ohlc[returns_fromClose_ohlc.index>=start]

#target_high = idx_high_w.shift(-1)
#target_low = idx_low_w.shift(-1)
positions = idx_high_w - idx_low_w
positions.columns =['hlpositions-3_tr' ,'hlpositions-3_mx','hlpositions-3_br','hlpositions-3_ru','hlpositions-3_sa' ]

idx_high_w.columns = ['hlpositions-1_tr' ,'hlpositions-1_mx','hlpositions-1_br','hlpositions-1_ru','hlpositions-1_sa' ]
idx_low_w.columns =  ['hlpositions-2_tr' ,'hlpositions-2_mx','hlpositions-2_br','hlpositions-2_ru','hlpositions-2_sa' ]

idx_high_w.to_excel('C:/Users/sb0538/Desktop/15022020/excels/hlpositions-1_high.xlsx') 
idx_low_w.to_excel('C:/Users/sb0538/Desktop/15022020/excels/hlpositions-2_low.xlsx') 
positions.to_excel('C:/Users/sb0538/Desktop/15022020/excels/hlpositions-3_positions.xlsx') 
