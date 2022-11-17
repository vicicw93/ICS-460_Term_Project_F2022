import yfinance as yf
import requests

API_KEY = 'VX347HPUIGGNOWSE'

search_text = "target corporation"

url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={search_text}&apikey={API_KEY}'
r = requests.get(url)
data = r.json()['bestMatches']

print(data)

symbol = None
for ticker in data:
    if (search_text in ticker['2. name'].lower()) and (ticker['4. region'] == 'United States'):
        symbol = ticker['1. symbol']
        break

if symbol is not None:
    print(symbol)

    data = yf.Ticker(symbol)
    print(data.info['regularMarketPrice'])
