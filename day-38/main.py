import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ['APP_KEY']
SHEETY_API_KEY = os.environ['SHEETY_API_KEY']

GENDER = "male"
WEIGHT = "86"
HEIGHT = "177"
AGE = "25"

exercise = input("Tell me which exercise you did: ")

nutritionix_headers = {"x-app-id": APP_ID, "x-app-key": APP_KEY}
sheety_headers = os.environ['sheety_headers']


params = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutritionix_response = requests.post(
    url=end_point, json=params, headers=nutritionix_headers
)

now = datetime.now()
date_now = now.strftime("%d/%m/%Y")
time_now = now.strftime("%X")

for excer in nutritionix_response.json()["exercises"]:
    workout = {
        "workout": {
            "date": date_now,
            "time": time_now,
            "exercise": excer["name"].title(),
            "duration": excer["duration_min"],
            "calories": excer["nf_calories"],
        }
    }
    sheety_end_point = os.environ['sheety_end_point']

    sheety_response = requests.post(
        url=sheety_end_point, json=workout, headers=sheety_headers
    )
    print(sheety_response.text)


# Header for bearer token and auth for user and password
