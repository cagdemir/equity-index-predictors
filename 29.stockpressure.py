# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:31:03 2019

@author: Administrator
"""

import pdblp
import pandas as pd
import numpy as np

#con = pdblp.BCon(debug=True, port=8194, timeout=5000)JAPAN* GENERIC* GOVERNMENT* BOND* 1* YEAR *
con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()

from datetime import date


start = '20040101'
today = date.today().strftime('%Y%m%d')
firstday = '19991230'

# for only this variable; XUTUM (TR) substituted with XU100

index_tickers = ['NYA Index', 'SPX Index', 'CCMP Index','NDX Index','CDAX Index' ,'DAX Index', 
            'ASX Index','UKX Index', 'TPX Index','NKY Index', 'SHCOMP Index' , 
           'SZCOMP Index','XU100 Index',  'MEXBOL Index', 
           'IBOV Index', 'IMOEX Index' , 'JALSH Index']

advancers = con.bdh(index_tickers, ['NUMBER OF WEEKLY ADVANCERS'],firstday, today)
advancers.columns = [i[0] for i in advancers.columns] 
advancers = advancers[index_tickers]
advancers_w = advancers.groupby(pd.Grouper(freq ='W')).mean() 
advancers_w = advancers_w[advancers_w.index>start]


decliners = con.bdh(index_tickers, ['NUMBER OF WEEKLY DECLINERS'],firstday, today)
decliners.columns = [i[0] for i in decliners.columns] 
decliners = decliners[index_tickers]
decliners_w = decliners.groupby(pd.Grouper(freq ='W')).mean() 
decliners_w = decliners_w[decliners_w.index>start]

decliners_w.replace(0,.1,inplace=True)

index_members = con.bdh(index_tickers, ['COUNT INDEX MEMBERS'],firstday, today)
index_members.columns = [i[0] for i in index_members.columns] 
index_members = index_members[index_tickers]
index_members_w = index_members.groupby(pd.Grouper(freq ='W')).mean()
index_members_w = index_members_w[index_members_w.index>start]

var_no='29'
stock_pressure = advancers_w.div(decliners_w)
stock_pressure.replace(np.nan,0,inplace=True)
#stock_pressure.columns = [i[0] for i in stock_pressure.columns]
stock_pressure.columns = [var_no+'_'+i for i in stock_pressure.columns] 

#○stock_pressure.columns = ['29_1_stock_pressure_US_NY','29_1_stock_pressure_US_SPX','29_1_stock_pressure_US_CCMP', '29_1_stock_pressure_DE','29_1_stock_pressure_UK','29_1_stock_pressure_JP','29_1_stock_pressure_CH_SH','29_1_stock_pressure_CH_SZ', '29_1_stock_pressure_TR','29_1_stock_pressure_MX','29_1_stock_pressure_BR','29_1_stock_pressure_RU','29_1_stock_pressure_SA']



stock_neutrality = ( index_members_w - (advancers_w + decliners_w) ).div(index_members_w)
stock_neutrality.replace(np.nan,0,inplace=True)
#stock_neutrality.columns = [i[0] for i in stock_neutrality.columns]
#stock_neutrality.columns = ['29_2_stock_neutrality_US_NY','29_2_stock_neutrality_US_SPX','29_2_stock_neutrality_US_CCMP', '29_2_stock_neutrality_DE','29_2_stock_neutrality_UK','29_2_stock_neutrality_JP','29_2_stock_neutrality_CH_SH','29_2_stock_neutrality_CH_SZ', '29_2_stock_neutrality_TR','29_2_stock_neutrality_MX','29_2_stock_neutrality_BR','29_2_stock_neutrality_RU','29_2_stock_neutrality_SA']
stock_neutrality.columns = [var_no+'_'+i for i in stock_neutrality.columns] 



stock_pressure.to_excel('C:/Users/sb0538/Desktop/15022020/excels/29-1_stockpressure.xlsx') 
stock_neutrality.to_excel('C:/Users/sb0538/Desktop/15022020/excels/29-2_stockneutrality.xlsx') 