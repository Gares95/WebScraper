# WebScraper
This project contains a python program that allows the user to explore data obtained from _https://finance.yahoo.com/_ as a _WebScraper_.

The program will obtain from _Yahoo Finance's_ main page the last *closing values* of the top 3 trending *stock market indexes* that you can see in the top of the main page. 

This will return a dataframe with all the data and will display it in different plots.

The aim of this project is not to provide a tool to extract useful information from _yahoo finances_ specifically (there are programs very efficient for that: https://github.com/ranaroussi/yfinance), instead this repository is going to explore the functions of the libraries bs4 and request and how to use them to represent results.

The object of this repository is to serve as a codebase to develop future projects.
An interface for this program is being developed in another repository: https://github.com/Gares95/WebScraperYF-Interface

 Library that the program uses:
 - bs4
 - requests
 - pandas
 - plotnine

### Files used
Files:
 - **main.py**: The python program
 - **main.IPYNB**: Jupyter Notebook with the main program and explanatory text.
 - **date_conversion.py**: This function converts in one line the dates of the dataframe as datetime.
 - **give_me_trend.py**: This function returns top 3 trending stock market indexes from yahoo finance and their urls.
 - **give_me_top3Data.py**: This function returns a Dataframe that contains the close values of the top 3 trending stock market indexes in yahoo finance's main page.
 - **README**: File that contains the description of the functionality of the program and the contents of the files.

### Credits
Work based in model by Manthan Koolwal: https://codeburst.io/how-to-scrape-yahoo-finance-using-python-31164aa06468

