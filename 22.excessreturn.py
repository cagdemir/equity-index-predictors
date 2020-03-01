# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 16:19:06 2019

@author: Administrator
"""
import pdblp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')

import eikon as ek

ek.set_app_key('9559d6b91c084b348f50f9bcc0ef6a010b997405')

con = pdblp.BCon(debug=False, port=8194, timeout=9000)
con.start()

from datetime import date


start = '2004-1-1'
today = date.today().strftime('%Y%m%d')
firstday = '19991230'

##################################### Treasur Bill Rates
                                                #US
#3month - weekly 
#us3m = ek.get_timeseries(['US3MT=RR'], fields=['CLOSE'], start_date='2000-01-01', end_date='2019-12-11', interval='weekly')
#1year  
#us1y = ek.get_timeseries(['US1YT=RR'], fields=['CLOSE'], start_date='2000-01-01', end_date='2019-12-11', interval='weekly')

short_term_us =  ek.get_timeseries(['US3MT=RR'], fields=['CLOSE'], start_date=firstday, end_date=today, interval='weekly')                                            #Uk
# 3 months
                                                    #UK

#3month - weekly 
#uk3m = ek.get_timeseries(['GB3MT=RR'], fields=['CLOSE'], start_date='2000-01-01', end_date='2019-12-11', interval='weekly')
#1year
#uk1y = ek.get_timeseries(['GB1YT=RR'], fields=['CLOSE'], start_date='2000-01-01', end_date='2019-12-11', interval='weekly')

short_term_uk =  ek.get_timeseries(['GB3MT=RR'], fields=['CLOSE'], start_date=firstday, end_date=today, interval='weekly')                                                #Uk
# 3 months
                                                    
                                                    #TR 
#3month - weekly 
#tr3m = ek.get_timeseries(['TR3MT=RR'], fields=['CLOSE'], start_date='2000-01-01', end_date='2019-12-11', interval='weekly')
#1year
#tr1y = ek.get_timeseries(['TR1YT=RR'], fields=['CLOSE'], start_date='2000-01-01', end_date='2019-12-11', interval='weekly')

short_term_tr =  ek.get_timeseries(['TR1YT=RR'], fields=['CLOSE'], start_date=firstday, end_date=today, interval='weekly')                                               #Uk
# 1 year selected
                                                    
                                                    #S.A.
#3month -weekly 
#sa3m = ek.get_timeseries(['ZA3MT=RR'], fields=['CLOSE'], start_date='2000-01-01', end_date='2019-12-11', interval='weekly')
#1year ?? 
#5 year
#sa5y = ek.get_timeseries(['ZA5YT=RR'], fields=['CLOSE'], start_date='2000-01-01', end_date='2019-12-11', interval='weekly')

short_term_sa =  ek.get_timeseries(['ZA3MT=RR'], fields=['CLOSE'], start_date=firstday, end_date=today, interval='weekly')                                                #Uk
# 3 months
                                                    
                                                    #Japan
#3month
#jp3m = ek.get_timeseries(['JP3MT=RR'], fields=['CLOSE'], start_date='2000-01-01', end_date='2019-12-11', interval='weekly')
#1year
#jp1y = ek.get_timeseries(['JP1YT=RR'], fields=['CLOSE'], start_date='2000-01-01', end_date='2019-12-11', interval='weekly')

short_term_jp =  ek.get_timeseries(['JP3MT=RR'], fields=['CLOSE'], start_date=firstday, end_date=today, interval='weekly')                                               #Uk
# 3 months
                                                    
                                                    #Mexico
#3month
#mx3m = ek.get_timeseries(['MX3MT=RR'], fields=['CLOSE'], start_date='2000-01-01', end_date='2019-12-11', interval='weekly')
#1year
#mx1y = ek.get_timeseries(['MX1YT=RR'], fields=['CLOSE'], start_date='2000-01-01', end_date='2019-12-11', interval='weekly')

short_term_mx =  ek.get_timeseries(['MX3MT=RR'], fields=['CLOSE'], start_date=firstday, end_date=today, interval='weekly')                                                #Uk
# 3 months 
                                                    
                                                    #Russia
#3month
#ru3m = ek.get_timeseries(['RU3MT=RR'], fields=['CLOSE'], start_date='2000-01-01', end_date='2019-12-11', interval='weekly')
#1year
#ru1y = ek.get_timeseries(['RU1YT=RR'], fields=['CLOSE'], start_date='2000-01-01', end_date='2019-12-11', interval='weekly')

short_term_ru =  ek.get_timeseries(['RU3MT=RR'], fields=['CLOSE'], start_date=firstday, end_date=today, interval='weekly')                                                #Uk
# 3 months
                                                    
                                                    #Brasil
#3month 
#br3m = ek.get_timeseries(['BR3MT=RR'], fields=['CLOSE'], start_date='2000-01-01', end_date='2019-12-11', interval='weekly')
#1year
#br1y = ek.get_timeseries(['BR1YT=RR'], fields=['CLOSE'], start_date='2000-01-01', end_date='2019-12-11', interval='weekly')

short_term_br =  ek.get_timeseries(['BR1YT=RR'], fields=['CLOSE'], start_date=firstday, end_date=today, interval='weekly')                                                #Uk
# 1 year selected
                                                    
                                                    #Germany
#3month
#gm3m = ek.get_timeseries(['DE3MT=RR'], fields=['CLOSE'], start_date='2000-01-01', end_date='2019-12-11', interval='weekly')
#1year
#gm1y = ek.get_timeseries(['DE1YT=RR'], fields=['CLOSE'], start_date='2000-01-01', end_date='2019-12-11', interval='weekly')

short_term_de =  ek.get_timeseries(['DE3MT=RR'], fields=['CLOSE'], start_date=firstday, end_date=today, interval='weekly')                                                #Uk
# 3 months
                                                    
                                                    #China
#3month
#ch3m = ek.get_timeseries(['HK3MT=RR'], fields=['CLOSE'], start_date='2000-01-01', end_date='2019-12-11', interval='weekly')
#1year
#ch1y = ek.get_timeseries(['HK1YT=RR'], fields=['CLOSE'], start_date='2000-01-01', end_date='2019-12-11', interval='weekly')

short_term_ch =  ek.get_timeseries(['HK3MT=RR'], fields=['CLOSE'], start_date=firstday, end_date=today, interval='weekly')                                                #Uk
# 3 months

#short_term_tickers = ['US3MT=RR' ,'GB3MT=RR','TR1YT=RR','ZA3MT=RR','JP3MT=RR','MX3MT=RR','RU3MT=RR','BR1YT=RR','DE3MT=RR','HK3MT=RR']

#short_term =  ek.get_timeseries( short_term_tickers, fields=['CLOSE'], start_date='2000-01-01', end_date='2019-12-11', interval='weekly')                                            #Uk

short_terms= pd.concat([short_term_us,short_term_de, short_term_uk,short_term_jp,short_term_ch,short_term_tr,short_term_mx,short_term_br,short_term_ru,short_term_sa], axis=1)

short_terms_int = short_terms.interpolate(method='linear')
short_terms_int_w =  ((short_terms_int/100)+1)**(1/52)-1

short_terms_int_w = short_terms_int_w[short_terms_int_w.index>=start]

short_terms_int_w = short_terms_int_w.groupby(pd.Grouper(freq='W')).last()
short_terms_int_w.columns = ['US','DE','UK','JP','CH','TR','MX','BR','RU','SA']



###############################################################################


index_tickers = ['NYA Index', 'SPX Index', 'CCMP Index','NDX Index','CDAX Index' ,'DAX Index', 
            'ASX Index','UKX Index', 'TPX Index','NKY Index', 'SHCOMP Index' , 
           'SZCOMP Index','XUTUM Index','XU100 Index',  'MEXBOL Index', 
           'IBOV Index', 'IMOEX Index' , 'JALSH Index']

prices = con.bdh(index_tickers, 'PX LAST', firstday,today)
prices_int = prices.interpolate(method='linear')
idxRet_int_w = prices_int.groupby(pd.Grouper(freq='W')).last().pct_change()

idxRet_int_w = idxRet_int_w[idxRet_int_w.index>=start]#.iloc[:-1,:]
idxRet_int_w.columns = [i[0] for i in idxRet_int_w.columns]
idxRet_int_w = idxRet_int_w[index_tickers]

idxExcessRet = pd.DataFrame()

idxExcessRet['NYA Index'] = idxRet_int_w['NYA Index'] - short_terms_int_w['US']

idxExcessRet['SPX Index'] = idxRet_int_w['SPX Index'] - short_terms_int_w['US']

idxExcessRet['CCMP Index'] = idxRet_int_w['CCMP Index'] - short_terms_int_w['US']

idxExcessRet['NDX Index'] = idxRet_int_w['NDX Index'] - short_terms_int_w['US']


idxExcessRet['CDAX Index'] = idxRet_int_w['CDAX Index'] - short_terms_int_w['DE']

idxExcessRet['DAX Index'] = idxRet_int_w['DAX Index'] - short_terms_int_w['DE']


idxExcessRet['ASX Index'] = idxRet_int_w['ASX Index'] - short_terms_int_w['UK']

idxExcessRet['UKX Index'] = idxRet_int_w['UKX Index'] - short_terms_int_w['UK']


idxExcessRet['TPX Index'] = idxRet_int_w['TPX Index'] - short_terms_int_w['JP']

idxExcessRet['NKY Index'] = idxRet_int_w['NKY Index'] - short_terms_int_w['JP']


idxExcessRet['SHCOMP Index'] = idxRet_int_w['SHCOMP Index'] - short_terms_int_w['CH']

idxExcessRet['SZCOMP Index'] = idxRet_int_w['SZCOMP Index'] - short_terms_int_w['CH']


idxExcessRet['XUTUM Index'] = idxRet_int_w['XUTUM Index'] - short_terms_int_w['TR']
idxExcessRet['XU100 Index'] = idxRet_int_w['XU100 Index'] - short_terms_int_w['TR']


idxExcessRet['MEXBOL Index'] = idxRet_int_w['MEXBOL Index'] - short_terms_int_w['MX']


idxExcessRet['IBOV Index'] = idxRet_int_w['IBOV Index'] - short_terms_int_w['BR']


idxExcessRet['IMOEX Index'] = idxRet_int_w['IMOEX Index'] - short_terms_int_w['RU']


idxExcessRet['JALSH Index'] = idxRet_int_w['JALSH Index'] - short_terms_int_w['SA']


var_no = '22'
idxExcessRet = idxExcessRet[index_tickers]
idxExcessRet.columns = [var_no+'_'+i for i in idxExcessRet.columns]
#idxExcessRet = idxExcessRet[index_tickers]
# idxRet_int_w.columns = ['22-NYA Index','22-SPX Index','22_US_CCMP', '22_DE','22_UK','22_JP','22_CH_SH','22_CH_SZ', '22_TR','22_MX','22_BR','22_RU','22_SA']

idxExcessRet.to_excel('C:/Users/sb0538/Desktop/15022020/excels/22_excessreturn.xlsx') 


