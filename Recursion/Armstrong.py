def Armstrong(num):
    if num == 0:
        return 0
    return ((num % 10)**power) + Armstrong(num // 10)
num = 1634
power = len(str(num))
if Armstrong(num) == num:
    print('Armstrong')
else:
    print('Not Armstrong')