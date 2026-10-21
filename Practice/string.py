#common strinf function

#sample string
text="  welocme to IMCC! "
#1.Strip spaces from both ends
print("Remove Spaces:",text.strip())

#2Lower case
print("Lower Case:",text.lower())

3#Upper case
print("Upper case:",text.upper())

#4Capitalized first letter
text=text.strip()
print("capitilize first letter:",text.capitalize())

#5 Title case (capitalize each word)
print(text.title())

#6 Count occurance of substring
print("Letter C occurse:",text.count("C"),"time in taxt")

#7 Find position of substring(-1 if not found)
print("position of IMCC in text is:",text.find("IMCC"))

#8 Replace Substring
print(text.replace("IMCC","python magic"))

#9 Check if string starts or ends with certain substring
print(text.startswith("  We"))
print(text.endswith("!  "))

#10 Split String into list by delimiter
print("Simple split:",text.split())

#11.join list of string with separator
words=["python","is","fun"]
print("".join(words))

