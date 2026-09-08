# Assignment 1 
try:
    num = int (input("Enter a number:"))
    print(f"The number you entered is: {num}")
except ValueError:
    input("Invalid input! Please enter a valid number: ")
print("Program continues...")

#=========================================================================================================================#

# Assignment 2
try:
    num1 , num2 = eval(input("Enter two numbers separated by a comma: "))
    result =  num1 / num2
    print(f"The result of the division is: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except SyntaxError:
    print("Error: Invalid input format. Please enter two numbers separated by a comma.")
else:
    print("Division operation completed successfully.")
finally:
    print("Program continues...")