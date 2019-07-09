list1 = [{},{},{}]
list2 = [{2,3},{},{}]
print(all(not d for d in list1))
print(all(not d for d in list2))
