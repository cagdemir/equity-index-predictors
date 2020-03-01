# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:08:08 2019

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

index_tickers = ['NYA Index', 'SPX Index', 'CCMP Index','NDX Index','CDAX Index' ,'DAX Index', 
            'ASX Index','UKX Index', 'TPX Index','NKY Index', 'SHCOMP Index' , 
          'XUTUM Index','XU100 Index',  'MEXBOL Index', 
           'IBOV Index', 'IMOEX Index' , 'JALSH Index']


#change in 1 year ahead analyst's earnings per share estimates
# US s&P500 Index Estimaed EPS

#DeltaForwardEPS =  con.bdh( 'SPEDESTI Index','PX LAST' , '19991231', '20191202')

#The estimated Index Long Term Growth Rate of Earnings per Share (EPS)
# is a weighted average of underlying members' Estimated LTG. Long term growth forecasts generally
# represent an expected annual increase in operating earnings over the company's next full business cycle.
# In general, these forecasts refer to a period of between three to five years. 
#Calculated by summing all members [BEst LTG EPS (BE017, BEST_LTG_EPS) times Percent Weight in the Index], adjusted for equity coverage.
#---> 


eps =  con.bdh( index_tickers, 'EST LTG EPS AGGTE' , firstday , today)

eps.columns =[i[0] for i in eps]
eps = eps[index_tickers]

eps_smoothed = eps.groupby(pd.Grouper(freq='W')).mean()
eps_smoothed_delta = eps_smoothed.pct_change()

#eps_smoothed_int = eps_smoothed.interpolate(method='linear')
eps_smoothed_last = eps_smoothed[eps_smoothed.index>=start]
eps_smoothed_delta_last = eps_smoothed_delta[eps_smoothed_delta.index>=start]


var_no='17'
eps_smoothed_last.columns = [var_no+'-1_'+i for i in eps_smoothed_last.columns]

eps_smoothed_delta_last.columns = [var_no+'-2_'+i for i in eps_smoothed_delta_last.columns]

#eps_smoothed_last.columns=  ['17_US_NY','17_US_CCMP', '17_DE','17_UK','17_JP','17_CH_SH', '17_TR','17_MX','17_BR','17_RU','17_SA']

eps_smoothed_last.to_excel('C:/Users/sb0538/Desktop/15022020/excels/17-1_epsforward.xlsx')

eps_smoothed_delta_last.to_excel('C:/Users/sb0538/Desktop/15022020/excels/17-2_epsdeltaforward.xlsx')
