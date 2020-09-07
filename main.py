#clear()
#del r
#install bs4

from bs4 import BeautifulSoup
import requests
#r = requests.get('https://finance.yahoo.com/quote/SAN/history?p=SAN')
#r.status_code
#b'Python is a programming language' in r.content
url = 'https://finance.yahoo.com/quote/SAN/history?p=SAN'
response = requests.get(url, timeout=10)
content = BeautifulSoup(response.content, "html.parser")
print(content)

FinanceData = content.find('tr', attrs={"class": "BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)"}).text
print (FinanceData)
