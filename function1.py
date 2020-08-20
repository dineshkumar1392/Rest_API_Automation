def wish():
    print('hello good morning')
wish()


#in faction take input through parameters
def squere(number):
    print( "squre root of ", number,'is' , number * number )

squere(4)
squere(5)

#return statement

def add(a,b):
    return(a+b)
sum=add(100,654)
print("the sum is ",add(12,36))
print("the sum is", sum )

# multiple argument

def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
#a,b,c,d=calc(100,50)
#print("the sum is", a)
#print('the sub is', b)
#print("the mul is", c)
#print("the div is", d)
i=calc(100,50)
print(i)