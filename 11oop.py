# WAP to store student info using class (OOP)

# Creating student class 
class student:
    
    # constructor for passing student info
    def __init__(self,name,rollno,adno,marks):
        self.name = name
        self.rollno = rollno
        self.adno = adno
        self.marks = marks

    # method to print details
    def printDetail(self):
        print(f"Name : {self.name}\nRoll no. : {self.rollno}\nAdmission no. : {self.adno}\nMarks : {self.marks}\n")
    
Std1 = student("Lakshay",17536,"2117536",(96,95,92,89))
Std1.printDetail()
Std2 = student("Suraj",17536,"2117510",(88,98,90,92))
Std2.printDetail()
Std3 = student("Priyanshu",17524,"2117524",(98,82,95,91))
Std3.printDetail()
