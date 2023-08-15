import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# status_code = response.raise_for_status()
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["longitude"]

# print(latitude)

MY_LAT = 14.588580
MY_LONG = 121.112370

time_now = datetime.now()

parameters = {
    "lat":  MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(time_now)
print(sunset )