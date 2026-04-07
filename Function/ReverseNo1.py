def RevNo(num,rev = 0):
    while num > 0:
        rem = num % 10
        rev = rev*10+rem
        num //= 10
    return rev
print(RevNo(123))
print(RevNo(1230))