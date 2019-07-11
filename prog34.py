class Employee:
    id=0
    name=""


    def __init__(self, i, n):
        self.id=i
        self.name=n

    def __call__(self, *args, **kwargs):
            print('Printing args')
            print(*args)

            print('Printing kwargs')
            for key, value in kwargs.items():
                print("%s == %s" % (key, value))

e=Employee(10,'fruit')
print(e)
print(callable(e))



