a=['a','e','i','o','u']
b="hello, have a good day"
c = []
for i in b:
    if i.lower() in a:
        c.extend(i)
print(c)
