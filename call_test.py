import requests

_url = 'https://<SERVER_URL_HERE>:8085/api/v3/XYZ'

_headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer <TOKEN>',
}

_params = {
    'jobType': 'PUSH',
}

response = requests.get(_url, params=_params, headers=_headers)
print()

print(response)
print(response.json())
