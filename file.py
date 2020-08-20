#file handling like open read  data from file , and  write data to file ,

obj= open("D:\py.txt",'r')
print(obj.read())

obj1= open("D:\drivers\py.txt",'r')

print(obj1.read(10))

obj2= open("C:\\Users\\Dinesh Rao\\Desktop\\SQL\\sql.txt",'r')
print(obj2.readline())

# print charactor from file one by one

obj3= open("D:\drivers\py.txt",'r')

for i in obj3.read():


  print(i)


# read all data from line by line
obj4= open("C:\\Users\\Dinesh Rao\\Desktop\\SQL\\sql.txt",'r')

s = obj4.readline()

while (s) :
    print(s)
    s= obj4.readline()







