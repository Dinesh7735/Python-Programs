class Sample:
    def __init__(self,a):
        self.a = a
    def M1(self):
        print(f'Inside class - {self.a}')
obj = Sample(10)
print(f'Outside class - {obj.a}')
obj.M1()