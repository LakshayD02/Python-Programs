# WAP to find sum, difference and division using argument with return to value

def add(a, b):
    "Returns the sum of two numbers"
    return a + b

def subtract(a, b):
    "Returns the difference of two numbers"
    return a - b

def divide(a, b):
    "Returns the division of two numbers"
    if b == 0:
        return "Error: division by zero"
    else:
        return a / b
    
# Get the user input
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Call the functions
print("The sum is:", add(a, b))
print("The difference is:", subtract(a, b))
print("The division is:", divide(a, b))
