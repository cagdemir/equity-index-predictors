# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 18:23:31 2019

@author: Administrator
"""

import pdblp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')

#con = pdblp.BCon(debug=True, port=8194, timeout=5000)
con = pdblp.BCon(debug=False, port=8194, timeout=50000)
con.start()

from datetime import date


start = '20040101'
today = date.today().strftime('%Y%m%d')
firstday = '19991230'

commodity_tickers = ['SI1 COMB Comdty','GC1 COMDTY','PL1  COMDTY','AA1 COMDTY','ng1 COMDTY','COAL INDEX','CL1 COMDTY',
                    'CO1 COMDTY','LS1 COMDTY', 'W 1 COMDTY', 'C 1 COMDTY', 'KC1 COMDTY','CT1 COMDTY','QW1 COMDTY',]


cmdt_tickers_variable_open = ['cmdt_silver_o','cmdt_gold_o','cmdt_platinum_o','cmdt_nickel_o' ,'cmdt_naturalgas_o',
                        'cmdt_coal_o', 'cmdt_crude_oil_o', 'cmdt_brent_o','cmdt_cattle_o', 'cmdt_wheat_o','cmdt_corn_o','cmdt_coffee_o','cmdt_cotton_o','cmdt_sugar_o']

cmdt_tickers_variable_close = ['cmdt_silver_c','cmdt_gold_c','cmdt_platinum_c','cmdt_nickel_c' ,'cmdt_naturalgas_c',
                        'cmdt_coal_c', 'cmdt_crude_cil_c', 'cmdt_brent_c','cmdt_cattle_c', 'cmdt_wheat_c','cmdt_corn_c','cmdt_coffee_c','cmdt_cotton_c','cmdt_sugar_c']

cmdt_tickers_variable_high = ['cmdt_silver_h','cmdt_gold_h','cmdt_platinum_h','cmdt_nickel_h' ,'cmdt_naturalgas_h',
                        'cmdt_hoal_h', 'cmdt_hrude_hil_h', 'cmdt_brent_h','cmdt_hattle_h', 'cmdt_wheat_h','cmdt_horn_h','cmdt_hoffee_h','cmdt_hotton_h','cmdt_sugar_h']

cmdt_tickers_variable_low = ['cmdt_silver_l','cmdt_gold_l','cmdt_platinum_l','cmdt_nickel_l' ,'cmdt_naturalgas_l',
                        'cmdt_loal_l', 'cmdt_lrude_lil_l', 'cmdt_brent_l','cmdt_lattle_l', 'cmdt_wheat_l','cmdt_lorn_l','cmdt_loffee_l','cmdt_lotton_l','cmdt_sugar_l']


commodity_open = con.bdh (commodity_tickers , 'PX OPEN', firstday, today)
commodity_open.columns = [i[0] for i in commodity_open.columns]
commodity_open = commodity_open[commodity_tickers]
commodity_open.columns = cmdt_tickers_variable_open
commodity_open_int = commodity_open.interpolate(method='linear')
commodity_open_int_w = commodity_open_int.groupby(pd.Grouper(freq='W')).first()


commodity_high = con.bdh (commodity_tickers , 'PX HIGH', firstday, today)
commodity_high.columns = [i[0] for i in commodity_high.columns]
commodity_high = commodity_high[commodity_tickers]
commodity_high.columns = cmdt_tickers_variable_open
commodity_high_int = commodity_high.interpolate(method='linear')
commodity_high_int_w = commodity_high_int.groupby(pd.Grouper(freq='W')).max()


commodity_low = con.bdh (commodity_tickers , 'PX LOW', firstday, today)
commodity_low.columns = [i[0] for i in commodity_low.columns]
commodity_low = commodity_low[commodity_tickers]
commodity_low.columns = cmdt_tickers_variable_open
commodity_low_int = commodity_low.interpolate(method='linear')
commodity_low_int_w = commodity_low_int.groupby(pd.Grouper(freq='W')).min()


commodity_close = con.bdh (commodity_tickers , 'PX LAST', firstday, today)
commodity_close.columns = [i[0] for i in commodity_close.columns]
commodity_close = commodity_close[commodity_tickers]
commodity_close.columns = cmdt_tickers_variable_open
commodity_close_int = commodity_close.interpolate(method='linear')
commodity_close_int_w = commodity_close_int.groupby(pd.Grouper(freq='W')).last()


########################################################################################
#RETURNS FROM CLOSE


return_cmdt_open = commodity_open_int_w / commodity_close_int_w.shift(1) - 1
return_cmdt_high = commodity_high_int_w / commodity_close_int_w.shift(1) - 1
return_cmdt_high.columns = cmdt_tickers_variable_high 
return_cmdt_low = commodity_low_int_w / commodity_close_int_w.shift(1) - 1
return_cmdt_high.columns = cmdt_tickers_variable_low
return_cmdt_close = commodity_close_int_w / commodity_close_int_w.shift(1) - 1
return_cmdt_high.columns = cmdt_tickers_variable_close


returns_cmdt_close_ohlc =  pd.concat([return_cmdt_open, return_cmdt_high, return_cmdt_low, return_cmdt_close],axis=1)

cmdt_tickers_variables = ['cmdt_silver','cmdt_gold','cmdt_platinum','cmdt_nickel' ,'cmdt_naturalgas',
                        'cmdt_coal', 'cmdt_crude_oil', 'cmdt_brent','cmdt_cattle', 'cmdt_wheat','cmdt_corn','cmdt_coffee','cmdt_cotton','cmdt_sugar']

cmdt_ohlc_tickers1 = ['extra_7_1_O','extra_7_1_H','extra_7_1_L', 'extra_7_1_C']
returns_cmdt_close_ohlc.columns =  [('_').join(i) for i in zip(np.repeat(cmdt_ohlc_tickers1,len(cmdt_tickers_variables)),returns_cmdt_close_ohlc.columns)]

returns_cmdt_close_ohlc = returns_cmdt_close_ohlc[returns_cmdt_close_ohlc.index>=start]
returns_cmdt_close_ohlc.to_excel('C:/Users/sb0538/Desktop/15022020/excels/extra6-1_returncommodityclose.xlsx') 


#######################################################################################
##PCT CHANGE
#commodity_open_int_w = cmdt_tickers_variable_open
commodity_close_int_w.columns = cmdt_tickers_variable_close
commodity_high_int_w.columns = cmdt_tickers_variable_high
commodity_low_int_w.columns  = cmdt_tickers_variable_low

commodity_prices = pd.concat([commodity_open_int_w , commodity_high_int_w , commodity_low_int_w , commodity_close_int_w], axis=1)
commodity_prices_pct = commodity_prices.pct_change()
commodity_prices_pct = commodity_prices_pct[commodity_prices_pct.index>=start]

commodity_prices_pct.to_excel('C:/Users/sb0538/Desktop/15022020/excels/extra6-2_pricescommodityclose.xlsx')

