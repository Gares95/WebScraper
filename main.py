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
CompName = soup.find("h1", attrs={"class": "D(ib) Fz(18px)"})


df = pd.DataFrame(columns=['Date', 'Close Value'])
# Close Value
count = 0
for i in alldata[0].find_all("tr"):
    auxTable = i.find_all("td")
    # Because each parameter for this specific webpage 
    # contains only one value we can use the indexes 0 and 1 only
    df.loc[count] = [auxTable[0].text, auxTable[4].text]
    count +=1

df2 = df.copy()
df2.iloc[:,1] = pd.to_numeric(df2.iloc[:,1], downcast="float")
df2.iloc[:,0] = date_conversion(df2)
(ggplot(df2)          # defining what data to use
 + aes(x='Date', y = 'Close Value')# defining what variable to use
 + geom_point() # defining the type of plot to use
 + ggtitle(CompName.text)
 + theme(axis_text_x  = element_text(angle = 90, hjust = 1))
)

(ggplot(df2)          # defining what data to use
 + aes(x='Date', y = 'Close Value')# defining what variable to use
 + geom_path() # defining the type of plot to use
 + title("Hi There")
 + ylim (2, 2.4)
 + xlim (fst, scd)
 # + scale_y_log10()T
 + theme(axis_text_x  = element_text(angle = 90, hjust = 1))
)