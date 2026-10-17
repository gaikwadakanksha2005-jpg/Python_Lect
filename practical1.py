
with open("sample.txt","r")as f:
    print(f.readline())

with open("sample.txt","a")as f:
    f.write("\n Welcome to magical  word python")
with open("sample.txt","r")as f:
   print(f.read())    

with open("sample.txt","r")as f:
    data=f.read()
print("Total Character:",len(data))  

