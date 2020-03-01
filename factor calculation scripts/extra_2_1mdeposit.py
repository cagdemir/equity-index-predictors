# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:37:28 2019

@author: Administrator
"""

import pdblp
import pandas as pd
import numpy as np
import eikon as ek
from datetime import date

ek.set_app_key('9559d6b91c084b348f50f9bcc0ef6a010b997405')


from datetime import date


start = '20040101'
today = date.today().strftime('%Y%m%d')
firstday = '19991230'



con = pdblp.BCon(debug=False, port=8194, timeout=9000)
con.start()

tickers_deposit = ['USDRA CMPN Curncy','EUDRA Curncy' , 
            'BPDRA Curncy', 'JYDRA Curncy', 'CCDRA Curncy' , 
            'TYDRA Curncy', 'MPDRA Curncy', 
           'BCDRA Curncy', 'RRDRA Curncy' , 'SADRA Curncy']


deposits = con.bdh(tickers_deposit, 'PX LAST', firstday, today)
deposits_int = deposits.interpolate(method='linear')
deposits_int_w= deposits_int.groupby(pd.Grouper(freq='W')).last()

deposits_int_w =  ((deposits_int_w/100)+1)**(1/52)-1

deposits_int_w = deposits_int_w[deposits_int_w.index>=start]

deposits_int_w.columns = [i[0] for i in deposits_int_w]
deposits_int_w = deposits_int_w[tickers_deposit]

deposits_int_w.columns = ['US','DE','UK','JP','CH','TR','MX','BR','RU','SA']



###########Short Terms
end_date = date.today().strftime('%Y-%m-%d')

short_term_us =  ek.get_timeseries(['US3MT=RR'], fields=['CLOSE'], start_date=firstday, end_date=end_date, interval='weekly')    

short_term_uk =  ek.get_timeseries(['GB3MT=RR'], fields=['CLOSE'], start_date=firstday, end_date=end_date, interval='weekly')   

short_term_tr =  ek.get_timeseries(['TR1YT=RR'], fields=['CLOSE'], start_date=firstday, end_date=end_date, interval='weekly')   

short_term_sa =  ek.get_timeseries(['ZA3MT=RR'], fields=['CLOSE'], start_date=firstday, end_date=end_date, interval='weekly')   

short_term_jp =  ek.get_timeseries(['JP3MT=RR'], fields=['CLOSE'], start_date=firstday, end_date=end_date, interval='weekly')   

short_term_mx =  ek.get_timeseries(['MX3MT=RR'], fields=['CLOSE'], start_date=firstday, end_date=end_date, interval='weekly')

short_term_ru =  ek.get_timeseries(['RU3MT=RR'], fields=['CLOSE'], start_date=firstday, end_date=end_date, interval='weekly')  

short_term_br =  ek.get_timeseries(['BR1YT=RR'], fields=['CLOSE'], start_date=firstday, end_date=end_date, interval='weekly')   

short_term_de =  ek.get_timeseries(['DE3MT=RR'], fields=['CLOSE'], start_date=firstday, end_date=end_date, interval='weekly')    

short_term_ch =  ek.get_timeseries(['HK3MT=RR'], fields=['CLOSE'], start_date=firstday, end_date=end_date, interval='weekly')  

short_terms= pd.concat([short_term_us,short_term_de, short_term_uk,short_term_jp,short_term_ch,short_term_tr,short_term_mx,short_term_br,short_term_ru,short_term_sa], axis=1)

short_terms_int = short_terms.interpolate(method='linear')
short_terms_int_w =  ((short_terms_int/100)+1)**(1/52)-1

short_terms_int_w = short_terms_int_w[short_terms_int_w.index>=start]

short_terms_int_w = short_terms_int_w.groupby(pd.Grouper(freq='W')).last()
short_terms_int_w.columns = ['US','DE','UK','JP','CH','TR','MX','BR','RU','SA']


################################################## spread

deposit_spread = (deposits_int_w - short_terms_int_w) * 100 

deposit_spread.columns = [i[0] for i in deposit_spread.columns]
deposit_spread.columns = ['extra2_US', 'extra2_GER','extra2_UK','extra2_JP','extra2_CH', 'extra2_TR','extra2_MX','extra2_BR','extra2_RU','extra2_SA']

deposit_spread.to_excel('C:/Users/sb0538/Desktop/15022020/excels/extra2_1Mdeposit.xlsx') 

