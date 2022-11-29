import yfinance as yf


def get_stock_price_by_symbol(symbol):
    if symbol is not None:
        data = yf.Ticker(symbol)
        return data.info['regularMarketPrice']

    return None
