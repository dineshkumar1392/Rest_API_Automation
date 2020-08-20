import requests
import json
import jsonpath
url = 'https://reqres.in/api/users?page=2'

dl = requests.delete(url)
print(dl)
print(dl.status_code)
assert dl.status_code == 204