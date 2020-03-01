# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 17:33:33 2019

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

vix =  con.bdh( ['VIX Index'], 'PX LAST' , firstday , today)
vix = vix[vix.index>=start]

vix_w = vix.groupby(pd.Grouper(freq='W')).last()
vix_w.columns = ['extra_8_vix']

vix_w.to_excel('C:/Users/sb0538/Desktop/15022020/excels/extra8_vix.xlsx')

