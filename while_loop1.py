# while loop with increment
#taking the input from the user and display table of that in respective format 7*1=7

t=(input('enter the table name'))
i=1
while i<=10 :
    print( t + '*' +str(i) + '=' + str(int(t)*i))
    i=i+1

# while loop with decrement
# write a table in reverce order

t=int(input('enter the table name '))
i=10
while i>=1 :
    print(str(t) + '*' + str(i) + '=' + str(t*i) )
    i=i-1
