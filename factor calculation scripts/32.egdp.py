# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:32:41 2019

@author: Administrator
"""

import pdblp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()

start = '2006-1-1'

gdp_tickers = ['GDP CHWG Index' ,'GRGDEGDP Index' , 
            'UKGRABMI Index', 'JGDPGDP Index', 'CNGDGDP Index' , 
           'TUGPIGD Index', 'MXGPLEVL Index', 'BZGDQOQ Index', 
           'RUDPGDPN Index','ZARSGDP Index']


gdp=con.bdh( gdp_tickers ,'PX LAST','19991231', '20191212')

gdp = gdp[gdp.index>start]



