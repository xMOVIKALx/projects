import smtplib
from email.message import EmailMessage
import time
msg = EmailMessage()
email = input("Enter your e-mail address : ")
msg['From'] = email
password = input("Enter your e-mail application passcode : ")
msg['To'] = input("Enter receiver e-mail address : ")
msg['Subject'] = input("Enter e-mail subject : ")
massage = input("Enter your massage : ")
msg.set_content(massage)
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email , password)
server.send_message(msg)
print("Almost done...")
time.sleep(3)
print("Done!")
server.quit()