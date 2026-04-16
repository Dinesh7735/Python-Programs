def Armstrong(num,Sum = 0):
    power = len(str(num))
    dup = num
    while num > 0:
        rem = num % 10
        Sum += rem**power
        num //= 10
    if dup == Sum:
        return 'Armstrong'
    return 'Not armstrong'
print(Armstrong(15))