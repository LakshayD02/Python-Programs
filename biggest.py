# WAP to find the biggest of the two numbers

# Get the user input
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

def maximum(a,b):
     
    if a >= b:
        return a
    else:
        return b

print('The Bigger number is',maximum(a, b))
