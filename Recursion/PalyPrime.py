def Palindrom(num):
    place = 10**(len(str(num))-1)
    if num == 0:
        return 0
    return ((num % 10)*place) + Palindrom(num // 10)
def Prime(num,val = 2):
    if num <= 1:
        return False
    if 2*val > num:
        return True
    if num % val == 0:
        return False
    return Prime(num,val + 1)
num = 7
if Palindrom(num) and Prime(num):
    print('Palyprime')
else:
    print('Not Palyprime')