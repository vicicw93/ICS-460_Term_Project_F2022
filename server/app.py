from flask import Flask, request, redirect, jsonify

app = Flask(__name__)


@app.route("/display_stock", methods=['POST'])
def devices():
    request_json = request.json
    stock_ticker = request_json['intent']['params']['company']['original'].split(' ')[-1]
    print(stock_ticker)
    response = {

    }
    return jsonify(response)


app.run()
