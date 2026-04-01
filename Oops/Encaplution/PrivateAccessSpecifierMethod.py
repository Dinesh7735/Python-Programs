class Sample:
    def __init__(self,a):
        self.a = a
    def M1(self):
        print(f'Inside M1 method - {self.a}')
        self.__M2()
    def __M2(self):
        print(f'Inside M2 method - {self.a}')
obj = Sample(10)  
obj.M1()
obj.M2() #We can't access private methods outside the class