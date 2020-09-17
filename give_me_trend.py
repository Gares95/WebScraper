# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 18:15:28 2020

@author: guill

This function returns top 3 trending companies from yahoo finance
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd
def give_me_trend():
    
    baseUrl = 'https://finance.yahoo.com/'
    r = requests.get(baseUrl).text
    soup = BeautifulSoup(r,"html.parser")
    # top5 = soup.find_all("div", attrs={"id": "market-summary"})
    # auxBlocks = top5[0].find_all("li")
    top5 = soup.find("div", attrs={"id": "market-summary"})
    auxBlocks = top5.find_all("li")
    TrendingUrl = {}
    for block in auxBlocks:
        auxBlocksA = block.find_all("a", attrs={"class": "Fz(s) Ell Fw(600) C($linkColor)"})    
        TrendingUrl[auxBlocksA[0].text] = baseUrl + "/history?".join(auxBlocksA[0].get('href').split("?"))  
    
    df = pd.DataFrame(list(TrendingUrl.items()), columns = ['column1', 'column2'])
    return df
