a = ['a','e','i','o','u','A','E','I','O','U',' ']
b = "Hello, have a good day"
for i in b:
  if i not in a:
    b = b[:b.index(i)]+b[b.index(i)+1:]
print (b)