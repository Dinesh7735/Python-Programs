# Accessing the properties and methods of a single parent call is known as single level inheritance.
class Parent:
    a = 10
    b = 20
class Child(Parent):
    c = 30
    b = 40
obj = Child()
print(obj.a,obj.b)