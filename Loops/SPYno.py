num = int(input('Enter the number: '))
temp = num
Sum = 0
Mul = 1
while num > 0:
    rem = num % 10
    Sum += rem
    Mul *= rem
    num //= 10
if Sum == Mul:
    print(f'{temp} is a SPY number')
else:
    print(f'{temp} is not a SPY number')