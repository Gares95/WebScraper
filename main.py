# for element in dir():
#     if element[0:2] != "__":
#         del globals()[element]
# del element

from bs4 import BeautifulSoup
import requests
import pandas as pd
from plotnine import *

from give_me_trend import give_me_trend
# from date_conversion import date_conversion
from give_me_top3Data import give_me_top3data

trends = give_me_trend()
urls = trends.iloc[:,1]
top3Table = give_me_top3data(urls)

top3TableM = pd.melt(top3Table, id_vars = 'Date', value_vars=[top3Table.columns[1], top3Table.columns[2], top3Table.columns[3]])
top3TableM

top1 = top3TableM[top3TableM['variable']==top3Table.columns[1]]
top2 = top3TableM[top3TableM['variable']==top3Table.columns[2]]
top3 = top3TableM[top3TableM['variable']==top3Table.columns[3]]
    
ggplot(top1) + \
    aes(x='Date', y = 'value') + \
    geom_path() + \
    ylab("Close value") + \
    ggtitle(top1['variable'][0])

ggplot(top3TableM) + \
    aes(x='Date') + \
    geom_line(aes(y=top3TableM.value, color=top3TableM.variable)) + \
    ggtitle("Close value")
    
# ===================adjusting axis============================================
# ggplot(df) + \
#     aes(x='Date', y = 'Close Value') + \
#     geom_path() + \
#     title(CompName.text) + \
#     ylim (2, 2.4) + \
#     xlim (fst, scd) + \
#     scale_y_log10() + \
#     theme(axis_text_x  = element_text(angle = 90, hjust = 1))
# =============================================================================