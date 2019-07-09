list1 = [{},{},{}]
list2 = [{1,2},{},{}]
print(all(not d for d in list1))
print(all(not d for d in list2))