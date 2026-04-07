def StrongNo(num,Sum = 0):
    dup = num
    while num > 0:
        rem = num % 10
        fact = 1
        while rem > 0:
            fact *= rem
            rem -= 1
        Sum += fact
        num //= 10
    if dup == Sum:
        return 'Strong No'
    return 'Not a Strong No'
print(StrongNo(145))
print(StrongNo(153))