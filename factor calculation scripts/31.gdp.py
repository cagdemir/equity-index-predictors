# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:31:36 2019

@author: Administrator
"""

import pdblp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()

from datetime import date


start = '20040101'
today = date.today().strftime('%Y%m%d')
firstday = '19991230'


gdp_tickers = ['GDP CHWG Index' ,'GRGDEGDP Index' , 
            'UKGRABMI Index', 'JGDPGDP Index', 'CNGDGDP Index' , 
           'TUGPIGD Index', 'MXGPLEVL Index', 'BZGDQOQ Index', 
           'RUDPGDPN Index','ZARSGDP Index']


gdp = con.bdh( gdp_tickers ,'PX LAST', firstday, today ) 


delta_gdp = gdp.pct_change()

lag = 10

idx_sent = pd.date_range(start=firstday, end=today, freq='D')

delta_gdp_sent = pd.DataFrame(columns=delta_gdp.columns,index=idx_sent)
delta_gdp_sent.update(delta_gdp)

ffill_limit = 100 #in terms of days to ffill

delta_gdp_w = delta_gdp_sent.ffill(limit=ffill_limit).groupby(pd.Grouper(freq='W')).last().shift(lag)

#delta_gdp_w = delta_gdp.groupby(pd.Grouper(freq='W')).last().shift(lag).ffill()




delta_gdp_w =delta_gdp_w[delta_gdp_w.index>=start]
delta_gdp_w.columns =  [i[0] for i in delta_gdp_w.columns]

delta_gdp_w = delta_gdp_w[gdp_tickers]

delta_gdp_w.columns = ['31_US', '31_GER','31_UK','31_JP','31_CH', '31_TR','31_MX','31_BR','31_RU','31_SA']


delta_gdp_w.to_excel('C:/Users/sb0538/Desktop/15022020/excels/31_gdp.xlsx') 


