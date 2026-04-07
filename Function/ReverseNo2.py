def RevNo(num,rev = 0):
    power = 10**(len(str(num))-1)
    while num > 0:
        rem = num % 10
        rev += rem*power
        num //= 10
        power //= 10
    return rev
print(RevNo(123))
print(RevNo(1234))
