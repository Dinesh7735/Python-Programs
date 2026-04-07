def IntToBin(num,place = 1,Sum = 0):
    while num > 0:
        rem = num % 2
        Sum += rem*place
        num //= 2
        place *= 10
    return Sum
print(IntToBin(5))
print(IntToBin(12))