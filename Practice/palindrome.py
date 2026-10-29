


n = 153
temp = n
total = 0
digits = len(str(n))

while n > 0:
    digit = n % 10
    total = total + digit ** digits
    n = n // 10

if total == temp:
    print("Armstrong number")
else:
    print("Not Armstrong")

    
str=input("Enter string:")
rev=str[::-1]
if str == rev:
    print("palindrom")
else:
    print("not palindrom")    

