'''a = int(input("Enter any number: "))
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
        print("c is greater than or equal to b")'''

#1. days of number should print acc to name of the months

January = 31
February = 28
March = 31
April = 30
May = 31
June = 30
July = 31
August = 30
September = 31
October = 30
November = 31
December = 30

month = (input("Enter the month: "))
if month == "31":
    print("January, March, May, July, August, October, December")
elif month == "30":
    print("April, June, September, November")


#2. Should guess the order of 3 numbers, like 3,4,5 is increasing, 5,4,3 is decreasing and 2,5,8 is unordered


