import requests
import json
 
url = "https://api.tago.io/data"

API_KEY = "932c43e0-91a1-47ad-8e99-790ed9659aba"
 
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Device-Token": API_KEY,
    "ssl": "false",
}

data = [
    {"variable": "temperatura","value": "50"},
    {"variable": "umidade","value": "20"},
]
 
response = requests.post(url, headers=headers, json=data)
 
print("Status Code", response.status_code)
print("JSON Response ", response.json())