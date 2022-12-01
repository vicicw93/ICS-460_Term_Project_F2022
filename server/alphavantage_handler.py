import requests  # HTTP library https://requests.readthedocs.io/en/latest/
import os  # used to pull in environment variables

# Alphavantage docs - https://www.alphavantage.co/documentation/
API_KEY = os.environ['ALPHAVANTAGE_KEY']


"""
    get_symbol_by_company_name
        This method uses the alphavantage api Seach to lookup a symbol by a company name
    
    :param search_text - company name we will search the api for.
     We filter the list by:
        name - name of the found company
        region - location of where the company is
        type - type of stock
        
    :return symbol of company or None
"""
def get_symbol_by_company_name(search_text):
    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={search_text}&apikey={API_KEY}'
    r = requests.get(url)
    data = r.json()['bestMatches']

    symbol = None
    for ticker in data:
        if search_text.lower() in ticker['2. name'].lower() and\
                (ticker['4. region'] == 'United States') and\
                (ticker['3. type'] == 'Equity'):

            symbol = ticker['1. symbol']
            break

    return symbol
