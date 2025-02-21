from dotenv import load_dotenv
import requests
import pyotp
import os

# secrets
load_dotenv()
setup_key = os.getenv("SECRET")


# get current 6-digit otp
totp = pyotp.TOTP(setup_key)
current_otp = totp.now()

# print
print(f"current otp: {current_otp}")

