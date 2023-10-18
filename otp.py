from twilio.rest import Client
import sms
import math
import random
client = Client(sms.account_sid, sms.auth_token)
digits="0123456789"

# function for otp generation
def generate_otp():
    otp=""
    for i in range(6):
      otp+=random.choice(digits)

    return otp

fotp=generate_otp()

message = client.messages.create(
    body="Your 6 digit OTP is "+otp,
    from_=sms.inputNO,
    to=sms.sendNo
)

print(message.body)

