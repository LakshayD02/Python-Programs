# WAP to Python program to create a Dictionary which has a record of student information.

Dict = {"StdName": None, "Rollno": None, "Admno" :None, "Marks": None}

Dict["StdName"] = input("Enter student name : ")
Dict["Rollno"] = input("Enter student roll number : ")
Dict["Admno"] = input("Enter student admission number : ")
Dict["Marks"] = float(input("Enter student marks(in percent) : "))

print(Dict)
