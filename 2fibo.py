# Program to display the Fibonacci series

n = int(input(" Enter the number of terms : "))

n1, n2 = 0, 1
count = 0

if n <= 0:        # Checking if the number of terms are valid
   print("Please enter a valid number")
   
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)

else:
   print("Fibonacci sequence:")  # Generating fibonacci sequence
   while count < n:
       print(n1)
       nth = n1 + n2
       # Updating values
       n1 = n2
       n2 = nth
       count += 1
