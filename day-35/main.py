import requests
from twilio.rest import Client

account_sid = 'ACd4d9dd535ea5913fcb8171a5d5a38b74'
auth_token = '58272d50c9b1679e6203e5747d315173'
client = Client(account_sid, auth_token)

my_api = '0502dfb4e8fa9ab4209619d3910412d6'
angela_api_key = '69f04e4613056b159c2761a9d9e664d2'
twillio_number = '+18149149924'

parameters = {
    'lat' : 14.586680,
    'lon' : 121.110880,
    'exclude': "current,minutely,daily,alerts",
    'appid' : angela_api_key
}

response = requests.get('https://api.openweathermap.org/data/2.5/onecall?', parameters)
response.raise_for_status()

# MY SOLUTION
# weather_api = response.json()['hourly']

# for num in range(12):
#     if weather_api[num]['weather'][0]['id'] < 700:
#         print("Bring an Umbrella")


# ANGELA's SOLUTION
weather_slice = response.json()['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if condition_code < 700:
        will_rain = True

if will_rain:
    message = client.messages.create(
            from_='+18149149924',
            body="It's going to rain tday. Remember to bring an umbrella☂️.",
            to='+639615281824'
            )
    print(message.status)