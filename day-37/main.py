import requests

USER_NAME = 'blackluster123'
TOKEN = 'asdbqweoa1'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USER_NAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

graph_params = {
    'id': 'blackluster123',
    'name': 'habit tracker',
    'unit': 'commit',
    'type': 'shee',
    'color': 'sora'
}

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graph"


# response = requests.post(url=pixela_endpoint, json=user_params)

# print(response.text)