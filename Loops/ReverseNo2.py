num = 123
power = 10**(len(str(num))-1)
Sum = 0
while num > 0:
    rem = num % 10
    Sum += rem*power
    num //= 10
    power //= 10
print(Sum)