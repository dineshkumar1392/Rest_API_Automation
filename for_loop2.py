#print table for perticuler table
t=int(input('enter the value which table you want'))
p=0
print('table of',t)
for x in range(1, 11):
    p=t*x;
    print(p)
#print table for perticuler table in respective format like 7*1=7
t=int(input('enter the value which table you want'))
print('table of',t)
for x in range(1,11):
    print(str(t) + '*' + str(x)  +'=' + str(t * x ))

# To display numbers from 0 to 10
for x in range(40, 50):
    print(x)

#To display odd numbers from 0 to 20
for x in range(21):
    if x%2==1 :
        print(x)

#To display numbers from 10 to 1 in descending order
for x in range(10, 0, -1):
    print(x)
