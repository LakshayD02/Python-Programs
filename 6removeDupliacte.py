# WAP to remove all the duplicate from a string
string = input("Enter your string : ")
x=""
for char in string:
	if char not in x:
		x = x+char
print(x)
x=list("string")
