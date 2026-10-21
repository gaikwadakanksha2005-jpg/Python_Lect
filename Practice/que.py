#create a list 10 item and display sum of last 4 number
list=[5,10,15,20,25,30,35,40,45,50]
print("Sum of last 4 items is:",sum(list[-4:]))

#remove the items for the list located at 2 and 5 th position
list.pop(1)
list.pop(4)
print(" After Removing 2nd and 5th position item",list)

#print difference between of hightest and smallest number
l1=max(list)
print(l1)
l2=min(list)
print(l2)
print(l1-l2)

#append a new element in list which is half of the item of 3rd position in list
new_list=list[2]/2
list.append(new_list)
print(list)