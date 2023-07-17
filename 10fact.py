# WAP to calculate factorial of a number.

num = int(input("Enter a number: ")) #Get user from input

# Initialize the factorial to 1
factorial = 1

for i in range(1, num + 1):   #Using for loop
    factorial *= i

print("Factorial of", num, "is", factorial)
