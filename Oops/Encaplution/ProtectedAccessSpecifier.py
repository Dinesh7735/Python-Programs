class Sample:
    def __init__(self,a):
        self._a = a
    def M1(self):
        print(self._a)
obj = Sample(10)
obj.M1()
print(obj._a)