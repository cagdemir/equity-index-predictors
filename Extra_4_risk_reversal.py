# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 18:02:50 2019

@author: Administrator
"""

import pdblp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')

#con = pdblp.BCon(debug=True, port=8194, timeout=5000)
con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()

from datetime import date


start = '20040101'
today = date.today().strftime('%Y%m%d')
firstday = '19991230'

usd_eur_v1m = con.bdh('EURUSDV1M BGN Curncy', 'PX LAST', firstday, today)
usd_eur_25r = con.bdh('EURUSD25R1M BGN Curncy', 'PX LAST', firstday, today)


usd_gbp_v1m = con.bdh('GBPUSDV1M BGN Curncy', 'PX LAST', firstday, today)
usd_gbp_25r = con.bdh('GBPUSD25R1M BGN Curncy', 'PX LAST', firstday, today)


usd_jpy_v1m  = con.bdh('USDJPYV1M BGN Curncy', 'PX LAST', firstday, today)
usd_jpy_25r = con.bdh('USDJPY25R1M BGN Curncy', 'PX LAST', firstday, today)


usd_cny_v1m  = con.bdh('USDCNYV1M BGN Curncy', 'PX LAST', firstday, today)
usd_cny_25r = con.bdh('USDCNY25R1M BGN Curncy', 'PX LAST', firstday, today)

usd_try_v1m  = con.bdh('USDTRYV1M BGN Curncy', 'PX LAST', firstday, today)
usd_try_25r = con.bdh('USDTRY25R1M BGN Curncy', 'PX LAST', firstday, today)

#usd/try 1 month a the money option volatility, 3M, 6M var , USDTRY25R1M


usd_mxn_v1m  = con.bdh('USDMXNV1M BGN Curncy', 'PX LAST', firstday, today)
usd_mxn_25r = con.bdh('USDMXN25R1M BGN Curncy', 'PX LAST', firstday, today)


usd_brl_v1m  = con.bdh('USDBRLV1M BGN Curncy', 'PX LAST', firstday, today)
usd_brl_25r = con.bdh('USDBRL25R1M BGN Curncy', 'PX LAST', firstday, today)



usd_rub_v1m  = con.bdh('USDRUBV1M BGN Curncy', 'PX LAST', firstday, today)
usd_rub_25r = con.bdh('USDRUB25R1M BGN Curncy', 'PX LAST', firstday, today)


usd_zar_v1m  = con.bdh('USDZARV1M BGN Curncy', 'PX LAST', firstday, today)
usd_zar_25r = con.bdh('USDZAR25R1M BGN Curncy', 'PX LAST', firstday, today)

#######################################
reversals_v1m = pd.concat([ usd_eur_v1m, usd_gbp_v1m ,usd_jpy_v1m ,usd_cny_v1m ,usd_try_v1m , usd_mxn_v1m, usd_brl_v1m, usd_rub_v1m , usd_zar_v1m],axis=1)
reversals_v1m = reversals_v1m.interpolate(method='linear')
reversals_v1m_w = reversals_v1m.groupby(pd.Grouper(freq='W')).last()
reversals_v1m_w.columns = [i[0] for i in reversals_v1m_w.columns]
reversals_v1m_w.columns = ['extra4-1_usdeur', 'extra4-1_usdgbp','extra4-1_usdjpy','extra4-1_usdcny' ,'extra4-1_usdtry','extra4-1_usdmxn','extra4-1_usdbrl','extra4-1_usdrub','extra4-1_usdzar']
reversals_v1m_w = reversals_v1m_w[reversals_v1m_w.index>=start]

reversals_25r  = pd.concat([usd_eur_25r ,usd_gbp_25r,usd_jpy_25r ,usd_cny_25r ,usd_try_25r , usd_mxn_25r, usd_brl_25r, usd_rub_25r , usd_zar_25r],axis=1)
reversals_25r = reversals_25r.interpolate(method='linear')
reversals_25r_w = reversals_25r.groupby(pd.Grouper(freq='W')).last()
reversals_25r_w.columns = [i[0] for i in reversals_25r_w.columns ]
reversals_25r_w.columns = ['extra4-2_usdeur', 'extra4-2_usdgbp','extra4-2_usdjpy','extra4-2_usdcny' ,'extra4-2_usdtry','extra4-2_usdmxn','extra4-2_usdbrl','extra4-2_usdrub','extra4-2_usdzar']
reversals_25r_w = reversals_25r_w [reversals_25r_w.index>=start]

reversals_v1m_w.to_excel('C:/Users/sb0538/Desktop/15022020/excels/extra4-1_riskreversalv1m.xlsx') 
reversals_25r_w.to_excel('C:/Users/sb0538/Desktop/15022020/excels/extra4-2_riskreversalv25r.xlsx') 















