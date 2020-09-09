from bs4 import BeautifulSoup
import requests
#url = 'https://api.scrapingdog.com/scrape?api_key=5ea541dcacf6581b0b4b4042&url=https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch'
url = 'https://finance.yahoo.com/quote/SAN/history?p=SAN'
r = requests.get(url).text
soup = BeautifulSoup(r,"html.parser")
alldata = soup.find_all("tbody", attrs={"data-reactid": "50"})
print (alldata)

myDict = {}
for tables in alldata:
    count = 0
    #print("table {}, tr: {}". format(tables, tables.find_all("tr"))
    #print(tables.find_all("tr"))
    for i in tables.find_all("tr"):
        count +=1
        auxTable = i.find_all("td")
        # Because each parameter for this specific webpage 
        # contains only one value we can use the indexes 0 and 1 only
        myDict[auxTable[0].text] = auxTable[1].text


# If we want it in dataFrame format
# =============================================================================
# import pandas as pd
# df = pd.DataFrame(list(myDict.items()), columns = ['column1', 'column2'])
# =============================================================================
