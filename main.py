#clear()
#del r
#install bs4

from bs4 import BeautifulSoup
import requests
# =============================================================================
# #r = requests.get('https://finance.yahoo.com/quote/SAN/history?p=SAN')
# #r.status_code
# #b'Python is a programming language' in r.content
# url = 'https://finance.yahoo.com/quote/SAN/history?p=SAN'
# response = requests.get(url, timeout=10)
# content = BeautifulSoup(response.content, "html.parser")
# print(content)
# 
# FinanceData = content.find('tr', attrs={"class": "BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)"}).text
# print (FinanceData)
# =============================================================================
#url = 'https://finance.yahoo.com/quote/SAN/history?p=SAN'
url = 'https://api.scrapingdog.com/scrape?api_key=<your-api-key>&url=https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch'
r = requests.get(url).text
soup = BeautifulSoup(r,"html.parser")
alldata = soup.find_all("tbody")

try:
 table1 = alldata[0].find_all("tr")
except:
 table1=None
 
try:
 table2 = alldata[1].find_all("tr")
except:
 table2 = None

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

for i in range(0,len(table2)):
    try:
        table2_td = table2[i].find_all("td")
    except:
        table2_td = None

    l[table2_td[0].text] = table2_td[1].text
    u.append(l)
    l={}
    
print(u)
