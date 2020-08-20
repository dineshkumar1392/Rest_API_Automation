#replace string with other string
p=('dineshkumar@gmail.com')
q=len(p.replace('i',''))
print(len(p)-q)

# find how many i exist in this string
c=0
for x in p:
 if x=='i':
  c=c+1
print(c)
#FIND FUNCTION FIND SUB STR IN  EXSISTING STRING
a='gmail'
print(p.find(a))

# split function
word = 'CatBatSatFatOr'
#print([word[i:i+3] for i in range(0, len(word), 3)])

for x in range(0,len(word),3):
 print(word[x:x+3])

 # split

s= 'dinesh kumar email address is dineshkumar1392@gmai.com'
print(s.split(" "))