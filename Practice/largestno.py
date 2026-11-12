def largeOfThree(a:int,b:int,c:int)->int:
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
a=int(input("Enter 1st Number:"))
b=int(input("Enter 2nd Number:"))
c=int(input("Enter 3rd Number:"))
print(largeOfThree(a,b,c))    
