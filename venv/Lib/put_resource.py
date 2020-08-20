# update by put method
import requests
import json
import jsonpath
url = "https://reqres.in/api/users/2"
file =open("D:\\py.txt",'r')
read = file.read()
resourse = json.loads(read)
response = requests.put(url,resourse)
print(response.status_code)
response_json = json.loads(response.text)
print(response_json)
updated = jsonpath.jsonpath(response_json,'updatedAt')
print(updated[0])