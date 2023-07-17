# WAP to calculate area of a circle,rectangle and square

# area of circle
def circle():
    radius = float(input("\nEnter radius of circle : "))
    return 3.14*radius*radius
# area of square
def square():
    side = float(input("\nEnter side of square : "))
    return side*side
# area of rectangle
def rectangle():
    length = float(input("\nEnter length of rectangle : "))
    breath = float(input("Enter breath of rectangle : "))
    return length*breath

# function call
while(True):
    print("\nChoose shape for area calculation :")
    print("1. Circle\n2. Rectangle\n3. Square\n4. Exit(any key)")
    choice = input("Enter your choice : ")
    if(choice=='1'):
        result = circle()
    elif(choice=='2'):
        result = rectangle()
    elif(choice=='3'):
        result = square()
    else:
        print("Exit")
        exit()
    print("Area of shape is",result)
    
