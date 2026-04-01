from abc import ABC, abstractmethod
class Tv(ABC):
    @abstractmethod                 #There must be atleast one abstract method inside abstract class
    def Display(self):
        pass
    @abstractmethod
    def Price(self):
        pass
    def Color(self):                #It's a concrete method
        print('Balck')
class LG(Tv):
    def Display(self):
        print('43 Inch')
    def Price(self):
        print(42000)
class Sony(Tv):
    def Display(self):
        print('32 Inch')
    def Price(self):
        print(32000)
class Samsung(Tv):
    def Display(self):
        print('72 Inch')
    def Price(self):
        print(62000)
obj = Sony()
obj.Price()
obj.Color()