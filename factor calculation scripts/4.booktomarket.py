# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:02:31 2019

@author: Administrator
"""


import pdblp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


plt.style.use('seaborn')

from datetime import date


start = '20040101'
today = date.today().strftime('%Y%m%d')
startday = '19991230'


#con = pdblp.BCon(debug=True, port=8194, timeout=5000)
con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()
index_tickers = ['NYA Index', 'SPX Index', 'CCMP Index','NDX Index','CDAX Index' ,'DAX Index', 
            'ASX Index','UKX Index', 'TPX Index','NKY Index', 'SHCOMP Index' , 
           'SZCOMP Index','XUTUM Index','XU100 Index',  'MEXBOL Index', 
           'IBOV Index', 'IMOEX Index' , 'JALSH Index']


price_to_book_raw = con.bdh(index_tickers, ['PX TO BOOK RATIO'],start, today)

price_to_book_weekly = price_to_book_raw.groupby(pd.Grouper(freq ='W')).mean()

price_to_book_weekly.loc['2007-1-25':'2007-4-7','CCMP Index'] = np.nan
price_to_book_weekly.loc['2006-1-1':'2006-1-7','XUTUM Index'] = 2.

price_to_book_int = price_to_book_weekly.interpolate(method='linear')

price_to_book = price_to_book_int[price_to_book_weekly.index>=start]

var_no = '4'
price_to_book.columns = [i[0] for i in price_to_book.columns]
price_to_book = price_to_book[index_tickers]
price_to_book.columns = [var_no+'_'+i for i in price_to_book.columns]


#price_to_book.columns = ['4_US_NY','4_US_SPX','4_US_CCMP', '4_DE','4_UK','4_JP','4_CH_SH','4_CH_SZ', '4_TR','4_MX','4_BR','4_RU','4_SA']

price_to_book.to_excel('C:/Users/sb0538/Desktop/15022020/excels/4_pricetobook.xlsx') 

#Prices=con.bdh(indices, 'PX LAST' ,'19991231', '20191129')
#MarketCap =con.bdh(indices,['CUR MKT CAP'],'19991231', '20191129')
#Book value pershare: BOOK VAL PER SH
#total common equity:RR010 TOT COMMON EQY
#Shares Outstanding: BS081, BS_SH_OS
#HISTORICAL MARKET CAP
#CUR MKT CAP (Current Market Cap)
#PRICE TO BOOK : PX TO BOOK RATIO

