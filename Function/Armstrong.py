def Armstrong(num,total = 0):
    power = len(str(num))
    dup = num
    while num > 0:
        rem = num % 10
        total += rem**power
        num //= 10
    if dup == total:
        return 'Armstrong Number'
    return 'Not an Armstrong Number'
print(Armstrong(153))
print(Armstrong(370))
print(Armstrong(371))