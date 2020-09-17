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


trends = give_me_trend()
urls = trends.iloc[:,1]

df = pd.DataFrame(columns=['Date', 'Company'])
for url in urls:
    
    r = requests.get(url).text
    soup = BeautifulSoup(r,"html.parser")
    # alldata = soup.find_all("tbody")
    alldata = soup.find_all("tbody", attrs={"data-reactid": "50"})
    # print (alldata)
    CompName = soup.find("h1", attrs={"class": "D(ib) Fz(18px)"})
    
    # Close Value
    count = 0
    if (df.loc[:,'Date'].empty):
        for i in alldata[0].find_all("tr"):
            auxTable = i.find_all("td")
            # Because each parameter for this specific webpage 
            # contains only one value we can use the indexes 0 and 1 only
            
            # if(df.loc[:,'Date'].empty):    
            df.loc[count] = [auxTable[0].text, auxTable[4].text]
            count +=1
        df.columns= ['Date', CompName.text]
    else:
        dfAux = pd.DataFrame(columns=['Date', CompName.text])
        for i in alldata[0].find_all("tr"):
            auxTable = i.find_all("td")
            
            # if(df.loc[:,'Date'].empty):    
            dfAux.loc[count] = [auxTable[0].text, auxTable[4].text]
            count +=1
        df[CompName.text] = dfAux.iloc[:,1]
    
#df2 = df.copy()
for c in range(len(df.columns)-1):
    df.iloc[:,c+1] = df.iloc[:,c+1].str.replace(',','')
    df.iloc[:,c+1] = df.iloc[:,c+1].str.replace('-','') # Remove empty data
    df.iloc[:,c+1] = pd.to_numeric(df.iloc[:,c+1], downcast="float")  

# =============================================================================
# df.iloc[:,3] = df.iloc[:,3].str.replace(',','')
# df.iloc[:,1:4] = df.iloc[:,1:4].str.replace('-','') # Remove empty data
# df.iloc[:,1:4] = pd.to_numeric(df.iloc[:,1], downcast="float")
# =============================================================================

df.iloc[:,0] = date_conversion(df)

ggplot(df) + \
    aes(x='Date') + \
    geom_line(aes(y=df.columns[1]), color='blue') + \
    geom_line(aes(y=df.columns[2]), color='red') + \
    geom_line(aes(y=df.columns[3]), color='green') + \
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