# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import eikon as ek
ek.set_app_key('9559d6b91c084b348f50f9bcc0ef6a010b997405')
from datetime import date

start = '20040101'
today = date.today().strftime('%Y-%m-%d')
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

short_terms_int_w.columns = ['2_US','2_GER','2_UK','2_JP','2_CH','2_TR','2_MX','2_BR','2_RU','2_SA']




short_terms_int_w.to_excel('C:/Users/sb0538/Desktop/15022020/excels/2_treasurybillrates.xlsx') 

