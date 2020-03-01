# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 17:47:13 2019

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
dy = con.bdh(index_tickers, ['GROSS AGGTE DVD YLD'] , start, today)


dy_int = dy.interpolate(method='cubic')

#dy_temp = dy.interpolate(method='spline',order=2,limit=10, limit_direction='backward')
#dy_int_temp = dy_int.copy()
#dy_int_temp.update(dy_temp, overwrite=True)

dy_w = dy_int.groupby(pd.Grouper(freq='W')).mean() / 100
dy_w = dy_w[dy_w.index>=start]
dy_w.fillna(method='bfill', inplace=True)

dy_w_log = np.log(dy_w+1)

var_no='7'
dy_w_log.columns = [i[0] for i in dy_w_log.columns]
dy_w_log = dy_w_log[index_tickers]
dy_w_log.columns = [var_no+'_'+i for i in dy_w_log.columns]
dy_w_log = dy_w_log[dy_w_log.index>=start]
#dy_w_log.columns = ['7_US_NY','7_US_SPX','7_US_CCMP', '7_DE','7_UK','7_JP','7_CH_SH','7_CH_SZ', '7_TR','7_MX','7_BR','7_RU','7_SA']

dy_w_log.to_excel('C:/Users/sb0538/Desktop/15022020/excels/7_dividendpriceratiolog.xlsx') 