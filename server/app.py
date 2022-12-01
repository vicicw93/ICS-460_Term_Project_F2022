from flask import Flask, request, json, Response
from service import send_stock_price

app = Flask(__name__)


@app.route("/display_stock", methods=["POST"])
def devices():
    request_json = request.json
    company_name = request_json["intent"]["params"]["company"]["original"]

    response_message, response_status = send_stock_price(company_name)
    response = {
        "message": response_message
    }

    return Response(
        response=json.dumps(response),
        status=response_status,
        mimetype='application/json'
    )


app.run()
