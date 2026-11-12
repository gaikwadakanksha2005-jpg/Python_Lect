def sumUpToN(n:int)->int:
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum    
n=int(input("Enter a Number:"))
print(sumUpToN(n))        