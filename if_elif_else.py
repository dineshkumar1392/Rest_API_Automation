brand=input('enter your favourite brand:');
if (brand=='re'):
    print("it is childern's brand")
elif brand=="kf":
    print('it is not that much  kick ')
elif (brand == "fo"):
    print("buy one get one free")
else:
    print("other brand are not recommended ")

    #  check if no is -tv then display negative number, if number is 0 then display 0
    # check if no is +tv then display then check for even and odd no

num=int(input('enter the number:'))
if num < 0:
    print('negative number')
elif num > 0 :
    if num%2==0:
        print('even number')
    else:
        print('odd number')
else:
    print('number is zero')