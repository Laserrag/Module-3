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