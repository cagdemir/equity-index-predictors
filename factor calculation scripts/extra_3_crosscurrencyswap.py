# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 17:28:40 2019

@author: Administrator
"""

import pdblp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()
from datetime import date


start = '20040101'
today = date.today().strftime('%Y%m%d')
firstday = '19991230'



###################################################Germany
swap_spread_de = con.bdh( 'EUSS1 CMPN Curncy', 'PX LAST' , firstday , today) 
#eu : EUSS1 CMPN Curncy , swap-bond spread 
swap_spread_de.names = 'DE'

######################################################UK 
swap_spread_uk = con.bdh( 'BPSP1 CMPN Curncy', 'PX LAST' , firstday , today)
swap_spread_uk.names = 'UK'


######################################################Japan:
swap_spread_jp = con.bdh( 'JYSS1 CMPN Curncy', 'PX LAST' , firstday , today)
swap_spread_jp.names = 'JP'

#####################################################China:


#swap_interest_rate_ch = con.bdh( 'CCUSWO1 BGN Curncy', 'PX LAST' , start , today)
#govt_ch = con.bdh( 'GCNY10YR Index', 'PX LAST' , start , today)

rates_ch =  con.bdh(['GCNY10YR Index','CCUSWO1 BGN Curncy'], 'PX LAST' , firstday , today)

#rates_ch_w = rates_ch.groupby(pd.Grouper(freq='W')).last() 
#rates_ch = rates_ch[rates_ch.index>start]

swap_spread_ch = rates_ch.iloc[:,0] - rates_ch.iloc[:,1].values
swap_spread_ch.names = 'CH'

#CCUSWO1 BGN Curncy , interest rate swap aldık , GOV BOND: GCNY10YR Index



####################################################Turkey
rates_tr = con.bdh( ['TYUSSW1 BGN Curncy','IECM1Y Index'], 'PX LAST' , firstday , today)
#rates_tr = rates_tr[rates_tr.index>start]
#rates_tr_w = rates_tr.groupby(pd.Grouper(freq='W')).last() 

swap_spread_tr = rates_tr.iloc[:,0] - rates_tr.iloc[:,1].values
swap_spread_tr.names = 'TR'

#govt_tr = con.bdh( 'IECM1Y Index', 'PX LAST' , start , today)
#govt_tr_int = govt_ch.interpolate(method= 'linear')
#govt_tr_int_w = govt_tr_int.groupby(pd.Grouper(freq='W')).last() 
#govt_tr_int_w = govt_tr_int_w[govt_tr_int_w.index>start] 


#TYUSSW1 BGN Curncy, interest rate swap , IECM1Y Index


###################################################Mexico
#swap_spread_mx = con.bdh( 'MPSP1 BGN Curncy', 'PX LAST' , start , today) 
#swap_spread_mx.names = 'MX'
#mxn : MPSP1 BGN Curncy , NO DATA 



##################################################Brazil
rates_br = con.bdh( ['BCSCN1Y CMPN Curncy','GTBRL1Y Govt'], 'PX LAST' , firstday , today)
#rates_br_w = rates_br[rates_br.index>start]
#rates_br_w = rates_br.groupby(pd.Grouper(freq='W')).last()

swap_spread_br = rates_br.iloc[:,0] - rates_br.iloc[:,1].values
swap_spread_br.names = 'BR'


#Brazil : BCSCN1Y CMPN Curncy, interest rate swap , GTBRL1Y Govt



#################################################Russia
swap_spread_ru = con.bdh( 'RRUSSW1 BGN Curncy', 'PX LAST' , firstday , today) 
#russia: RRUSSW1 BGN Curncy, spread
swap_spread_ru.names = 'RU'



################################################South Africa
rates_sa = con.bdh( ['SASW1 BGN Curncy','GTZAR10Y Govt'], 'PX LAST' , firstday , today)
#rates_sa_w = rates_sa[rates_sa.index>start]
#rates_sa_w = rates_sa.groupby(pd.Grouper(freq='W')).last()

swap_spread_sa = rates_sa.iloc[:,0] - rates_sa.iloc[:,1].values
swap_spread_sa.names = 'SA'

#South Africa : SASW1 BGN Curncy, interest rate swap aldık, GTZAR10Y GOvt 

swap_spread= pd.concat( [swap_spread_de, swap_spread_uk, swap_spread_jp, swap_spread_ch, swap_spread_tr, swap_spread_br, swap_spread_ru, swap_spread_sa ],axis=1)
swap_spread_int = swap_spread.interpolate(method = 'linear')
swap_spread_int_w = swap_spread_int.groupby(pd.Grouper(freq = 'W')).last()
swap_spread_int_w.columns = [i[0] for i in swap_spread_int_w.columns]
swap_spread_int_w = swap_spread_int_w[swap_spread_int_w.index>=start]


swap_spread_int_w.columns = ['extra3_GER', 'extra3_UK','extra3_JP','extra3_CH','extra3_TR','extra3_BR', 'exta3_RU','extra3_SA']

swap_spread_int_w.to_excel('C:/Users/sb0538/Desktop/15022020/excels/extra3_swapspread.xlsx') 






