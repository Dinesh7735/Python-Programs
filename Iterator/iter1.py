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
        self.a += 2
        return val
obj = Sample(10,16)
itobj = iter(obj)
while True:
    print(next(itobj))