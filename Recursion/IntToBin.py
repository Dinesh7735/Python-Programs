def Binary(num,place = 1):
    if num == 0:
        return 0
    return (num % 2)*place + Binary(num // 2,place*10)
num = 12
print(Binary(num))
