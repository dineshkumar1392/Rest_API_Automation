# customised header through get method
import requests
import json

url= "http://httpbin.org/get"
header_data = {'k1': 'python', 'k2': 'jsn', 'j': '22'}
header = requests.get(url, headers=header_data)
print(header.text)
# add parameter in url
parameter = {'k1': 'python', 'k2': 'jsn', 'j': '22'}
para = requests.get(url, params= parameter)
print(para.text)
