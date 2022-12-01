# This service is meant to be the joining file for all other API/Service calls
from alphavantage_handler import get_symbol_by_company_name
from arduino_iot_cloud_handler import publish_stock_to_arduino
from y_finance_handler import get_stock_price_by_symbol


"""
    send_stock_price
        This is the main service function for our API
    
    :param company_name - value passed in from google api
    We get the symbol from the alphavantage api,
    send the symbol to y_finance service to get stock price,
    send stock price and symbol to the Arduino IOT cloud api to display
    
    :returns:
        message_text - text to display in response;
        status_code - code to return in API (200, 404, 500);
"""
def send_stock_price(company_name):
    symbol = get_symbol_by_company_name(company_name)
    if symbol is None:
        return "Unable to find company", 404

    stock_price = get_stock_price_by_symbol(symbol)
    if stock_price is None:
        return "Unable to get stock price", 500

    stock_price_data = f"{symbol}: ${stock_price}"

    # if we made it here, all is good
    # send stock price to arduino
    published = publish_stock_to_arduino(stock_price_data)
    if published:
        return f"Successfully displayed stock price ${stock_price} for {symbol}", 200
    else:
        return "Unable to display stock price", 500
