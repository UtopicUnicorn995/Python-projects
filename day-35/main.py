import requests
my_api = '0502dfb4e8fa9ab4209619d3910412d6'
angela_api_key = '69f04e4613056b159c2761a9d9e664d2'

parameters = {
    "lat" : 14.586680,
    'lon' : 121.110880,
    "appid" : '69f04e4613056b159c2761a9d9e664d2'
}

request = requests.get('https://api.openweathermap.org/data/3.0/onecall?', parameters)
request.raise_for_status()
print(request.json())