import collections
output=collections.defaultdict(int)
input=[[('hi','bye')],['sandeep'],
       [('a','b')],[('d','j','k')]]
for elem in input:
    output[elem[0]]+=1
print(output)