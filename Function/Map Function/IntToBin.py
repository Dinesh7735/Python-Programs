def Binary(num,Bin = 0,place = 1):
    while num > 0:
        rem = num % 2
        Bin += rem * place
        num //= 2
        place *= 10
    return Bin
print(list(map(Binary,range(1,10))))