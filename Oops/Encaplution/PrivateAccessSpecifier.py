class Sample:
    def __init__(self, a):
        self.__a = a
    def M1(self):
        print(self.__a)
obj = Sample(10)
obj.M1()
print(obj.__a) #we can't access private data members outside the class