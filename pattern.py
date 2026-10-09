
n=int(input("Enter Number:"))
for i in range(1,n):
    for j in range(i):
        if i %2 != 0:
            print("*",end="")
        else:
            print("#",end="")    
    print()        