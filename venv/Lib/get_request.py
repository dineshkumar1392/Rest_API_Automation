# get api response through get
import requests
import json
response =requests.get('https://reqres.in/api/users?page=2')
print(response)

# print the content of request
print(response.content)


# print header of response
print(response.headers)
print(response.status_code)


# to validate status code we use assert it
assert response.status_code == 200

# print specific  response header content
print(response.headers.get('date'))
print(response.headers.get('content-type'))

# fatch cookies
print(response.cookies)

# fatch  encoding
print(response.encoding)
print(response.elapsed)

# fatch content of the tesponse in json form
json_response = json.loads(response.text)
# or we can use response.content 
print(json_response)