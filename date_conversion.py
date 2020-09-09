# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 23:52:59 2020

@author: guill
"""

from datetime import datetime
def date_conversion(df):
    dates= []
    for i in df.iloc[:,0]:
        dates.append(datetime.strptime(i, '%b %d, %Y'))
    # print(dates)
    # print(dates[0])
    return dates
