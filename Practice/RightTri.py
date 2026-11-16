def rightTri(n:int)->list[str]:
    pattern=[]
    for i in range(1,n+1):
        pattern.append("*"*i)
    return pattern
n=int(input("Enter a Number:"))
print(rightTri(n))    