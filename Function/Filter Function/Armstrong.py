def Armstrong(num,Sum = 0):
    power = len(str(num))
    dup = num
    while num > 0:
        rem = num % 10
        Sum += rem**power
        num //= 10
    return dup == Sum
print(list(filter(Armstrong,range(1,1001))))