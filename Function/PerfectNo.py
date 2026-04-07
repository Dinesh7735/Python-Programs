def Perfect(num,Sum = 0):
    dup = num
    for val in range(1,num):
        if num % val == 0:
            Sum += val
    if dup == Sum:
        return 'Perfect No'
    return 'Not a Perfect No'
print(Perfect(6))
print(Perfect(24))
