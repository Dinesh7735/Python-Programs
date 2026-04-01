num = int(input('Enter the number: '))
temp = num
while num > 9:
    result = 0
    while num > 0:
        rem = num % 10
        result += rem**2
        num //=10
    num = result
if num == 1 or num == 7:
    print(f'{temp} is a Happy number')
else:
    print(f'{temp} is not a Happy number') 