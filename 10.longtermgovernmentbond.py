# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 14:31:37 2019

@author: Administrator
"""

#import pdblp #kullanılmadığı tespit edildi
import pandas as pd
import eikon as ek
import numpy as np
from datetime import date
ek.set_app_key('9559d6b91c084b348f50f9bcc0ef6a010b997405')

#reuters

start = '2004-1-1'
today = date.today().strftime('%Y%m%d')
firstday = '1999-12-30'


### TURKEY

turkey_yield_tickers = ['TR3MT=RR','TR1YT=RR','TR2YT=RR','TR5YT=RR','TR10YT=RR'  ]
list_yield_tr = []
real_tickers_tr = []

for ticker in turkey_yield_tickers:
    
    try:
    
        list_yield_tr.append(ek.get_timeseries(ticker, fields=['CLOSE'], start_date=firstday, end_date=today, interval='weekly'))
        real_tickers_tr.append(ticker)
    except:
        pass

yield_tr = pd.concat([i for i in list_yield_tr], axis=1)


####
a = yield_tr[yield_tr.index>='2004-1-1'] 
a.columns = [0,1,2,3,4]
b =a.columns[-1::-1]
aa = a.interpolate(method='linear')
b = aa.interpolate(method='spline',order=1,axis=1)

#longterm_tr = b[4]

##################################################

longterm_us = ek.get_timeseries('US10YT=RR',fields=['CLOSE'],  start_date=start, end_date=today, interval='weekly')
longterm_us = longterm_us.groupby(pd.Grouper(freq='W')).last()

longterm_de = ek.get_timeseries('DE10YT=RR',fields=['CLOSE'],  start_date=start, end_date=today, interval='weekly')
longterm_de = longterm_de.groupby(pd.Grouper(freq='W')).last()


longterm_uk = ek.get_timeseries('GB10YT=RR',fields=['CLOSE'], start_date=start, end_date=today, interval='weekly')
longterm_uk = longterm_uk.groupby(pd.Grouper(freq='W')).last()[longterm_uk.index>='2004-01-01']

longterm_jp = ek.get_timeseries('JP10YT=RR',fields=['CLOSE'],  start_date=start, end_date=today, interval='weekly')
longterm_jp = longterm_jp.groupby(pd.Grouper(freq='W')).last()

longterm_ch = ek.get_timeseries('HK10YT=RR',fields=['CLOSE'],  start_date=start, end_date=today, interval='weekly')
longterm_ch = longterm_ch.groupby(pd.Grouper(freq='W')).last()

longterm_tr = b[4].copy()
longterm_tr = longterm_tr.groupby(pd.Grouper(freq='W')).last()

longterm_mx = ek.get_timeseries('MX10YT=RR',fields=['CLOSE'],  start_date=start, end_date=today, interval='weekly')
longterm_mx = longterm_mx.groupby(pd.Grouper(freq='W')).last()

longterm_br = ek.get_timeseries('BR10YT=RR',fields=['CLOSE'],  start_date=start, end_date=today, interval='weekly')
longterm_br = longterm_br.groupby(pd.Grouper(freq='W')).last()

longterm_br.iloc[:3] = np.nan
#longterm_br = longterm_br.interpolate(method='linear',limit_direction='both')


longterm_ru = ek.get_timeseries('RU10YT=RR',fields=['CLOSE'],  start_date=start, end_date=today, interval='weekly')
longterm_ru = longterm_ru.groupby(pd.Grouper(freq='W')).last()

longterm_sa = ek.get_timeseries('ZA10YT=RR',fields=['CLOSE'],  start_date=start, end_date=today, interval='weekly')
longterm_sa = longterm_sa.groupby(pd.Grouper(freq='W')).last()

############################### Long Term Government Bonds

longterms = pd.concat([longterm_us, longterm_de, longterm_uk, longterm_jp,
                              longterm_ch, longterm_tr, longterm_mx, longterm_br,longterm_ru, longterm_sa], axis=1)

longterms.columns = ['10_US', '10_GER','10_UK','10_JP','10_CH', '10_TR','10_MX','10_BR','10_RU','10_SA']

longterms = longterms.interpolate(method='linear')
longterms = (longterms.iloc[-1::-1,:].interpolate(method='linear')).iloc[-1::-1,:]

longterms = longterms[longterms.index>=start] 
longterms.to_excel('C:/Users/sb0538/Desktop/15022020/excels/10_longtermgovernmentbond.xlsx') 
