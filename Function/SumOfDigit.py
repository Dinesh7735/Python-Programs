def Add(num,Sum = 0):
    while num > 0:
        rem = num % 10
        Sum += rem
        num //= 10
    return Sum
print(Add(123))