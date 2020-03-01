# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:17:09 2019

@author: Administrator
"""

import pdblp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import datetime as dt


def date_to_str(dt_object):
    return  [dt.datetime.strftime(i,"%Y%m%d") for i in dt_object]

def bulk_data_reader(df,index):
    
    list_idx =  date_to_str(index)
    
    
    
    
    
    

#con = pdblp.BCon(debug=True, port=8194, timeout=5000)
con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()


indices = ['NYA Index', 'CCMP Index' ,'CDAX Index' , 
            'ASX Index', 'TPX Index', 'SHCOMP Index' , 
           'SZCOMP Index', 'XUTUM Index', 'MEXBOL Index', 
           'IBOV Index', 'IMOEX Index' , 'JALSH Index']


#INDX MOST DOWN
#INDX MOST UP
#BETA ROW OVERRIDABLE
#BS TOT ASSET


#svar = con.bdh('SPX Index', ['INDX MOST DOWN' ], '19991231', '20191128')

start = '20060101' 
end = '20191211'

price_spx = con.bdh('SPX Index', 'PX LAST', start, end)

df_down = pd.DataFrame(index = price_spx.index, columns = list(range(10)))
df_up = pd.DataFrame(index = price_spx.index, columns = list(range(10)))

dates_spx = []
price_spx.groupby(pd.Grouper(freq='W')).apply(lambda x: dates_spx.append(x.index))





a = con.bulkref_hist('SPX Index', 'INDX MOST DOWN', '20191109')
a = con.bulkref_hist('SPX Index', 'INDX MOST DOWN', ['20181109','20191110'])
a = con.bulkref_hist('SPX Index', 'INDX MOST DOWN', ['201811','201911'])
a = con.bulkref_hist('SPX Index', 'INDX MOST DOWN', ['2018','2019'])
