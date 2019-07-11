people = {1: {'Name': 'joshi', 'Age': '20', 'Sex': 'Male'},
          2: {'Name': 'rakesh', 'Age': '19', 'Sex': 'Male'},
          3:{'Name':'sandeep','Age':'18','Sex':'Male'},
          4:{'Name':'pranav','Age':'17','sex':'Male'}}

print(people[1])
for i in people:
    del i ['Sex']
print(people)
# for idnumber, pinfo in people.items():
#     print("\nPerson ID:", idnumber)
#     for key in pinfo:
#         print(key + ':', pinfo[key])