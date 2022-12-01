# Installation and Use Guide
## Startup Notes
 - You should be familiar with the following before getting started:
    - Arduino / Arduino IOT Cloud
        - https://cloud.arduino.cc/home/
        - You will need to have a device setup, a variable, and paid for a secret for API Access
        - This application provides default code from Arduino IOT cloud. It is mostly copy and paste
            - Your Arduino code will likely look different, but this code interacts with the OLED Display
    - Socket XP
        - https://portal.socketxp.com/#/home
        - You will need to download the client and setup via their docs
    - Google Actions Console
        - https://console.actions.google.com/
        - Getting deprecated in near future
        - You will need to create a custom action that will send a web socket request
        - This request should be a stock company name like 'Microsoft'

## Installation
 - Download files
 - Run `pip install` to install required python libraries
 - Setup Environment variables:
    - CLIENT_SECRET - Client Secret Generated from Arduino IOT Cloud
    - CLIENT_ID - Client ID from Arduino IOT Cloud
    - THING_ID - This will be the device id of your Arduino Device
    - PROPERTY_ID - This will be your property ID in Arduino IOT Cloud
    - ALPHAVANTAGE_KEY - get this from signing up with AlphaVantage

## Start python app.py file
 - Run the app.py file, this should start a server on `http://127.0.0.1:5000`

## Start SocketXP
 - In directory where SocketXP was installed, run `./socketxp connect http://127.0.0.1:5000`
 - This will provide a web address like `https://ics460iot-lm489e51mb3d0lk4.socketxp.com`
 - This is the URL you need to provide to the google actions console web socket
 
## Testing
 - You can test without the google actions console with this JSON from the test.json file
 - You can make a This POST call:
    - curl --request POST \
    --url https://ics460iot-lm489e51mb3d0lk4.socketxp.com/display_stock \
    --header 'Content-Type: application/json' \
    --data ''
    
    - Note, put the JSON from in the --data '' section from the test file
    - Note, replace the url with `your custom url/display_stock`
 - If you setup everything from Arduino IOT Cloud and your personal IOT device, this should display
 `MSFT: $255.14` on your device
