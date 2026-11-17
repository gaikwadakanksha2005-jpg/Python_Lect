def armstrongInrange(start:int,end:int)->list[int]:
    result=[]
    for n in range(start,end+1):
        temp=n
        power=len(str(n))
        total=0
        while temp>0:
            digit=temp%10
            total=total+digit**power
            temp=temp//10
        if total==n:
            result.append(n)   
    return result
start=int(input("Enter Start Number:"))
end=int(input("Enter End Number:"))
print(armstrongInrange(start,end))        