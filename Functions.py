# #Functions-It is a block of code that is designed to perform a specific task. It can take inputs, process them, and return an output. Functions help in organizing code, making it reusable, and improving readability.
# ****************************** Functions *****************************

# it is a block of code that does one particular job

# def sayhello():

# print("hello")

# sayhello()

# ******************* types of function *******************

# 1. built in function

# print("hello")

# len("python")

# max(10,20)

# 2. user defined function

# calling a function

# sayhello()

# *************************** arguments *****************************

# def greet(name):

# print("hello",name)

# name=input("what is your name")

# greet(name)

# *********************************** return statement ************************8

# sum=a+b

# def add(a,b):

# return a+b

# result=add(2,3)

# print(result)//5


#Assignment 1

# def greet(name):
#     print("Hello", name)

# greet("Isha")


# #Assignment 2

# def add(a, b):
#     return a + b

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# result = add(a, b)
# print("The sum is:", result)
# # hahhahah


# # Assignment 3

# def square(c):
#     return c * c

# c = float(input("Enter the number: "))
# result = square(c)
# print("The square is:", result)


# Assignment 4

def number_check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
result = number_check(num)
print("The number is:", result)


# Assignment 5

def person():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print("Your name is", name, "and your age is", age)

person()


