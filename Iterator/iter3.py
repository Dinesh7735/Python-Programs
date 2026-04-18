class Sample:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __iter__(self):
        return self
    def __next__(self):
        val = self.a
        if self.a > self.b:
            raise StopIteration('Iteration Khatam Hogya re Baba')
        self.a += 1
        return val
obj = Sample(12,15)
itobj = iter(obj)
while 1:
    print(next(itobj))