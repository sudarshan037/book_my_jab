import traceback
from json import JSONDecodeError
from pprint import pprint
from time import time

from flask import Flask, request

app = Flask(__name__)

payload = {
    "otp": None,
    "time": None
}


@app.route("/broadcast_otp")
def send():
    if payload['otp'] is not None and round(time(), 2) - payload['time'] < 10:
        print("sending response with: ", payload)
        return payload
    else:
        return {
            "otp": None,
            "time": None
        }


@app.route("/catch_otp", methods=['POST'])
def get_pin():
    try:
        global payload
        payload['otp'] = request.json['OTP']
        payload['time'] = round(time(), 2)
        pprint(payload)
        return payload
    except JSONDecodeError:
        traceback.print_exc()
        return {
            "result": "Error Encountered"
        }


if __name__ == '__main__':
    #app.run(debug=True)
     app.run(host='0.0.0.0', port=8080, debug=True)
