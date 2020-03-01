# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:30:53 2019

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


con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()

index_tickers = ['NYA Index', 'SPX Index', 'CCMP Index','NDX Index','CDAX Index' ,'DAX Index', 
            'ASX Index','UKX Index', 'TPX Index','NKY Index', 'SHCOMP Index' , 
           'SZCOMP Index','XUTUM Index','XU100 Index',  'MEXBOL Index', 
           'IBOV Index', 'IMOEX Index' , 'JALSH Index']



######################### Total Asset

total_asset = con.bdh(index_tickers, ['BS TOT ASSET'], firstday, today)


total_asset_w = total_asset.groupby(pd.Grouper(freq='W')).last()
total_asset_w_delta = total_asset_w.pct_change()

total_asset_w_delta_last = total_asset_w_delta[total_asset_w_delta.index>=start]

total_asset_w_delta_last.columns = [i[0] for i in total_asset_w_delta_last.columns]
total_asset_w_delta_last = total_asset_w_delta_last[index_tickers]

#total_asset_w_delta_last.columns = = ['US', 'DE','UK','JP','CH', 'TR','MX','BR','RU','SA']
var_no='28'
total_asset_w_delta_last.columns = [var_no+'_'+i for i in total_asset_w_delta_last.columns]
#total_asset_w_delta_last.columns = ['28_US_NY','28_US_SPX','28_US_CCMP', '28_DE','28_UK','28_JP','28_CH_SH','28_CH_SZ', '28_TR','28_MX','28_BR','28_RU','28_SA']
total_asset_w_delta_last[['28_XUTUM Index','28_XU100 Index']] = total_asset_w_delta_last[['28_XUTUM Index','28_XU100 Index']].bfill()

total_asset_w_delta_last.to_excel('C:/Users/sb0538/Desktop/15022020/excels/28_cma.xlsx') 