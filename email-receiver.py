import imaplib
import email

email_address = input("Enter your e-mail address : ")
password = input("Enter your e-mail password/code : ")
imap_server = "imap.gmail.com"

mail = imaplib.IMAP4_SSL(imap_server)
mail.login(email_address, password)

mail.select("inbox")

status, messages = mail.search(None, "ALL")

messages = messages[0].split()

for message in messages:
    status, data = mail.fetch(message, "(RFC822)")

    msg = email.message_from_bytes(data[0][1])

    print("Subject:", msg["Subject"])
    print("From:", msg["From"])
    print("To:", msg["To"])
    print("Date:", msg["Date"])

    if msg.is_multipart() :
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))

            if content_type == "text/plain" and "attachment" not in content_disposition:
                body = part.get_payload(decode=True).decode()
                print(body)

    else:
        content_type = msg.get_content_type()
        if content_type == "text/plain":
            body = msg.get_payload(decode=True).decode()
            print(body)

    print("-" * 50)

mail.close()
mail.logout()