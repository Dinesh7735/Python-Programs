def SpyNo(num,Sum = 0, Mul = 1):
    while num > 0:
        rem = num % 10
        Sum += rem
        Mul *= rem
        num //= 10
    if Sum == Mul:
        return 'Spy No'
    return 'Not a Spy No'
print(SpyNo(123))