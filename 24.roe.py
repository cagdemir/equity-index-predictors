# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:13:58 2019

@author: Administrator
"""



import pdblp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')

from datetime import date


start = '2004-1-1'
today = date.today().strftime('%Y%m%d')
firstday = '19991230'


#con = pdblp.BCon(debug=True, port=8194, timeout=5000)
con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()
index_tickers = ['NYA Index', 'SPX Index', 'CCMP Index','NDX Index','CDAX Index' ,'DAX Index', 
            'ASX Index','UKX Index', 'TPX Index','NKY Index', 'SHCOMP Index' , 
           'SZCOMP Index','XUTUM Index','XU100 Index',  'MEXBOL Index', 
           'IBOV Index', 'IMOEX Index' , 'JALSH Index']

start = '2004-1-1'
########################################### Price to Book
price_to_book_raw = con.bdh(index_tickers, ['PX TO BOOK RATIO'],firstday, today)

price_to_book_weekly = price_to_book_raw.groupby(pd.Grouper(freq ='W')).mean()

price_to_book_weekly.loc['2007-1-25':'2007-4-7','CCMP Index'] = np.nan
price_to_book_weekly.loc['2006-1-1':'2006-1-7','XUTUM Index'] = 2.

price_to_book_int = price_to_book_weekly.interpolate(method='linear')

price_to_book = price_to_book_int[price_to_book_weekly.index>=start]

var_no='24'
price_to_book.columns = [i[0] for i in  price_to_book.columns]
#price_to_book.columns = [var_no+'_'+i for i in price_to_book.columns]
price_to_book = price_to_book[index_tickers]

########################################## EarningsToPrice

#pe_ratio_nya = con.bdh( 'NYA Index', ['PE RATIO'], '19991231','20191210')
#
#pe_ratio_spx = con.bdh( 'SPX Index', ['PE RATIO'], '19991231','20191210')
#
#pe_ratio_ccmp = con.bdh( 'CCMP Index', ['PE RATIO'], '19991231','20191210')
#
#
#pe_ratio_cdax = con.bdh( 'CDAX Index', ['PE RATIO'], '19991231','20191210')
#
#pe_ratio_asx = con.bdh( 'ASX Index', ['PE RATIO'], '19991231','20191210')
#
#pe_ratio_tpx = con.bdh( 'TPX Index', ['PE RATIO'], '19991231','20191210')
#
#pe_ratio_shcomp = con.bdh( 'SHCOMP Index', ['PE RATIO'], '19991231','20191210')
#
#pe_ratio_szcomp = con.bdh( 'SZCOMP Index', ['PE RATIO'], '19991231','20191210')
#
#pe_ratio_xutum = con.bdh( 'XUTUM Index', ['PE RATIO'], '19991231','20191210')
#
#pe_ratio_mexbol = con.bdh( 'MEXBOL Index', ['PE RATIO'], '19991231','20191210')
#
#pe_ratio_ibov = con.bdh( 'IBOV Index', ['PE RATIO'], '19991231','20191210')
#
#pe_ratio_imoex = con.bdh( 'IMOEX Index', ['PE RATIO'], '19991231','20191210')
#
#pe_ratio_jalsh = con.bdh( 'JALSH Index', ['PE RATIO'], '19991231','20191210')
#
#pe_ratio = pd.concat([pe_ratio_spx, pe_ratio_ccmp,
#                     pe_ratio_cdax ,pe_ratio_asx ,pe_ratio_tpx,
#                     pe_ratio_shcomp,pe_ratio_szcomp,pe_ratio_xutum,pe_ratio_mexbol,
#                     pe_ratio_ibov, pe_ratio_imoex, pe_ratio_jalsh], axis=1)

pe_ratio = con.bdh(index_tickers, ['PE RATIO'],firstday, today)

pe_ratio_int = pe_ratio.interpolate(method='linear')
pe_ratio_int_w = pe_ratio_int.groupby(pd.Grouper(freq='W')).last()

pe_ratio_last = pe_ratio_int_w[pe_ratio_int_w.index>start] 
pe_ratio_last.columns = [i[0] for i in pe_ratio_last.columns]
#pe_ratio_last.columns = [var_no+'_'+i for i in pe_ratio_last.columns]
pe_ratio_last = pe_ratio_last[index_tickers]
####################################################################


roe = price_to_book.div(pe_ratio_last)
roe.columns = [var_no+'_'+i for i in roe.columns]
roe = roe [roe.index>start]
#roe.columns = ['24-US_NY','24_US_SPX','24_US_CCMP', '24_DE','24_UK','24_JP','24_CH_SH','24_CH_SZ','24_TR','24_MX','24_BR','24_RU','24_SA']

roe.to_excel('C:/Users/sb0538/Desktop/15022020/excels/24_roe.xlsx') 




