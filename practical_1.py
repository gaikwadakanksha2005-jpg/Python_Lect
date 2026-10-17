with open("myfile.txt","r")as f:
    lines=f.readlines()
    print(lines[2])

with open("sample.txt","a")as f:
    f.write("\n This is appended text from Akanksha")
    print("text appended successfully")    
    
with open("sample.txt","r")as f:
    f.seek(5)
    print(f.read(10))

with open("sample.txt","r")as f:
    lines=f.readlines()
    for i in range(len(lines)):
        print(i+1,":",lines[i],end=" ")    

with open("sample.txt","r")as f:
    lines=f.readlines()
with open("reversed.txt","w")as f:
    for line in reversed(lines):
        f.write(line)
print("Lines Written in reverse order")       