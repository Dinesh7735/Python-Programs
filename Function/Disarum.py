def Disarum(num,total = 0):
    dup = num
    power = len(str(num))
    while num > 0:
        rem = num % 10
        total += rem**power
        power -= 1
        num //= 10
    if total == dup:
        return 'Disarum Number'
    return 'Not a Disarum Number'
print(Disarum(135))
print(Disarum(136))