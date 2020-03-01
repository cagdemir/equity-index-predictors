# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 16:48:14 2019

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
firstday='19991230'

con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()

index_tickers = ['NYA Index', 'SPX Index', 'CCMP Index','NDX Index','CDAX Index' ,'DAX Index', 
            'ASX Index','UKX Index', 'TPX Index','NKY Index', 'SHCOMP Index' , 
           'SZCOMP Index','XUTUM Index','XU100 Index',  'MEXBOL Index', 
           'IBOV Index', 'IMOEX Index' , 'JALSH Index']

#################################################################dividend yield

 #Gross Aggregate Dividend Yield
dy = con.bdh(index_tickers,['NET AGGTE DVD YLD'], firstday , today)

dy_int = dy.interpolate(method='linear')
dy_w = dy_int.groupby(pd.Grouper(freq='W')).last()

dy_w = dy_w[dy_w.index>=start]
dy_w.fillna(method='bfill', inplace=True)

dy_w.columns =  [i[0] for i in dy_w.columns]
dy_w = dy_w[index_tickers]
dy_w_last = dy_w / 100


######################################################################### ep ratio

pe_ratio = con.bdh(index_tickers, ['PE RATIO'], firstday, today)

pe_ratio_int = pe_ratio.interpolate(method='linear')
pe_ratio_int_w = pe_ratio_int.groupby(pd.Grouper(freq='W')).last()

pe_ratio_last = pe_ratio_int_w[pe_ratio_int_w.index>=start]
pe_ratio_last.fillna(method='bfill', inplace=True)

pe_ratio_last.columns =  [i[0] for i in pe_ratio_last.columns]
pe_ratio_last = pe_ratio_last[index_tickers]

######################################################################## payout

net_payout_ratio = dy_w_last.mul(pe_ratio_last)
#net_payout_ratio.columns = ['11_US_NY','11_US_SPX','11_US_CCMP', '11_DE','11_UK','11_JP','11_CH_SH','11_CH_SZ', '11_TR','11_MX','11_BR','11_RU','11_SA']
net_payout_ratio = net_payout_ratio[net_payout_ratio.index>=start]

var_no = '11'
net_payout_ratio.columns = [var_no+'_'+i for i in net_payout_ratio.columns] 



net_payout_ratio.to_excel('C:/Users/sb0538/Desktop/15022020/excels/11_netpayoutratio.xlsx') 
