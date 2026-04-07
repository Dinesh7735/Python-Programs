def Happy(num):
    while num > 9:
        num = square(num)
    if num == 1 or num == 7:
        return 'Happy Number'
    return 'Not a Happy Number'

def square(num,res = 0):
    while num > 0:
        res += (num % 10)**2
        num //= 10
    return res

print(Happy(19))