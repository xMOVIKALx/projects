import requests

url = "https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages"

auth = ("api", "gzkfaoqrevhbsohl")
senderemail = input("Enter sender e-mail address : ")
receiveremail = input("Enter receiver e-mail address : ")
subject = input("Enter e-mail subject : ")
massage = input("Enter your massage : ")
data = {
  "from": senderemail,
  "to": receiveremail,
  "subject": subject,
  "text": massage
}

response = requests.post(url, auth=auth, data=data)

print(response.status_code)
print(response.text)