def Prime(num, val = 2):
    if num <= 1:
        return 'Not Prime'
    if 2*val > num:
        return 'Prime'
    if num % val == 0:
        return 'Not Prime'
    return Prime(num,val + 1)

num = 15
print(Prime(num))
