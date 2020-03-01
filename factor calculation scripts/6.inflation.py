# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 15:43:17 2019

@author: Administrator
"""

import pdblp
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date


start = '20030101'
today = date.today().strftime('%Y%m%d')
firstday = '19981230'



con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()

list_inf_tickers=['CPICMOM Index','GRCP20MM Index','UKRPCJMR Index','JNCPIMOM Index',
              'CNCPIMOM Index','TUCPIM Index','MXCPCHNG Index', 'BZPIIPCM Index',
              'RUCPIMOM Index', 'SACPIMOM Index' ]


data_inf = con.bdh(list_inf_tickers,  'PX LAST',firstday, today)
data_inf.columns = [i[0] for i in data_inf.columns]
data_inf = data_inf[list_inf_tickers]


idx =  pd.date_range(start=data_inf.index[0], end=today, freq='D')
inflation = pd.DataFrame(columns=data_inf.columns, index=idx)

lag = 5
ffill_limit = 31 #in terms of days to ffill

inflation.update(data_inf)

inf_w = inflation.shift(lag).ffill(limit=ffill_limit).groupby(pd.Grouper(freq='W')).last()


inf_w_last = inf_w [inf_w.index>=start]


inf_w_last.columns = ['6_US', '6_GER','6_UK','6_JP','6_CH', '6_TR','6_MX','6_BR','6_RU','6_SA']

inf_w_last.to_excel('C:/Users/sb0538/Desktop/15022020/excels/6_inflation.xlsx') 

#list

#US

#Germany

#England

#Japan

#China

#Turkey

#Mexico

#Brazil

#Russia

#South Africa


