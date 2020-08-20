# add new student record data and post request required
import requests
import json
import jsonpath

def test_add_student_data():
    api_url = "http://www.thetestingworldapi.com/api/studentsDetails"
    file = open("D:\\py.txt",'r')
    read=file.read()
    student_details = json.loads(read)
    response = requests.post(api_url,student_details)
    print(response.status_code)
    print(response.text)
    assert response.status_code ==201

def test_show_student_data():
    api_url = "http://www.thetestingworldapi.com/api/studentsDetails/53708"
    response = requests.get(api_url)
   # json_response = json.loads(response.text)
    json_response = response.json()
    print(json_response)
    Id = jsonpath.jsonpath(json_response,"data.id")
    print(Id)
    assert Id[0] == 53708

def test_update_student_data():
    api_url = "http://www.thetestingworldapi.com/api/studentsDetails/53708"
    file = open("D:\\py.txt", 'r')
    read = file.read()
    student_details = json.loads(read)
    update = requests.put(api_url,student_details)
    print(update)
    print(update.text)

def test_delete_student_data():
    api_url = "http://www.thetestingworldapi.com/api/studentsDetails/53708"
    response = requests.delete(api_url)
    print(response)