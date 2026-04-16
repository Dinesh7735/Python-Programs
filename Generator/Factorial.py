def Sample(num,fact = 1):
    if num >= 0:
        yield 1
    for val in range(1,num+1):
        fact *= val
        yield fact
num = 4
genobj = Sample(num)
while 1:
    print(next(genobj))
