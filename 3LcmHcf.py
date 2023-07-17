def HCF(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            HCF = i
    return HCF

def LCM(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            LCM = greater
            break
        greater += 1
    return LCM

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("The H.C.F. of", x,"and", y,"is", HCF(x, y))
print("The L.C.M. of", x,"and", y,"is", LCM(x, y))
