def Sample():
    a = 5
    yield a
    a += 2
    yield a, 'abc', 45
genobj = Sample()
print(genobj)
while 1:
    print(next(genobj))