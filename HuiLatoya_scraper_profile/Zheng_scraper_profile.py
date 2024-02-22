import json
import csv
import sys
from typing import Any, Dict
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_data(ticker_symbol: str) -> Dict[str, Any]:
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

  r = requests.get(url) #will add timeout here
  soup = BeautifulSoup(r.text, 'html.parser')

  stock = {
    # scraping the stock data from the price indicators
    'symbol': ticker_symbol,
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

def get_profile(ticker_symbol: str) -> Dict[str, Any]:
  headers = {
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:122.0) Gecko/20100101Firefox/122.0'}
  url = f'https://finance.yahoo.com/quote/{ticker_symbol}/profile'

  r = requests.get(url, headers=headers) #will add timeout here
  executive_df = pd.read_html(r.text)[0]
  soup = BeautifulSoup(r.text, 'html.parser')
  profile_info = {
      'symbol': ticker_symbol,
      'StockName': soup.find('h1', {"class": "D(ib) Fz(18px)"}).text.strip(),
      'Address': '; '.join([x.text for x in soup.find('p', {'class':'D(ib) W(47.727%) Pend(40px)'}).children]),
      'Description': soup.find('p', {'class': 'Mt(15px) Lh(1.6)'}).text.strip()
  }
  for i, name in enumerate(executive_df['Name'].tolist()):
    profile_info[f'Executive{i+1}'] = name
  return profile_info

# Check if ticker symbols are provided as command line arguments 
if len(sys.argv) < 2:     
  print("Usage: python script.py <ticker_symbol1> <ticker_symbol2> ...")     
  sys.exit(1)  
# Extract ticker symbols from command line arguments 
ticker_symbols = sys.argv[1:] 

#get stock data
stockdata = [get_data(symbol) for symbol in ticker_symbols] 

# get profile data
profile_info = get_profile('TSLA')

#save profile data to  CSV file
profile_df = pd.DataFrame([profile_info])
profile_df.to_csv('profile_info.csv', index=False)

# save profile data to JSON file
with open('profile_info.json', 'w') as f:
    json.dump(profile_info, f, indent=4)

# save profile data to  Excel file
profile_df.to_excel('profile_info.xlsx', index=False)
 

print('Done!')
