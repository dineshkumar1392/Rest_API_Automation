import csv
#f = open("D://api_json/csv1.csv", 'r')
#r = csv.reader(f)

#for line in r :
#    print(line)



#write in csv file

with open("D://api_json/emp.csv","w",newline='') as f:
 w=csv.writer(f) # returns csv writer object
 w.writerow(["ENO","ENAME","ESAL","EADDR"])
 n=int(input("Enter Number of Employees:"))
 for i in range(n):
    eno=input("Enter Employee No:")
    ename=input("Enter Employee Name:")
    esal=input("Enter Employee Salary:")
    eaddr=input("Enter Employee Address:")
    w.writerow([eno,ename,esal,eaddr])
    print("Total Employees data written to csv file successfully")
f = open("D://api_json/emp.csv", 'r')
r = csv.reader(f)
for line in r :
    print(line)