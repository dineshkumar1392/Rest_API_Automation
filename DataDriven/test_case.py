import requests
import json
import jsonpath
import openpyxl

from DataDriven import library

def test_add_multiple_student() :

    api_url = "http://www.thetestingworldapi.com/api/studentsDetails"
    f = open("D://api_json/py.txt", 'r')
    json_request = json.loads(f.read())
    obj = library.common("D://api_json/xl_data.xlsx","Sheet1")
    col = obj.fetch_column_count()
    row = obj.fetch_raw_count()
    keylist = obj.fetch_key_name()

    for i in range (2,row +1):
        update_json_requests = obj.update_request_with_data(i,json_request,keylist)
        response = requests.post(api_url,update_json_requests)
        print(response)
        print(response.text)
