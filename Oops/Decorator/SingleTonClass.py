#A class which can create only one object for it's life.
def Outer(arg):
    L = []
    def Inner():
        if len(L) == 0:
            obj = arg()
            L.append(obj)
        return L[0]
    return Inner
@Outer
class Sample():
    def __init__(self):
        print('Hii')
obj1 = Sample()
obj2 = Sample()
print(obj1)
print(obj2)