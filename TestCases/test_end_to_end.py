import requests
import json
import jsonpath
def test_add_student():
    api_url = "http://www.thetestingworldapi.com/api/studentsDetails"
    file = open("D://api_json/py.txt", 'r')
    read = file.read()
    student_details = json.loads(read)
    response = requests.post(api_url, student_details)
    id = jsonpath.jsonpath(response.json(),"id")
    print(response.text)
    print(id[0])

    api_tech_url ="http://www.thetestingworldapi.com/api/technicalskills"
    file = open("D://api_json/post_py.txt", 'r')
    read = file.read()
    tech_details = json.loads(read)
    tech_details['id'] = int(id[0])
    tech_details['st_id'] = id[0]
    response = requests.post(api_tech_url, tech_details)
    print(response.text)

    api_address_url = "http://www.thetestingworldapi.com/api/addresses"
    file1 = open("D://api_json/address_py.txt", 'r')
    read1 = file1.read()
    address_details = json.loads(read1)
    address_details["stId"]= id[0]
    response1 = requests.post(api_address_url, address_details)
    print(response1.text)

    final_details ="http://www.thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response2 = requests.get(final_details)
    print(response2.text)