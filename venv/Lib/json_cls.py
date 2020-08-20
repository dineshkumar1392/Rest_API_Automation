#parse json to dictionary
import json
d= '{"name": "dinesh", "age": 25, "city": "hyd"}'
obj= json.loads(d)
print(obj)

obj1 = open("D:\drivers\py1.txt",'a') # create file
obj1.write(str(obj))                  # print json in the for of string in py1.txt file

