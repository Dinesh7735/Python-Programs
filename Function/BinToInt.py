def BinToInt(num,power = 0,Sum = 0):
    while num > 0:
        rem = num % 10
        Sum += rem*2**power
        power += 1
        num //= 10
    return Sum
print(BinToInt(101))
print(BinToInt(1100))