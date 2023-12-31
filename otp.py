from twilio.rest import Client
import sms
import math
import random
client = Client(sms.account_sid, sms.auth_token)
digits="0123456789"

def generate_otp():
    otp=""
    for i in range(6):
      otp+=random.choice(digits)

    return otp

fotp=generate_otp()

def validate_mobile(num):
    return len(num) == 10 and num.isdigit()

def send_otp_over_mobile(target_no,fotp):
    
    if(validate_mobile(target_no)):
        target_no="+91"+target_no
        message=client.messages.create(
          body="Your OTP is "+fotp,
          from_=sms.twilio_no,
          to=sms.target_no
        )
        print(message.body)
      
    else:
       print("INVALID MOBILE NUMBER!")
       target_no=input("ENTER AGAIN: ")
       validate_mobile(target_no)
       send_otp_over_mobile(target_no,fotp)
message = client.messages.create(
    body="Your 6 digit OTP is "+otp,
    from_=sms.inputNO,
    to=sms.sendNo
)

def validate_email(mail):
   if "@" not in mail and "." not in mail:
      return False
   else:
      return True

def send_otp_over_email(mail,fotp,sender,password):
   if(validate_email(mail)):
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender,password)
        msg_body="Your OTP is "+fotp
        server.sendmail(sender,mail,msg_body)
        print("OTP sent! ",fotp)
   else:
        print("INVALID MAIL!")
        mail=input("ENTER AGAIN: ")
        validate_email(mail)
        send_otp_over_email(mail,fotp,sender,password)

print("How do you want to send the otp?")
ans=input("Through Mobile or Email: ")

sender="sarikatare16@gmail.com"  
password="qrqxkweelnbgqmoa"

if(ans.lower()=="mobile"):
    
    number=input("ENTER YOUR MOBILE NUMBER: ")
    validate_mobile(number)
    send_otp_over_mobile(number,fotp)

elif(ans.lower()=="email"):
    
    recipent=input("ENTER YOUR MAIL ID: ")
    send_otp_over_email(recipent,fotp,sender,password)

      

