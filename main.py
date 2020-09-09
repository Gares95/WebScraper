# for element in dir():
#     if element[0:2] != "__":
#         del globals()[element]
# del element
from bs4 import BeautifulSoup
import requests
import pandas as pd
#url = 'https://api.scrapingdog.com/scrape?api_key=5ea541dcacf6581b0b4b4042&url=https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch'
url = 'https://finance.yahoo.com/quote/SAN/history?p=SAN'
r = requests.get(url).text
soup = BeautifulSoup(r,"html.parser")
alldata = soup.find_all("tbody", attrs={"data-reactid": "50"})
print (alldata)

myDict = {}
df = pd.DataFrame(columns=['Date', 'Open Value'])

count = 0
for i in alldata[0].find_all("tr"):
    auxTable = i.find_all("td")
    # Because each parameter for this specific webpage 
    # contains only one value we can use the indexes 0 and 1 only
    # myDict[auxTable[0].text] = auxTable[1].text
    df.loc[count] = [auxTable[0].text, auxTable[1].text]
    count +=1
print(myDict)
print(df)
