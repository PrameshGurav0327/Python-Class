n = 153
sum = 0
order = len(str(n))
copy_n = n
while(n>0):
    digit = n%10
    sum += digit ** order
    n = n//10

    if(sum == copy_n):
        print("f{copy_n} is an Armstrong number")
    else:
        if(sum ==copy_n):
            print("f{copy_n} is not an Armstrong number")
'''
# n = int(input("Enter any number: "))

# for i in range(1 ,6):
#     print (i*n)
#     print ("Another loop started") 

# n = int(input("Ener any Number"))

# i = 5
# while (i>11):
#     print("i" * "n" : i*n)
#     i+=1


# n = int(input("Type any number"))

# a = 1
# while (6>n):
#     n+=1
#     print(1,5)
#     print("end loop")


# Get the number from the user
# n = int(input("Type any number: "))



# n = "Avenger"
# print(n[-3:])

# x = "avenger"

'''

# def avenger(f_name= "pramesh", age="20"):
#     print("first name is", f_name, "Age is", age)
# avenger("Steve")

'''
print("-------------------------------------------")

# def show(*x):
#     print(x)
# show(100, 200, 300)

print("--------------------------------------------------------")


# def show(**x):
#     print( x ["a"], x["b"])

# show(a = 100, b = 200, c = 300)


print("--------------------Global Variable-------------------------")

x=100

def show():
    print("variable indside function", x)

show()

print("variable outside function", x)

print("-----------------Local Variable-------------------")

x=100

def show():
    global x
    x=200
    print("Variable inside function",x)
    print("variable indside function",x)

show()

print("variable outside function", x)

'''
# a = str("Hello")

# def replace_character(str,curr_char,new_char,output):
#      input(replace_character(""))


# print("------------Fibnocci,Using recursive Function----------------")

# def febonacci(n):
#     if n<=1:
#         return n

'''def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n//10)
    
n = 123  # Example number
print(sum_of_digits(n))'''

# print("-----------Implicit and explicit type conversion--------------------")

# x=5
# y=2.5

# result=x+y
# print(result)
# print(type(result))

print("---------------  ----------------------")

# a = input("Write Something: " )

# print(a)
# print(a.count("$"))

# 1. list of input only specific data-type


# Given input
n = 5

# Initialize factorial variable
fact = 1

# Calculate factorial
for i in range(1, n + 1):
    fact *= i

# Print the result
print(fact)

