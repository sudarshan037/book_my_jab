import json
from pprint import pprint

from src.TokenGenerator import TokenGenerator

if __name__ == "__main__":
    try:
        token_generator = TokenGenerator('8946998793')
        token_generator.generate_otp()
        token_generator.confirm_otp()
        with open("data/token.json", "w") as token_data:
            json.dump(token_generator.token, token_data)
    except TimeoutError:
        print("timed out")
