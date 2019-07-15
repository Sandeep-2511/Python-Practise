if __name__ == '__main__':
    class object():
        def __init__(self,t,n):
            self.unit=t
            self.units=n
        def printer(self):
            print(self.unit,self.units)
x=object("Sandeep",2019)
print(x.unit,x.units)