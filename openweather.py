import requests
from pprint import pprint
from datetime import datetime
def weather():
    city = input("enter city name : ")
    key = "646c4e5be6f1f78a1fe101e266ec7bc5"
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
    r = requests.get(url = URL)
    data = r.json()
    for i in data :
        if i == "name" :
            n = data["name"]
        elif i == "dt":
            d = data["dt"]
            rd = datetime.fromtimestamp(d)
        elif i == "main":
            for j in data["main"]:
                if j == "temp":
                    c = str(data["main"]["temp"] - 273.15)
                    rc = c[0:4]
                    h = data["main"]["humidity"]
    print(f"name : {n}\ntemp : {rc}\ndate : {rd}\nhumidity : {h}")
    
    weather()
    
weather()

