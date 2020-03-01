# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:48:09 2019

@author: Administrator
"""


import pdblp
import pandas as pd
import numpy as np
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
 #Gross Aggregate Dividend Yield
dy = con.bdh(index_tickers,['GROSS AGGTE DVD YLD'],start, today)


dy_int = dy.interpolate(method='cubic')

#dy_temp = dy.interpolate(method='spline',order=2,limit=10, limit_direction='backward')
#dy_int_temp = dy_int.copy()
#dy_int_temp.update(dy_temp, overwrite=True)

dy_w = dy_int.groupby(pd.Grouper(freq='W')).mean() / 100
dy_w = dy_w[dy_w.index>=start]
dy_w.fillna(method='bfill', inplace=True) 

var_no = '8'
dy_w.columns = [i[0] for i in dy_w.columns] 
dy_w = dy_w[index_tickers]
dy_w.columns = [var_no+'_'+i for i in dy_w.columns]

#dy_w.columns = ['8_US_NY','8_US_SPX','8_US_CCMP', '8_DE','8_UK','8_JP','8_CH_SH','8_CH_SZ', '8_TR','8_MX','8_BR','8_RU','8_SA']

dy_w.to_excel('C:/Users/sb0538/Desktop/15022020/excels/8_dividendpriceratio.xlsx') 