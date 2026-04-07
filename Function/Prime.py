def Prime(num):
    count = 0
    for val in range(1,num+1):
        if num % val == 0:
            count += 1
    if count == 2:
        return 'Prime Number'
    return 'Not a Prime Number'
print(Prime(13))
print(Prime(12))