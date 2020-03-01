# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 18:00:53 2019

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
firstday='19991230'


pe_ratio_tickers = ['NYA Index', 'SPX Index', 'CCMP Index','NDX Index','CDAX Index' ,'DAX Index', 
            'ASX Index','UKX Index', 'TPX Index','NKY Index', 'SHCOMP Index' , 
           'SZCOMP Index','XUTUM Index','XU100 Index',  'MEXBOL Index', 
           'IBOV Index', 'IMOEX Index' , 'JALSH Index']

pe_ratio = con.bdh(pe_ratio_tickers, 'PE RATIO', firstday , today)

pe_ratio_int = pe_ratio.interpolate(method='linear')
pe_ratio_int_w = pe_ratio_int.groupby(pd.Grouper(freq='W')).last()

pe_ratio_last = pe_ratio_int_w[pe_ratio_int_w.index>=start] 

var_no='13'

pe_ratio_last.columns = [i[0] for i in pe_ratio_last.columns]
pe_ratio_last = pe_ratio_last[pe_ratio_tickers]
pe_ratio_last.columns = [var_no+'_'+i for i in pe_ratio_last.columns]

#pe_ratio_last.columns = ['13_US_NY','13_US_SPX','13_US_CCMP', '13_DE','13_UK','13_JP','13_CH_SH','13_CH_SZ', '13_TR','13_MX','13_BR','13_RU','13_SA']

pe_ratio_last.to_excel('C:/Users/sb0538/Desktop/15022020/excels/13_peratio.xlsx') 

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
#pe_ratio = pd.concat([pe_ratio_nya,pe_ratio_spx, pe_ratio_ccmp,
#                     pe_ratio_cdax ,pe_ratio_asx ,pe_ratio_tpx,
#                     pe_ratio_shcomp,pe_ratio_szcomp,pe_ratio_xutum,pe_ratio_mexbol,
#                     pe_ratio_ibov, pe_ratio_imoex, pe_ratio_jalsh], axis=1)

