people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'sagar', 'age': '22', 'sex': 'male'},
          3:{'name':'sandeep','age':'18','sex':'male'}}
people[4]={'name':'anthony','age':'28','sex':'male'}
dict.update(people)
for x in people:
    print(people[x])
