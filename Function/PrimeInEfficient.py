def Prime(num):
    if num > 1:
        for val in range(2,int(num**0.5)+1):
            if num % val == 0:
                return 'Not Prime'
        return 'Prime'
    return 'Not Prime'
print(Prime(12))
print(Prime(13))