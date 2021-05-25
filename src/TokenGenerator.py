import random
from hashlib import sha256
from pprint import pprint
import time
import requests
import json


def fetch_otp(count):
    print(count)
    count += 1
    if count == 10:
        raise TimeoutError
    # url = "http://127.0.0.1:5000/broadcast_otp"
    url = "http://52.172.236.68:8080/broadcast_otp"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    if data['otp'] is not None:
        return data
    time.sleep(1)
    return fetch_otp(count)


class TokenGenerator:
    def __init__(self, mobile):
        # self.otp = sha256(fetch_otp(0)['otp'].encode('utf-8')).hexdigest()
        self.mobile = mobile
        self.txn_id = None
        self.token = None
        self.user_agents = [
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
             (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
             (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36\
             (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        ]

    def generate_otp(self):
        # url = "https://cdn-api.co-vin.in/api/v2/auth/public/generateOTP"
        # payload = "{\n    \"mobile\": \"" + self.mobile + "\"\n}"
        url = "https://cdn-api.co-vin.in/api/v2/auth/generateMobileOTP"
        payload = {
            "mobile": self.mobile,
            "secret": "U2FsdGVkX1+z/4Nr9nta+2DrVJSv7KS6VoQUSQ1ZXYDx/CJUkWxFYG6P3iM/VW+6jLQ9RDQVzp/RcZ8kbT41xw=="
        }
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': self.user_agents[random.randint(0, 2)]
        }

        response = requests.request(
            method="POST",
            url=url,
            headers=headers,
            data=json.dumps(payload)
        )

        pprint(response.text)
        self.txn_id = response.json()['txnId']

    def confirm_otp(self):
        print("fetching otp...")
        otp = sha256(fetch_otp(0)['otp'].encode('utf-8')).hexdigest()
        # url = "https://cdn-api.co-vin.in/api/v2/auth/public/confirmOTP"
        # payload = '{\n    \"otp\": \"' + otp + '\",\n    \"txnId\": \"' + self.txn_id + '\"\n}'
        url = "https://cdn-api.co-vin.in/api/v2/auth/validateMobileOtp"
        payload = {
            "otp": otp,
            "txnId": self.txn_id
        }
        headers = {
            'Content-Type': 'application/json',
            "User-Agent": self.user_agents[random.randint(0, 2)]
        }

        response = requests.request(
            method="POST",
            url=url,
            headers=headers,
            data=json.dumps(payload)
        )

        pprint(response.text)
        self.token = response.json()['token']
