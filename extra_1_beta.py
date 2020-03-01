# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:20:06 2019

@author: Administrator
"""
import pdblp
import pandas as pd
import numpy as np
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

beta_raw = con.bdh(index_tickers, 'BETA RAW OVERRIDABLE', firstday, today)

beta_raw_int = beta_raw.interpolate(method='linear')


beta_int_w= beta_raw_int.groupby(pd.Grouper(freq='W')).last()

beta_int_w = beta_int_w [beta_int_w.index>=start]
#beta_raw_int_w.columns = [i[0] for i in beta_raw_int_w.columns]

var_no='extra1'
beta_int_w.columns = [i[0] for i in beta_int_w.columns]
beta_int_w =beta_int_w[index_tickers]
beta_int_w.columns = [var_no+'_'+i for i in beta_int_w.columns]

#beta_raw_int_w.columns = ['Extra_1_US_NY','Extra_1_US_SPX','Extra_1_US_CCMP', 'Extra_1_DE','Extra_1_UK','Extra_1_JP','Extra_1_CH_SH','Extra_1_CH_SZ', 'Extra_1_TR','Extra_1_MX','Extra_1_BR','Extra_1_RU','Extra_1_SA']


beta_int_w.to_excel('C:/Users/sb0538/Desktop/15022020/excels/extra1_beta.xlsx') 