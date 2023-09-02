import requests

sheety_endpoint = f"https://api.sheety.co/9a710f7a641e40a8f6a733ec60bdd598/flightDeals/prices"
sheety_response = requests.get(url=sheety_endpoint)

class DataManager:
    def __init__(self):
        self.data = sheety_response.json()["prices"]
