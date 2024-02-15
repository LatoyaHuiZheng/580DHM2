import bs4 as bs
import requests
# prompt: Write a python script to scrape stock price movement in the US stock market on this webpage: https://finance.yahoo.com/quote/TSLA/holders

url = 'https://finance.yahoo.com/quote/TSLA'
res = requests.get(url)

import pandas as pd
from bs4 import BeautifulSoup
from IPython.core.display import HTML
from html import escape
import json
# HTML(str(res.content).replace('\\n', '\n'))

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7; AppleWebKit/537.36) Gecko/121.0.0.0 Safari/537.36'}   
url = f'https://finance.yahoo.com/quote/TSLA'

# Make a request to the URL
r = requests.get(url) #will add timeout here
soup = BeautifulSoup(r.text, 'html.parser')
# regularMarketPrice = soup.find('fin-streamer', {'class':'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text.strip()
# regularMarketChange= soup.find('fin-streamer', {'class':'Fw(500) Pstart(8px) Fz(24px)'}).text.strip()
# regularMarketChangePercent = soup.find('fin-streamer', {'class':'Fw(500) Pstart(8px) Fz(24px)'}).text.strip()

regularMarketPrice = soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text.strip()
regularMarketChange = soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text.strip()
regularMarketChangePercent = soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text.strip()

print(regularMarketPrice, regularMarketChange, regularMarketChangePercent)


# scraping the stock data from the "Summary" table
previous_close = soup.find('table', {'class':'W(100%)'}).find_all('td')[1].text.strip()
open_value= soup.find('table', {'class':'W(100%)'}).find_all('td')[3].text.strip()
bid= soup.find('table', {'class':'W(100%)'}).find_all('td')[5].text.strip()
ask= soup.find('table', {'class':'W(100%)'}).find_all('td')[7].text.strip()
days_range= soup.find('table', {'class':'W(100%)'}).find_all('td')[9].text.strip()
week_range= soup.find('table', {'class':'W(100%)'}).find_all('td')[11].text.strip()
volume= soup.find('table', {'class':'W(100%)'}).find_all('td')[13].text.strip()
avg_volume= soup.find('table', {'class':'W(100%)'}).find_all('td')[5].text.strip()
market_cap= soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[1].text.strip()
beta= soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[3].text.strip()
pe_ratio= soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[5].text.strip()
eps= soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[7].text.strip()
earnings_date= soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[9].text.strip()
dividend_yield= soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[11].text.strip()
ex_dividend_date= soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[13].text.strip()
year_target_est= soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[15].text.strip()
stock = {
 # scraping the stock data from the price indicators
 'stock_name': soup.find('div', {'class':'D(ib) Mt(-5px) Maw(38%)--tab768 Maw(38%) Mend(10px) Ov(h) smartphone_Maw(85%) smartphone_Mend(0px)'}).find_all('div')[0].text.strip(),
 'regularMarketPrice': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text.strip(),
 'regularMarketChange': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text.strip(),
 'regularMarketChangePercent': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text.strip(),
 'quote': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('span')[2].text.strip(),

 # scraping the stock data from the "Summary" table
 'previous_close': soup.find('table', {'class':'W(100%)'}).find_all('td')[1].text.strip(),
 'open_value': soup.find('table', {'class':'W(100%)'}).find_all('td')[3].text.strip(),
 'bid': soup.find('table', {'class':'W(100%)'}).find_all('td')[5].text.strip(),
 'ask': soup.find('table', {'class':'W(100%)'}).find_all('td')[7].text.strip(),
 'days_range': soup.find('table', {'class':'W(100%)'}).find_all('td')[9].text.strip(),
 'week_range': soup.find('table', {'class':'W(100%)'}).find_all('td')[11].text.strip(),
 'volume': soup.find('table', {'class':'W(100%)'}).find_all('td')[13].text.strip(),
 'avg_volume': soup.find('table', {'class':'W(100%)'}).find_all('td')[5].text.strip(),
 'market_cap': soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[1].text.strip(),
 'beta': soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[3].text.strip(),
 'pe_ratio': soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[5].text.strip(),
 'eps': soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[7].text.strip(),
 'earnings_date': soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[9].text.strip(),
 'dividend_yield': soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[11].text.strip(),
 'ex_dividend_date': soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[13].text.strip(),
 'year_target_est': soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[15].text.strip(),
}
print(json.dumps(stock, indent=2))

import json
import csv
import sys
from typing import Any, Dict
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_data(ticker_symbol: Any) -> Dict[str, Any]:
  """
  Get stock data for a given ticker symbol from Yahoo Finance.
  Parameters:
  - ticker_symbol (Any): Ticker symbol of the stock.
  Returns:
  - Dict[str, Any]: Dictionary containing stock data.
  """
  print('Getting stock data of ', ticker_symbol)

  # Set user agent to avoid detection as a scraper
  headers = {
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:122.0) Gecko/20100101Firefox/122.0'}
  url = f'https://finance.yahoo.com/quote/{ticker_symbol}'

  r = requests.get(url, headers=headers) #will add timeout here
  soup = BeautifulSoup(r.text, 'html.parser')

  stock = {
    # scraping the stock data from the price indicators
    'stock_name': soup.find('div', {'class':'D(ib) Mt(-5px) Maw(38%)--tab768 Maw(38%) Mend(10px) Ov(h) smartphone_Maw(85%) smartphone_Mend(0px)'}).find_all('div')[0].text.strip(),
    'regularMarketPrice': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text.strip(),
    'regularMarketChange': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text.strip(),
    'regularMarketChangePercent': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text.strip(),
    'quote': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('span')[2].text.strip(),

    # scraping the stock data from the "Summary" table
    'previous_close': soup.find('table', {'class':'W(100%)'}).find_all('td')[1].text.strip(),
    'open_value': soup.find('table', {'class':'W(100%)'}).find_all('td')[3].text.strip(),
    'bid': soup.find('table', {'class':'W(100%)'}).find_all('td')[5].text.strip(),
    'ask': soup.find('table', {'class':'W(100%)'}).find_all('td')[7].text.strip(),
    'days_range': soup.find('table', {'class':'W(100%)'}).find_all('td')[9].text.strip(),
    'week_range': soup.find('table', {'class':'W(100%)'}).find_all('td')[11].text.strip(),
    'volume': soup.find('table', {'class':'W(100%)'}).find_all('td')[13].text.strip(),
    'avg_volume': soup.find('table', {'class':'W(100%)'}).find_all('td')[5].text.strip(),
    'market_cap': soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[1].text.strip(),
    'beta': soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[3].text.strip(),
    'pe_ratio': soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[5].text.strip(),
    'eps': soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[7].text.strip(),
    'earnings_date': soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[9].text.strip(),
    'dividend_yield': soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[11].text.strip(),
    'ex_dividend_date': soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[13].text.strip(),
    'year_target_est': soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[15].text.strip(),
  }
  return stock

get_data('TSLA')

# Check if ticker symbols are provided as command line arguments 
if len(sys.argv) < 2:     
    print("Usage: python script.py <ticker_symbol1> <ticker_symbol2> ...")     
    sys.exit(1)  
# Extract ticker symbols from command line arguments 
ticker_symbols = sys.argv[1:]  
# Get stock data for each ticker symbol 
stockdata = [get_data(symbol) for symbol in ticker_symbols]  

# Writing stock data to a JSON file 
with open('stock_data.json', 'w', encoding='utf-8') as f:     
    json.dump(stockdata, f)  
    # Writing stock data to a CSV file with aligned values 
CSV_FILE_PATH = 'stock_data.csv' 
with open(CSV_FILE_PATH, 'w', newline='', encoding='utf-8') as csvfile: 
    fieldnames = stockdata[0].keys()     
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')     
    writer.writeheader()     
    writer.writerows(stockdata)  
# Writing stock data to an Excel file 
EXCEL_FILE_PATH = 'stock_data.xlsx' 
df = pd.DataFrame(stockdata) 
df.to_excel(EXCEL_FILE_PATH, index=False)  
print('Done!') 