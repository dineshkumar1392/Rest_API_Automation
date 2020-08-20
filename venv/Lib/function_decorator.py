def f():
    def g():
        print("Hi, it's me 'g'")
        print("Thanks for calling me")

    print("This is the function 'f'")
    print("I am calling 'g' now:")
    g()
f()

######################################################
def f(x):
    def g(y):
        return y + x + 3

    return g


nf1 = f(1)    # this is first parameter like a= 1
nf2 = f(2)

print(nf1(1))   # this is second parameter like b = 1
print(nf2(3))

