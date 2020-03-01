# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 15:52:55 2019

@author: Administrator
"""

import pdblp
import pandas as pd
from datetime import date


start = '20040101'
today = date.today().strftime('%Y%m%d')
firstday = '19991230'

con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()

window_long = 150
window_medium = 100
window_short = 20

index_tickers = ['NYA Index', 'SPX Index', 'CCMP Index','NDX Index','CDAX Index' ,'DAX Index', 
            'ASX Index','UKX Index', 'TPX Index','NKY Index', 'SHCOMP Index' , 
           'SZCOMP Index','XUTUM Index','XU100 Index',  'MEXBOL Index', 
           'IBOV Index', 'IMOEX Index' , 'JALSH Index']

prices = con.bdh(index_tickers, 'PX LAST', firstday, today)
prices[('XUTUM Index','PX LAST')] = prices[('XUTUM Index','PX LAST')].bfill()
prices_int = prices.interpolate(method='linear')
prices_int_w = prices_int.groupby(pd.Grouper(freq='W')).last()


mom_long = prices_int_w.pct_change(window_long)
mom_medium = prices_int_w.pct_change(window_medium)
mom_short = prices_int_w.pct_change(window_short)
mom_reversal = prices_int_w.pct_change(1).shift(1)
mom_reversal = mom_reversal [mom_reversal.index>=start]


var_no='26'
mom_reversal.columns =  [i[0] for i in mom_reversal.columns]
mom_reversal = mom_reversal[index_tickers]
mom_reversal.columns = [var_no+'-1_'+i for i in mom_reversal.columns]
# mom_reversal.columns = ['26_rev_US_NY','26_rev_US_SPX','26_rev_US_CCMP', '26_rev_DE','26_rev_UK','26_rev_JP','26_rev_CH_SH','26_rev_CH_SZ', '26_rev_TR','26_rev_MX','26_rev_BR','26_rev_RU','26_rev_SA']


mom_medium.columns =  [i[0] for i in mom_medium.columns]
mom_medium = mom_medium[index_tickers]
mom_medium.columns = [var_no+'-2_'+i for i in mom_medium.columns]
# mom_medium.columns = ['26_med_US_NY','26_med_US_SPX','26_med_US_CCMP', '26_med_DE','26_med_UK','26_med_JP','26_med_CH_SH','26_med_CH_SZ', '26_med_TR','26_med_MX','26_med_BR','26_med_RU','26_med_SA']
mom_medium = mom_medium [mom_medium.index>=start]

mom_long.columns =  [i[0] for i in mom_long.columns]
mom_long = mom_long[index_tickers]
mom_long.columns = [var_no+'-3_'+i for i in mom_long.columns]
# mom_long.columns = ['26_lng_US_NY','26_lng_US_SPX','26_lng_US_CCMP', '26_lng_DE','26_lng_UK','26_lng_JP','26_lng_CH_SH','26_lng_CH_SZ', '26_lng_TR','26_lng_MX','26_lng_BR','26_lng_RU','26_lng_SA']
mom_long = mom_long [mom_long.index>=start]

mom_short.columns =  [i[0] for i in mom_short.columns]
mom_short = mom_short[index_tickers]
mom_short.columns = [var_no+'-4_'+i for i in mom_short.columns]
#♠mom_short.columns = ['26_short_US_NY','26_short_US_SPX','26_short_US_CCMP', '26_short_DE','26_short_UK','26_short_JP','26_short_CH_SH','26_short_CH_SZ', '26_short_TR','26_short_MX','26_short_BR','26_short_RU','26_short_SA']
mom_short = mom_short [mom_short.index>=start]

mom_reversal.to_excel('C:/Users/sb0538/Desktop/15022020/excels/26-1_momreversal.xlsx') 
mom_long.to_excel('C:/Users/sb0538/Desktop/15022020/excels/26-2_momlong.xlsx')
mom_medium.to_excel('C:/Users/sb0538/Desktop/15022020/excels/26-3_mommed.xlsx')
mom_short.to_excel('C:/Users/sb0538/Desktop/15022020/excels/26-4_momshort.xlsx')


