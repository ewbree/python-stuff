import requests                             # Import requests module for HTTP(S) requests.
#from requests.auth import HTTPBasicAuth     # Not sure if needed yet.
import json                                 # JSON en-/decoder module.

device_address = "XYZ"
device_port = "XYZ"
username = "XYZ"
password = "XYZ"
#version = "v1"


# URL to do call against.
_url = "https://" + device_address

# Headers should be placed here.
headers = {
    'content-type': 'application/json'
}

# Do request and get response
_response = requests.post(
    device_address,
    auth=HTTPBasicAuth(username=username,password=password),
    headers=headers,
    verify=False # Set to True if using a valid certificate. Otherwise, leave it on False.
)
print ("Response: ",_response.status_code)

# Get the json-encoded content from response
_response_json = _response.json()
print ("\n",json.dumps(_response_json,indent=4))