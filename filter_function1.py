def isEven(x):
    if x%2 == 0:
        return True
    else:
        return False
l= [5,10,15,20,25,30]
l1=list(filter(isEven, l))
print(l1)

# filter with lambda function
l=[5,10,15,20,25,30]
s=list(filter(lambda x:x%2==0,l))
print(s)

# filter with lambda function for odd number
l=[5,10,15,20,25,30]
s=list(filter(lambda x:x%2!=0,l))
print(s)
