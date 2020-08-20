# create a file and write a data on it

#obj = open("D:\drivers\py1.txt",'w')
#obj.write("my name is dinesh")
#obj.close()

# add the data on existing file

obj = open("D:\drivers\py1.txt",'a')
obj.write("i am from himachal pradesh")
obj.tell()

# tell() , current cursor potion
obj2 = open("D:\drivers\py1.txt",'r')
obj2.readline()
print(obj2.tell())
obj2.readline()
print(obj2.tell())

# seek() move the cursor to perticular position

obj2 = open("D:\drivers\py1.txt",'r')
obj2.readline()
obj2.seek(17)
print(obj2.tell())