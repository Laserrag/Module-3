#Positonal arguments.
def greet(name, age):
    print("Hello", name, ", you are", age, "years old.")
#Recursion-when a calls itself.
def square(num):
    """
    Returns the square of a number.
    """
    return num * num

print(square(5))
print(square.__doc__)

#Assignment 1
def factorial(n):
    """This is a recursive function to find the factorial of an integer."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
print(factorial.__doc__)

#Assignment 2
def total_calc(bill_amount, tip_percentage):
    total = bill_amount * (1 + 0.01 * tip_percentage)
    print("The total bill amount is", total, "dollars.")
    total = round(total, 2) 
    print("The total bill amount rounded to 2 decimal places is", total, "dollars.")
    print("Please pay", total, "dollars.")

total_calc(150,20)