import requests
import json
import jsonpath
def test_oauthentication ():
    token_url = "http://www.thetestingworldapi.com/Token"
    data = {"grant_type" : 'password', "username" : 'admin',"password" : "adminpass"}
    response = requests.post(token_url,data)
   # print(response.text)
    token_value = jsonpath.jsonpath(response.json(),"access_token")
   # print(token_value[0])
    auth = {'Authorized': 'Bearer ' +token_value[0]}
    print(auth)

    api_url="http://www.thetestingworldapi.com/api/StDetails/1104"
    response = requests.get(api_url, headers=auth)
    print(response.text)
