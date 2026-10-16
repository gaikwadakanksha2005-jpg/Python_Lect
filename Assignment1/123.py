#1
with open("file.txt",'r') as f:
    content=f.read()
    count=0
    for ch in content:
        if ch.lower() in "aeiou":
            count+=1
    print("Total Vowels:",count)        

# 2.read all lines from a file into a list. print the total number of lines and display the 2nd and 4th line
with open("file.txt",'r') as f:
    lines=f.readlines()
print("Total number of lines:",len(lines))
print("2nd Line:",lines[1])
print("4th Line:",lines[3])    

#3
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Words:", words)
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)

#4.1
with open("file.txt", "r") as file:
    content = file.read()
words = content.split()
print("Words:", words)

#4.2
with open("file.txt", "r") as file:
    content = file.read()
words = content.split()
print("Total words:", len(words))