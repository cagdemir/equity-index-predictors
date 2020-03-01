# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:33:42 2019

@author: Administrator
"""


import pdblp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import date


start = '20040101'
today = date.today().strftime('%Y%m%d')
firstday = '19991230'


con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()


indp_tickers = ['IP CHNG Index' ,'GRIPIMOM Index' , 
            'UKIPIMOM Index', 'JNIPMOM Index', 'CHVAIOM Index' , 
           'TUIOIMOM Index', 'MXPSTMOM Index', 
           'BZIPTL% Index','RUIPWSMM Index','SFPMMOM Index' ]

delta_indprod = con.bdh(indp_tickers, ['PX LAST'], firstday , today)

delta_indprod /=100



idx_sent = pd.date_range(start=firstday, end=today, freq='D')

delta_indprod_sent = pd.DataFrame(columns=delta_indprod.columns,index=idx_sent)
delta_indprod_sent.update(delta_indprod)


lag = 16 # in terms of days

delta_indprod_shifted = delta_indprod_sent.astype(float).ffill(limit=31).shift(lag)


delta_indprod_last = delta_indprod_shifted.groupby(pd.Grouper(freq='W')).last()


delta_indprod_last.columns = [i[0] for i in delta_indprod_last.columns ]

delta_indprod_last = delta_indprod_last[indp_tickers]

delta_indprod_last=delta_indprod_last[delta_indprod_last.index>=start]


delta_indprod_last.columns = ['35_US', '35_GER','35_UK','35_JP','35_CH', '35_TR','35_MX','35_BR','35_RU','35_SA']

delta_indprod_last.to_excel('C:/Users/sb0538/Desktop/15022020/excels/35_deltaindustrialproduction.xlsx') 

#us:      IP Index
#germany: GRIPI Index
#england: UKIPI Index
#japan:   JNIP Index
#china:   CHVAIOY Index
#turkey:  TUIOIYOY Index
#mexico:  'MXIPTYOY Index
#brazil: BZIPTLYO Index
#russia:
#south africa: ECOIZAN-NSA ECOIZAS-SA





















 
