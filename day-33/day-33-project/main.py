import requests
from datetime import datetime
import smtplib

my_email = "christianpy123@gmail.com"
password = "sdclnpccssmamibh"
MY_LAT = 14.588580 # Your latitude
MY_LONG = 121.112370 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def is_close():
    if iss_latitude - MY_LAT > 5 or iss_latitude - MY_LAT < -5:
        return False
    else:
        if iss_longitude - MY_LONG > 5 or iss_longitude - MY_LONG < -5:
            return False
        else:
            return True

        
def is_night():
    if is_close():
        if sunrise > time_now.hour or sunset < time_now.hour:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(my_email, password)
                connection.sendmail(from_addr=my_email, to_addrs="christian.degulacion@gmail.com", msg="Subject:Look at the sky\n\nThe ISS is visible right now.")
    else:
        return

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


is_night()