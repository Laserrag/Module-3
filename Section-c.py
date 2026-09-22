a = 0 
b=0

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    Operation = input("Enter operation (+, -, *, /): ")
    if Operation == '+':
        print("Result:", add(a, b))
    elif Operation == '-':
        print("Result:", subtract(a, b))
    elif Operation == '*':
        print("Result:", multiply(a, b))
    elif Operation == '/':
        print("Result:", divide(a, b))
    else:
        None
except ValueError:
    input("Invalid input. Please enter numeric values:")
    Operation = input("Enter operation (+, -, *, /): ")
    if Operation == '+':
        print("Result:", add(a, b))
    elif Operation == '-':
        print("Result:", subtract(a, b))
    elif Operation == '*':
        print("Result:", multiply(a, b))
    elif Operation == '/':
        print("Result:", divide(a, b))
    else:
        None
except ZeroDivisionError:
    input("Error: Division by zero is not allowed.Please enter numeric values:")
    Operation = input("Enter operation (+, -, *, /): ")
    if Operation == '+':
        print("Result:", add(a, b))
    elif Operation == '-':
        print("Result:", subtract(a, b))
    elif Operation == '*':
        print("Result:", multiply(a, b))
    elif Operation == '/':
        print("Result:", divide(a, b))
    else:
        None
finally:
    print("Thank you for using the calculator.")