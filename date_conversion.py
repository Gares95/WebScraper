# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 23:52:59 2020

@author: Gares95

This function converts in one line the dates of the dataframe as datetime.
"""

from datetime import datetime
def date_conversion(df):
    dates= []
    for i in df.iloc[:,0]:
        dates.append(datetime.strptime(i, '%b %d, %Y'))
    # print(dates)
    # print(dates[0])
    return dates
