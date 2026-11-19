def insertElement(arr:list[int],x:int,p:int)->list[int]:
    for i in range(len(arr)-1,p,-1):
        arr[i]=arr[i-1]
    arr[p]=x
    return arr    
arr=list(map(int,input("Enter list:").split(",")))
x=int(input("Enter number:"))
p=int(input("Enter position:"))
print(insertElement(arr,x,p))

