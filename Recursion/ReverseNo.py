def Reverse(num):
    place = 10**(len(str(num))-1)
    if num == 0:
        return 0
    return (num % 10)*place + Reverse(num // 10)
num = 123
print(Reverse(num))