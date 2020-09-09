# for element in dir():
#     if element[0:2] != "__":
#         del globals()[element]
# del element

from bs4 import BeautifulSoup
import requests
import pandas as pd
from plotnine import *

import give_me_trend
from date_conversion import date_conversion

#url = 'https://api.scrapingdog.com/scrape?api_key=5ea541dcacf6581b0b4b4042&url=https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch'
url = 'https://finance.yahoo.com/quote/SAN/history?p=SAN'
r = requests.get(url).text
soup = BeautifulSoup(r,"html.parser")
alldata = soup.find_all("tbody", attrs={"data-reactid": "50"})
print (alldata)

# myDict = {}
df = pd.DataFrame(columns=['Date', 'Open Value'])

count = 0
for i in alldata[0].find_all("tr"):
    auxTable = i.find_all("td")
    # Because each parameter for this specific webpage 
    # contains only one value we can use the indexes 0 and 1 only
    df.loc[count] = [auxTable[0].text, auxTable[1].text]
    count +=1
# print(df)
# print(df.iloc[:,1])
# print(type(float(df.iloc[:,1][0])))

df2 = df
df2.iloc[:,1] = pd.to_numeric(df2.iloc[:,1], downcast="float")
df2.iloc[:,0] = date_conversion(df2)
(ggplot(df2)          # defining what data to use
 + aes(x='Date', y = 'Open Value')# defining what variable to use
 + geom_point() # defining the type of plot to use
 + theme(axis_text_x  = element_text(angle = 90, hjust = 1))
)