from pprint import pprint

from src.TokenGenerator import TokenGenerator

if __name__ == "__main__":
    try:
        token_generator = TokenGenerator('8946998793')
        token_generator.generate_otp()
        token_generator.confirm_otp()
    except TimeoutError:
        print("timed out")
