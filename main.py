# for element in dir():
#     if element[0:2] != "__":
#         del globals()[element]
# del element

from bs4 import BeautifulSoup
import requests
#url = 'https://finance.yahoo.com/quote/SAN/history?p=SAN'
#url = 'https://api.scrapingdog.com/scrape?api_key=<your-api-key>&url=https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch'
#url = 'https://api.scrapingdog.com/scrape?api_key=5ea541dcacf6581b0b4b4042&url=https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch'
url = 'https://finance.yahoo.com/quote/SAN/history?p=SAN'
r = requests.get(url).text
soup = BeautifulSoup(r,"html.parser")
alldata = soup.find_all("tbody", attrs={"data-reactid": "50"})
print (alldata)

try:
 table1 = alldata[0].find_all("tr")
except:
 table1=None

l={}
u=list()

for i in range(0,len(table1)):
    try:
        table1_td = table1[i].find_all("td")
    except:
        table1_td = None

    l[table1_td[0].text] = table1_td[1].text
    u.append(l)
    l={}
    
print(u)
