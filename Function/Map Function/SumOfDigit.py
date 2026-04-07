def SumOfDigit(num,Sum = 0):
    dup = num
    while num > 0:
        rem = num % 10
        Sum += rem
        num //= 10
    return f'Sum of each digit in {dup} is {Sum}'
for ans in map(SumOfDigit,range(121,127)):
    print(ans)