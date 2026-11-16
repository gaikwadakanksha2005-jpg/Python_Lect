def removeDuplicateNum(nums:list[int])->list[int]:
    result=[]
    for x in nums:
        if x  not in result:
            result.append(x)
    return result
nums=list(map(int,input("Enter a numbers:").split(",")))
print(removeDuplicateNum(nums))        
