# creat class and define function in the class

class a:
    def hello(self):
        print('hello world ')

# create functin with argument but no return value
    def sum(self,b,c):
        d=b+c
        print("sum of two numbers is", d)

# create function with argument and return value
    def mul(self,b,c):
        d=b*c
        return d

# constructor
    def __init__(self,a,b):
        c=a+b
        print("the sum of constructed number",c)

obj =a(122,50)
obj.hello()
obj.sum(12,15)
x=obj.mul(20,10)
print(x)
