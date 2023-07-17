# Program for Calculating the area of a Circle, Rectangle and Square

# 1. Area of Circle
def circle():
    radius = float(input("\nEnter the Radius of Circle : "))
    return 3.14*radius*radius

# 2. Area of Square
def square():
    side = float(input("\nEnter the Side of Square : "))
    return side*side

# Area of Rectangle
def rectangle():
    length = float(input("\nEnter the Length of Rectangle : "))
    breath = float(input("Enter the Breath of Rectangle : "))
    return length*breath

while(True):
    print("\nChoose shape for area calculation :")
    print("1. Circle\n2. Rectangle\n3. Square\n4. Exit(Any Key)")
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
    
