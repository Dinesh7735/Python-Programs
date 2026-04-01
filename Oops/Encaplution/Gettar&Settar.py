# gettar() - It is used to access private data members obside the class
# settar() - It is used to modify the private data members in side class
class Sample:
    def __init__(self,a):
        self.__a = a
    def gettar(self):
        return self.__a
    def settar(self):
        self.__a = 20
obj = Sample(10)
print(obj.gettar())
obj.settar()
print(obj.gettar())
