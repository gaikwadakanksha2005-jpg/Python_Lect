s=input("Enter a string:")
lower=0
upper=0
for ch in s:
    if ch.isupper():
       
            upper=+1
    elif ch.islower:
            lower+=1
print("Uppercase:",upper)
print("Lowercase:",lower)                    