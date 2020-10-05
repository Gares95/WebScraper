# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 14:47:03 2020

@author: Gares95

This function returns a Dataframe that contains the close values of the top 3
trending stock market indexes in yahoo finance's main page.

"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

from date_conversion import date_conversion

def give_me_top3data(listOfUrls):
    df = pd.DataFrame(columns=['Date', 'Company'])
    for url in listOfUrls:
        
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
        
    for c in range(len(df.columns)-1):
        df.iloc[:,c+1] = df.iloc[:,c+1].str.replace(',','')
        df.iloc[:,c+1] = df.iloc[:,c+1].str.replace('-','') # Remove empty data
        df.iloc[:,c+1] = pd.to_numeric(df.iloc[:,c+1], downcast="float")  
        
    df.iloc[:,0] = date_conversion(df)
    # df = pd.melt(df, id_vars = 'Date', value_vars=[df.columns[1], df.columns[2], df.columns[3]])
    return df
