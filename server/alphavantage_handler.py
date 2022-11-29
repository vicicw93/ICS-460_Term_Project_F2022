import requests

API_KEY = 'VX347HPUIGGNOWSE'


def get_symbol_by_company_name(search_text):
    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={search_text}&apikey={API_KEY}'
    r = requests.get(url)
    data = r.json()['bestMatches']

    symbol = None
    for ticker in data:
        if (search_text in ticker['2. name'].lower()) and (ticker['4. region'] == 'United States'):
            symbol = ticker['1. symbol']
            break

    return symbol
