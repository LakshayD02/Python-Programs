# Write a program to count number of vowels in a string

string = input("Enter your string : ")  #User defined

vowel = ('a','e','i','o','u')  #Vowels
count = 0

for i in range(len(string)):
    if(string[i] in vowel):
        count +=1

print("Number of vowel in string is",count)
