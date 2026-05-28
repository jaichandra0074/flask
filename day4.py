'''
POST ---> reqest.form
-------------------------
---> Data sunmitted for html

json data ---> request.get_json()

'''
import smtplib
from email.message import EmailMessage

sender = "chandunedui7273@gmail.com"

# Remove spaces from app password
password = "sijudaisdpcuyjzk"

msg = EmailMessage()

msg['Subject'] = "Registration"
msg['From'] = sender
msg['To'] = "rneduri@gitam.in"

msg.set_content("Registration Successful")

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login(sender, password)

server.send_message(msg)

print("Email Sent Successfully")

server.quit()