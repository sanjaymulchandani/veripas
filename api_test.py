import requests
 
URL = "http://127.0.0.1:8000/api/user-details/"

call_api = requests.get(URL)

if call_api.status_code == 200:
    data = call_api.json()
    print(data)
else:
    print(call_api.status_code)