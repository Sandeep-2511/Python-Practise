print("Enter string:")
s=input()
a = s.lower()


vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
digits = "1234567890"
whitespace = " "

c = 0
v = 0
d = 0
ws= 0

for i in a:
    if i in vowels:
        v+=1
    elif i in consonants:
        c+=1
    elif i in digits:
        d+=1
    elif i in whitespace:
        ws+=1

print(v,c,d,ws)