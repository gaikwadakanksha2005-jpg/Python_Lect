def swapNumbers(a:int,b:int)->list[int]:
    a,b=b,a
    return [a,b]
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
print(swapNumbers(a,b))