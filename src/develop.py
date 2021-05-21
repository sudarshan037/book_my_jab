import json
from pprint import pprint

import requests

user_agents = [
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
     (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
     (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36\
     (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
]


def get_user_details():
    with open("../data/token.json") as token_file:
        token = json.load(token_file)

    url = "https://cdn-api.co-vin.in/api/v2/appointment/beneficiaries"
    # headers = {
    #     "User-Agent": user_agents[random.randint(0, 2)],
    #     "Authorization": f"Bearer {token}"
    # }
    headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    payload = {}
    pprint(headers)
    response = requests.request("GET", url, headers=headers, data=payload)
    pprint(response.text)


if __name__ == "__main__":
    get_user_details()
