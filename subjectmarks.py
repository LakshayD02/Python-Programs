# WAP to read subject marks and print pass or fail using single return value.

print('Enter marks obtained in 3 subjects')
s1=int(input("Enter marks of the first subject: "))
s2=int(input("Enter marks of the second subject: "))
s3=int(input("Enter marks of the third subject: "))
avg=(s1+s2+s3)/3

if s1>40 and s2>40:
    print('Pass')
elif s2>40 and s3>40:
    print('Pass')
elif s3>40 and s1>40:
    print('Pass')
elif avg>40:
    print('Pass')
else:
    print('Fail')
