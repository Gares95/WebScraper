# for element in dir():
#     if element[0:2] != "__":
#         del globals()[element]
# del element

from bs4 import BeautifulSoup
import requests
import pandas as pd
from plotnine import *

from give_me_trend import give_me_trend
from date_conversion import date_conversion
from give_me_top3Data import give_me_top3data

trends = give_me_trend()
urls = trends.iloc[:,1]
top3Table = give_me_top3data(urls)

ggplot(top3Table) + \
    aes(x='Date') + \
    geom_line(aes(y=top3Table.columns[1]), color='blue') + \
    geom_line(aes(y=top3Table.columns[2]), color='red') + \
    geom_line(aes(y=top3Table.columns[3]), color='green') + \
    ggtitle("Close value") + \
    theme(axis_text_x  = element_text(angle = 90, hjust = 1))
    
# =============================================================================
# ggplot(df) + \
#     aes(x='Date', y = df.columns[1]) + \
#     geom_path() + \
#     ggtitle("Close value") + \
#     theme(axis_text_x  = element_text(angle = 90, hjust = 1))
# =============================================================================

# =============================================================================
# ggplot(df) + \
#     aes(x='Date', y = 'Close Value') + \
#     geom_path() + \
#     ggtitle(CompName.text) + \
#     theme(axis_text_x  = element_text(angle = 90, hjust = 1))
# =============================================================================

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