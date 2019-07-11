i=0
class vroom:
    name=""
    number=0
    def __call__(self, *args, **kwargs):
        print(args)
    def __init__(self,i,n):
        self.name=i
        self.number=n

print(vroom)
print(callable(vroom))