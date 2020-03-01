# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 15:43:54 2019

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


window = 250
#con = pdblp.BCon(debug=True, port=8194, timeout=5000)
con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()

index_tickers = ['NYA Index', 'SPX Index', 'CCMP Index','NDX Index','CDAX Index' ,'DAX Index', 
            'ASX Index','UKX Index', 'TPX Index','NKY Index', 'SHCOMP Index' , 
           'SZCOMP Index','XUTUM Index','XU100 Index',  'MEXBOL Index', 
           'IBOV Index', 'IMOEX Index' , 'JALSH Index']

trade_volume = con.bdh(index_tickers, 'TURNOVER', firstday , today)

trade_volume_w = trade_volume.groupby(pd.Grouper(freq='W')).sum()
trade_volume_w.replace(0,np.nan,inplace=True)
trade_volume_w = trade_volume_w.interpolate(method='linear')

delta_trade_volume_w = trade_volume_w.pct_change()

var_no='25'
delta_trade_volume_w = delta_trade_volume_w [delta_trade_volume_w.index>start]
delta_trade_volume_w.columns =  [i[0] for i in delta_trade_volume_w.columns]
delta_trade_volume_w = delta_trade_volume_w[index_tickers]
delta_trade_volume_w.columns = [var_no+'_'+i for i in delta_trade_volume_w.columns]



#delta_trade_volume_w.columns= ['25_1_US_NY_turnover','25_1_US_SPX_turnover','25_1_US_CCMP_turnover', '25_1_DE_turnover','25_1_UK_turnover','25_1_JP_turnover','25_1_CH_SH_turnover', '25_1_CH_SZ_turnover','25_1_TR_turnover','25_1_MX_turnover','25_1_BR_turnover','25_1_RU_turnover','25_1_SA_turnover']



turnover = trade_volume_w - trade_volume_w.rolling(window, min_periods=100).mean()

turnover= turnover [turnover.index>=start]
turnover.columns =  [i[0] for i in turnover.columns]
turnover = turnover[index_tickers]
turnover.columns = [var_no+'_'+i for i in turnover.columns]



#♣turnover.columns= ['25_2_US_NY_turnover','25_2_US_SPX_turnover','25_2_US_CCMP_turnover', '25_2_DE_turnover','25_2_UK_turnover','25_2_JP_turnover','25_2_CH_SH_turnover', '25_2_CH_SZ_turnover','25_2_TR_turnover','25_2_MX_turnover','25_2_BR_turnover','25_2_RU_turnover','25_2_SA_turnover']


delta_trade_volume_w.to_excel('C:/Users/sb0538/Desktop/15022020/excels/25-1_shareturnoverdelta.xlsx') 
turnover.to_excel('C:/Users/sb0538/Desktop/15022020/excels/25-2_shareturnoverrolled.xlsx') 

