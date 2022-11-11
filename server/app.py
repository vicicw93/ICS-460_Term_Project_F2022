from flask import Flask, request, redirect, jsonify

app = Flask(__name__)


@app.route("/devices", methods=['POST'])
def devices():
    google_request = request.json
    response = {
        "requestId": google_request['requestId'],
        "payload": {
            "agentUserId": "1836.15267389",
            "devices": [
                {
                    "id": "1",
                    "type": "action.devices.types.TV",
                    "traits": [
                        "action.devices.traits.AppSelector",
                        "action.devices.traits.InputSelector",
                        "action.devices.traits.MediaState",
                        "action.devices.traits.OnOff",
                        "action.devices.traits.TransportControl",
                        "action.devices.traits.Volume"
                    ],
                    "name": {
                        "defaultNames": [
                            "Display"
                        ],
                        "name": "Alex Arduino",
                        "nicknames": [
                            "display"
                        ]
                    },
                    "willReportState": False
                }
            ]
        }}
    return jsonify(response)


@app.route("/auth")
def auth():
    args = request.args
    redirect_url = args.get("redirect_uri")
    state = args.get("state")
    redirect_url = f"{redirect_url}?state={state}&code=ACCESS_TOKEN"
    return redirect(redirect_url)


@app.route("/token", methods=['POST'])
def token():
    token_response = {
        "token_type": "Bearer",
        "access_token": "ACCESS_TOKEN",
        "refresh_token": "REFRESH_TOKEN",
        "expires_in": 10000000
    }
    return jsonify(token_response)


app.run()
