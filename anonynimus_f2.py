#anonymus function or lambda function
# square function
l=lambda n:n*n

print('square of 4 is', l(4))

# add values by lambda

add= lambda a,b: a+b
print(add(12,13))

#find the gratest amoung two

big =lambda a,b: a if a>b else b
print("biggest number among 200 and 400 is ",big(200,400))


# sum of n numbers
i = 0
add=0
while i < 12:
    add = add + i
    i=i+1
print(add)



