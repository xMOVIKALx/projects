from email.message import EmailMessage
import ssl
import smtplib
print("you can know your password-code on this link : https://www.youtube.com/watch?v=g_j6ILT-X0k")
try :
    def email():
        email_sender = input("Enter sender email-address : ")
        email_password = input("Enter sender password-code : ")
        email_receiver = input("Enter receiver email-address : ")
        subject = input("Enter subject : ")
        body = input("Enter your text : ")
        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = email_receiver
        em["Subject"] = subject
        em.set_content(body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp :
            smtp.login(email_sender,email_password)
            smtp.sendmail(email_sender,email_receiver,em.as_string())
    email()

    again = input("send again a mail ? (y/n) : ")

    if again == "y" :
        email()
    elif again == "n" :
        input("press 'Enter' key to Exit")
    else :
        print("invalid input !")
except :
    print("an error! use a valid e-mail or check your network connection. try again.")