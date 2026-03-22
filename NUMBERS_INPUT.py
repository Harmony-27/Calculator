a = float(input("Write Your First Number. "))
b = input("Write Operation. ")
c = float(input("Write Your Second Number. "))
if b == '+':
    print(a+c)
elif b == '-':
    print(a-c)
elif b == '*':
    print(a*c)
elif b == '/':
    if c != 0:
        print(a/c)
    else:
        print("Can not Divide By Zero.")
else:
    print("No Results.")