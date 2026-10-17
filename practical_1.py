with open("myfile.txt","r")as f:
    lines=f.readlines()
    print(lines[2])

with open("sample.txt","a")as f:
    f.write("\n This is appended text from Akanksha")
    print("text appended successfully")    
    
with open("sample.txt","r")as f:
    f.seek(5)
    print(f.read(10))