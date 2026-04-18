class Sample:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __iter__(self):
        return self
    def __next__(self):
        val = self.a
        if self.a > self.b:
            raise StopIteration
        self.a = chr(ord(self.a)+1)
        return val
obj = Sample('a','d')
itobj = iter(obj)
while 1:
    print(next(itobj))