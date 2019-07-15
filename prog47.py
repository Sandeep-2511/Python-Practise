class addition:
    def __init__(self,j,k):
        self.first=j
        self.second=k
    def display(self):
        print("first number:"+str(self.first))
        print("second number:"+str(self.second))
        print("addition="+str(self.answer))
    def calculate(self):
        self.answer=self.first+self.second
obj=addition(54,45)
obj.calculate()
obj.display()