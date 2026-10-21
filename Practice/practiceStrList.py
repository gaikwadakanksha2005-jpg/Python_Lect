#print sum of first 10 even num
sum=0
for i in range(1,21):
    if i %2==0:
        sum+=i
print("sum of frist 10 even num:",sum)     

str="hello"
print("Reverse:",str[::-1])

#Accept sentence from user and count the vowels
text=input("Enter a sentence:")
count=0
for ch in text:
    if ch in "aeiouAEIOU":
        count=count+1
print("Number of Vowel:",count)        

#Remove duplicates from list
num=[10,20,30,40,20]
num=list(set(num))
print(num)

#accept 2 values S and N.print square of frist N numbers starting from S
S=int(input("Enter S: "))
N=int(input("Enter N: "))
for i in range(S,S+N):
    print(i*i)

#reverse the list
list=[10,20,30,40,50]
list.reverse()
print("Reverse list:",list)
