import requests
import json
import jsonpath


response =requests.get('https://reqres.in/api/users?page=2')

# fatch content of the tesponse in json form
# or we can use response.content
json_response = json.loads(response.text)
#print(json_response)

# fatch any value by jsonpath

pages = jsonpath.jsonpath(json_response,'total_pages')
print(pages[0])
# for comparing we use assert
#assert pages[0]== 2

# advance json path

first_names = jsonpath.jsonpath(json_response,'data[3].first_name')
print(first_names)

for i in range(0, 6):
# first_names1 = jsonpath.jsonpath(json_response,'data['+str(i)+'].first_name')
    first_names1 = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
    print(first_names1[0])







