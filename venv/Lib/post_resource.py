# create recource in server
import requests
import jsonpath
import json
url="https://reqres.in/api/users"

#open the file in read mode
file = open("D:\\py.txt",'r')
# read file data
read = file.read()

resource = json.loads(read)
print(resource)
# make jason request with json input body
response=requests.post(url,resource)
print(response.content)
print(response.headers.get("Content-Length"))
#parse response to json format
response_json = json.loads(response.text)
id= jsonpath.jsonpath(response_json,'id')
print(id[0])

