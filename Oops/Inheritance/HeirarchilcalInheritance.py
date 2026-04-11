class Parent:
    a = 12
    b = 23
class Child1(Parent):
    b = 231
    c = 234
class Child2(Parent):
    c = 32
    d = 11
obj1 = Child1()
obj2 = Child2()
print(obj1.b)
print(obj1.a)
print(obj2.a)
print(obj2.d)