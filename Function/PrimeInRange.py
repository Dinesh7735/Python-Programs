def Prime(num):
    count = 0
    for val in range(1,num+1):
        if num % val == 0:
            count += 1
    if count == 2:
        return 'Prime'
    return 'Not Prime'
for num in range(1,101):
    print(f'{num} is {Prime(num)}')