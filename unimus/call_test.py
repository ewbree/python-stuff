
###
### Just a simple short API call for Unimus.
### For more info, check Unimus' Swagger: https://download.unimus.net/api-v3-preview/
###


import requests

url = 'http://<SERVER_URL_HERE>:8085/api/v3/XYZ'
token = "<TOKEN HERE>"

headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer ' + token,
}

parameters = {
    'jobType': 'PUSH',
}

response = requests.get(
    verify = False, # Set to True or False depending on your situation.
    url = url,
    params = parameters,
    headers=headers
)

print()
print(response)
print(response.json())