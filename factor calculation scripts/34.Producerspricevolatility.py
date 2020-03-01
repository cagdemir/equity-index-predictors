# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:33:31 2019

@author: Administrator
"""

import pdblp
import pandas as pd
import numpy as np
from datetime import date


start = '20040101'
today = date.today().strftime('%Y%m%d')
firstday = '19981230'


con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()


ppi_tickers=['PPI CHNG Index','GRPFIMOM Index', 'UKPPIOC Index', 
     'JNWSDOM Index','CHEFMOM Index','TUDPMOM Index',
     'MXPICHNG Index','2236629 Index','RUPPNEWM Index','1996629 Index' ]

####bRAZIL VE CHINA MOM%

#US: PPI final demand SA : FDIDFDMO Index
#Germany: GRPFIYOY Index : Germany Producer prices
#UK: UKPPIOY : UK PPI Manufactured products YoY NSA
#Japan:JNWSDYOY : Japan Producer Price Index Yoy
#China: CHEFTYOY
#Turkey: EHPPTRY
#Mexico: MXPIYOY
#Brazil: BPPICY:Manucacturing Industry i BPPITOTY: PPI Index total YoY
#Russia: RUPPNEWY 2000=100 YoY , All industries: RUPPIYOY
#South Africa: SAPRFMGY : SA PPI Final Manufacturted goods YoY


producersprice = con.bdh(ppi_tickers, ['PX LAST'], firstday, today)
producersprice.columns = [i[0] for i in producersprice.columns]
producersprice = producersprice[ppi_tickers]

producersprice.columns = ['34_US', '34_GER','34_UK','34_JP','34_CH', '34_TR','34_MX','34_BR','34_RU','34_SA']

producersprice/=100

window = 6
producersprice[['34_BR','34_SA']] = producersprice[['34_BR','34_SA']].pct_change()

std_ppi = producersprice.rolling(window,min_periods=1).std()
std_ppi['34_MX'] = std_ppi['34_MX'].bfill()

#producersprice= producersprice[producersprice.index>start]

std_ppi_w= std_ppi.groupby(pd.Grouper(freq='W')).last()

lag = 2
#idx =  pd.date_range(start=producersprice.index[0], end=today, freq='W')
#pro_price_last = pd.DataFrame(columns=pro_price_w.columns, index=idx)

#pro_price_last.update(pro_price_w)
std_ppi_w_last  =std_ppi_w.shift(lag).ffill()#.astype(float)


std_ppi_w_last= std_ppi_w_last[std_ppi_w_last.index>=start]
std_ppi_w_last.columns = ['34_US', '34_GER','34_UK','34_JP','34_CH', '34_TR','34_MX','34_BR','34_RU','34_SA']

std_ppi_w_last.to_excel('C:/Users/sb0538/Desktop/15022020/excels/34_producerspricevol.xlsx') 
