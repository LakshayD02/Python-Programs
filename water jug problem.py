print("This program implements water jug problem")
print("Jug x:min=0 lit to max=4 lit Jug y:min=0 lit to max=3 lit")
x=int(input("enter the initial state of x:"))
y=int(input("enter the initial state of y:"))
print()

print('*'*3, "RULE CHART",'*'*3)
print("1. Fill the x jug upto brim (4 litres)")
print("2. Fill the y jug upto brim (3 litres)")
print("3. Discharge some water from x jug")
print("4. Discharge some water from y jug")
print("5. empty the x jug")
print("6. empty the y jug")
print("7. pour some water from jug y to jug x to attain x's highest capacity(4 litres)")
print("8. pour some water from jug x to jug y to attain y's highest capacity(3 litres)")
print("9. transfer water from y to x jug")
print("10. transfer water from x to y jug")
while x!=2:
    ruleno=int(input("enter the rule number:"))
    if ruleno==1:
        if x<4:
            x=4
            print("x=",x)
            print("y=",y)
    elif ruleno==2:
        if y<3:
            y=3
            print("x=",x)
            print("y=",y)
    elif ruleno==3:
        if x>0:
            d=int(input("we have to drain some water from jug x. enter how many litres you want to drain"))
            x=x-d
            print("x=",x)
            print("y=",y)
    elif ruleno==4:
        if y>0:
            d=int(input("we have to drain some water from jug y. enter how many litres you want to drain"))
            y=y-d
            print("x=",x)
            print("y=",y)
    elif ruleno==5:
        if x>0:
            x=0
            print("x=",x)
            print("y=",y)
    elif ruleno==6:
        if y>0:
            y=0
            print("x=",x)
            print("y=",y)
    elif ruleno==7:
        if x+y>4 and y>0:
            y=y-(4-x)
            x=4
            print("x=",x)
            print("y=",y)
    elif ruleno==8:
       if x+y>3 and x>0:
            x=x-(3-y)
            x=3
            print("x=",x)
            print("y=",y)
    elif ruleno==9:
            x=x+y
            y=0
            print("x=",x)
            print("y=",y)
    elif ruleno==10:
            x=0
            y=x+y
            print("x=",x)
            print("y=",y)
    print("The Goal is Achieved")
                    
                    
                    
            
