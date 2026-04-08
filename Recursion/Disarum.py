def Disarum(num):
    power = len(str(num))
    if num == 0:
        return 0
    return ((num % 10)**power) + Disarum(num // 10)
num = 135
if Disarum(num) == num:
    print('Disarum')
else:
    print('Not Disarum')