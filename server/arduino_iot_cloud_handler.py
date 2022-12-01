# my adds from solution:
# https://forum.arduino.cc/t/setting-and-reading-thing-variables-via-the-python-api/1016744
import os
import iot_api_client as iot
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from iot_api_client.rest import ApiException
from iot_api_client.configuration import Configuration
from openapi_client.rest import ApiException

THING_ID = os.environ['THING_ID']  # ID of the Arduino Device in IOT Cloud
PROPERTY_ID = os.environ['PROPERTY_ID']  # ID of the Arduino Variable
CLIENT_ID = os.environ['CLIENT_ID']  # Client ID generated in Arduino Cloud
CLIENT_SECRET = os.environ['CLIENT_SECRET']  # Client Secret generated in Arduino Cloud

"""
    Makes a call to the Arduino IoT Cloud API and sends the information to the Thing variable for display on the
    OLED. The code on the arduino may need to take the info string and format it for proper display.

    :param: stock_data_string - string to be displayed to the given arduino
    
    :return: True if successful else False
"""
def publish_stock_to_arduino(stock_data_string):
    # gets the token to make arduino call
    auth_token = get_token()

    # configure and instance the API client with our access_token
    client_config = Configuration(host="https://api2.arduino.cc/iot")
    client_config.access_token = auth_token
    client = iot.ApiClient(client_config)

    # Update the Thing variable
    properties = iot.PropertiesV2Api(client)
    property_value = {"value": str(stock_data_string)}
    try:
        # publish properties_v2
        properties.properties_v2_publish(THING_ID, PROPERTY_ID, property_value)
        return True
    except ApiException as e:
        print("Exception when calling PropertiesV2Api->propertiesV2Publish: %s\n" % e)
        return False


"""
    get_token
        Retrieves the oauth token to call arduino api
        
    :return: token - oauth token to be used
"""
def get_token():
    oauth_client = BackendApplicationClient(client_id=CLIENT_ID)
    token_url = "https://api2.arduino.cc/iot/v1/clients/token"

    oauth = OAuth2Session(client=oauth_client)
    token = oauth.fetch_token(
        token_url=token_url,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        include_client_id=True,
        audience="https://api2.arduino.cc/iot"
    )

    # return token
    return token.get("access_token")
