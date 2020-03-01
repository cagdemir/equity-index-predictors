# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:30:31 2019

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
total_asset_last = total_asset_w[total_asset_w.index>=start]

var_no='27'
total_asset_last.columns = [i[0] for i in total_asset_last]
total_asset_last= total_asset_last[index_tickers]
#total_asset_last.columns = [var_no+'_'+i for i in total_asset_last.columns]
########################## Price to Earnings
pe_ratio = con.bdh(index_tickers, ['PE RATIO'],firstday, today)

pe_ratio_int = pe_ratio.interpolate(method='linear')
pe_ratio_int_w = pe_ratio_int.groupby(pd.Grouper(freq='W')).last()

pe_ratio_last = pe_ratio_int_w[pe_ratio_int_w.index>=start] 
pe_ratio_last.columns = [i[0] for i in pe_ratio_last.columns]
pe_ratio_last= pe_ratio_last[index_tickers]
#pe_ratio_last.columns = [var_no+'_'+i for i in pe_ratio_last.columns]
########################### Market Cap

mcap =con.bdh(index_tickers,['CUR MKT CAP'],firstday, today)


mcap_w = mcap.groupby(pd.Grouper(freq='B')).last().groupby(pd.Grouper(freq='W')).last()
#mcap_w.fillna(method='bfill', inplace=True)

mcap_w_last = mcap_w[mcap_w.index>=start]

mcap_w_last.columns = [i[0] for i in mcap_w_last]
mcap_w_last = mcap_w_last[index_tickers]
#mcap_w_last.columns = [var_no+'_'+i for i in mcap_w_last.columns]

################################
rmw = total_asset_last.div(mcap_w_last.div(pe_ratio_last))
rmw.columns = [var_no+'_'+i for i in rmw.columns]

#rmw.columns = ['27_US_NY','27_US_SPX','27_US_CCMP', '27_DE','27_UK','27_JP','27_CH_SH','27_CH_SZ', '27_TR','27_MX','27_BR','27_RU','27_SA']
rmw.to_excel('C:/Users/sb0538/Desktop/15022020/excels/27-rmw.xlsx') 




