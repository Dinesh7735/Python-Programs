class Parent:
    def M1(self):
        print('Inside Parent M1')
    def M2(self):
        print('Inside Parent M2')
class Child(Parent):
    def M2(self):
        print('Inside Child M2')
        super().M2()
        Parent.M1(self)
    def M3(self):
        print('Inside Child M3')
obj = Child()
obj.M1()
obj.M2()
obj.M3()