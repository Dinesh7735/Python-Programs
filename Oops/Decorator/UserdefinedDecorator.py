def Outer(arg):
    def Inner(a,b):
        print('Hello')
        return arg(a,b)
    return Inner
@Outer
def Sample(n1,n2):
    return n1+n2
print(Sample(1,2))