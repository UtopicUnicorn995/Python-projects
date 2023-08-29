import requests
from datetime import datetime

USER_NAME = 'blackluster123'
TOKEN = 'asdbqweoa1'
GRAPH_ID = 'graph1'

pixela_endpoint = 'https://pixe.la/v1/users'
# https://pixe.la/v1/users/blackluster123/graphs/graph1.html

user_params = {
    'token': TOKEN,
    'username': USER_NAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

graph_params = {
    'id': GRAPH_ID,
    'name': 'habit tracker',
    'unit': 'commits',
    'type': 'int',
    'color': 'sora'
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"


# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text),

today = datetime(2023, 8, 28)
# year = today.strftime("%Y")
# month = today.strftime('%m')
# day = today.strftime('%d')

req_body = {
    'date' : today.strftime('%Y%m%d'),
    'quantity': '6'
}

req_body_put = {
    'quantity': '14'
}

post_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{req_body['date']}"

# response = requests.post(url=post_pixel_endpoint, json=req_body_put, headers=headers)

# response = requests.put(url=post_pixel_endpoint, json=req_body_put, headers=headers)

response = requests.delete(url=post_pixel_endpoint, headers=headers)

print(response.text)