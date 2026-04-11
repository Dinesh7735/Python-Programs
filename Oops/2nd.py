class Calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f'Square of {self.n} is {self.n*self.n}')

    def cube(self):
        print(f'Cube of {self.n} is {self.n*self.n*self.n}')

    def squareroot(self):
        print(f'Squareroot of {self.n} is {int(self.n**0.5)}')
    
    @staticmethod
    def greet():
        print('Hello')

c = Calculator(4)
c.square()
c.cube()
c.squareroot()
c.greet()
    
