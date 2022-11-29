# This service is meant to be the joining file for all other API/Service calls
from alphavantage_handler import get_symbol_by_company_name
from y_finance_handler import get_stock_price_by_symbol


# function meant to be
def send_stock_price(company_name):
    symbol = get_symbol_by_company_name(company_name)
    if symbol is None:
        return "Unable to find company", 404

    stock_price = get_stock_price_by_symbol(symbol)
    if stock_price is None:
        return "Unable to get stock price", 500

    # if we made it here, all is good
    # send stock price to arduino
    return f"Successfully displayed stock price {stock_price} for {symbol}", 200
