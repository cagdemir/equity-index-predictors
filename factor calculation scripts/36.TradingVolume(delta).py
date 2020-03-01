# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:35:07 2019

@author: Administrator
"""


import pdblp
import pandas as pd
import numpy as np
from scipy import signal


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

trade_volume = con.bdh(index_tickers, 'TURNOVER', firstday , today)

trade_volume_int = trade_volume.interpolate (method='linear')
trade_volume_int_w = trade_volume_int.groupby(pd.Grouper(freq='W')).sum()
trade_volume_int_w.columns = [i[0] for i in trade_volume_int_w.columns] 


delta_tradevolume = trade_volume_int_w.pct_change()
delta_tradevolume = delta_tradevolume.replace([np.inf,-np.inf,np.nan],0)
delta_tradevolume = delta_tradevolume[delta_tradevolume.index>=start]



#delta_trade_volume_w = trade_volume_w.pct_change()
#turnover = trade_volume_w - trade_volume_w.rolling(window).mean()


#turnover_delta= turnover.pct_change()
#turnover_delta = turnover_delta[turnover_delta.index>start]
trade_volume_int_w = trade_volume_int_w[trade_volume_int_w.index>=start]

var_no='36'
trade_volume_int_w.columns = [var_no+'_'+i for i in trade_volume_int_w.columns]
delta_tradevolume.columns= [var_no+'_'+i for i in delta_tradevolume.columns]

delta_tradevolume.to_excel('C:/Users/sb0538/Desktop/15022020/excels/36-2_deltatradevolume.xlsx') 
trade_volume_int_w.to_excel('C:/Users/sb0538/Desktop/15022020/excels/36-1_tradevolume.xlsx') 
