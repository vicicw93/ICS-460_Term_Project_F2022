import yfinance as yf  # https://pypi.org/project/yfinance/


"""
    get_stock_price_by_symbol
        gets the stock price based on symbol passed in from y_finance
        
    ":return: stock price if found, otherwise none
"""
def get_stock_price_by_symbol(symbol):
    if symbol is not None:
        data = yf.Ticker(symbol)
        return data.info['regularMarketPrice']

    return None
