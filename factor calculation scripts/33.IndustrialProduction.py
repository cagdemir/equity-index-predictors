# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:33:05 2019

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

delta_indprod= delta_indprod[indp_tickers]
delta_indprod.columns = [i[0] for i in delta_indprod.columns]
delta_indprod.columns = indp_tickers


delta_indprod /=100


window = 6
std_ind_prod = delta_indprod.rolling(window).std()


idx_sent = pd.date_range(start=firstday, end=today, freq='D')

std_ind_prod_sent = pd.DataFrame(columns=std_ind_prod .columns,index=idx_sent)
std_ind_prod_sent.update(std_ind_prod)


lag = 16 # in terms of days

std_ind_prod_shifted = std_ind_prod_sent.astype(float).ffill(limit=31).shift(lag)


std_ind_prod_w = std_ind_prod_shifted.groupby(pd.Grouper(freq='W')).last()



std_indprod_last = std_ind_prod_w[std_ind_prod_w.index>=start]

std_indprod_last.columns = ['33_US', '33_GER','33_UK','33_JP','33_CH', '33_TR','33_MX','33_BR','33_RU','33_SA']

std_indprod_last.to_excel('C:/Users/sb0538/Desktop/15022020/excels/33_industrialproductionvol.xlsx') 

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
