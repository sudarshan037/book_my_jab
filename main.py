import json
from pprint import pprint

import requests

from src.TokenGenerator import TokenGenerator


def get_user_details(token):
    # with open("../data/token.json") as token_file:
    #     token = json.load(token_file)

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
    try:
        token_generator = TokenGenerator('8946998793')
        token_generator.generate_otp()
        token_generator.confirm_otp()
        # token = token_generator.token
        get_user_details(token_generator.token)
        # with open("data/token.json", "w") as token_data:
        #     json.dump(token_generator.token, token_data)
    except TimeoutError:
        print("timed out")
