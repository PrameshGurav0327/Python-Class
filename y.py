a = int(input("Enter any number: "))
b = int(input("Enter any number: "))
c = int(input("Enter any number: "))

if (a > b):
    print("a is greater than b")
    if (b > c):
        print("b is greater than c")
    else:
        print("c is greater than b")
else:
    print("b is greater than or equal to a")
    if (b > c):
        print("b is greater than c")
    else:
        print("c is greater than or equal to b")