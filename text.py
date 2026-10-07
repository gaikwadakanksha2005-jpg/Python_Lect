
text="ha"
print(text*3)

text1="hello"
text2="Wolds"
print(text1+text2)

name="akanksha"
print("Letter a occurse:",name.count("a"),"time in name")
print("replace:",name.replace("a","z"))

print("Split name:",name.split())

ls=[1,2,4,3]
sorted(ls)
print(ls)

my_list=[] #empty list
print(my_list)

fruits=["Apple","Mango","Cherry"]
print(fruits)

num=[10,20,30,40]
print(num[0])
print(num[-2])

#Append item in list
fruits=["Apple","Mango","Cherry"]
fruits.append("Guava")
print("After append:",fruits)

#insert at specific location
fruits.insert(2,"Watermelon")
print("After insert:",fruits)

#function
#length
num=[1,2,3,4,5,6,7]
print("No of itesm is list are:",len(num))

#sum
print("Sum of items:",sum(num))

#sorting
print("List in Ascending order:",sorted(num))
print("List in descending order:",sorted(num, reverse=True))


numbers=[]

#create a list 10 item and display sum of last 4 number
list=[5,10,15,20,25,30,35,40,45,50]
print("Sum oflast 4 items is:",sum(list[-4:]))

#remove the items for the list located at 2 and 5 th position
list.pop(1)
list.pop(4)
print(list)
#print difference betwwen of hightest and smallest number
l1=max(list)
print(l1)
l2=min(list)
print(l2)
print(l1-l2)

#append a new element in list which is half of the item of 3rd position in list
num_list=list[2]/2
list.append(num_list)
print(list)