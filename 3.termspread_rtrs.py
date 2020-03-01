# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:58:30 2019

@author: Administrator
"""
import eikon as ek
import pandas as pd
ek.set_app_key('9559d6b91c084b348f50f9bcc0ef6a010b997405')
from datetime import date


start = '2004-01-01'
end_date = date.today().strftime('%Y-%m-%d')
firstday='1999-12-30'

##################################################### America

us_yield_tickers = ['US3MT=RR','US1YT=RR','US2YT=RR', 'US5YT=RR', 'US10YT=RR' ]

list_yield_us = []
real_tickers_us = []

for ticker in us_yield_tickers:
    try:
        list_yield_us.append(ek.get_timeseries(ticker, fields=['CLOSE'], start_date=firstday, end_date=end_date, interval='weekly'))
        real_tickers_us.append(ticker)
    except :
            pass
        
yield_us = pd.concat([i for i in list_yield_us], axis=1)

yield_us.columns = real_tickers_us

yield_us_smoothed = yield_us.groupby(pd.Grouper(freq ='W')).mean()

yield_us_int = yield_us_smoothed.interpolate(method='linear')
 
first_best_us = yield_us_int.iloc[:,-1] - yield_us_int.iloc[:,0]
second_best_us = yield_us_int.iloc[:,-1] - yield_us_int.iloc[:,1]
third_best_us = yield_us_int.iloc[:,-2] - yield_us_int.iloc[:,0]
fourth_best_us =  yield_us_int.iloc[:,-2] - yield_us_int.iloc[:,1]

third_best_us.update(fourth_best_us)
second_best_us.update(third_best_us)
first_best_us.update(second_best_us)

term_spread_us = first_best_us[first_best_us.index>=start]

    
##################################################### Germany


de_yield_tickers = ['DE3MT=RR','DE1YT=RR','DE2YT=RR', 'DE5YT=RR',  'DE10YT=RR', ]

list_yield_de = []
real_tickers_de = []

for ticker in de_yield_tickers:
    try:
        list_yield_de.append(ek.get_timeseries(ticker, fields=['CLOSe'], start_date=firstday, end_date=end_date, interval='weekly'))
        real_tickers_de.append(ticker)
    except :
            pass
yield_de = pd.concat([i for i in list_yield_de], axis=1)
yield_de.columns = real_tickers_de

yield_de_smoothed = yield_de.groupby(pd.Grouper(freq ='W')).mean()

yield_de_int = yield_de_smoothed.interpolate(method='linear')

 
first_best_de = yield_de_int.iloc[:,-1] - yield_de_int.iloc[:,0]
second_best_de = yield_de_int.iloc[:,-1] - yield_de_int.iloc[:,1]
third_best_de = yield_de_int.iloc[:,-2] - yield_de_int.iloc[:,0]
fourth_best_de =  yield_de_int.iloc[:,-2] - yield_de_int.iloc[:,1]

third_best_de.update(fourth_best_de)
second_best_de.update(third_best_de)
first_best_de.update(second_best_de)

term_spread_de = first_best_de[first_best_de.index>=start]
 
##################################################### UK

uk_yield_tickers = ['GB3MT=RR','GB1YT=RR','GB2YT=RR','GB5YT=RR','GB10YT=RR' ]

list_yield_uk = []
real_tickers_uk = []

for ticker in uk_yield_tickers:
    
    try:
    
        list_yield_uk.append(ek.get_timeseries(ticker, fields=['CLOSE'], start_date=firstday, end_date=end_date, interval='weekly'))
        real_tickers_uk.append(ticker)
    except:
        pass

yield_uk = pd.concat([i for i in list_yield_uk], axis=1)
yield_uk.columns = real_tickers_uk

yield_uk_smoothed = yield_uk.groupby(pd.Grouper(freq ='W')).mean()

yield_uk_int = yield_uk_smoothed.interpolate(method='linear')

first_best_uk = yield_uk_int.iloc[:,-1] - yield_uk_int.iloc[:,0]
second_best_uk = yield_uk_int.iloc[:,-1] - yield_uk_int.iloc[:,1]
third_best_uk = yield_uk_int.iloc[:,-2] - yield_uk_int.iloc[:,0]
fourth_best_uk =  yield_uk_int.iloc[:,-2] - yield_uk_int.iloc[:,1]

third_best_uk.update(fourth_best_uk)
second_best_uk.update(third_best_uk)
first_best_uk.update(second_best_uk)


term_spread_uk = first_best_uk[first_best_uk.index>=start]

##################################################### JAPAN

jp_yield_tickers = ['JP3MT=RR','JP1YT=RR','JP2YT=RR','JP5YT=RR','JP10YT=RR'  ]

list_yield_jp = []
real_tickers_jp = []

for ticker in jp_yield_tickers:
    
    try:
    
        list_yield_jp.append(ek.get_timeseries(ticker, fields=['CLOSE'],start_date=firstday, end_date=end_date, interval='weekly'))
        real_tickers_jp.append(ticker)
    except:
        pass

yield_jp = pd.concat([i for i in list_yield_jp], axis=1)
yield_jp.columns = real_tickers_jp

yield_jp_smoothed = yield_jp.groupby(pd.Grouper(freq ='W')).mean()

yield_jp_int = yield_jp_smoothed.interpolate(method='linear')


first_best_jp = yield_jp_int.iloc[:,-1] - yield_jp_int.iloc[:,0]
second_best_jp = yield_jp_int.iloc[:,-1] - yield_jp_int.iloc[:,1]
third_best_jp = yield_jp_int.iloc[:,-2] - yield_jp_int.iloc[:,0]
fourth_best_jp =  yield_jp_int.iloc[:,-2] - yield_jp_int.iloc[:,1]

third_best_jp.update(fourth_best_jp)
second_best_jp.update(third_best_jp)
first_best_jp.update(second_best_jp)


term_spread_jp = first_best_jp[first_best_jp.index>=start]
 
##################################################### CHINA

ch_yield_tickers = ['HK3MT=RR','HK1YT=RR','HK2YT=RR','HK5YT=RR','HK10YT=RR'  ]

list_yield_ch = []
real_tickers_ch = []

for ticker in ch_yield_tickers:
    
    try:
    
        list_yield_ch.append(ek.get_timeseries(ticker, fields=['CLOSE'], start_date=firstday, end_date=end_date, interval='weekly'))
        real_tickers_ch.append(ticker)
    except:
        pass

yield_ch = pd.concat([i for i in list_yield_ch], axis=1)
yield_ch.columns = real_tickers_ch

yield_ch_smoothed = yield_ch.groupby(pd.Grouper(freq ='W')).mean()

yield_ch_int = yield_ch_smoothed.interpolate(method='linear')


first_best_ch = yield_ch_int.iloc[:,-1] - yield_ch_int.iloc[:,0]
second_best_ch = yield_ch_int.iloc[:,-1] - yield_ch_int.iloc[:,1]
third_best_ch = yield_ch_int.iloc[:,-2] - yield_ch_int.iloc[:,0]
fourth_best_ch =  yield_ch_int.iloc[:,-2] - yield_ch_int.iloc[:,1]

third_best_ch.update(fourth_best_ch)
second_best_ch.update(third_best_ch)
first_best_ch.update(second_best_ch)


term_spread_ch = first_best_ch[first_best_ch.index>=start]

 
##################################################### Turkey

# getting tr raw data

turkey_yield_tickers = ['TR3MT=RR','TR1YT=RR','TR2YT=RR','TR5YT=RR','TR10YT=RR'  ]

list_yield_tr = []
real_tickers_tr = []

for ticker in turkey_yield_tickers:
    
    try:
    
        list_yield_tr.append(ek.get_timeseries(ticker, fields=['CLOSE'], start_date=firstday, end_date=end_date, interval='weekly'))
        real_tickers_tr.append(ticker)
    except:
        pass

yield_tr = pd.concat([i for i in list_yield_tr], axis=1)
yield_tr.columns = real_tickers_tr

yield_tr_smoothed = yield_tr.groupby(pd.Grouper(freq ='W')).mean()

yield_tr_int = yield_tr_smoothed.interpolate(method='linear')

first_best_tr = yield_tr_int.iloc[:,-1] - yield_tr_int.iloc[:,0]
second_best_tr = yield_tr_int.iloc[:,-1] - yield_tr_int.iloc[:,1]
third_best_tr = yield_tr_int.iloc[:,-2] - yield_tr_int.iloc[:,0]
fourth_best_tr =  yield_tr_int.iloc[:,-2] - yield_tr_int.iloc[:,1]

third_best_tr.update(fourth_best_tr)
second_best_tr.update(third_best_tr)
first_best_tr.update(second_best_tr)


term_spread_tr = first_best_tr[first_best_tr.index>=start]


##################################################### MEXICO

mx_yield_tickers = ['MX3MT=RR','MX1YT=RR','MX2YT=RR','MX5YT=RR','MX10YT=RR'  ]

list_yield_mx = []
real_tickers_mx = []

for ticker in mx_yield_tickers:
    
    try:
    
        list_yield_mx.append(ek.get_timeseries(ticker, fields=['CLOSE'],  start_date=firstday, end_date=end_date, interval='weekly'))
        real_tickers_mx.append(ticker)
    except:
        pass

yield_mx = pd.concat([i for i in list_yield_mx], axis=1)
yield_mx.columns = real_tickers_mx

yield_mx_smoothed = yield_mx.groupby(pd.Grouper(freq ='W')).mean()

yield_mx_int = yield_mx_smoothed.interpolate(method='linear')

first_best_mx = yield_mx_int.iloc[:,-1] - yield_mx_int.iloc[:,0]
second_best_mx = yield_mx_int.iloc[:,-1] - yield_mx_int.iloc[:,1]
third_best_mx = yield_mx_int.iloc[:,-2] - yield_mx_int.iloc[:,0]
fourth_best_mx =  yield_mx_int.iloc[:,-2] - yield_mx_int.iloc[:,1]

third_best_mx.update(fourth_best_mx)
second_best_mx.update(third_best_mx)
first_best_mx.update(second_best_mx)


term_spread_mx = first_best_mx[first_best_mx.index>=start]

##################################################### BRAZIL

br_yield_tickers = ['BR3MT=RR','BR1YT=RR','BR2YT=RR','BR5YT=RR','BR10YT=RR'  ]

list_yield_br = []
real_tickers_br = []

for ticker in br_yield_tickers:
    
    try:
    
        list_yield_br.append(ek.get_timeseries(ticker, fields=['CLOSE'], start_date=firstday, end_date=end_date, interval='weekly'))
        real_tickers_br.append(ticker)
    except:
        pass

yield_br = pd.concat([i for i in list_yield_br], axis=1)
yield_br.columns = real_tickers_br

yield_br_smoothed = yield_br.groupby(pd.Grouper(freq ='W')).mean()

yield_br_int = yield_br_smoothed.interpolate(method='linear')

first_best_br = yield_br_int['BR10YT=RR'  ] - yield_br_int['BR1YT=RR']
second_best_br = yield_br_int['BR5YT=RR'  ] - yield_br_int['BR1YT=RR']
third_best_br = yield_br_int['BR10YT=RR'  ] - yield_br_int['BR3MT=RR']
#fourth_best_br =  yield_br_int.iloc[:,-2] - yield_br_int.iloc[:,1]

#third_best_br.update(fourth_best_br)
second_best_br.update(third_best_br)
first_best_br.update(second_best_br)


term_spread_br = first_best_br[first_best_br.index>=start]
 
##################################################### RUSSIA

ru_yield_tickers = ['RU3MT=RR','RU1YT=RR','RU2YT=RR','RU5YT=RR','RU10YT=RR'  ]

list_yield_ru = []
real_tickers_ru = []

for ticker in ru_yield_tickers:
    
    try:
    
        list_yield_ru.append(ek.get_timeseries(ticker, fields=['CLOSE'],  start_date=firstday, end_date=end_date, interval='weekly'))
        real_tickers_ru.append(ticker)
    except:
        pass

yield_ru = pd.concat([i for i in list_yield_ru], axis=1)
yield_ru.columns = real_tickers_ru

yield_ru_smoothed = yield_ru.groupby(pd.Grouper(freq ='W')).mean()

yield_ru_int = yield_ru_smoothed.interpolate(method='linear')


first_best_ru = yield_ru_int.iloc[:,-1] - yield_ru_int.iloc[:,0]
second_best_ru = yield_ru_int.iloc[:,-1] - yield_ru_int.iloc[:,1]
third_best_ru = yield_ru_int.iloc[:,-2] - yield_ru_int.iloc[:,0]
fourth_best_ru =  yield_ru_int.iloc[:,-2] - yield_ru_int.iloc[:,1]

third_best_ru.update(fourth_best_ru)
second_best_ru.update(third_best_ru)
first_best_ru.update(second_best_ru)


term_spread_ru = first_best_ru[first_best_ru.index>=start]

##################################################### SOUTH AFRICA

za_yield_tickers = ['ZA3MT=RR','ZA1YT=RR','ZA2YT=RR','ZA5YT=RR','ZA10YT=RR'  ]

list_yield_za = []
real_tickers_za = []

for ticker in za_yield_tickers:
    
    try:
    
        list_yield_za.append(ek.get_timeseries(ticker, fields=['CLOSE'],  start_date=firstday, end_date=end_date, interval='weekly'))
        real_tickers_za.append(ticker)
    except:
        pass

yield_za = pd.concat([i for i in list_yield_za], axis=1)
yield_za.columns = real_tickers_za

yield_za_smoothed = yield_za.groupby(pd.Grouper(freq ='W')).mean()

yield_za_int = yield_za_smoothed.interpolate(method='linear')


first_best_za = yield_za_int.iloc[:,-1] - yield_za_int.iloc[:,0]
second_best_za = yield_za_int.iloc[:,-1] - yield_za_int.iloc[:,1]
third_best_za = yield_za_int.iloc[:,-2] - yield_za_int.iloc[:,0]
fourth_best_za =  yield_za_int.iloc[:,-2] - yield_za_int.iloc[:,1]

third_best_za.update(fourth_best_za)
second_best_za.update(third_best_za)
first_best_za.update(second_best_za)


term_spread_za = first_best_za[first_best_za.index>=start]
#term_spread_za.to_excel('C:/Users/Administrator/Desktop/term_spread_za.xlsx') 


termspread = pd.concat([term_spread_us , term_spread_de , term_spread_uk , term_spread_jp, term_spread_ch, term_spread_tr,term_spread_mx,term_spread_br,term_spread_ru,term_spread_za ], axis=1)
termspread.columns = ['3_US', '3_GER','3_UK','3_JP','3_CH', '3_TR','3_MX','3_BR','3_RU','3_SA']


termspread.to_excel('C:/Users/sb0538/Desktop/15022020/excels/3_termspread.xlsx') 





