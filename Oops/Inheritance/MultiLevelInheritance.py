class grantParent:
    a = 3
    b = 2
class Parent(grantParent):
    c = 4
    b = 9
class Child(Parent):
    c = 5
    d = 7
obj = Child()
print(obj.a)
print(obj.b)
print(obj.c)