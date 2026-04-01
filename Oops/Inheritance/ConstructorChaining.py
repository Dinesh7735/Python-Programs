class Parent:
    def __init__(self,a,b):
        self.a = a
        self.b = b
class Child(Parent):
    def __init__(self,c,d):
        super().__init__(30,40)
        Parent.__init__(self,50,60)
        self.c = c
        self.d = d
obj = Child(10,20)
print(obj.c,obj.d)
print(obj.a,obj.b)

