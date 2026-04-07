def Prime(num):
    if num > 1:
        for val in range(2,int(num**0.5)+1):
            if num % val == 0:
                return f'{num} is not Prime'
        return f'{num} is Prime'
    return f'{num} is not Prime'
for ans in map(Prime,range(1,101)):
    print(ans)