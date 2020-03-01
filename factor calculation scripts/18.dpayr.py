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

con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()

index_tickers = ['NYA Index', 'SPX Index', 'CCMP Index','NDX Index','CDAX Index' ,'DAX Index', 
            'ASX Index','UKX Index', 'TPX Index','NKY Index', 'SHCOMP Index' , 
           'SZCOMP Index','XUTUM Index','XU100 Index',  'MEXBOL Index', 
           'IBOV Index', 'IMOEX Index' , 'JALSH Index']
# index_tickers = [i.split(' ')[0] for i in indices]

#Dividend payout ratio hesaplanacak: difference btw log of dividends and log of earnings
from datetime import date


start = '2004-1-1'
today = date.today().strftime('%Y%m%d')
firstday = '19991230'


#################################################################dividend yield

 #Gross Aggregate Dividend Yield
dy = con.bdh(index_tickers,['GROSS AGGTE DVD YLD'],firstday, today)

dy_int = dy.interpolate(method='cubic')

dy_w = dy_int.groupby(pd.Grouper(freq='W')).mean()
dy_w = dy_w[dy_w.index>=start]
dy_w.fillna(method='bfill', inplace=True)

#◘dy_w.columns =  [i[0].split(' ')[0] for i in dy_w.columns]
dy_w = dy_w[index_tickers]
dy_w_last = dy_w / 100

dy_w_last.columns =  [i[0] for i in dy_w_last.columns]


######################################################################### ep ratio

pe_ratio = con.bdh(index_tickers, ['PE RATIO'],firstday, today)

pe_ratio_int = pe_ratio.interpolate(method='linear')
pe_ratio_int_w = pe_ratio_int.groupby(pd.Grouper(freq='W')).last()

pe_ratio_last = pe_ratio_int_w[pe_ratio_int_w.index>=start]

#pe_ratio_last.columns =  [i[0].split(' ')[0] for i in pe_ratio_last.columns]


pe_ratio_last.columns =  [i[0] for i in pe_ratio_last.columns]
pe_ratio_last = pe_ratio_last[index_tickers]

######################################################################## payout

payout_ratio = dy_w_last.mul(pe_ratio_last)
payout_ratio = payout_ratio[index_tickers]


var_no = '18'
payout_ratio.columns = [var_no+'_'+i for i in payout_ratio.columns] 


#payout_ratio.columns = ['18_US_NY','18_US_SPX','18_US_CCMP', '18_DE','18_UK','18_JP','18_CH_SH','18_CH_SZ', '18_TR','18_MX','18_BR','18_RU','18_SA']


payout_ratio.to_excel('C:/Users/sb0538/Desktop/15022020/excels/18_dividendpayoutratio.xlsx') 
